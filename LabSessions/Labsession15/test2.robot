*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://automationexercise.com/

*** Test Cases ***
Login User With Correct Credentials

    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

    # Verify home page
    Page Should Contain    Automation Exercise

    # Go to login page
    Click Element    xpath://a[contains(text(),'Signup / Login')]

    # Verify login text
    Page Should Contain    Login to your account

    # Enter login details
    Input Text    xpath://input[@data-qa='login-email']    bhashkkar912new@gmail.com
    Input Text    xpath://input[@data-qa='login-password']    123456

    # Click login
    Click Button    xpath://button[@data-qa='login-button']

    # Verify successful login
    Wait Until Page Contains    Logged in as    10s

    Close Browser
