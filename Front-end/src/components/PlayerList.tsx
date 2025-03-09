import { useEffect, useState } from "react";
import usePlayers, { Player } from "../hooks/usePlayers";
import PlayerStats from "./PlayerStats";

export default function PlayerList() {
  const { data: players = [] } = usePlayers();
  const [selectedPlayer, setSelectedPlayer] = useState<Player | null>(null);

  useEffect(() => {
    if (players.length > 0) {
      setSelectedPlayer(players[0]);
    }
  }, [players]);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 p-6">
      <div className="w-full max-w-6xl bg-white shadow-lg rounded-lg flex">
        <div className="w-1/3 bg-gray-200 p-4 h-[500px] overflow-auto">
          <h2 className="text-xl font-bold mb-4 text-gray-800">Players</h2>
          <div className="space-y-2">
            {players.map((player) => (
              <div
                key={player.id}
                className={`p-3 rounded-lg cursor-pointer border border-gray-300 transition-all ${
                  selectedPlayer?.id === player.id
                    ? "bg-blue-500 text-white"
                    : "hover:bg-gray-300"
                }`}
                onClick={() => setSelectedPlayer(player)}
              >
                <h3 className="text-lg font-semibold">{player.name}</h3>
                <p className="text-sm">{player.university}</p>
              </div>
            ))}
          </div>
        </div>

        <div className="w-2/3 p-6 h-[500px] overflow-y-auto">
          {selectedPlayer ? (
            <PlayerStats player={selectedPlayer} />
          ) : (
            <p className="text-center text-gray-500">
              Select a player to view stats
            </p>
          )}
        </div>
      </div>
    </div>
  );
}
