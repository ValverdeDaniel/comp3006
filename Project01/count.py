#Daniel Valverde
#592378718

#how to run in command line examples:
    #python count.py text.txt -c
        #reads text.txt counts letters a and A separately (case sensitive)
    #python count.py text.txt -l abccdd
        #reads through text.txt and counts only the letters specified ignores case sensitivity
    #python count.py text.txt -z
        #reads text.txt and counts the letters in the file but displays entire alphabet
        #including those that are not in file
    #python count.py text.txt -c -l aAbb
        #reads through text.txt and counts only the letters specified is case sensitive
    #python count.py text.txt -cz
        #
    #python count.py text.txt
        #reads text.txt counts letters a and A as the same character

#reads in 1 text file specified in command line
##TODO: read in more than one text file

import sys

#3 add_frequencies
def add_frequencies(d, file, remove_case):
    file = open(file, mode = 'r')
    text = file.read()
    file.close()
    if remove_case is True:
        text = text.lower()
    #print('text: ',text)

    add_frequencies('text.txt', False)

def other():

    f = open(sys.argv[1],"r")
    contents = f.read()
    f.close()

    #1. Parse the command line arguments -c, -l, -z
    #checking for arguments and flags
    arguments = []
    for i in sys.argv:
        arguments.append(i)
    #print('arguments', arguments)
    #finding all flags by looking through arguments for anything starting with a '-'
    #this process allows you to input flags as -c or -cl or -c -l
    flags = [i for i in arguments if '-' in i]
    #removing all '-' from flags list
    flags = [x.replace('-', '') for x in flags]
    flagsstr = " "
    flagsstr = flagsstr.join(flags)
    flags = [i for i in flagsstr]
    if ' ' in flags:
        flags.remove(' ')
    flags.sort()
    #print('flags2', flags)

    #2. create an empty Dictionary
    lettersCountDict = {}

    if ['c'] == flags:
        #print('we have a c')
        allLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cleanContents = ""
        lettersList = []
        uniqueLetters = []
        lettersCount = []
        for char in contents:
            if char in allLetters:
                cleanContents += char
        #print('cleanContents:', cleanContents)
        lettersList = [char for char in cleanContents]
        #print('lettersList: ',lettersList)
        S1 = set(lettersList)
        uniqueLetters = list(S1)
        uniqueLetters.sort()
