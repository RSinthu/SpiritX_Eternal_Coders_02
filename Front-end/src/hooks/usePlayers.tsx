import { useQuery } from "@tanstack/react-query";
import APIClient from "../services/apiClient";

export interface Player {
  id: number;
  name: string;
  university: string;
  category: string;
  totalRuns: number;
  ballsFaced: number;
  inningsPlayed: number;
  wickets: number;
  oversBowled: number;
  runsConceded: number;
  batting_strike_rate: number;
  batting_average: number;
  bowling_strike_rate: number;
  economy_rate: number;
  points: number;
  value: number;
}

const usePlayers = () => {
  return useQuery({
    queryKey: ["players"],
    queryFn: new APIClient<Player>("/players").getAll,
    staleTime: 1000 * 60 * 5,
  });
};

export default usePlayers;
