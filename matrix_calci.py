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
        if (choice.lower() == 'd'):
            print(self.a*self.b)
        else:
            for i in range(len(self.a)):
                print(f'[{sum(z for i in [self.a[i]*self.b[0]])} {sum(z for i in [self.a[i]*self.b[1].T])} {sum(z for i in [self.a[i]*self.b[3].T])}]')
    def div(self,a,b):
        print(self.a/self.b)
    def tra(self,a):
        print(self.a.T)
    def inc(self,a,incc):
        print(self.a + incc)
    def get(self,a,row,col):
        print(self.a[row])
        print((((self.a).T)[col]).T)
    def negative_out(self,a):
        for i in range(len(self.a)):
            for x in range(len(self.a[0])):
                if self.a[i,x]<0:
                    self.a[i,x] = 0
        print(self.a)

    def abss(self,a):
        for i in range(len(self.a)):
            for x in range(len(self.a[0])):
                if self.a[i,x]<0:
                    self.a[i,x] = abs(self.a[i,x])
        print(self.a)
    def sor(self,a):
        for i in self.a:
            print(sorted(i))

def input_mat():
    matrixStr = input(f'Enter matrix ')
    print(f'{type(matrixStr)} is mayrixstr')
    matrixList = ast.literal_eval(matrixStr)
    return np.array(matrixList)
intro()
calci = NpCalc(a,b)

def intro():
    print('Welcome to matrix calculator\nHere are some of the function of this calculator what doyou want to use')
    print('Add\nSubtract\nMultiply\nDivide\nTranspose\nSort\nAbsolute\nPositive element matrix\nIncrement of valuse\nGet row and column')
    print('For an operation enter first three letters of the operation')
    operation = input('Enter operation')
    if (operation.lower() == 'add' or operation.lower() == 'sub' or operation.lower() == 'mul' or operation.lower() == 'div'):
        
        a = input_mat()
        b = input_mat()
        if operation.lower() == 'add':
            calci.add(a,b)
        if operation.lower() == 'sub':
            calci.sub(a,b)
        if operation.lower() == 'mul':
            calci.mul(a,b)
        if operation.lower() == 'div':
            calci.div(a,b)
    else:
        a = input_mat()
        if operation.lower() == 'tra':
            calci.tra(a)
        if operation.lower() == 'inc':
            incc = input('Pass increment value')
            calci.inc(a,incc)
        if operation.lower() == 'get':
            row = input('Enter row: ')
            col = input('Enter col: ')
            calci.get(a,row,col)
        if operation.lower() == 'neg':
            calci.negative_out(a)
        if operation.lower() == 'abs':
            calci.abss(a)
        if operation.lower() == 'sor':
            calci.sor(a)
