import csv
import random
from modules.model.Card import Card

class Deck:
    """Class which contains CARDS objects and allows to operate on that objects"""
    def __init__(self, source_file):
        #Load Playable cards from csv file
        self.load_cards(source_file)
        del (self.cards[0]) #Deleting header row in source file
        self.shuffle()


    def load_cards(self, source_file):
        path = f'externaldata/cards{source_file}.csv'

        with open(path, newline='') as csvfile:
            self.cards = list(csv.reader(csvfile, delimiter=';')) #I've removed "quotechar='|'" 
        
        if source_file=='Buyable':
            pass

        #Converting all strings into the Card objects
        for x in range(0, len(self.cards)):
            if self.cards[x][1] == "Treasure": #Treasure card are loaded from different file and need to be readed in different way
                self.cards[x] = Card(card_type=self.cards[x][1], inputList=self.cards[x][4:10], points=self.cards[x][2], bonus=0)
            else:
                self.cards[x] = Card(card_type=self.cards[x][1], inputList=self.cards[x][2:7], outputList=self.cards[x][7:12])
        

    def shuffle(self):
        random.shuffle(self.cards)

    def pickOneCard(self):
        return self.cards.pop()
