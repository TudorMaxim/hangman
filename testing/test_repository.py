'''
Created on 30 ian. 2018

@author: Asus
'''
import unittest
from repository.repository import SentenceRepository


class RepositoryTestCase(unittest.TestCase):
  
    def test_find(self):
        sentences = SentenceRepository()
        a = "anna has apples"
        b = "I love hangman"
        self.assertEqual(sentences.find(a), True, "Assertion failed in repository find function")
        self.assertEqual(sentences.find(b), False, "Assertion failed in repository find function")
        
    def test_validate(self):
        sentences = SentenceRepository()
        a = "anna has apples"
        b = "I love hangman"
        self.assertEqual(sentences.validate(a), True, "Assertion failed in repository validate function")
        self.assertRaises(ValueError)
        
    def test_add_sentence(self):
        sentences = SentenceRepository()
        a = "anna has apples"
        b = "I love hangman"
        c = "Tudor tests the programe"
        self.assertRaises(ValueError)
        self.assertEqual(sentences.add_sentence(c), 0, "Assertion failed in repository add_sentence function")
    
    def test_pick_sentence(self):
        sentences = SentenceRepository()
        self.assertNotEqual(sentences.pick_sentence(), "", "Assertion failed in repository pick_sentence function")
    
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RepositoryTestCase))
    return suite

