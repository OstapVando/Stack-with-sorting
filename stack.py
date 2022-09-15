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
    def Add (self, data):
        self.items.append(data)
        self.sorted.append(data)
        i = 2
        while (data < self.sorted[-i]):
            self.sorted[-(i-1)] = self.sorted[-i]
            self.sorted[-i] = data
            i += 1
        self.lenght += 1

    #pop - method that delete last value from stack and the same value from sorted list
    def Pop (self):
        data = self.items.pop()
        i = 1
        while (data != self.sorted[-i]):
            i += 1
        self.sorted.pop(-(i-1))
        self.lenght -= 1

    #Max - method that returns maximum value of stack
    def Max(self):
        print(self.sorted[-1])

    
if __name__ == '__main__':
    stack = Stack()

    num_queries = int(sys.stdin.readline())
    for i in range(num_queries):
        query = sys.stdin.readline().split()

        if query[i] == "push":
            stack.Push(int(query[1]))
        elif query[i] == "pop":
            stack.Pop()
        elif query[i] == "max":
            print(stack.Max())
        else:
            assert(0)