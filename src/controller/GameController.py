'''
Created on 30 ian. 2018

@author: Asus
'''
class GameController:
    def __init__(self, repo):
        self.__repository = repo
        
    def add_sentence(self, s):
        '''
        Add a sentece s to the repository
        Return 0 in case of success
        '''
        self.__repository.add_sentence(s)
        return 0 #EXIT_SUCCESS
        
    def pick_sentence(self):
        '''
        Pick a random sentence to play and return it
        '''
        return self.__repository.pick_sentence()
    
    def find(self, str, chr):
        '''
        Search for a char in a string
        output: True if it exists, False otherwise
        '''
        for i in range(len(str)):
            if str[i] == chr:
                return True
        return False

    def hangman_style(self, sentence):
        '''
        Return a sentence transformed in hangman style.
        Only the letters that appear in the first and last position of a word are showed
        input: the sentence
        output ans - the sentence transformed in hangman style
        '''
        to_print = ""
        snt = sentence
        s = sentence.split(" ")
        ans = ""
        for word in s:
            to_print += word[0]
            l = len(word) - 1
            to_print += word[l]
            
        for i in range(len(snt)):
            if self.find(to_print, snt[i]) == True:
                ans += snt[i]
            elif snt[i] != ' ':
                ans += "_"
            else:
                ans += " "
        return ans
                
    def check_win(self, sentence):
        '''
        Check if the player wins
        output: True if the player wins, False otherwise
        '''
        for i in range(len(sentence)):
            if sentence[i] == '_':
                return False
        return True
    
    def check_lose(self, sentence):
        '''
        Check if the player loses
        output: True if the player loses, False otherwise
        '''
        if sentence == "hangman":
            return True
        return False
    
    def update(self, sentence, s, ch):
        '''
        Update the sentence - replace all the appearences of _ in s cresponding to ch in sentences
        '''
        ans = ""
        for i in range(len(sentence)):
            if sentence[i] == ch:
                ans += ch
            else:
                ans += s[i]
        
        return ans
        
    
        