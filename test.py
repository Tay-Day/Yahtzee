import unittest
import game
import expectimax

class TestYahtzeeScores(unittest.TestCase):
    def test_basicHands(self):
        testHand = [2, 2, 3, 3, 3]
        self.assertTrue(game.Dice(testHand).check_full_house())
        testHand = [2, 2, 3, 3, 4]
        self.assertFalse(game.Dice(testHand).check_full_house())
        testHand = [2, 3, 3, 3, 3]
        self.assertFalse(game.Dice(testHand).check_full_house())
        testHand = [2, 2, 2, 2, 3]
        self.assertFalse(game.Dice(testHand).check_full_house())
        testHand = [2, 2, 2, 2, 2]
        self.assertTrue(game.Dice(testHand).check_yatzee())
        testHand = [2, 3, 4, 5, 6]
        self.assertTrue(game.Dice(testHand).check_high_straight())
        self.assertFalse(game.Dice(testHand).check_yatzee())
        self.assertFalse(game.Dice(testHand).check_low_straight())
        self.assertFalse(game.Dice(testHand).check_three_kind())
        testHand = [1, 2, 3, 4, 5]
        self.assertTrue(game.Dice(testHand).check_low_straight())
        self.assertFalse(game.Dice(testHand).check_yatzee())
        self.assertFalse(game.Dice(testHand).check_high_straight())
        self.assertFalse(game.Dice(testHand).check_three_kind())
        testHand = [2, 3, 5, 3, 3]
        self.assertTrue(game.Dice(testHand).check_three_kind())
        testHand = [2, 2, 3, 3, 3]
        self.assertTrue(game.Dice(testHand).check_three_kind())
        self.assertTrue(game.Dice(testHand).check_two_pairs())
        self.assertTrue(game.Dice(testHand).check_one_pair())
        testHand = [1, 3, 4, 6, 2]
        self.assertEquals(game.Dice(testHand).add_up(), 16)
    def test_basicExpectimax(self):
        dice = game.Dice()
        bestMove = expectimax.expectimax_Yhatzee(dice, 0)
        dice.roll_keeping(bestMove)
        bestMove = expectimax.expectimax_Yhatzee(dice, 1)
        dice.roll_keeping(bestMove)
        bestMove = expectimax.expectimax_Yhatzee(dice, 2)
        dice.roll_keeping(bestMove)
        self.assertGreaterEqual(dice.score_hand(), 0)

        testHand = [1, 6, 6, 6, 6]
        dice = game.Dice(testHand)
        bestMove = expectimax.expectimax_Yhatzee(dice, 0)
        self.assertEquals(bestMove, 0)

        testHand = [1, 6, 6, 6, 1]
        dice = game.Dice(testHand)
        bestMove = expectimax.expectimax_Yhatzee(dice, 0)
        dice.roll_keeping(bestMove)
        bestMove = expectimax.expectimax_Yhatzee(dice, 1)
        
        testHand = [3, 2, 6, 4, 5]
        dice = game.Dice(testHand)
        bestMove = expectimax.expectimax_Yhatzee(dice, 0)
        dice.roll_keeping(bestMove)

if __name__ == '__main__':
    unittest.main()
