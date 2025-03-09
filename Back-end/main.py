from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import chatRoutes,playerRoutes

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(chatRoutes.router, prefix="/chats")
app.include_router(playerRoutes.router, prefix="/players")

@app.get("/")
async def root():
    return {"message": "System API is running!"}