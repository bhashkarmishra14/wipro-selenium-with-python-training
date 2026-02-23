*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/

*** Test Cases ***
Verify login scenario with valid credentials
    Open Browser    ${url}    chrome
    # maximize the browser window
    Maximize Browser Window
    Set Selenium Implicit Wait    3s
    Go Back
    Sleep    2s
    Go To    ${url}
    Sleep    2s
    Reload Page
    # close browser
    Close Browser