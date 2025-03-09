
from fastapi import APIRouter
from models.chatMessage import chatRequest
from services.llm_answer import process_user_query

# Create the API router for user requests
router = APIRouter()

@router.post("")
def create_item(chat: chatRequest):
    # Get the request data
    user_question = chat.question

    # Process and generate response
    generated_response = process_user_query(user_question)

    return {"response": generated_response}