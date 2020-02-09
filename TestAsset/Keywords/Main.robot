*** Settings ***
Library    Screenshot
Library    BuiltIn
Library    autoit
Library    SeleniumLibrary
Variables    ../Locators/locators.yaml
Library    ../CustomLibrary/ExcelReader.py
Library    ../CustomLibrary/ExcelWriter.py

*** Variables ***
${temp}    https://www.amazon.com

*** Keywords ***
OpenNotepad
   Send    {LWINDOWN}
   Sleep    1
   Send    {r}
   Sleep    1
   Send    {LWINUP}
   Sleep    1
   Take Screenshot    Screen_01.jpg
   ${WinTitle}=   WinGetTitle    [ACTIVE]
   Log    ${WinTitle}
   Send    {ESC}
   Take Screenshot    Screen_02.jpg

Browser
   Open Browser    ${google.url}    ie
   Maximize Browser Window
   Take Screenshot    Browser_1.jpg
   Input Text    ${google.edtSearch}    ${google.txtSearch}
   Send    {ENTER}
   Wait Until Page Contains Element    ${google.edtLink}
   Take Screenshot    Browser_2.jpg
   Click Element    ${google.edtLink}
   Wait Until Page Contains Element    ${google.imgLogo}
   Take Screenshot    Browser_3.jpg

Amazon
   Open Browser    ${amazon.url}    gc
   #Maximize Browser Window
   Take Screenshot    Browser_1.jpg
   #${WinTitle}=  Get Title
   #Should Contain    ${WinTitle}    ${amazon.loginTitle}    msg='Ttitle does not match'
   Sleep    4
   Click Element    '(//span[@class='nav-action-inner'])[1]'
   Page Should Contain Element    ${amazon.edtSearch}    timeout=5.0
   Element Should Be Visible    ${amazon.edtSearch}    timeout=5.0
   Click Element    ${amazon.txtSearch}
   Input Text    ${amazon.edtSearch}    ${amazon.txtSearch}
   Sleep    0.200
   Take Screenshot    Browser_2.jpg
   Send    {ENTER}
   Wait Untill Page Contains Element    ${amazon.txtResult}    timeout=5.0
   Take Screenshot    Browser_3.jpg
   Should Contain    Get Title    'Amazon.in: '${amazon.txtSearch}
   Scroll Element Into View    ${amazon.result}
   Take Screenshot    Browser_4.jpg
   ${text}=    Get Text    ${amazon.result}
   Click Element    ${amazon.result}
   Wait Until Page Contains    ${text}    timeout=5.0
   Take Screenshot    Browser_5.jpg

GetData
   [Arguments]    ${Datatable}    ${rowId}
   ${rowVar}=    readRow    ${Datatable}    ${rowId}
   Log    ${rowVar['Name']}
   Log    ${rowVar['Age']}
   Log    ${rowVar['Tag_Name']}

SetData
   [Arguments]    ${Datatable}    ${rowId}
   #${rowVar}=    readRow    ${Datatable}    ${rowId}
   @{value}=    getIndex    Name    TC_02
   writeToFile    @{value}    hemendra






