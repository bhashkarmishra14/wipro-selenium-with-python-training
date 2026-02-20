*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.tutorialspoint.com/selenium/practice/alerts.php

*** Test Cases ***
Verify Tutorialspoint Alerts
    Open Browser    ${URL}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    xpath:(//button[normalize-space()='Alert'])[1]

    # -------- Simple Alert --------
    Click Element    xpath:(//button[normalize-space()='Alert'])[1]
    Handle Alert    action=ACCEPT    timeout=10
    Sleep    2s

    # -------- Confirmation Alert --------
    Click Element    xpath:(//button[normalize-space()='Click Me'])[2]
    Handle Alert    action=DISMISS    timeout=10
    Sleep    2s

    # -------- Prompt Alert --------
    Click Element    xpath:(//button[normalize-space()='Click Me'])[3]
    Input Text Into Alert    Hello=
    Sleep    2s
    Close Browser
