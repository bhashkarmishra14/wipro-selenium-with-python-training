*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify Tabs
    Open Browser    ${url}    chrome
    # maximize the browser window
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

    # -------- Switch Window Example --------
    Click Element    id=openwindow
    @{windows}=    Get Window Handles
    Log To Console    ${windows}
    @{titles}=    Get Window Titles
    Log To Console    ${titles}
    Switch Window    title=QAClick Academy - A Testing Academy to Learn, Earn and Shine
    Element Should Contain    xpath://body    info@qaclickacademy.com
    Switch Window    MAIN

    # -------- Switch Tab Example --------
    Click Element    id=opentab
    @{windows}=    Get Window Handles
    Log To Console    ${windows}
    @{titles}=    Get Window Titles
    Log To Console    ${titles}
    Switch Window    title=QAClick Academy - A Testing Academy to Learn, Earn and Shine
    Element Should Contain    xpath://body    info@qaclickacademy.com
    Switch Window    MAIN

    # close browser
    Close Browser