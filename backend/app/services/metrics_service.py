from sqlalchemy.orm import Session

from app.models import Document, ChatLog


def get_metrics(db: Session):

    documents_total = (
        db.query(Document)
        .count()
    )

    documents_processed = (
        db.query(Document)
        .filter(
            Document.status == "processed"
        )
        .count()
    )

    chat_total = (
        db.query(ChatLog)
        .count()
    )

    chat_success = (
        db.query(ChatLog)
        .filter(
            ChatLog.status == "success"
        )
        .count()
    )

    chat_failed = (
        db.query(ChatLog)
        .filter(
            ChatLog.status == "failed"
        )
        .count()
    )

    latencies = [
        row[0]
        for row in db.query(ChatLog.latency).all()
        if row[0] is not None
    ]

    if latencies:
        avg_latency = sum(latencies) / len(latencies)
    else:
        avg_latency = 0

    return {
        "rag_requests_total": chat_total,
        "rag_success_total": chat_success,
        "rag_failed_total": chat_failed,
        "rag_avg_latency_seconds": round(avg_latency, 3),
        "documents_total": documents_total,
        "documents_processed_total": documents_processed
    }