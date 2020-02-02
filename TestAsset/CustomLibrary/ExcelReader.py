import pandas as pd

filePath = "F:\\Study\\RobotFramework\\RF_Pilot\\TestAsset\\DataTables\\"

def readRow(fileDetail, rowId):
	fileName = filePath + fileDetail.split('.')[0] + ".xlsx"
	sheetName = fileDetail.split('.')[1]
	dataframe = pd.read_excel(fileName, sheetName)
	#df.set_index("TestCaseName", inplace=True)
	rowDict = dataframe.set_index('TestCaseName').T.to_dict('dict')[rowId]
	return rowDict


### Add validation to check if file present
### Add validation to check sheet exists
### Add validation to check if column exists


