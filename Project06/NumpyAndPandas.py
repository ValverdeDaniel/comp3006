#Daniel Valverde
#DU-ID: 873527848
#this program creates a numpy matrix, converts it to a csv named myMatrix.csv
#then converts that csv to a dataframe using pandas and generates some summary statistics for each column in the matrix
#lastly it saves the summary statistics and a couple of rows of sample data from the dataframe as myStatistics.txt

import numpy as np
import pandas as pd

def main():
    #part 1: creating matrix and saving as csv
    num_rows = 1000
    num_columns = 10
    matrix = np.random.randint(100, size = (num_rows, num_columns))
    print('my matrix')
    print(matrix)
    myHeader = "A,B,C,D,E,F,G,H,I,J"
    np.savetxt("myMatrix.csv", matrix, delimiter=',', header=myHeader, comments="")

    #part2: reading csv and converting to dataframe
    df = pd.read_csv("myMatrix.csv", header = 0)
    print('my csv to dataframe')
    print(df)

    #part3: mean, Std, Mode, Median for each column
    myMean = df.mean(axis=0)
    myStd = df.std()
    myMode = df.mode(dropna=True).head(1).transpose()
    myMedian = df.median()
    myTop3 = df.head(3)

    #part4: converting dataframe to string and then textfile
    dff = pd.DataFrame()
    dff['Mean'] = myMean
    dff['Standard Deviation'] = myStd
    dff['Mode'] = myMode
    dff['Median'] = myMedian
    dffStats = dff.to_string()
    print(dffStats)
    dffTop3 = myTop3.to_string()
    print(dffTop3)

    text_file = open("myStatistics.txt", "w")
    text_file.write("My Statistics \n \n")
    text_file.write(dffStats)
    text_file.write("\n \n")
    text_file.write("Top 3 Rows of Dataframe for Sample Data \n \n ")
    text_file.write(dffTop3)

    text_file.close()

main()



