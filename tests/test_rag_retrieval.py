from rag.retriever import retrieve, retrieve_with_scores


def test_retrieve_returns_relevant_documents():
    docs = retrieve("What is the annual leave policy?")
    assert len(docs) > 0
    assert all(doc.metadata.get("department") for doc in docs)


def test_retrieve_with_scores_returns_relevance_scores():
    pairs = retrieve_with_scores("What is the annual leave policy?")
    assert len(pairs) > 0
    for doc, score in pairs:
        assert isinstance(score, float)
        assert doc.metadata.get("relevance_score") is not None


def test_department_filter_narrows_results():
    hr_docs = retrieve("What is the annual leave policy?", department="hr")
    assert all(doc.metadata.get("department") == "hr" for doc in hr_docs)
