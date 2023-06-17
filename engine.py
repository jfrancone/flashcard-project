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

        #Reading CSV File and Finding Words
        try:
            self.french_flashcards = pandas.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            self.french_flashcards = pandas.read_csv("data/french_words.csv")
            self.french_flashcards.to_csv("data/words_to_learn.csv", index = False)
                
        #Notice I changed orient to equal records. This gives the dictionary the proper format
        finally:
            self.words_to_learn = self.french_flashcards.to_dict(orient='records')
            self.random_card = None

        self.flip_timer = self.window.after(3000, self.flip_card)
        self.pick_random_card()

        #Buttons
        self.x_button_img = tkinter.PhotoImage(file = "./images/wrong.png")
        self.x_button = tkinter.Button(image = self.x_button_img, highlightthickness=0, command = self.pick_random_card)
        self.x_button.image = self.x_button_img
        self.x_button.grid(column = 0, row = 1)
        self.check_button_img = tkinter.PhotoImage(file = "./images/right.png")
        self.check_button = tkinter.Button(image = self.check_button_img, highlightthickness=0, command = self.check_button_click)
        self.check_button.grid(column = 1, row = 1)

    def run(self):
        self.window.mainloop()


    def pick_random_card(self):
        self.window.after_cancel(self.flip_timer)
        self.random_card = random.choice(self.words_to_learn)
        self.french_side = self.random_card["French"]
        self.canvas.itemconfig(self.card_img, image = self.card_front_img)
        self.canvas.itemconfig(self.card_word, text = self.french_side, fill = 'black')
        self.canvas.itemconfig(self.language_name_img, text = "French", fill = 'black')
        self.flip_timer = self.window.after(3000, self.flip_card)

    def flip_card(self):
        self.english_side = self.random_card["English"]
        self.canvas.itemconfig(self.card_img, image = self.card_back_img)
        self.canvas.itemconfig(self.card_word, text = self.english_side, fill = 'white')
        self.canvas.itemconfig(self.language_name_img, text = "English", fill = 'white')
            
    def check_button_click(self):
        #print(f"Old Dictionary: {self.words_to_learn}")
        #print(type(self.words_to_learn))
        self.words_to_learn.remove(self.random_card)
        words_to_learn_csv = pandas.read_csv("data/words_to_learn.csv")
        #print(words_to_learn_csv)
        my_word = words_to_learn_csv[words_to_learn_csv.French == self.french_side]
        print(my_word)
        my_word_index = words_to_learn_csv.index[words_to_learn_csv['French'] == self.french_side].tolist()
        print(my_word_index)
        words_to_learn_csv = words_to_learn_csv.drop(index = my_word_index)
        words_to_learn_csv.to_csv('data/words_to_learn.csv', index = False)
        #print(f"New Dictionary: {self.words_to_learn}")
        self.pick_random_card()
            


