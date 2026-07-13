import os
import shutil
import uuid
from pathlib import Path

from fastapi import UploadFile


UPLOAD_DIR = Path(os.getenv("UPLOAD_DIR", "uploads")).expanduser()
UPLOAD_DIR.mkdir(exist_ok=True, parents=True)


ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt",
    ".md"
}


def save_file(file: UploadFile):

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(
            "Unsupported file type"
        )


    unique_name = (
        f"{uuid.uuid4().hex}_"
        f"{file.filename}"
    )


    file_path = UPLOAD_DIR / unique_name


    with file_path.open("wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )


    return {
        "filename": file.filename,
        "file_path": str(file_path),
        "file_type": extension,
        "file_size": file_path.stat().st_size
    }