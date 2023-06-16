import tkinter


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
        self.canvas.create_image(425, 288, image = self.card_front_img)
        self.card_back_img = tkinter.PhotoImage(file = "images/card_back.png")
        #self.canvas.create_image(800, 526, image = self.card_back_img)
        
        #Flashcard Text
        self.engl_text = "French"
        self.french_text = "trouve"
        self.engl_text_img = self.canvas.create_text(400, 150, text = self.engl_text, font =("Ariel", 40,  "italic"))
        self.french_text_img = self.canvas.create_text(400, 253, text = self.french_text, font = ("Ariel", 60, "bold"))
        self.canvas.grid(column = 0, row = 0, columnspan = 2)

        #Buttons
        self.x_button_img = tkinter.PhotoImage(file = "./images/wrong.png")
        self.x_button = tkinter.Button(image = self.x_button_img, highlightthickness=0)
        self.x_button.image = self.x_button_img
        self.x_button.grid(column = 0, row = 1)
        self.check_button_img = tkinter.PhotoImage(file = "./images/right.png")
        self.check_button = tkinter.Button(image = self.check_button_img, highlightthickness=0)
        self.check_button.grid(column = 1, row = 1)

    def run(self):
        self.window.mainloop()