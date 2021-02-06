##INSTRUCTIONS:
#To Run from command line make sure that in count.py AMITesting = True there is a note at the top of count.py
#command line command: python test_count.py

#Description:
#This file tests the different combinations of flags in count.py
import unittest
import sys
import count

class TestCount(unittest.TestCase):

    def test_NO_flag(self):
        """This Tests looks at the c flag and determines if the dictionary reads only the letter that has been asked
        to count"""
        sys.argv = ['text.txt']
        print('testsys',sys.argv)
        result = count.main()
        print('testResult: ',result)
        check = {'a': 2, 'b': 2, 'c': 2, 'd': 2}
        self.assertDictEqual(result,check)


    def test_c_flag(self):
        """This Tests looks at the c flag and determines if the dictionary reads only the letter that has been asked
        to count"""
        sys.argv = ['-c', 'text.txt']
        print('testsys',sys.argv)
        result = count.main()
        print('testResult: ',result)
        check = {'A': 2, 'b': 2, 'C': 1, 'c': 1, 'D': 1, 'd': 1}
        self.assertDictEqual(result,check)

    def test_l_flag(self):
        """This Tests looks at the l flag and determines if the dictionary reads only the letter that has been asked
        to count"""
        sys.argv = ['-l', 'abc', 'text.txt']
        print('testsys',sys.argv)
        result = count.main()
        print('testResult: ',result)
        check = {'a': 2, 'b': 2, 'c': 2}
        self.assertDictEqual(result,check)

    def test_z_flag(self):
        """This Tests looks at the z flag and determines if the dictionary reads only the letter that has been asked
        to count"""
        sys.argv = ['-z', 'text.txt']
        print('testsys',sys.argv)
        result = count.main()
        print('testResult: ',result)
        check = {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        self.assertDictEqual(result,check)

    def test_c_l_flag(self):
        """This Tests looks at the -c -l flag and determines if the dictionary reads only the letter that has been asked
        to count"""
        sys.argv = ['-c', '-l', 'abcA', 'text.txt']
        print('testsys',sys.argv)
        result = count.main()
        print('testResult: ',result)
        check = {'a': 0, 'b': 2, 'c': 1, 'A': 2}
        self.assertDictEqual(result,check)

    def test_c_z_flag(self):
        """This Tests looks at the -c -z flag and determines if the dictionary reads only the letter that has been asked
        to count"""
        sys.argv = ['-c', '-z', 'text.txt']
        print('testsys',sys.argv)
        result = count.main()
        print('testResult: ',result)
        check = {'a': 0, 'b': 2, 'c': 1, 'd': 1, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, 'A': 2,
'B': 0, 'C': 1, 'D': 1, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
        self.assertDictEqual(result,check)



if __name__ == '__main__':
    unittest.main()
