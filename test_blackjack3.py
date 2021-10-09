"""Unit tests for the blackjack program."""
import unittest

import blackjack3

class TestBlackjack(unittest.TestCase):

    def test_score_basic(self):
        
        h=blackjack3.Hand([3])
        h.score()
        self.assertEqual((3,0),(h.total,h.soft_ace_count))

        h=blackjack3.Hand([3,2])
        h.score()
        self.assertEqual((5,0),(h.total,h.soft_ace_count))
           
        h=blackjack3.Hand([3,2,10])
        h.score()
        self.assertEqual((15,0),(h.total,h.soft_ace_count))

        # 11 counts as 10
        h=blackjack3.Hand([3,2,10,11])
        h.score()
        self.assertEqual((25,0),(h.total,h.soft_ace_count))
          
        # 12 counts as 10
        h=blackjack3.Hand([3,2,10,11,12])
        h.score()
        self.assertEqual((35,0),(h.total,h.soft_ace_count))

        # 13 counts as 10
        h=blackjack3.Hand([3, 2, 10, 11, 12, 13])
        h.score()
        self.assertEqual((45,0),(h.total,h.soft_ace_count))

    def test_part_one_cases(self):
        h=blackjack3.Hand([3,12])
        h.score()
        self.assertEqual((13,0),(h.total,h.soft_ace_count))
        h=blackjack3.Hand([5,5,10])
        h.score()
        self.assertEqual((20,0),(h.total,h.soft_ace_count))
        h=blackjack3.Hand([11,10,1])
        h.score()
        self.assertEqual((21,0),(h.total,h.soft_ace_count))
        h=blackjack3.Hand([1,5])
        h.score()
        self.assertEqual((16,1),(h.total,h.soft_ace_count))
        h=blackjack3.Hand([1,1,5])
        h.score()
        self.assertEqual((17,1),(h.total,h.soft_ace_count))
        h=blackjack3.Hand([1,1,1,7])
        h.score()
        self.assertEqual((20,1),(h.total,h.soft_ace_count))
        h=blackjack3.Hand([7,8,10])
        h.score()
        self.assertEqual((25,0),(h.total,h.soft_ace_count))


    def test_score_with_soft_aces(self):
        h=blackjack3.Hand([1])
        h.score()
        self.assertEqual((11,1),(h.total,h.soft_ace_count))
        
        h=blackjack3.Hand([1,10])
        h.score()
        self.assertEqual((21,1),(h.total,h.soft_ace_count))
        
        h=blackjack3.Hand([1,2,3])
        h.score()
        self.assertEqual((16,1),(h.total,h.soft_ace_count))
        
        h=blackjack3.Hand([1,2,3,1])
        h.score()
        self.assertEqual((17,1),(h.total,h.soft_ace_count))
        
        h=blackjack3.Hand([1,2,3,10])
        h.score()
        self.assertEqual((16,0),(h.total,h.soft_ace_count))
        
        h=blackjack3.Hand([1,2,3,10,1])
        h.score()
        self.assertEqual((17,0),(h.total,h.soft_ace_count))
        


    def test_stand_on_soft_rubric(self):
        STAND_ON_SOFT = True
        HIT_ON_SOFT = False
        """Soft strategy """
        # below stand on value, never stand
        pS=blackjack3.Strategy(16,STAND_ON_SOFT)
        h=blackjack3.Hand([5,8])
        self.assertFalse(pS.stand(h))
        h=blackjack3.Hand([5,7,3])
        self.assertFalse(pS.stand(h))
        # at stand on value, always stand
        h=blackjack3.Hand([5,7,2,2])
        self.assertTrue(pS.stand(h))
        h=blackjack3.Hand([5,5,5,1])
        self.assertTrue(pS.stand(h))
        h=blackjack3.Hand([5,1])
        self.assertTrue(pS.stand(h))
        # above stand value,always stand
        h=blackjack3.Hand([3,3,1])
        self.assertTrue(pS.stand(h))
        h=blackjack3.Hand([5,5,3,4])
        self.assertTrue(pS.stand(h))

        """Hard strategy"""
        # below stand on value, never stand
        pS=blackjack3.Strategy(16,HIT_ON_SOFT)
        h=blackjack3.Hand([5,7,3])
        self.assertFalse(pS.stand(h))
        h=blackjack3.Hand([5,8])
        self.assertFalse(pS.stand(h))
        # at stand on value, and the hand is hard....stand
        h=blackjack3.Hand([5,7,2,2])
        self.assertTrue(pS.stand(h))
        h=blackjack3.Hand([5,5,5,1])
        # at stand on value, and the hand is soft...no stand
        self.assertTrue(pS.stand(h))
        h=blackjack3.Hand([5,1])
        self.assertFalse(pS.stand(h))
        # above stand value , always stand
        h=blackjack3.Hand([3,3,1])
        self.assertTrue(pS.stand(h))
        h=blackjack3.Hand([5,5,3,4])
        self.assertTrue(pS.stand(h))
        
        

        
       
if __name__ == '__main__':
    unittest.main()

