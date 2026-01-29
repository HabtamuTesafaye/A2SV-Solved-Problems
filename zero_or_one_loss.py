class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = {}
        players = set()

        # count the loss and collect the players
        for winner , loser in matches:
            players.add(loser)
            players.add(winner)

            if loser in loss_count:
                loss_count[loser] += 1
            else:
                loss_count[loser] = 1
            
        zero_loss = []
        one_loss = []

        # identify the player with the loss and no loss
        for player in players:
            if player not in loss_count:
                zero_loss.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)

        zero_loss.sort()
        one_loss.sort()

        return [zero_loss, one_loss]
