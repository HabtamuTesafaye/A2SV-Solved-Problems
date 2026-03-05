class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        player_ptr = trainer_ptr = 0
        matchs = 0

        while player_ptr < len(players) and  trainer_ptr < len(trainers):
            if players[player_ptr] <=  trainers[trainer_ptr]:
                matchs += 1
                player_ptr += 1

            trainer_ptr += 1
        
        return matchs