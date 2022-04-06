

from sample import runParser
import unittest

class SampleTest(unittest.TestCase):

    def test1(self):
        
        v = runParser("1+2\n")
        self.assertEqual( v, 3 )

        v = runParser("1*2\n")
        self.assertEqual( v, 2 )

        v = runParser("1-2\n")
        self.assertEqual( v, -1 )
        
        v = runParser("1/2\n")
        self.assertEqual( v, 0.5 )

    def test2(self):
        
        v = runParser("x=1\n"
                      "y=2\n"
                      "x+y\n"
                      )
        self.assertEqual( v, 3 )


    def test3(self):
        
        v = runParser("2 ^ 3\n")
        self.assertEqual( v, (2 ** 3) )


    def test4(self):
        
        v = runParser("(1+2)*3\n")
        self.assertEqual( v, 9)

        v = runParser("(1+2)/3\n")
        self.assertEqual( v, 1)

    def test5(self):
        
        v = runParser("10.0e+10\n")
        self.assertEqual( v, 10.0e+10)

        v = runParser("10.0E+10\n")
        self.assertEqual( v, 10.0e+10)
        

if __name__ == "__main__":
    unittest.main()
        
