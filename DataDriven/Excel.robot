*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=C:/Users/bhash/PycharmProjects/Feb2026WiproRobotFramework/TestData/ddtLogindata.xlsx    sheet_name=ddtLogindata

Test Template    Login Test
Test Setup       Open Browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    firefox
Test Teardown    Close Browser

*** Test Cases ***
Login with user    ${username}    ${password}

*** Keywords ***
Login Test
    [Arguments]    ${username}    ${password}

    Wait Until Element Is Visible    xpath://input[@name='username']
    Input Text    xpath://input[@name='username']    ${username}
    Input Text    xpath://input[@name='password']    ${password}
    Click Element    xpath://button[@type='submit']
    # validate that the user is on the home page
    Wait Until Element Is Visible    xpath://h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']
    Element Should Be Visible    xpath://h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']
    #close browser
    Close Browser



