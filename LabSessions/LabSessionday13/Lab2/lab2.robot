*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php

*** Test Cases ***
Select State And City
    Open Browser    ${URL}    chrome
    Maximize Browser Window

    # Wait until dropdown is visible
    Wait Until Element Is Visible    xpath://select[@id='state']

    # Select State
    Select From List By Label    id=state    Uttar Pradesh

    # Select City
    Select From List By Label    id=city    Lucknow

    Sleep    2s
    Close Browser
