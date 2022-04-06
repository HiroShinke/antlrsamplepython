

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
        

if __name__ == "__main__":
    unittest.main()
        
