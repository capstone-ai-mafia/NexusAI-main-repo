from datetime import datetime
from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: int
    filename: str
    department: str | None = None
    file_type: str | None = None
    file_size: int | None = None
    status: str
    uploaded_at: datetime | None = None

    class Config:
        from_attributes = True