*** Settings ***
Resource    ../Keywords/Main.robot

*** Test Cases ***
TC_02
   GetData    DataTable.Data    TC_01
   GetData    Kroll.Sheet1    Run
   GetData    Kroll.Sheet2    New


