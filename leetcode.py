# Determine the Winner of a Bowling Game #2660

# You are given two 0-indexed integer arrays player1 and player2, representing the number of pins that player 1 and player 2 hit in a bowling game, respectively.

# The bowling game consists of n turns, and the number of pins in each turn is exactly 10.

# Assume a player hits xi pins in the ith turn. The value of the ith turn for the player is:

# 2xi if the player hits 10 pins in either (i - 1)th or (i - 2)th turn.
# Otherwise, it is xi.
# The score of the player is the sum of the values of their n turns.

# Return

# 1 if the score of player 1 is more than the score of player 2,
# 2 if the score of player 2 is more than the score of player 1, and
# 0 in case of a draw.

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def calculate_score(player: List[int]) -> int:
            score = 0
            n = len(player)
            for i in range(n):
                if i > 1 and (player[i - 1] == 10 or player[i - 2] == 10):
                    score += 2 * player[i]
                elif i > 0 and player[i - 1] == 10:
                    score += 2 * player[i]
                else:
                    score += player[i]
            return score
        
        score1 = calculate_score(player1)
        score2 = calculate_score(player2)
        
        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0