def calculate_player_points(player):
    runs = int(float(player["Total Runs"])) if player.get("Total Runs") is not None else 0
    balls_faced = int(float(player["Balls Faced"])) if player.get("Balls Faced") is not None else 0
    innings = int(float(player["Innings Played"])) if player.get("Innings Played") is not None else 0
    wickets = int(float(player["Wickets"])) if player.get("Wickets") is not None else 0
    overs_bowled = int(float(player["Overs Bowled"])) if player.get("Overs Bowled") is not None else 0
    runs_conceded = int(float(player["Runs Conceded"])) if player.get("Runs Conceded") is not None else 0

    batting_strike_rate = (runs / balls_faced * 100) if balls_faced > 0 else 0
    batting_average = (runs / innings) if innings > 0 else 0

    total_balls_bowled = overs_bowled * 6
    bowling_strike_rate = (total_balls_bowled / wickets) if wickets > 0 else 0
    economy_rate = ((runs_conceded / total_balls_bowled) * 6) if total_balls_bowled > 0 else 0

    points = (batting_strike_rate / 5) + (batting_average * 0.8)
    
    if bowling_strike_rate > 0:
        points += (500 / bowling_strike_rate)
    if economy_rate > 0:
        points += (140 / economy_rate)
    
    value = (9 * points + 100) * 1000
    value = round(value / 50000) * 50000

    return {
        "batting_strike_rate": batting_strike_rate,
        "batting_average": batting_average,
        "bowling_strike_rate": bowling_strike_rate,
        "economy_rate": economy_rate,
        "points": points,
        "value": value
    }
