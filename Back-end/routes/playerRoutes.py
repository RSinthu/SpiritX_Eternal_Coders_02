from fastapi import APIRouter
from models.player import player
from typing import List
from services.playerService import get_all_players

router = APIRouter()

@router.get("", response_model=List[player])
def get_players():
    players = get_all_players()  # Fetches players from the database
    return players