from services.player_stat_cal import calculate_player_points
import pandas as pd
from db.db import db_connection

# Read CSV file
csv_file_path = "sample_data.csv"
df = pd.read_csv(csv_file_path)

print("CSV Columns:", df.columns.tolist())
# Connect to MySQL

cursor = db_connection.cursor()

# Create table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS cricketers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    university VARCHAR(255),
    category VARCHAR(50),
    totalRuns INT,
    ballsFaced INT,
    inningsPlayed INT,
    wickets INT,
    oversBowled INT,
    runsConceded INT,
    batting_strike_rate FLOAT,
    batting_average FLOAT,
    bowling_strike_rate FLOAT,
    economy_rate FLOAT,
    points FLOAT,
    value INT
);
""")

# Insert data into MySQL
for _, row in df.iterrows():
    player_data = row.to_dict()
    stats = calculate_player_points(player_data)

    query = """
    INSERT INTO cricketers (
        name, university, category, totalRuns, ballsFaced, inningsPlayed, wickets, 
        oversBowled, runsConceded, batting_strike_rate, batting_average, total_balls_bowled, 
        bowling_strike_rate, economy_rate, points, value
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    values = (
        player_data["Name"], player_data["University"], player_data["Category"], player_data["Total Runs"],
        player_data["Balls Faced"], player_data["Innings Played"], player_data["Wickets"],
        player_data["Overs Bowled"], player_data["Runs Conceded"], stats["batting_strike_rate"],
        stats["batting_average"], stats["total_balls_bowled"], stats["bowling_strike_rate"],
        stats["economy_rate"], stats["points"], stats["value"]
    )

    cursor.execute(query, values)

# Commit and close connection
db_connection.commit()
cursor.close()
db_connection.close()

print("Player data and stats successfully inserted into the database!")