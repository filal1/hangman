import random
from typing import List, Union

class Hangman:
    """
    It's hangman game and this is in Python, that is played in the terminal.
    The Hangman game is a simple game where one or more players try to guess a word, each turn suggesting a letter.
    """

    def __init__(self):

        # add attributes
        
        self.nb_char_of_word: int = 0                                    # nb of characters of the selected word
        self.answer : str = ""                                           # answer given by the player
        self.letter = "1"
        self.count_of_good_answer = 0

        
        self.possible_words: List[str] = ["becode","learning","mathematics","sessions","hello","test"]
        """
        A possible_words attribute contains a list of words. 
        Out of these words, one will be selected as the word to find in the game. 
        """
        
        self.random_choice: str = random.choice(self.possible_words)
        """
        Makes a random choice in the list :possible_words.
        """
        
        self.word_to_find = list(self.random_choice)
        """
        Makes a list with the letters of the choosen word
        """
        
        self.nb_char_of_word: int  = len(self.word_to_find)               # nb of characters of the selected word
        # nb_char_of_underscore: int = "_ " * nb_char_of_word          # nb of _ when the game starts f.e. _ _ _ _ _
        """
        A word_to_find attribute contains a list of strings. Each element will be a letter of the word.
        """
        

        self.lives: int = 5
        """
        number of lives of the player
        """

        self.correctly_guessed_letters: List[str] = ["_ "] * self.nb_char_of_word  

        self.wrongly_guessed_letters : List[str]  = []

        self.turn_count : int = 0

        self.error_count : int = 0

        

    def game_over (self):
        print ("Game over ...")
        exit()


    def well_played(self):
        print (f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")
        exit()
    
    
    
    
    def play(self):

        
        
        while  self.letter == "1":

            print (self.correctly_guessed_letters)            

            self.answer = input("Enter a letter please ? ")
            if self.answer.isalpha():
                if self.answer in self.word_to_find :
                    

                    for i in range (len(self.word_to_find)):
                        if self.answer == self.word_to_find[i]:
                            self.correctly_guessed_letters [i] = self.answer
                            self.count_of_good_answer += 1 

                    self.turn_count += 1
                    self.letter = "1"
                
                    if self.count_of_good_answer == self.nb_char_of_word:
                        self.well_played()


                else:
                    self.wrongly_guessed_letters.append(self.answer)
                    self.error_count += 1
                    self.turn_count += 1
                    self.lives -= 1
                    if self.lives == 0:
                        self.game_over()

                    self.letter = "1"                    



            else:
                self.answer = input("Enter a valid letter please ?")
                self.letter = "1" 



    def start_game(self):
        
        
        
        while self.lives >=1 :
            
            self.play()


hangman_game = Hangman()
hangman_game.start_game()