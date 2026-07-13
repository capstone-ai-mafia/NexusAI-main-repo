from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import time
import json

from app.logging_config import logger
from app.database import get_db
from app.models import ChatLog, SystemMetric
from app.schemas.chat_schema import ChatRequest, ChatResponse, ChatHistoryResponse
from app.services.rag_service import get_rag_answer


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "/",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):

    try:

        if not request.question.strip():

            logger.error("Empty question received")

            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty"
            )


        start_time = time.time()


        result = get_rag_answer(
            request.question
        )


        latency = round(
            time.time() - start_time,
            3
        )


        chat_log = ChatLog(
            question=request.question,
            answer=result["answer"],
            department=result["department"],
            sources=json.dumps(result["sources"]),
            confidence=result["confidence"],
            latency=latency,
            status="success"
        )


        db.add(chat_log)
        
        # Populate system metrics
        db.add(SystemMetric(metric_name="latency", metric_value=latency))
        db.add(SystemMetric(metric_name="confidence", metric_value=result["confidence"]))
        
        db.commit()
        db.refresh(chat_log)


        logger.info(
            f"Chat request processed. id={chat_log.id}, latency={latency}s"
        )


        return {
            "answer": result["answer"],
            "department": result["department"],
            "sources": result["sources"],
            "confidence": result["confidence"],
            "latency": latency,
            "graph": result.get("graph"),
        }


    except HTTPException:
        raise


    except Exception as e:

        logger.error(
            f"Chat error: {str(e)}"
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


@router.get("/history", response_model=list[ChatHistoryResponse])
def chat_history(
    db: Session = Depends(get_db)
):

    try:

        logs = (
            db.query(ChatLog)
            .order_by(ChatLog.id.desc())
            .limit(100)
            .all()
        )

        logger.info(
            f"Chat history requested. Count={len(logs)}"
        )

        return logs


    except Exception as e:

        logger.error(
            f"Chat history error: {str(e)}"
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )