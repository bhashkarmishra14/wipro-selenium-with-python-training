*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}      https://www.amazon.in/

*** Test Cases ***
Verify radio buttons
        Open Browser        ${url}        chrome
        Maximize Browser Window

        # implicit wait (applies to all elements)
        Set Selenium Implicit Wait     10s

        Scroll Element Into View     xpath://a[contains(.,'Sell on Amazon')]
        Sleep     2s
        Click Element     xpath://a[contains(.,'Sell on Amazon')]
        Sleep     2s

        Title Should Be     Amazon.in: Selling on Amazon - Start Selling Now
        Close Browser