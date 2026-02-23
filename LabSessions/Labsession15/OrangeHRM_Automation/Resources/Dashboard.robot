*** Settings ***
Library    SeleniumLibrary

*** Keywords ***

Verify User Logged In
    Wait Until Location Contains    dashboard    15s