*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://automationexercise.com/

*** Test Cases ***
Register User With Existing Email

    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

    # Verify home page
    Page Should Contain    Automation Exercise

    # Go to Signup/Login page
    Click Element    xpath://a[contains(text(),'Signup / Login')]

    # Verify signup section
    Page Should Contain    New User Signup!

    # Enter name and existing email
    Input Text    xpath://input[@data-qa='signup-name']    Bhashhkkar
    Input Text    xpath://input[@data-qa='signup-email']   bhashkkar912new@gmail.com

    # Click Signup button
    Click Button    xpath://button[@data-qa='signup-button']

    # Verify error message
    Wait Until Page Contains    Email Address already exist!    20s

    Close Browser