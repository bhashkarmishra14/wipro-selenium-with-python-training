*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://automationexercise.com/

*** Test Cases ***
Verify Subscription In Home Page

    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

    # Verify home page
    Page Should Contain    Automation Exercise

    # Scroll to footer (IMPORTANT FIX)
    Execute Javascript    window.scrollTo(0, document.body.scrollHeight)
    Sleep    2s

    # Verify SUBSCRIPTION text
    Wait Until Element Is Visible    xpath://h2[contains(text(),'Subscription')]
    Sleep    10s

    # Enter email
    Input Text    id=susbscribe_email    bhashkar912new@gmail.com

    # Click subscribe button
    Click Element    id=subscribe

    # Verify success message
    Wait Until Page Contains    You have been successfully subscribed!
    Sleep    5s

    Close Browser