import random

numSides = 6
numRolls = 5
class Dice:

    def __init__(self):
        """
        Initializes dice to random numbers according to sides and number of dice
        """
        self.roll
    def __init__(self, hand):
        """
        Initializes dice to random numbers according to sides and number of dice
        """
        self.values = hand
        hand.sort()
    
    def roll(self):
        """
        Sets dice to random numbers based on how many sides we have
        """
        self.values = [random.randint(1, numSides) for i in range(0, numRolls)]
        self.values.sort()

    def score_hand(self):
        """
        Returns the score of a Yatzhee hand
        """ 
    
    def add_up(self):
        """
        Sums all dice values
        """
        return sum(self.values)

    def check_one_pair(self):
        """
        function checks if there are at least two equal dice in the dice list.
        - returns bool
        """
        hand = self.values
        if (len(set(hand))) > 4:
            return False
        return True

        

    def check_two_pairs(self):
        '''
        function checks if there are two pairs in the dice list
        - updates scores
        - returns bool
        '''
        hand = self.values
        if (hand[0] == hand[1] and hand[2] == hand[3]) or (hand[0] == hand[1] and hand[3] == hand[4]) or (hand[1] == hand[2] and hand[3] == hand[4]):
            return True
        return False

    def check_three_kind(self):
        '''
        function checks if there are at least three identical dice in the dice list.
        - updates scores
        '''
        hand = self.values
        if hand[0] == hand[2] or hand[1] == hand[3] or hand[2] == hand[4]:
            return True
        return False

    def check_four_kind(self):
        '''
        function checks if there are at least four equal dice in the dice list.
        - updates scores
        - returns bool
        '''
        hand = self.values
        if hand[0] == hand[3] or hand[1] == hand[4]:
            return True
        return False
        

    def check_low_straight(self):
        '''
        function checks if the dice in the dice list are in sequence 1-5. Only for hands of size 5
        - returns bool
        '''
        hand = self.values
        if len(set(hand)) == 5 and hand[4] == 5 and hand[0] == 1:
            return True
        return False

    def check_high_straight(self):
        '''
        function checks if the dice in the dice list are in sequence 2-6. Only for hands of size 5
        - returns bool
        '''
        hand = self.values
        if len(set(hand)) == 5 and hand[4] == 6 and hand[0] == 2:
            return True
        return False

    def check_full_house(self):
        """
        function checks if the dice are two equal plus three equal in the dice list. Only works for hands of size 5.
        - returns bool
        """
        hand = self.values
        #if the set representation of the list is 2, we have a possible full house. 
        if len(self.values) != 5:
            return False
        elif len(set(hand)) != 2:
            return False
        elif hand[1] != hand[3]:
            return True
        return False

    def check_yatzee (self):
        """
        if unique set then its a yhatzee
        """
        hand = self.values
        if len(set(hand)) == 1:
            return True
        return False