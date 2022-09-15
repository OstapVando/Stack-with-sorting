import sys

class Stack():
    def __init__(self):
        #stack object consists of two list 
        #first one - in order that it was appended/poped
        #secound - in order of element ascending
        self.items = []
        self.sorted =[]
        self.lenght = 0

    #add - method that add a new value to the stack 
    #and add a new value in sorted list in the right place
    def add (self, data):
        self.items.append(data)
        self.sorted.append(data)
        i = 2
        while (data < self.sorted[-i]):
            self.sorted[-(i-1)] = self.sorted[-i]
            self.sorted[-i] = data
            i += 1
        self.lenght += 1

    #pop - method that delete last value from stack and the same value from sorted list
    def pop (self):
        data = self.items.pop()
        i = 1
        while (data != self.sorted[-i]):
            i += 1
        self.sorted.pop(-(i-1))
        self.lenght -= 1

    #Max - method that returns maximum value of stack
    def max(self):
        print(self.sorted[-1])

    