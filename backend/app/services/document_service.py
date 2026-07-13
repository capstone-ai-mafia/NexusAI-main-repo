from sqlalchemy.orm import Session

from app.models import Document


def get_documents(db: Session):

    return (
        db.query(Document)
        .filter(Document.status != "deleted")
        .all()
    )


def get_document_by_id(
    db: Session,
    document_id: int
):

    return (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )


def delete_document(
    db: Session,
    document_id: int
):

    document = get_document_by_id(
        db,
        document_id
    )

    if document:

        document.status = "deleted"

        db.commit()
        db.refresh(document)

    return document