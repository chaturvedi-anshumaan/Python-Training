import pandas as pd

data = pd.read_excel(r'C:\Anshumaan_Sprint\Anshumaan_Learning\Assignments\assignment_data.xlsx')
print(data)


dataFrame = pd.DataFrame(data, columns=['Name','Gender','Height', 'Weight'])
dataFrame['BMI'] = " "
dataFrame['Status'] = " "

dfs = [row for _, row in dataFrame.groupby('Gender')]

dataFrameForFemale = pd.DataFrame(dfs[0])
dataFrameForFemale.is_copy = False

dataFrameForMale = pd.DataFrame(dfs[1])
dataFrameForMale.is_copy = False

print('\n DataFrame for Female:\n ', dataFrameForFemale)
dataFrameForMale = pd.DataFrame(dfs[1]);
print('\n DataFrame for Female:\n ', dataFrameForMale)

print('\n ===============================================================')
print('---------------Final DataFrames Output----------------------------')
print('===============================================================\n')


for i in dataFrameForFemale.index:
    dataFrameForFemale.loc[i, 'BMI'] = dataFrameForFemale['Weight'][i] / (dataFrameForFemale['Height'][i]/100)**2
    if(dataFrameForFemale.loc[i, 'BMI'] > 30):
        dataFrameForFemale.loc[i, 'Status'] = "High"
    else:
        dataFrameForFemale.loc[i, 'Status'] = "Low"


for i in dataFrameForMale.index:
    dataFrameForMale.loc[i, 'BMI'] = dataFrameForMale['Weight'][i] / (dataFrameForMale['Height'][i]/100)**2
    if(dataFrameForMale.loc[i, 'BMI'] > 30):
        dataFrameForMale.loc[i, 'Status'] = "High"
    else:
        dataFrameForMale.loc[i, 'Status'] = "Low"

print('\n DataFrame for Female: \n')
print(dataFrameForFemale.sort_values(by=['BMI'], ascending=False), '\n \n')
print('===============================================================\n')
print('\n DataFrame for Male: \n')
print(dataFrameForMale.sort_values(by=['BMI'], ascending=False))
