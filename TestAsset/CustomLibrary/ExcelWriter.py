import pandas as pd
from xlrd import open_workbook
from xlwt import Workbook
from xlutils.copy import copy

filePath = "F:\\Study\\RobotFramework\\RobotFrameworkPilot\\TestAsset\\DataTables\\DataTable.xls"

def getIndex(colmLabel, rowId):
	dataframe = pd.read_excel(filePath, 'Data', )
	rowIndex= dataframe.loc[dataframe['TestCaseName']==rowId].index[0]
	colIndex= dataframe.columns.get_loc(colmLabel)
	return rowIndex, colIndex

def writeToFile(rowIndex, colIndex, value):
	rb = open_workbook(filePath)
	wb = copy(rb)
	s = wb.get_sheet('Data')
	s.write(rowIndex+1,colIndex,value)
	wb.save(filePath)