

from sample import runParser
import unittest

class SampleTest(unittest.TestCase):

    def test1(self):
        
        v = runParser("1+2\n")
        self.assertTrue( v == 3 )

        v = runParser("1*2\n")
        self.assertTrue( v == 2 )

        v = runParser("1-2\n")
        self.assertTrue( v == -1 )

        v = runParser("1/2\n")
        self.assertTrue( v == 0.5 )


if __name__ == "__main__":
    unittest.main()
        
