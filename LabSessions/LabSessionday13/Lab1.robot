*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${CHECKBOX_URL}    https://www.tutorialspoint.com/selenium/practice/check-box.php
${RADIO_URL}       https://www.tutorialspoint.com/selenium/practice/radio-button.php

*** Test Cases ***

Verify Checkbox Using Common XPath
    Open Browser    ${CHECKBOX_URL}    chrome
    Maximize Browser Window

    # Common xpath for Main Level 1 and Main Level 2
    ${elements}=    Get WebElements    xpath://input[starts-with(@id,'c_bs_')]

    FOR    ${element}    IN    @{elements}
        Click Element    ${element}
    END

    Close Browser


Verify Radio Button Impressive
    Open Browser    ${RADIO_URL}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    xpath://input[@value='igotthree']
    Click Element    xpath://input[@value='igotthree']

    Close Browser
