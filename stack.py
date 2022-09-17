import sys
import numpy as np

class Stack():
    def __init__(self):
        self.items = np.array([0])
        self.sorted = np.array([0])

    #Add new element of stack    
    def Push (self, data):
        self.items = np.append(self.items, data)
        index = np.searchsorted(self.sorted, data)
        self.sorted = np.insert(arr=self.sorted, obj=index, values=data)
        
    #Delete last element of stack
    def Pop (self):
        data = self.items[-1]
        self.items = self.items[0:-1]
        index = np.searchsorted(self.sorted, data)
        self.sorted = np.concatenate((self.sorted[0:index], self.sorted[index+1::]))
        
    #Prints the greatest element of current stack
    def Max(self):
        print(self.sorted[-1])


if __name__ == '__main__':
    stack = Stack()
    
    num_queries = int(sys.stdin.readline())
    for query in range(num_queries):
        query = sys.stdin.readline().split()
        #print('query:', query)
        if "push" in query:
            stack.Push((int(query[1])))     
        elif "pop" in query:
            stack.Pop()
        elif "max" in query:
            stack.Max()
        else:
            pass
