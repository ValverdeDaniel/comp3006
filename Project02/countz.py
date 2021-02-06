#!/usr/bin/env python3
## Max Roschke
## Data Science 2, Project 01, Counting Characters -- Reference Implementation
import sys
import string

## function to do the counting
def add_frequencies(d, f, remove_case):
   '''Adds the character frequencies of the given text file to the given
   dictionary.

   Arguments:
      d (dict): map from characters (str) to frequency counts (int)
      f (file): text file to read characters from
      remove_case (bool): if true, runs .lower() on chars before mapping
   '''
   ## iterate through the file, char-by-char
   for line in f:
      for c in line:
         ## convert c to key (use 'remove_case' to check for lower-casing)
         key = c.lower() if remove_case else c

         ## increment that char in the dictionary
         if key in d:
            d[key] += 1
         else:
            d[key] = 1

   ## return that dictionary (unnecessary, but matches intuition when calling)
   return d

def counter(args):
   ## main function
   '''Prints out the frequencies of various characters in input files. Uses
   sys.argv to determine what those characters are, and which input files to
   read from.'''
   ## default settings
   output_chars = string.ascii_letters
   remove_case = True
   print_zeroes = False

   ## get "real arguments".  that is, ignore the script name
   args = []


   # args = sys.argv[1:]

   ## process the leading flags
   while args and args[0].startswith('-'):
      ## remove the next flag from the list
      arg = args.pop(0)

      ## handle that flag
      if arg == '-c':
         remove_case = False
      elif arg == '-l':
         output_chars = args.pop(0)
      elif arg == '-z':
         print_zeroes = True
      elif arg == '--':
         break
      else:
         ## unknown argument!
         print(f'unknown argument: \'{arg}\'', file=sys.stderr)

   ## if we have to remove the case, remove it from the output_chars first!
   if remove_case == True:
      output_chars = ''.join(c for c in output_chars if c.islower())
      print('output_chars',output_chars)

   ## the remaining arguments must all be files... process them!
   d = {}
   for filename in args:
      with open(filename, 'r') as f:
         d = add_frequencies(d, f, remove_case)

   dannysChars = []
   dannysLZChars = []
   dannysFreq = []
   dannysDict = {}

   ## print out the output characters, as requested, in CSV format
   for c in output_chars:
      ## get the frequency count from the dictionary, or zero if not present
      freq = d[c] if c in d else 0
      dannysFreq.append(freq)

      ## print that row, if needed (if zero, check print_zeroes first)
      if freq != 0 or print_zeroes:
         print(f'"{c}",{freq}')

   #dannys stuff to return a list
      # #####if freq != 0 or print_zeroes:
   dannysLZChars = [x for x in output_chars]
   # print('dannysLZChars',dannysLZChars)
   # print('dannys C And not C', d)
   # print('prints l chars:', output_chars)
   # print('prints first l freq:', freq)
   # print('dannysFreq', dannysFreq)

   ## return based on flag
   if arg == '-c':
      print('we have c')
      dannysDict = d
   elif arg == '-l':
      print('we have l')
      # to convert lists to dictionary
      dannysDict = {dannysLZChars[i]: dannysFreq[i] for i in range(len(dannysLZChars))}
   elif arg == '-z':
      print('we have z')
      # to convert lists to dictionary
      dannysDict = {dannysLZChars[i]: dannysFreq[i] for i in range(len(dannysLZChars))}
   elif arg == '--':
      print('break')
   else:
      print('shit!!! :(')

   return dannysDict


def main():
   """this is the main function and we are calling it """
   sys.argv = ['-l', 'abc', 'text.txt']
   args = sys.argv
   print('mainArgs: ',args)
   d= counter(args)
   print('main: ',d)

if __name__ == '__main__':
   main()





