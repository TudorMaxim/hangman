'''
Created on 30 ian. 2018

@author: Asus
'''
from random import random, shuffle

class SentenceRepository:
    def __init__(self, fileName = "sentences.txt"):
        self.__sentences = []
        self.__fileName = fileName
        self.__load()

    def find(self, sentence):
        '''
        Search for a sentence in the list of sentences
        output:
            True if the sentence exists
            False, otherwise
        '''
        for s in self.__sentences:
            if s == sentence:
                return True
        return False
    
    def validate(self, sentence):
        '''
        Check if a sentence is valid or not
        output:
            True if it is valid
            Raise ValueError - otherwise
        '''
        s = sentence
        words = s.split(" ")
        if len(words) < 1:
            raise ValueError("A sentence must have at least 1 word and a word must have at least 3 letters!")
        for w in words:
            if len(w) < 3:
                raise ValueError("A sentence must have at least 1 word and a word must have at least 3 letters!")
        return True
        
    def add_sentence(self, sentence):
        '''
        Add a sentence in the repository
        If the sentence already exists or is invalid, raise ValueError
        '''
        self.validate(sentence)
        if self.find(sentence) == False:
            self.__sentences.append(sentence)
            self.__store()
            return 0 # EXIT_SUCCESS
        else:
            raise ValueError("There can be no duplicate sentences!")
    
    def pick_sentence(self):
        '''
        Pick a random sentence in order to play the game
        output - the random sentence
        '''
        l = []
        for i in range(len(self.__sentences)):
            l.append(i)
        shuffle(l)
        return self.__sentences[l[0]]
        
    def __load(self):
        '''
        Load the sentences from the text file
        '''
        try:
            fin = open(self.__fileName, "r")
            line = fin.readline().strip()
            while line != "":
                self.__sentences.append(line)
                #print(line)
                line = fin.readline().strip()
        except IOError:
            print("Error in opening the file")
        finally:
            fin.close()
            
    def __store(self):
        '''
        Store the sentences in the text file
        '''
        fout = open(self.__fileName, "w")
        for i in self.__sentences:
            line = i + '\n'
            fout.write(line)
           
            
            
