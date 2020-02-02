from robot.libraries.BuiltIn import BuiltIn
from datetime import datetime
import time


class listener(object):

    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        self.builtin = BuiltIn()

    def start_test(self,name,attributes):
        print("\nExecution Started for " + name + " at : " + datetime.now().strftime("%Y-%b-%d_%I:%M:%S_%p"))

    def end_test(self,name,attributes):        
        print("Execution Finished for " + name + " at : " + datetime.now().strftime("%Y-%b-%d_%I:%M:%S_%p"))
        if attributes['status'] == 'FAIL':
            print("Test Case " + name + " : FAILED")
            print("Reason: " + attributes['message'])
        elif attributes['status'] == 'PASS':
            print("Test Case " + name + " : PASSED")