'''
Created on 30 ian. 2018

@author: Asus
'''
import sys

class Console():
    def __init__(self, sentences):
        self.__sentences = sentences
        
    def print_menu(self):
        print("Welcome to my Hangman Game")
        print("Type: ")
        print("0 - exit the program")
        print("1 - add a sentence")
        print("2 - play the game")
    
    def ui_add_sentence(self):
        try:
            s = input("Give the sentence that you want to add:")
            self.__sentences.add_sentence(s)
        except ValueError as ve:
            print(ve)
    
    def exit_program(self):
        sys.exit()
        
    def ui_play_game(self):
        '''
            Play the game
         '''
        sentence = self.__sentences.pick_sentence()
        s = self.__sentences.hangman_style(sentence)
        print(s + " - ")
        step = 0
        hangman = ""
        letters = "hangman"
        while True:
            if self.__sentences.check_win(s) == True:
                print(sentence + " - YOU WON")
                self.exit_program()
            if self.__sentences.check_lose(hangman) == True:
                print(sentence + " - YOU LOSE")
                self.exit_program()
            ch = input("You guess: ")
            if ch >= 'a' and ch <= 'z':
                if self.__sentences.find(sentence, ch):
                    s = self.__sentences.update(sentence, s, ch)
                    print(s + " - " + hangman)
                else:
                    hangman += letters[step]
                    step += 1
                    print(s + " - " + hangman)
            else:
                hangman += letters[step]
                step += 1
                print(s + " - " + hangman)
        print(s)
        
    def run_game(self):
        self.print_menu()
        options = {'1' : self.ui_add_sentence,
                   '2' : self.ui_play_game 
                   }
        while True:
            try:
                op = input("Choose an option: ")
                if op == '0':
                    break
                options[op]()
            except KeyError:
                print("Wrong option!")
                print("Type 1 to add a sentence or 2 to play the game!")
                