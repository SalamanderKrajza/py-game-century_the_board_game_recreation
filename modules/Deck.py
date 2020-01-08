import csv
import random
from modules.Card import Card

class Deck:
    """Class which contains CARDS objects and allows to operate on that objects"""
    def __init__(self, source_file):
        #Load playable cards from csv file
        self.load_cards(source_file)
        del (self.cards[0]) #Deleting header row in source file
        self.shuffle()


    def load_cards(self, source_file):
        path = f'modules/cards{source_file}.csv'

        with open(path, newline='') as csvfile:
            self.cards = list(csv.reader(csvfile, delimiter=';')) #I've removed "quotechar='|'" 
        
        #Converting all strings into the 
        for x in range(0, len(self.cards)):
            self.cards[x] = Card(card_type=self.cards[x][1], inputList=self.cards[x][2:7], outputList=self.cards[x][7:12])
    
    def shuffle(self):
        random.shuffle(self.cards)

    def pickOneCard(self):
        return self.cards.pop()
