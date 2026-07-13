from rag.pipeline import ask


def test_end_to_end_rag_flow_produces_grounded_answer():
    result = ask("What is the annual leave policy?")

    assert result["answer"]
    assert isinstance(result["sources"], list)
    assert len(result["sources"]) > 0
    assert 0.0 <= result["confidence"] <= 1.0

    for source in result["sources"]:
        assert source.get("source")
        assert source.get("department")


def test_end_to_end_rejects_out_of_scope_question_gracefully():
    result = ask("What is the capital of France?")

    assert isinstance(result["answer"], str)
    assert 0.0 <= result["confidence"] <= 1.0
