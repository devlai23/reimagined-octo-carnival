from tkinter import *
import pyfirmata
import time

board = pyfirmata.Arduino('COM4')

it = pyfirmata.util.Iterator(board)
it.start()
digital_input = board.get_pin('d:10:i')
digital_input2 = board.get_pin('d:9:i')

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.p1int = 0
        self.p2int = 0
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "", font = ("Impact", 50)).grid(row=0)
        self.p1label = Label(self, text=("      " + str(self.p1int)), font=("Impact", 50))
        self.p1label.grid(row = 1, column = 0)
        Label(self, text = "         .       ").grid(row = 1, column= 1)
        self.p2label = Label(self, text=(str(self.p2int) + "      "), font=("Impact", 50))
        self.p2label.grid(row = 1, column = 2)
        Label(self, text="", font=("Impact", 50)).grid(row=2)

        while True:
            sw = digital_input.read()
            se = digital_input2.read()
            if sw is True:
                self.p1up()
            if se is True:
                self.p2up()
            time.sleep(0.5)
            root.update()

        # Button(self, text="Score", command = self.p1up).grid(row=3, column = 0, sticky = E)
        # Button(self, text = "Score", command = self.p2up).grid(row = 3, column=2, sticky = W)

    def p1up(self):
        self.p1int += 1
        self.p1label['text'] = "      " + str(self.p1int)
        root.update()
        if (self.p1int == 6):
            board.digital[12].write(1)

            # THIS IS THE LOOP WITH THE PROBLEMS
            # WHILE THIS LOOP IS RUNNING THE TKINTER SCREEN CRASHES
            while True:
                board.digital[13].write(1)
                time.sleep(.25)
                board.digital[13].write(0)
                time.sleep(.25)

    def p2up(self):
        self.p2int += 1
        self.p2label['text'] = str(self.p2int) + "      "
        root.update()
        if (self.p2int == 6):
            board.digital[12].write(1)

            # THIS IS THE LOOP WITH THE PROBLEMS
            # WHILE THIS LOOP IS RUNNING THE TKINTER SCREEN CRASHES
            while True:
                board.digital[13].write(1)
                time.sleep(.25)
                board.digital[13].write(0)
                time.sleep(.25)

root = Tk()
root.title("Score Keeper")
app = Application(root)
root.mainloop()