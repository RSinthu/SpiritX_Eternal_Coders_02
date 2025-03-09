from pydantic import BaseModel
# Define a Pydantic model for input validation
class chatRequest(BaseModel):
    question: str  # Assuming you expect a question in the request body