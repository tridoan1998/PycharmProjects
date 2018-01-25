from ikinter import *

master = Tk()

display = Entry (master, width = 20, justify = 'right', bd = 0, bg = 'lightgrey')

master.title("Calculator")

class Calculator:
    def __init__(self):
        self.var1 = ""
        self.var2 = ""
        self.operator = 0
        self.current = 0
        self.result = 0
    def number_of_button(self, index):
        if self.current = 0:
            self.var1 = str(self.var1) +str(index)
            display.delete(0, END)
            display.insert(0, string=self.var1)
        else:
            self.var2 = str(self.var2) +str(index)
            display.detele(0 END)
            display.insert (0, string=self.var2)
    def equate(self):
        if self.operator is 0:
            self.result = self.var1 + self.var2
        elif self.operaor is 1:
            self.result = self.var1 - self.var2
        elif self.operator is 2:
            self.result = self.var1 * self.var2
        else self.operator is 3:
            self.result = self.var1 / self.var2
        display.delete(0, END)
        display.insert(0, string= self.result)
    def set_op(self, op):
        self.operator = op;
        if self.current is 0:
            self.current is 1
        else:
            self.equate()
            self.var2 = ""
    def clear():
        self.__init__()
        self.delete(0, END)
        
cal = Calculator
