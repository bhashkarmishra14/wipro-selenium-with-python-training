*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://automationexercise.com/

*** Test Cases ***
Logout User

    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

    # Verify home page
    Page Should Contain    Automation Exercise

    # Go to login page
    Click Element    xpath://a[contains(text(),'Signup / Login')]

    # Verify login section
    Page Should Contain    Login to your account

    # Login with correct credentials
    Input Text    xpath://input[@data-qa='login-email']    bhashkkar912new@gmail.com
    Input Text    xpath://input[@data-qa='login-password']    123456
    Click Button    xpath://button[@data-qa='login-button']

    # Verify login success
    Wait Until Page Contains    Logged in as    20s

    # Click logout
    Click Element    xpath://a[contains(text(),'Logout')]

    # Verify user navigated to login page
    Wait Until Page Contains    Login to your account    20s

    Close Browser