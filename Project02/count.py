   #Daniel Valverde
   #DU ID: 873527848

import sys
import string

#!!!INSTRUCTIONS!!!
#IMPORTANT!!! If you are running Tests you will need to set AmITesting = True
#IMPORTANT!!!if you are trying to run count.py from the command line or running count_to_csv set AmITesting = True

#How To properly run count.py from command line
#Make sure that AmITesting=False
#PS for combo flags -c needs to come first...sorry its maxs code and i couldnt figure out how to fix it
#python count.py -c -l abcA text.txt

#DESCRIPTION:
#This file counts the frequency of letters from text.txt file

AmITesting = True
#AmITesting = False


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
   ## counter function
   '''Prints out the frequencies of various characters in input files. Uses
   sys.argv to determine what those characters are, and which input files to
   read from.'''
   ## default settings
   output_chars = string.ascii_letters
   remove_case = True
   print_zeroes = False

   ## get "real arguments".  that is, ignore the script name
   ##for test
   # args = []
   if AmITesting == False:
      #TOGGLE comment for args below on when running from command line and off for running test_count.py
      args = sys.argv[1:]
   else:
      #TOGGLE comment args below on when running test_count.py and off for running from commnad line
      args = sys.argv

   # MAXS LOOPING THROUGH FLAGS
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
   print('args', args)
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
   # if arg == '-c':

   try:
      if '-c' in arg:
         print('we have c')
         if '\n' in d:
            del d['\n']
         dannysDict = d
      elif '-l' in arg:
         print('we have l')
         # to convert lists to dictionary
         dannysDict = {dannysLZChars[i]: dannysFreq[i] for i in range(len(dannysLZChars))}
      elif '-z' in arg:
         print('we have z')
         # to convert lists to dictionary
         dannysDict = {dannysLZChars[i]: dannysFreq[i] for i in range(len(dannysLZChars))}
      elif arg == '--':
         print('break')
      else:
         print('wooops!!!')
   except NameError:
      print('we have no flags')
      arg = False
      if '\n' in d:
         del d['\n']
      dannysDict = d
   else:
      arg = True
      # print('we made it to this else and argTrue')

   return dannysDict


def main():
   """this is the main function and we are calling it """

   #this was the in count.py sys.argv spoof
   # sys.argv = ['-z', 'text.txt']
   #end TOGGLE

   args = sys.argv
   # print('mainArgs: ',args)
   d= counter(args)
   print('main dictionary: ',d)
   return d

if __name__ == '__main__':
   main()





