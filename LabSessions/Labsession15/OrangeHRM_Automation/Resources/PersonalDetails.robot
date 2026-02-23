*** Settings ***
Library    SeleniumLibrary

*** Keywords ***

Open Personal Details Page
    Wait Until Element Is Visible    xpath://span[text()='My Info']    20s
    Click Element    xpath://span[text()='My Info']

Change First Name
    [Arguments]    ${newname}

    Wait Until Element Is Visible    xpath:(//input[@name='firstName'])[1]    20s
    Clear Element Text    xpath:(//input[@name='firstName'])[1]
    Input Text    xpath:(//input[@name='firstName'])[1]    ${newname}

Change Last Name
    [Arguments]    ${lastname}

    Wait Until Element Is Visible    xpath:(//input[@name='lastName'])[1]    20s
    Clear Element Text    xpath:(//input[@name='lastName'])[1]
    Input Text    xpath:(//input[@name='lastName'])[1]    ${lastname}

Save Personal Details
    Wait Until Element Is Visible    xpath:(//button[@type='submit'])[1]    20s
    Scroll Element Into View    xpath:(//button[@type='submit'])[1]
    Click Button    xpath:(//button[@type='submit'])[1]

    Wait Until Page Contains    Successfully Updated    20s

Verify First Name Updated
    [Arguments]    ${newname}

    ${actual}=    Get Value    xpath:(//input[@name='firstName'])[1]
    Should Be Equal    ${actual}    ${newname}