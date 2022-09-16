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
    def Push (self, data):
        self.items.append(data)
        self.sorted.append(data)

        #sorting with semi-bubble algorithm
        #bool_case solve "Index out of list problem"
        if self.lenght >= 2:
            i = 1
            bool_case = True
            if i == self.lenght:
                bool_case = (self.sorted[-i] < self.sorted[0])
            else:
                bool_case = (self.sorted[-i] < self.sorted[-(i+1)])
            while (bool_case):
                self.sorted[-i] = self.sorted[-(i+1)]
                self.sorted[-(i+1)] = data
                i += 1 
                if i == self.lenght:
                    bool_case = (self.sorted[-i] < self.sorted[0])
                elif i < self.lenght:
                    bool_case = (self.sorted[-i] < self.sorted[-(i+1)])
                else: 
                    break

        elif self.lenght == 1:
            if self.sorted[1] < self.sorted[0]:
                self.sorted[1] = self.sorted[0]
                self.sorted[0] = data    
        self.lenght += 1

    
    #pop - method that delete last value from stack and the same value from sorted list
    def Pop (self):
        if self.lenght > 0:
            data = self.items.pop()
            i = 1
            while (data != self.sorted[-i]):
                i += 1
            self.sorted.pop(-i)
            self.lenght -= 1


    #Max - method that returns maximum value of stack
    def Max(self):
        return(self.sorted[-1])


# this function helps us to iterate sorting in Push-method in correct way
    def Case(self, i):
        if (i+1) == self.lenght - 1:
            return(self.sorted[-i] < self.sorted[0])
        else:
            return(self.sorted[-i] < self.sorted[-(i+1)])


if __name__ == '__main__':
    stack = Stack()
    outputs = []
    num_queries = int(sys.stdin.readline())
    for query in range(num_queries):
        query = sys.stdin.readline().split()
        #print('query:', query)
        if "push" in query:
            stack.Push(int(query[1]))     
        elif "pop" in query:
            stack.Pop()
        elif "max" in query:
            print(stack.sorted[-1])
        else:
            pass
