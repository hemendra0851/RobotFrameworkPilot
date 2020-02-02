import os, sys, subprocess, time, webbrowser
import pandas as pd
from datetime import datetime


class Foundation:

	def __init__(self, testAssetPath, testResultPath, timeStamp):
		self.testAssetPath = testAssetPath
		self.testResultPath = testResultPath
		self.timeStamp = timeStamp
		self.outputXMLList = ""
		self.RunManager_data = ""

	def readRunManager(self):
		self.RunManager_data = pd.read_csv(testAssetPath + "\\RunManager.csv")

	def executeScripts(self):
		for i in self.RunManager_data.index:
			temp_dict = {}
			if (self.RunManager_data['Run_Flag'][i]).lower() == 'yes':
				temp_dict['TC_Name'] = str(self.RunManager_data['Test Case Name'][i])
				testScriptPath = testAssetPath + "\\Scripts"
				self.mainoutputdir = testResultPath + "\\Result_" + timeStamp
				outputdir = self.mainoutputdir + "\\" + temp_dict['TC_Name'][0:-6]
				self.outputXMLList = self.outputXMLList + outputdir + "\output.xml "
				cmd = "python -m robot --listener listener --console none --outputdir " + outputdir + " " + testScriptPath + "\\" + temp_dict['TC_Name']
				self.processCMD(cmd)
		return self.mainoutputdir

	def mergeResults(self):
		cmd = "python -m robot.rebot --name Combined_TestSuite --logtitle Combined_Log --reporttitle Overall_Execution_Report --outputdir " + self.mainoutputdir + " " + self.outputXMLList
		self.processCMD(cmd)
		
	def processCMD(self, cmd):
		_process = subprocess.Popen(cmd, shell=True)
		_process.communicate()
		_process.kill()


if __name__ == "__main__":

	projectPath= os.path.dirname(os.path.realpath(__file__))
	testAssetPath = projectPath + "\\TestAsset"
	testResultPath = projectPath + "\\Result"
	timeStamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

	obj = Foundation(testAssetPath, testResultPath, timeStamp)

	print("Reading Run Manager.............")
	obj.readRunManager()

	print("\nStarting Execution............")
	mainoutputdir = obj.executeScripts()

	print("\nStarting merging of Results...\n")
	obj.mergeResults()
	time.sleep(1)
	print("\n** Test Execution Finished **")

	webbrowser.open('file://' + mainoutputdir + "/log.html", new=2)
