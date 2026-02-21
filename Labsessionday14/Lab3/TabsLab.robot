*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify Window And Tab
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

    # ---------- Switch Window Example ----------
    Click Element    id=openwindow

    @{windows}=    Get Window Handles
    Log To Console    ${windows}

    Switch Window    NEW
    Element Should Contain    xpath://body    info@qaclickacademy.com

    Switch Window    MAIN

    # ---------- Switch Tab Example ----------
    Click Element    id=opentab

    @{tabs}=    Get Window Handles
    Log To Console    ${tabs}

    Switch Window    NEW
    Element Should Contain    xpath://body    info@qaclickacademy.com

    Switch Window    MAIN

    Close Browser