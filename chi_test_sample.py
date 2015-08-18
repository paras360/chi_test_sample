from scipy import stats 
import collections  
import pandas as pd 
import matplotlib.pyplot as plt 


loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

#counts the number of observations in each credit line
freq = collections.Counter(loansData['Open.CREDIT.Lines'])


#plots a bar graph showing the number of observations 
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

chi, p = stats.chisquare(freq.values())

print chi, p

#notes
#if the p value is greater > .05 then HO is true, thus, the data is evenly distributed. because the test statistics is 2048.xx and the p value is 0.0, the opposite of the hypothesis is true
#and the data is not normally distributed. in fact, the data is skewed right. 