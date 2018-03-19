"""
PostDoc in Barcelona
Author: Damien Allonsius
Date: 2018/4/3
A programme to solve the Sudoku's problem using Backtracking technique
"""

"""
TODO: solve sudoku function 
TODO: 2eme étape : solve sudoku function avec une fonction intermédiaire qui a chaque étape fait une passe sur toutes les valeurs possibles qui ne contiennent qu'une seul entrée.
"""

import random
import time
import pygame.mixer
from pygame.locals import *

class Matrix:
    """
    The class of Matrix that reprensents the Sudoku
    """
    def __init__(self,file):
        """
        Defines the Matrix from a path which contains a 9x9 matrix. See sudoku_example.txt.
        #Input 
        file -> string
        #Output
        Null
        """
        matrix=[]
        with open(file,"r") as f:
            #Read the lines
            for line in f:
                l=[]
                #Read the elements of the line
                for e in line:
                    if e != "\n":
                        l.append(int(e))
                matrix.append(l)
        self.matrix=matrix
        #Record the number of backtrackings
        self.operation=0
            
    def getCellNumber(self,i,j):
        """
        Return the cell number from a line and a column
        #Input
        i-> integer between 0 and 9
        j-> integer between 0 and 9
        #Output
        integer between 0 and 9
        """
        return i*9 + j

    def getLineNumber(self,c):
        """
        Return the line number from a cell number
        #Input
        c-> integer between 0 and 9
        #Output
        integer between 0 and 9
        """
        return c//9

    def getColumnNumber(self,c):
        """
        Return the column number from a cell number
        #Input
        c-> integer between 0 and 9
        #Output
        integer between 0 and 9
        """
        return c%9
    

    def getLine(self, i,j):
        """
        Returns the sudoku's line which contains the coefficient 
        at position (i,j).

        #Input
        i -> integer between 1 and 9
        j -> integer between 1 and 9

        #Output
        list 
        """
        return self.matrix[i]
    
    def getColumn(self, i,j):
        """
        Returns the sudoku's column which contains the coefficient 
        at position (i,j).

        #Input
        i -> integer between 1 and 9
        j -> integer between 1 and 9

        #Output
        list 
        """
        c=[]
        for l in self.matrix:
            c.append(l[j])
        return c

    def getSquare(self,i,j):
        """
        Returns the sudoku's square (3x3 matrix) which contains the coefficient 
        at position (i,j).

        #Input
        i -> integer between 1 and 9
        j -> integer between 1 and 9

        #Output
        list 
        """
        isq=(i//3)*3
        jsq=(j//3)*3
        lSquare=[]
        for k in range(isq,isq+3):
            for l in range(jsq,jsq+3):
                lSquare.append(self.matrix[k][l])
        return lSquare
        
        

    def getPossibleValues(self, i, j):
        """
        Return a list of possible values, given a position (i,j)
        #Input
        i -> integer between 1 and 9
        j -> integer between 1 and 9
        
        #Output
        list
        """
        c=self.getColumn(i,j)
        l=self.getLine(i,j)
        square=self.getSquare(i,j)
        values=[]
        #Get the values of the corresponding lines and column (except zero)
        for e in c:
            if e != 0:
                values.append(e)
        for e in l:
            if e !=0:
                values.append(e)
        for e in square:
            if e !=0:
                values.append(e)
        #Return the values beteween 1 and 9 which do not appear in values
        possibleValues=[]
        for e in range(1,10):
            if not(e in values):
                possibleValues.append(e)
        return possibleValues

    def solveSudoku(self,c):
        """
        Solve the Sudoku
        #Input
        Null
        #Output
        Boolean
        """
        #If we have reached the last position then the Sudoku is complete
        if c==81:
            return True
        else:
            i=self.getLineNumber(c)
            j=self.getColumnNumber(c)
            #Test if the position is already filled
            if self.matrix[i][j] != 0:
                return self.solveSudoku(c+1)
            else:
                #If there is no possible values then the Sudoku is not filled correctly
                possibleValues=self.getPossibleValues(i,j)
                if possibleValues==[]:
                    return False
                else:
                    #Try all possible values 
                    for indexValue in range(0,len(possibleValues)):
                        self.matrix[i][j]=possibleValues[indexValue]
                        if(self.solveSudoku(c+1)):
                            return True
                     #If you reached the last possible value then put 0
                    self.matrix[i][j]=0
                    self.operation+=1
                    return False

class UI:
    """
    User Interface
    """
    def __init__(self):
        self.window = pygame.display.set_mode((1000,1000))
        
        one= pygame.image.load("1.png").convert_alpha()
        two= pygame.image.load("2.png").convert_alpha()
        three= pygame.image.load("3.png").convert_alpha()
        four= pygame.image.load("4.png").convert_alpha()
        five= pygame.image.load("5.png").convert_alpha()
        six= pygame.image.load("6.png").convert_alpha()
        seven= pygame.image.load("7.png").convert_alpha()
        eight= pygame.image.load("8.png").convert_alpha()
        nine= pygame.image.load("9.png").convert_alpha()
        
        self.numbers=[one,two,three,four,five,six,seven,eight,nine]
        
    def main(self):
        """
        The main function which is called to run the programme
        #Input
        NULL
        #Output
        NULL
        """
        #Create an object Matrix
        sudoku=Matrix("sudoku_example.txt")
        #Solve and print the Sudoku
        sudoku.solveSudoku(0)
        #Print the Sudoku
        print("\n")
        print("Number of backtrackings:" + str(sudoku.operation))
        self.printSudoku(sudoku)

    def printSudoku(self, sudoku):
        """
        Print a sudoku in console
        #Input
        sudoku -> Matrix
        #Output
        NULL
        """
        posi=-70
        posj=0
        for i in range(0,9):
            posi+=70
            posj=0
            if i%3==0:
                posi+=20
            for j in range(0,9):
                posj+=80
                if j%3==0:
                    posj+=20
                
                n=sudoku.matrix[i][j]
                if n!=0:
                    num=self.numbers[n-1]
                    position=num.get_rect()
                    position=position.move(posj,posi)
                    self.window.blit(num,position)
                pygame.display.flip()
        cont=1
        while cont:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    cont=0

