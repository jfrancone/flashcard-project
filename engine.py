import tkinter
import csv
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

class Engine():
    def __init__(self):

        #Window Setup
        self.window = tkinter.Tk()
        self.window.title("Flashcards")
        self.window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)
        self.canvas = tkinter.Canvas(width = 850, height = 576, bg = BACKGROUND_COLOR, highlightthickness=0)
        #Card Images
        self.card_front_img = tkinter.PhotoImage(file = "images/card_front.png")
        #the first two arguments below are the position of the image
        self.card_img = self.canvas.create_image(425, 288, image = self.card_front_img)
        self.card_back_img = tkinter.PhotoImage(file = "images/card_back.png")
        #self.canvas.create_image(800, 526, image = self.card_back_img)
        
        #Flashcard Text
        self.language_name_img = self.canvas.create_text(400, 150, text = "French", font =("Ariel", 40,  "italic"))
        self.card_word = self.canvas.create_text(400, 253, text = "Trouve", font = ("Ariel", 60, "bold"))
        self.canvas.grid(column = 0, row = 0, columnspan = 2)
        self.french_flashcards = pandas.read_csv("data/french_words.csv")
        #Notice I changed orient to equal records. This gives the dictionary the proper format
        self.words_to_learn = self.french_flashcards.to_dict(orient='records')
        self.french_words = self.french_flashcards['French']
        self.french_words_list = self.french_words.to_list()

        self.pick_random_card()

        #Buttons
        self.x_button_img = tkinter.PhotoImage(file = "./images/wrong.png")
        self.x_button = tkinter.Button(image = self.x_button_img, highlightthickness=0, command = self.pick_random_card)
        self.x_button.image = self.x_button_img
        self.x_button.grid(column = 0, row = 1)
        self.check_button_img = tkinter.PhotoImage(file = "./images/right.png")
        self.check_button = tkinter.Button(image = self.check_button_img, highlightthickness=0, command = self.pick_random_card)
        self.check_button.grid(column = 1, row = 1)

    def run(self):
        self.window.mainloop()


    def pick_random_card(self):
        random_card = random.choice(self.words_to_learn)
        french_side = random_card["French"]
        self.canvas.itemconfig(self.card_img, image = self.card_front_img)
        self.canvas.itemconfig(self.card_word, text = french_side, fill = 'black')
        self.canvas.itemconfig(self.language_name_img, text = "French", fill = 'black')
        self.window.after(3000, self.flip_card, random_card)

    def flip_card(self, random_card):
        english_side = random_card["English"]
        self.canvas.itemconfig(self.card_img, image = self.card_back_img)
        self.canvas.itemconfig(self.card_word, text = english_side, fill = 'white')
        self.canvas.itemconfig(self.language_name_img, text = "English", fill = 'white')
            
            