#compares text file to  letters list
        for x in range(len(uniqueLetters)):
            lettersCount.append(lettersList.count(uniqueLetters[x]))
        lettersCountDict = {uniqueLetters[i]: lettersCount[i] for i in range(len(uniqueLetters))}
        #print('uniqueLetters: ', uniqueLetters)
        #print('lettersCount: ', lettersCount)
        #print('lettersCountDict: ', lettersCountDict)

        #4. Print out the elements of that dictionary in CSV FORMAT
        csvFormat = ""
        for key, value in lettersCountDict.items():
            csvFormat = csvFormat + '"' + key + '"' + "," + str(value) + "\n"
        print(csvFormat)

    if ['c','l'] == flags:
        #print(' we have a c and an l')
        #creating an ldict list for potential use with -l argument
        lDictList = arguments
        lDictList = [ x for x in lDictList if "-" not in x ]
        lDictList = [ x for x in lDictList if ".py" not in x ]
        lDictList = [ x for x in lDictList if ".txt" not in x ]
        lDictStr = ""
        lDictStr = lDictStr.join(lDictList)
        lDictList = [i for i in lDictStr]
        #print('lDictList: ', lDictList)
        #checking for characters from files; and declaring lists and dicts
        lettersCountDict = {}
        allowedKeys = lDictList
        cleanContents = ""
        lettersList = []
        lettersCount = []
        #converting allowedKeys to a list
        myKeys = [char for char in allowedKeys]
        #print(myKeys)
        #cleaning up the contents from the .txt files
        for char in contents:
            if char in allowedKeys:
                cleanContents += char
        #print('cleanContents:', cleanContents)
        lettersList = [char for char in cleanContents]
        #adding the count to the list lettersList
        for x in range(len(myKeys)):
            lettersCount.append(lettersList.count(myKeys[x]))
        lettersCountDict = {myKeys[i]: lettersCount[i] for i in range(len(myKeys))}
        # print('myKeys: ', myKeys)
        # print('lettersCount: ', lettersCount)
        # print('lettersCountDict: ', lettersCountDict)

        #4. Print out the elements of that dictionary in CSV FORMAT
        csvFormat = ""
        for key, value in lettersCountDict.items():
            csvFormat = csvFormat + '"' + key + '"' + "," + str(value) + "\n"
        print(csvFormat)


    if ['c','z'] == flags:
        # print(' we have a c and a z')
            #checking for characters from files; and declaring lists and dicts
        allowedKeys = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cleanContents = ""
        lettersList = []
        lettersCount = []
        #converting allowedKeys to a list
        myKeys = [char for char in allowedKeys]
        #print(myKeys)
        #cleaning up the contents from the .txt files
        for char in contents:
            if char in allowedKeys:
                cleanContents += char
        #print('cleanContents:', cleanContents)
        lettersList = [char for char in cleanContents]
        #adding the count to the list lettersList
        for x in range(len(myKeys)):
            lettersCount.append(lettersList.count(myKeys[x]))
        lettersCountDict = {myKeys[i]: lettersCount[i] for i in range(len(myKeys))}
        # print('myKeys: ', myKeys)
        # print('lettersCount: ', lettersCount)
        # print('lettersCountDict: ', lettersCountDict)

        #4. Print out the elements of that dictionary in CSV FORMAT
        csvFormat = ""
        for key, value in lettersCountDict.items():
            csvFormat = csvFormat + '"' + key + '"' + "," + str(value) + "\n"
        print(csvFormat)

    if ['c','l','z'] == flags:
        print('we have a c and l and z')

    if not flags:
        #print('we have no flags')
        contents = contents.lower()
        allLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cleanContents = ""
        lettersList = []
        uniqueLetters = []
        lettersCount = []
        for char in contents:
            if char in allLetters:
                cleanContents += char
        #print('cleanContents:', cleanContents)
        lettersList = [char for char in cleanContents]
        #print('lettersList: ',lettersList)
        S1 = set(lettersList)
        uniqueLetters = list(S1)
        uniqueLetters.sort()
        for x in range(len(uniqueLetters)):
            lettersCount.append(lettersList.count(uniqueLetters[x]))
        lettersCountDict = {uniqueLetters[i]: lettersCount[i] for i in range(len(uniqueLetters))}
        #print('uniqueLetters: ', uniqueLetters)
        #print('lettersCount: ', lettersCount)
        #print('lettersCountDict: ', lettersCountDict)

        #4. Print out the elements of that dictionary in CSV FORMAT
        csvFormat = ""
        for key, value in lettersCountDict.items():
            csvFormat = csvFormat + '"' + key + '"' + "," + str(value) + "\n"
        print(csvFormat)

    if ['l'] == flags:
        # print('we have an l')

        #creating an ldict list for potential use with -l argument
        lDictList = arguments
        lDictList = [ x for x in lDictList if "-" not in x ]
        lDictList = [ x for x in lDictList if ".py" not in x ]
        lDictList = [ x for x in lDictList if ".txt" not in x ]
        lDictStr = ""
        lDictStr = lDictStr.join(lDictList)
        lDictStr = lDictStr.lower()
        lDictList = [i for i in lDictStr]
        # print('lDictList: ', lDictList)
        #checking for characters from files; and declaring lists and dicts
        contents = contents.lower()
        lettersCountDict = {}
        allowedKeys = lDictList
        cleanContents = ""
        lettersCount = []
        #converting allowedKeys to a list
        myKeys = [char for char in allowedKeys]
        #cleaning up the contents from the .txt files
        for char in contents:
            if char in allowedKeys:
                cleanContents += char
        lettersList = [char for char in cleanContents]
        for x in range(len(myKeys)):
            lettersCount.append(lettersList.count(myKeys[x]))

        lettersCountDict = {myKeys[i]: lettersCount[i] for i in range(len(myKeys))}
        csvFormat = ""
        for key, value in lettersCountDict.items():
            csvFormat = csvFormat + '"' + key + '"' + "," + str(value) + "\n"
        print(csvFormat)

    if ['z'] == flags:  #print out lines for characters with frequency of 0
        #print('we have a z')
        #checking for characters from files; and declaring lists and dicts
        contents = contents.lower()
        lettersCountDict = {}
        allowedKeys = "abcdefghijklmnopqrstuvwxyz"
        cleanContents = ""
        lettersCount = []
        #converting allowedKeys to a list
        myKeys = [char for char in allowedKeys]
        #cleaning up the contents from the .txt files
        for char in contents:
            if char in allowedKeys:
                cleanContents += char
        lettersList = [char for char in cleanContents]
        #adding the count to the list lettersList
        for x in range(len(myKeys)):
            lettersCount.append(lettersList.count(myKeys[x]))
        lettersCountDict = {myKeys[i]: lettersCount[i] for i in range(len(myKeys))}

        #4. Print out the elements of that dictionary in CSV FORMAT
        csvFormat = ""
        for key, value in lettersCountDict.items():
            csvFormat = csvFormat + '"' + key + '"' + "," + str(value) + "\n"
        print(csvFormat)

    if ['l','z'] == flags:
        print('we have an l and a z')

main()
