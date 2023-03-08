import json
import pandas as pd
import matplotlib as plt

#method1 to read json data
json_file = open('loan_data_json.json') #open json
data = json.load(json_file) #load json

#method2 to read json data: WITH and AS
#with open('loan_data_json.json') as json_file:
#    data = json.load(json_file)

#transform to dataframe
loandata = pd.DataFrame(data)
loandata.head()

loandata.info()
#finding unique values for the purpose column
loandata['purpose'].unique()

#describe the data
loandata.describe()
#describe data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

import numpy as np


#using exp to get annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#BACKGROUND ON ARRAY
array = np.array([1,2,3,4])

#0D array
array = np.array(43)

#1D array
array = np.array([1,2,3,4])

#2D array
array = np.array([[1,2],[3,4]])

#working with IF statement
a = 40 
b = 500
if b > a:
    print('b is greater than a')
#let's add more conditions
c = 1000
if b>a and b<c:
    print('b is greater than a but less than c')
#what if a condition is not met?
c = 20
if b>a and b<c:
    print('b is greater than a but less than c')
else: 
    print('no condition met')
#another condition different metrics
a=40
b=500
c=30
if b>a and b<c:
    print('b is greater than a but less than c')
elif b>a and b>c:
    print('b is greater than both a and c')
else:
    print('no conditions met')

#same thing using or
a=40
b=500
c=30
if b>a or b<c:
    print('b is greater than a or less than c')
elif b>a or b>c:
    print('b is greater than a or c')
else:
    print('no conditions met')

#FICO score
fico=700
if fico>=300 and fico<400:
    ficocat = 'very poor'
elif fico>=400 and fico<600:
   ficocat = 'poor'
elif fico>=600 and fico<660:
   ficocat = 'fair'
elif fico>=660 and fico<700:
   ficocat = 'good'
elif fico >=700:
    ficocat = 'excellent'
else:
    ficocat = 'unknown'
print(ficocat)

#for loops
fruits = ['apple','banana','pear','cherry']

for x in fruits:
    print(x)
    y = x + ' fruit'
    print(y)

for x in range(0,4):
    y = fruits[x]+' for sale'
    print(y)

length = len(loandata)

ficocat = []

#applying for loops to loan data
for x in range(0,length):
    category = loandata['fico'][x]
    if category >= 300 and category < 400:
        cat = 'very poor'
    elif category >= 400 and category <600:
        cat = 'poor'
    elif category >=600 and category <660:
        cat = 'fair'
    elif category >= 660 and category <700:
        cat = 'good'
    elif category >= 700:
        cat = 'excellent'
    else:
        cat = 'unknown'
    ficocat.append(cat) #results in list

ficocat = pd.Series(ficocat) #convert this list to a series

loandata['fico.category'] = ficocat #create column in loaddata df 

loandata.info()

#while loops
i = 1
while i < 10:
    print(i)
    i = i + 1

#python's try and accept
#testing error
#applying for loops to loan data
for x in range(0,length):
    category = loandata['fico'][x]

    try:
        if category >= 300 and category < 400:
            cat = 'very poor'
        elif category >= 400 and category <600:
            cat = 'poor'
        elif category >=600 and category <660:
            cat = 'fair'
        elif category >= 660 and category <700:
            cat = 'good'
        elif category >= 700:
            cat = 'excellent'
        else:
            cat = 'unknown'
    except:
        cat = 'unknown'
    ficocat.append(cat) #results in list

#sf.loc as conditional statements
#create a new column with certain conditions
# df.loc[df[colname] condition, newcolname = 'value if condition is met']
#for interest rates, a new column is wante. rate > 0.12 then high, else low

loandata.info()
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'
loandata['int.rate.type']

#number of loans/rows by fico.category

catplot = loandata.groupby(['fico.category']).size() #from loan data, group by fico category and count the number of rows (size)
catplot
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount
purposecount.plot.bar(color = 'red', width = 0.1)
plt.show()

#scatter plots
xpoint = loandata['dti']
ypoint = loandata['annualincome']
plt.scatter(xpoint,ypoint,color = 'blue')

#write to csv
loandata.to_csv('loan_cleaned.csv', index = True)