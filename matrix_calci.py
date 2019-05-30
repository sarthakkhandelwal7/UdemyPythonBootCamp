import ast
import numpy as np
class NpCalc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self,a,b):
        print(self.a + self.b)
    
    def subtract(self,a,b):
        print(self.a - self.b)
    
    def multiply(self,a,b):
        choice = input('What tupe of product you want d: for dot and e: for element wise')
        if (choice == 'e'):
            print(self.a*self.b)
        else:
            print(np.dot(a,b))
    
    def divide(self,a,b):
        print(self.a/self.b)
    
    def transpose(self,a):
        print(self.a.T)
    
    def increment(self,a,incc):
        print(self.a + incc)
    
    def get_row_and_column(self,a,row,col):
        print(self.a[row])
        print((((self.a).T)[col]).T)
    
    def negative_out(self,a):
        for i in range(len(self.a)):
            for x in range(len(self.a[0])):
                if self.a[i,x]<0:
                    self.a[i,x] = 0
        print(self.a)

    def absolute(self,a):
        for i in range(len(self.a)):
            for x in range(len(self.a[0])):
                if self.a[i,x]<0:
                    self.a[i,x] = abs(self.a[i,x])
        print(self.a)
    
    def sort(self,a):
        for i in self.a:
            print(sorted(i))

def input_mat():
    """
    Take matrix as a string and convert it to a nested list
    using ast library
    and then converted to a numpy array using np.array function
    """
    matrixStr = input(f'Enter matrix as a string')
    matrixList = ast.literal_eval(matrixStr)
    return np.array(matrixList)


def intro():
    
    print('Welcome to matrix calculator\nHere are some of the function of this calculator what doyou want to use')
    
    print('\n1)Add\n2)Subtract\n3)Multiply\n4)Divide\n5)Transpose\n6)Sort\n7)Absolute\n8)Positive element matrix\n9)Increment of valuse\n10)Get row and column')
    
    print('\nFor an operation enter first three letters of the operation')
    
    operation = input('\nEnter operation: ')
    if (operation in ['1','2','3','4']):
        
        a = input_mat()
        b = input_mat()
        calci = NpCalc(a,b)
        
        if operation == '1':
            calci.add(a,b)
        
        elif operation == '2':
            calci.subtract(a,b)
        
        elif operation == '3':
            calci.multiply(a,b)
        
        elif operation == '4':
            calci.divide(a,b)
        
    else:
        a = input_mat()
        calci = NpCalc(a,None)
        
        if operation == '5':
            calci.transpose(a)
        
        elif operation == '6':
            calci.sort(a)
        
        elif operation == '7':
            calci.absolute(a)
        
        elif operation == '8':
            calci.negative_out(a)
        
        elif operation == '9':
            inc = int(input('Pass increment value'))
            calci.increment(a,inc)
        
        elif operation == '10':
            row = int(input('Enter row: '))
            col = int(input('Enter col: '))
            calci.get_row_and_column(a,row-1,col-1)
        
        
        
intro()