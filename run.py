import os, subprocess, time, webbrowser
from datetime import datetime
import pandas as pd
from robot.parsing.model import TestData

class Foundation:

	def __init__(self, projectPath):
		self.projectPath = projectPath
		self.scriptPath = projectPath + "\\TestAsset\\\\Scripts\\"
		self.resultPath = projectPath + "\\Result\\Result_" + datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

	def readRunManager(self):
		self.df = pd.read_csv(projectPath + "\\TestAsset\\RunManager.csv")

	def getSuiteName(self):
		#Get Suite list and their test cases from robot lib
		outputXMLList = ""
		for i in self.df.index:
			if (self.df['Run_Flag'][i]).lower() == 'yes':
				suiteName = str(self.df['Test Suite Name'][i])
				suiteResultFolder = self.resultPath + "\\" + suiteName[0:-6]
				outputXMLList = outputXMLList + suiteResultFolder + "\\output.xml "
				self.executeTestScript(suiteName, suiteResultFolder)
		return self.resultPath, outputXMLList

	def executeTestScript(self, suiteName, suiteResultFolder):
		#Run for each test cases in Suite
		outputXMLList = ""
		suitePath = self.scriptPath + suiteName
		suite = TestData(parent=None, source=suitePath)
		for testcase in suite.testcase_table:
			outputdir = suiteResultFolder + "\\" + testcase.name
			outputXMLList = outputXMLList + outputdir + "\\output.xml "
			cmd = ("python -m robot --listener listener --console none -d " + outputdir 
			+ " -t " + testcase.name + " " + suitePath)
			self.processCMD(cmd)
		self.mergeResults(suiteName[0:-6], suiteResultFolder, outputXMLList)

	def mergeResults(self, suiteName, outputdir, outputXMLList):
		cmd = ("python -m robot.rebot -R -N " + suiteName + " --logtitle " + suiteName + "_Log "
			+ "--reporttitle " + suiteName + "_Report -o output.xml -d " + outputdir 
			+ " " + outputXMLList)
		self.processCMD(cmd)

	def combineResults(self, outputdir, outputXMLList):
		cmd = ("python -m robot.rebot -N Combined_Suite --logtitle Overall_Execution_Log "
			+ "--reporttitle Overall_Execution_Report -o output.xml -d " + outputdir 
			+ " " + outputXMLList)
		self.processCMD(cmd)

	def processCMD(self, cmd):
		_process = subprocess.Popen(cmd, shell=True)
		_process.communicate()
		_process.kill()

if __name__ == "__main__":
	projectPath= os.path.dirname(os.path.realpath(__file__))
	obj = Foundation(projectPath)

	print("Reading Run Manager.............")
	obj.readRunManager()

	print("Starting Execution............")
	resultPath, outputXMLList = obj.getSuiteName()

	print("\nStarting merging of Results...\n")
	obj.combineResults(resultPath, outputXMLList)
	time.sleep(1)
	print("\n** Test Execution Finished **")

	webbrowser.open('file://' + resultPath + "/log.html", new=2)

