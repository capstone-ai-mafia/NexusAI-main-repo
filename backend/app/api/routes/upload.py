from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session

from app.logging_config import logger
from app.database import get_db
from app.models import Document
from app.services.file_service import save_file


router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    try:

        file_data = save_file(file)


        document = Document(
            filename=file_data["filename"],
            file_path=file_data["file_path"],
            file_type=file_data["file_type"],
            file_size=file_data["file_size"],
            status="uploaded"
        )


        db.add(document)
        db.commit()
        db.refresh(document)


        await file.close()


        logger.info(
            f"File uploaded successfully: {document.filename}, id={document.id}"
        )


        return {
            "message": "File uploaded successfully.",
            "document": {
                "id": document.id,
                "filename": document.filename,
                "status": document.status
            }
        }


    except ValueError as e:

        logger.error(
            f"Upload validation error: {str(e)}"
        )

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


    except Exception as e:

        logger.error(
            f"Upload internal error: {str(e)}"
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )