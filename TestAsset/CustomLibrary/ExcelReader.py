import pandas as pd
from os.path import dirname, abspath

filePath = dirname(dirname(abspath(__file__))) + "\\DataTables\\"

def readRow(fileDetail, rowId):
	fileName = filePath + fileDetail.split('.')[0] + ".xlsx"
	sheetName = fileDetail.split('.')[1]
	dataframe = pd.read_excel(fileName, sheetName)
	rowDict = dataframe.set_index('TestCaseName').T.to_dict('dict')[rowId]
	return rowDict


def writeToExcel(rowvar, columnname, valuetowrite):
	rowvar[columnname] = valuetowrite
	
