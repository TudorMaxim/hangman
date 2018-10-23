'''
Created on 30 ian. 2018

@author: Asus
'''
import unittest
from controller.GameController import GameController
from repository.repository import SentenceRepository

class ControllerTestCase(unittest.TestCase):
    
    def test_add_sentence(self):
        sentence = GameController(SentenceRepository())
        a = "Tudor does tests"
        self.assertEqual(sentence.add_sentence(a), 0, "Assertion failed in controller add_sentence")
        self.assertRaises(ValueError)
        
    
    def test_pick_sentence(self):
        sentence = GameController(SentenceRepository())
        self.assertNotEqual(sentence.pick_sentence(), "", "Assertion failed in controller pick_sentence")
        
    def test_find(self):
        sentence = GameController(SentenceRepository())
        str = "Ana are mere"
        a = 'a'
        b = 'g'
        self.assertEqual(sentence.find(str, a), True, "Assertion failed in controller find function")
        self.assertEqual(sentence.find(str, b), False, "Assertion failed in controller find function")
        
    def test_hangman_style(self):
        sentence = GameController(SentenceRepository())
        s = "abc def ghi"
        ans = "a_c d_f g_i"
        wrong = "a_c_d_f_g_i"
        self.assertEqual(sentence.hangman_style(s), ans, "Assertion failed in controller hangman_style function")
        self.assertNotEqual(sentence.hangman_style(s), wrong, "Assertion failed in controller hangman_style function")
        
    def test_check_win(self):
        sentence = GameController(SentenceRepository())
        a = "ana has apples"
        b = "ana has a__les"
        self.assertEqual(sentence.check_win(a), True, "Assertion failed in controller check_win function")
        self.assertEqual(sentence.check_win(b), False, "Assertion failed in controller check_win function")
        
    def check_lose(self):
        sentence = GameController(SentenceRepository())
        a = "hang"
        b = "hangman"
        self.assertEqual(sentence.check_lose(a), False, "Assertion failed in controller check_lose function")
        self.assertEqual(sentence.check_lose(b), True, "Assertion failed in controller check_lose function")
        
    def test_update(self):
        sentence = GameController(SentenceRepository())
        a = "ana has apples"
        b = "a_a has a____s"
        ans = "ana has a____s"
        ch = 'n'
        self.assertEqual(sentence.update(a, b, ch), ans, "Assertion failed in controller update function")
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ControllerTestCase))
    return suite