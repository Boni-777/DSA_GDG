class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)
        players = set()
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            losses[loser] += 1
            zero_losses = []
            one_loss = []
        for p in players:
            c = losses.get(p, 0)
            if c == 0:
                zero_losses.append(p)
            elif c == 1:
                one_loss.append(p)
        zero_losses.sort()
        one_loss.sort()
        return [zero_losses, one_loss]
