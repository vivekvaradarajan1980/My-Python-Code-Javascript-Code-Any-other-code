from pandas import *

"extract data frame from file, I renamed the file for convinience !!"

data=read_excel('c:\\Users\\vivek\\Desktop\\AFCsurvey.xlsx')


"How many are part of softwawre factory"

" here is where I use filters to parse on one or more columns and get the numbers !!!, how many said what bla bla "
" start of by eliminating the null value from receipient ID"

AIfilter=(data.iloc[:,12].str.contains(('AI')))
softwarefac=(data.iloc[:,11]=='Software Factory')
nonull_rid=(data.iloc[:,0].notnull())
dontknowotherprogram=(data.iloc[:,13].str.contains(('I did not')))

"total applied for software factory only"
print(data[softwarefac & nonull_rid].shape)

"total applied for AI"
print(data[AIfilter & nonull_rid].shape)

"total applied for both"
print(data[softwarefac & AIfilter & nonull_rid].shape)

"total applied to Software fac but didnt know about other program...."
print(data[softwarefac & nonull_rid &dontknowotherprogram].shape)

"use value_counts built in method , it gives some real breakdown into the specific column data"
print(data.iloc[:,83].value_counts())

