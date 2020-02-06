*** Settings ***
Resource    ../Keywords/Main.robot

*** Test Cases ***
ReadExcelData
   GetData    DataTable.Data    TC_01
   GetData    Kroll.Sheet1    Run
   GetData    Kroll.Sheet2    New


