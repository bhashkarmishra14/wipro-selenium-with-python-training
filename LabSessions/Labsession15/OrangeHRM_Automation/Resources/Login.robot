*** Settings ***
Library    SeleniumLibrary
Resource   ../Variables.robot

*** Keywords ***

Open OrangeHRM Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    name=username    20s

Enter Username
    [Arguments]    ${username}
    Input Text    name=username    ${username}

Enter Password
    [Arguments]    ${password}
    Input Text    name=password    ${password}

Click Login Button
    Click Button    xpath://button[@type='submit']

Verify Invalid Login Error
    Wait Until Page Contains    Invalid credentials    10s