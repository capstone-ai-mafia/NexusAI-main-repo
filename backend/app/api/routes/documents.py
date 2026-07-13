from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.logging_config import logger
from app.database import get_db
from app.schemas.document_schema import DocumentResponse
from app.services.document_service import (
    get_documents,
    get_document_by_id,
    delete_document
)


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.get(
    "/",
    response_model=list[DocumentResponse]
)
def read_documents(
    db: Session = Depends(get_db)
):

    try:

        documents = get_documents(db)

        logger.info(
            f"Documents list requested. Count={len(documents)}"
        )

        return documents

    except Exception as e:

        logger.error(
            f"Get documents error: {str(e)}"
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


@router.get(
    "/{id}",
    response_model=DocumentResponse
)
def read_document(
    id: int,
    db: Session = Depends(get_db)
):

    try:

        document = get_document_by_id(
            db,
            id
        )

        if not document:

            logger.error(
                f"Document not found. id={id}"
            )

            raise HTTPException(
                status_code=404,
                detail="Document not found"
            )


        logger.info(
            f"Document retrieved. id={id}"
        )

        return document


    except HTTPException:
        raise


    except Exception as e:

        logger.error(
            f"Get document error: {str(e)}"
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


@router.delete(
    "/{id}"
)
def remove_document(
    id: int,
    db: Session = Depends(get_db)
):

    try:

        document = delete_document(
            db,
            id
        )


        if not document:

            logger.error(
                f"Delete failed. Document not found. id={id}"
            )

            raise HTTPException(
                status_code=404,
                detail="Document not found"
            )


        logger.info(
            f"Document deleted. id={document.id}, filename={document.filename}"
        )


        return {
            "message": "Document deleted successfully",
            "id": document.id,
            "filename": document.filename,
            "status": document.status
        }


    except HTTPException:
        raise


    except Exception as e:

        logger.error(
            f"Delete document error: {str(e)}"
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )