import numpy as np
import pandas as pd

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

#part4: converting dataframe to string and then textfile
dff = pd.DataFrame()
dff['Mean'] = myMean
dff['Standard Deviation'] = myStd
dff['Mode'] = myMode
dff['Median'] = myMedian
dff2 = dff.to_string()
print(dff2)
text_file = open("myStatistics.txt", "w")
n = text_file.write(dff2)
text_file.close()




