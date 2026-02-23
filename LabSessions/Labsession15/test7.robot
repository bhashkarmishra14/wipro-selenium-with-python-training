*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://automationexercise.com/

*** Test Cases ***
Verify Test Cases Page

    Open Browser    ${url}    firefox
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

    # Verify home page
    Page Should Contain    Automation Exercise

    # Click Test Cases
    Click Element    xpath://a[contains(text(),'Test Cases')]

    # STABLE verification (URL check)
    Wait Until Location Contains    test_cases    20s

    Close Browser