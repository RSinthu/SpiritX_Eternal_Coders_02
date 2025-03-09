from pydantic import BaseModel

class player(BaseModel):
    id: int
    name: str
    university: str
    category: str
    totalRuns: int
    ballsFaced: int
    inningsPlayed: int
    wickets: int
    oversBowled: int
    runsConceded: int
    batting_strike_rate: float
    batting_average: float
    bowling_strike_rate: float
    economy_rate: float
    points: float
    value: int
   