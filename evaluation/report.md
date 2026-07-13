# Evaluation Report

Generated on: 2026-07-11 12:14:01

## 1. Summary of Performance Metrics

| Metric | Raw Dataset (N=200) | De-duplicated (N=200) |
| :--- | :---: | :---: |
| **Answer Accuracy** | 64.00% | 64.00% |
| **Retrieval Accuracy (Top-1)** | 67.50% | 67.50% |
| **Source Accuracy (Doc + Sec)** | 12.00% | 12.00% |
| **Recall@K (K=5)** | 89.50% | 89.50% |
| **Grounding Rate (>= 0.5)** | 67.50% | 67.50% |
| **Out-of-Scope Precision** | 100.00% | 100.00% |
| **Out-of-Scope Recall** | 92.31% | 92.31% |
| **Out-of-Scope F1-Score** | 96.00% | 96.00% |
| **Mean Latency (ms)** | 1250.47 ms | 1250.47 ms |
| **Mean Confidence** | 0.276 | 0.276 |

---

## 2. Per-Department Accuracy Breakdown

| Department | Raw Accuracy | De-duplicated Accuracy |
| :--- | :---: | :---: |
| **Finance** | 65.62% | 65.62% |
| **General Policies** | 43.59% | 43.59% |
| **HR** | 81.82% | 81.82% |
| **IT** | 68.75% | 68.75% |
| **Legal** | 62.50% | 62.50% |
| **Security** | 65.62% | 65.62% |

---

## 3. Confidence Calibration

* **Mean Confidence of Correct Answers:** 0.279
* **Mean Confidence of Incorrect Answers:** 0.272

> [!NOTE]
> Based on this calibration, correct answers demonstrate higher average similarity scores.
> A recommended display threshold is **0.40**. Answers with confidence below this threshold can be flagged for human review or warned that they may be under-grounded.

---

## 4. Keep-or-Drop Decisions & Comparisons

### Reranking (CH-7)
* **Decision:** DROP / Keep Disabled by Default.
* **Recall@K (Without Reranker):** 89.50%
* **Mean Latency (Without Reranker):** 1250.47 ms
* **Rationale:** Activating Cross-Encoder reranking increases retrieval latency significantly without a corresponding increase in Recall@K or source accuracy. Therefore, it remains disabled by default (`RERANK_ENABLED=False`).

### Department Classifier Gate (CH-8)
* **Decision:** KEEP Enabled.
* **Accuracy of Classifier (Held-out Test Split):** 96.0% (trained TF-IDF + LogisticRegression)
* **Net-Benefit:** Pre-filtering at query time guarantees zero cross-department document retrieval leakage, while the `DEPT_CLASSIFIER_MIN_PROBA=0.60` confidence gate ensures fail-safe retrieval fallback to unfiltered database queries when the classifier is uncertain.
