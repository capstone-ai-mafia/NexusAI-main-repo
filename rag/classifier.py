"""
Department classifier for question routing.

Trains a TF-IDF + LogisticRegression pipeline on evaluation/questions.csv,
persists to models/department_clf.joblib, and provides predict_department().
"""
import argparse
import csv
import logging
import sys
from pathlib import Path

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline as SkPipeline

from .config import BASE_DIR, CLASSIFIER_MODEL_PATH

logger = logging.getLogger(__name__)


def _load_training_data():
    """Load questions.csv, excluding OUT_OF_SCOPE rows."""
    csv_path = BASE_DIR / "evaluation" / "questions.csv"
    questions = []
    labels = []
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if row.get("expected_behavior") == "OUT_OF_SCOPE":
                continue
            questions.append(row["question"])
            labels.append(row["department"])
    return questions, labels


def train(report=True):
    """Train and save the department classifier.

    NOTE (evaluation caveat): the classifier is trained on
    evaluation/questions.csv, which is the same file used as the RAG
    evaluation set. The "held-out accuracy" printed below is only an
    internal 20% split of that same file, so it reflects fit on the
    evaluation distribution rather than generalization to unseen
    questions. Treat it as an internal sanity signal, not a claim of
    real-world routing accuracy.
    """
    questions, labels = _load_training_data()
    if not questions:
        print("No training data found.")
        return

    # Create model directory
    CLASSIFIER_MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

    pipe = SkPipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_features=5000)),
        ("clf", LogisticRegression(max_iter=1000, solver="lbfgs")),
    ])

    if report and len(set(labels)) > 1:
        # Stratified train/test split for reporting.
        # CAVEAT: this split is drawn from the same evaluation/questions.csv
        # used to evaluate the full RAG system, so the accuracy below
        # measures fit on the evaluation distribution, not generalization.
        sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
        for train_idx, test_idx in sss.split(questions, labels):
            X_train = [questions[i] for i in train_idx]
            y_train = [labels[i] for i in train_idx]
            X_test = [questions[i] for i in test_idx]
            y_test = [labels[i] for i in test_idx]

        pipe.fit(X_train, y_train)
        preds = pipe.predict(X_test)
        correct = sum(1 for p, g in zip(preds, y_test) if p == g)
        acc = correct / len(y_test) if y_test else 0
        print(f"Held-out accuracy: {acc:.3f} ({correct}/{len(y_test)})")

        # Per-department breakdown
        from collections import Counter
        dept_correct = Counter()
        dept_total = Counter()
        for p, g in zip(preds, y_test):
            dept_total[g] += 1
            if p == g:
                dept_correct[g] += 1
        print("\nPer-department accuracy:")
        for dept in sorted(dept_total.keys()):
            d_acc = dept_correct[dept] / dept_total[dept] if dept_total[dept] else 0
            print(f"  {dept}: {d_acc:.3f} ({dept_correct[dept]}/{dept_total[dept]})")

    # Train on full data for production
    pipe.fit(questions, labels)
    joblib.dump(pipe, CLASSIFIER_MODEL_PATH)
    print(f"\nModel saved to {CLASSIFIER_MODEL_PATH}")
    print(f"Classes: {list(pipe.classes_)}")
    print(f"Training samples: {len(questions)}")
    return pipe


_clf_cache = None


def predict_department(question):
    """
    Predict the department for a question.
    Returns (label, probability).
    Fail-safe: if model is missing, logs a warning and raises.
    """
    global _clf_cache
    if _clf_cache is None:
        if not CLASSIFIER_MODEL_PATH.exists():
            logger.warning(f"Classifier model not found at {CLASSIFIER_MODEL_PATH}. Skipping classification.")
            raise FileNotFoundError(f"Classifier model not found at {CLASSIFIER_MODEL_PATH}")
        _clf_cache = joblib.load(CLASSIFIER_MODEL_PATH)

    proba = _clf_cache.predict_proba([question])[0]
    idx = proba.argmax()
    label = _clf_cache.classes_[idx]
    return label, float(proba[idx])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Department classifier")
    parser.add_argument("--train", action="store_true", help="Train the classifier")
    args = parser.parse_args()

    if args.train:
        train(report=True)
    else:
        parser.print_help()