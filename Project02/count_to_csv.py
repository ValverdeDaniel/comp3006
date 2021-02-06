#example on how to run count_to_csv.py from command line
    #if you add the -c the order matters this is why i have the examples... sorry i built off of sample code provided by Dalton and couldn't fix everything in 3 days
    # python count_to_csv.py -c -z text.txt sample.csv
    # python count_to_csv.py -l abc text.txt sample.csv
#IMPORTANT!!!
#make sure that in count.py AmITesting = False in order to run count_to_csv There is a note at the top

#Description:
#This file runs the function in count.py and then prints the resulting dictionary into csv file
import csv
import sys
import count

def count2Csv():
    try:
        csvArgs = sys.argv
        csvFileArgs = [i for i in csvArgs if '.csv' in i]
        # print('csvFileArgs: ', csvFileArgs)
        csvFileName = ""
        for i in csvFileArgs:
            csvFileName += i

        # print(csvFileName)

        #removing the file name with csv from sys.argv
        csvArgs.remove(csvFileName)
        # print('csvArgs',csvArgs)



        d={}
        d = count.main()

        # print('countd', d)
        # csvFileName = "defaultCSV.csv"
        # print('csvArgs',sys.argv)

        #process that writes dictionary to csv
        a_file = open(csvFileName, "w")
        writer = csv.writer(a_file)
        for key, value in d.items():
            writer.writerow([key,value])
        a_file.close()

        print('you have successfully saved to the csv: ', csvFileName)
    except:
        print('make sure that you followed this format: python count_to_csv.py -c -z text.txt sample.csv')


def main():
    count2Csv()

main()
