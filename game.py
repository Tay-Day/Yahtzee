import random

numSides = 6
numRolls = 5
class Dice:

    def __init__(self, *args):
        """
        Initializes dice to random numbers according to sides and number of dice
        """
        if len(args) > 0 and isinstance(args[0], list):
            self.values = args[0]
            self.values.sort()
        else:
            self.roll()
    
    def get_hand(self):
        return self.values
    
    def roll(self):
        """
        Sets dice to random numbers based on how many sides we have
        """
        self.values = [random.randint(1, numSides) for i in range(0, numRolls)]
        self.values.sort()
    
    def roll_keeping(self, index):
        if index >= numRolls:
            return
        self.values[index] = random.randint(1, numSides)
    
    def generate_successors(self, index):
        if index >= numRolls:
            return [Dice(self.values.copy())]
        successors = []
        for n in range(1, 7):
            hand = self.values.copy()
            hand[index] = n
            successors.append(Dice(hand.copy()))
        return successors

    def score_hand(self):
        """
        Modified scoring algorithm for simplicity with expectimax
        TODO add full yhatzee functionality
        """ 
        if self.check_yatzee():
            return 50
        elif self.check_high_straight():
            return 40
        elif self.check_low_straight():
            return 30
        elif self.check_full_house():
            return 25
        elif self.check_four_kind() or self.check_three_kind():
            return self.add_up()
        else:
            return 0

    
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