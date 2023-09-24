

maxRolls = 3
def expectimax_Yhatzee(hand, numRolls):
        def value(hand, depth, index):
            if  depth == maxRolls:
                return hand.score_hand()
            if index == -1:
                return maxValue(hand, depth)
            elif 0 <= index and index < 6:
                return expValue(hand, depth, index)

        def maxValue(hand, depth):
            v = float('-inf')
            for i in range(0, 6):
                v = max(v, value(hand, depth, i))             
            return v
        def expValue(hand, depth, index):
            v = 0
            for successor in hand.generate_successors(index):
                if index == 5:
                    return value(successor, depth + 1, -1)
                p = 1 / 6
                v  += p * value(successor, depth + 1, -1)           
            return v
        actions = range(0, 6)
        values = []
        for i in range(0, 6):
            values.append(value(hand, numRolls, i))
        return actions[values.index(max(values))]