from sudoku import *

class Tests:
    """
    A bunch of functions to test the programme
    """
    def __init__(self):
        self.sudoku=Matrix("sudoku_example.txt")

    def main(self):
        #Run the test functions
        b=self.tests()
        
        #If the tests passes then
        if b:
            print("All tests are OK")
            print("Main is now running")
        else:
            print("WARNING TEST FAILURE")
        return b
    
        
        
    def tests(self):
        """
        Launch the tests
        #Input 
        NULL
        #Output
        boolean
        """
        b=True
        b=b*self.testGetLine()
        b=b*self.testGetColumn()
        b=b*self.testGetPossibleValues()
        b=b*self.testGetCellNumber()
        b=b*self.testGetLineNumber()
        b=b*self.testGetColumnNumber()
        b=b*self.testGetSquare()
        return b

    def testGetColumn(self):
        """ 
        A unitary test
        Return True and print "testGetColumn OK" if the test passed and 
        False and print "WARNING testGetColumn NOK" otherwise

        #Input
        Null
        #Output
        bolean
        """
        #Create of matrix 9x9 with zeros
        s=[]
        for j in range(0,9):
            i=random.randrange(0,9)
            s.append(self.sudoku.getColumn(i,j))
        #Let us transpose this matrix
        st=[]
        for i in range(0,9):
            l=[]
            for j in range(0,9):
                l.append(s[j][i])
            st.append(l)
        if st==self.sudoku.matrix:
            print("testGetColumn OK")
            return True
        else:
            print("WARNING testGetColumn NOK")
            return False

    def testGetLine(self):
        """ 
        A unitary test
        Return True and print "testGetLine OK" if the test passed and 
        False and print "WARNING testGetLine NOK" otherwise
        
        #Input
        Null
        #Output
        boolean
        """
        s=[]
        for i in range(0,9):
            j=random.randrange(0,9)
            s.append(self.sudoku.getLine(i,j))
        if s==self.sudoku.matrix:
            print("testGetLine OK")
            return True
        else:
            print("WARNING testGetLine NOK")
            return False
    
    def testGetPossibleValues(self):
        """
        A unitary test
        Return True and print "testGetPossibleValues OK" if the test passed and 
        False and print "WARNING testGetPossibleValues NOK" otherwise
        #Input
        Null
        #Output
        boolean
        """
        for i in range(0,9):
            for j in range(0,9):
                inter=list(set(self.sudoku.getPossibleValues(i,j)) & set(self.sudoku.getLine(i,j)) & set(self.sudoku.getColumn(i,j)) & set(self.sudoku.getSquare(i,j)))
                if inter!=[]:
                    print("WARNING testGetPossibleValues NOK")
                    return False
        print("testGetPossibleValues OK")
        return True
    
    def testGetCellNumber(self):
        """
        A unitary test
        Return True and print "testGetCellNumber OK" if the test passed and 
        False and print "WARNING testGetCellNumber NOK" otherwise
        #Input
        Null
        #Output
        boolean
        """
        cells=[]
        for i in range(0,9):
            for j in range(0,9):
                cells.append(self.sudoku.getCellNumber(i,j))
        for c in range(0,81):
            if cells[c]!=c:
                print("WARNING testGetCellNumber NOK")
                return False
            else:
                print("testGetCellNumber OK")
                return True
        
    def testGetLineNumber(self):
        """
        A unitary test
        Return True and print "testGetLineNumber OK" if the test passed and 
        False and print "WARNING testGetLineNumber NOK" otherwise
        #Input
        Null
        #Output
        boolean
        """
        lineNumber=[]
        for c in range(0,81):
            lineNumber.append(self.sudoku.getLineNumber(c))
        for i in range(0,9):
            for j in range(0,9):
                if lineNumber[i*9+j]!=i:
                    print("WARNING testGetLineNumber NOK")
                    return False
        print("testGetLineNumber OK")
        return True
        
        
    def testGetColumnNumber(self):
        """
        A unitary test
        Return True and print "testGetColumnNumber OK" if the test passed and 
        False and print "WARNING testGetColumnNumber NOK" otherwise
        #Input
        Null
        #Output
        boolean
        """
        columnNumber=[]
        for c in range(0,81):
            columnNumber.append(self.sudoku.getColumnNumber(c))
        for i in range(0,9):
            for j in range(0,9):
                if columnNumber[j]!=j:
                    print("WARNING testGetColumnNumber NOK")
                    return False
        print("testGetColumnNumber OK")
        return True
    
    def testGetSquare(self):
        """
        A unitary test
        Return True and print "testGetSquare OK" if the test passed and 
        False and print "WARNING testGetSquare NOK" otherwise
        #Input
        Null
        #Output
        boolean
        """
        pos=range(0,7,3)
        for lig in pos:
            for col in pos:
                l=self.sudoku.getSquare(lig,col)
                s=[]
                for i in range(lig,lig+3):
                    for j in range(col,col+3):
                        s.append(self.sudoku.matrix[i][j])
                if l!=s:
                    print("WARNING testGetSquare NOK")
                    return False

        print("testGetSquare OK") 
        return True

