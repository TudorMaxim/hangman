'''
Created on 30 ian. 2018

@author: Asus
'''
from repository.repository import SentenceRepository
from controller.GameController import GameController
from ui.console import Console

class Hangman():
    def play(self):
        sentences = GameController(SentenceRepository())
        console = Console(sentences)
        console.run_game()
        
if __name__ == '__main__':
    game = Hangman()
    game.play()