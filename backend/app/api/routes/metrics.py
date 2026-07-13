from fastapi import APIRouter, Depends
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.metrics_service import get_metrics


router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"]
)


@router.get(
    "/",
    response_class=PlainTextResponse
)
def metrics(
    db: Session = Depends(get_db)
):

    data = get_metrics(db)


    response = "\n".join(
        [
            f"{key} {value}"
            for key, value in data.items()
        ]
    )


    return response