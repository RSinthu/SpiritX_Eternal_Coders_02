import { Player } from "../hooks/usePlayers";

export default function PlayerStats({ player }: { player: Player }) {
  return (
    <div className="w-full">
      <h2 className="text-2xl font-bold text-gray-800">{player.name}</h2>
      <p className="text-gray-500">{player.university}</p>
      <p className="text-gray-700">Category: {player.category}</p>

      <div className="mt-6">
        <h3 className="text-lg font-semibold text-blue-600">Batting Stats</h3>
        <div className="grid grid-cols-2 gap-4">
          <div>
            <p className="font-semibold">Total Runs:</p>
            <p>{player.totalRuns}</p>
          </div>
          <div>
            <p className="font-semibold">Balls Faced:</p>
            <p>{player.ballsFaced}</p>
          </div>
          <div>
            <p className="font-semibold">Innings Played:</p>
            <p>{player.inningsPlayed}</p>
          </div>
          <div>
            <p className="font-semibold">Batting Strike Rate:</p>
            <p>{player.batting_strike_rate}</p>
          </div>
          <div>
            <p className="font-semibold">Batting Average:</p>
            <p>{player.batting_average}</p>
          </div>
        </div>
      </div>

      <div className="mt-6">
        <h3 className="text-lg font-semibold text-green-600">Bowling Stats</h3>
        <div className="grid grid-cols-2 gap-4">
          <div>
            <p className="font-semibold">Wickets:</p>
            <p>{player.wickets}</p>
          </div>
          <div>
            <p className="font-semibold">Overs Bowled:</p>
            <p>{player.oversBowled}</p>
          </div>
          <div>
            <p className="font-semibold">Runs Conceded:</p>
            <p>{player.runsConceded}</p>
          </div>
          <div>
            <p className="font-semibold">Bowling Strike Rate:</p>
            <p>{player.bowling_strike_rate}</p>
          </div>
          <div>
            <p className="font-semibold">Economy Rate:</p>
            <p>{player.economy_rate}</p>
          </div>
        </div>
      </div>

      <div className="mt-6">
        <h3 className="text-lg font-semibold text-purple-600">Fantasy Stats</h3>
        <div className="grid grid-cols-2 gap-4">
          <div>
            <p className="font-semibold">Points:</p>
            <p>{player.points}</p>
          </div>
          <div>
            <p className="font-semibold">Value:</p>
            <p>{player.value}M</p>
          </div>
        </div>
      </div>
    </div>
  );
}
