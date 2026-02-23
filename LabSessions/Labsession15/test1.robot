*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://automationexercise.com/

*** Test Cases ***
Register User Full Flow

    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

    # Go to Signup/Login
    Click Element    xpath://a[contains(text(),'Signup / Login')]

    # Signup details
    Input Text    xpath://input[@data-qa='signup-name']    Bhashhkkar
    Input Text    xpath://input[@data-qa='signup-email']   bhashkkar912new@gmail.com
    Click Button  xpath://button[@data-qa='signup-button']

    # Wait for account page (STABLE FIX)
    Wait Until Element Is Visible    id=password    20s

    # Account information
    Click Element    id=id_gender1
    Input Text       id=password    123456

    Select From List By Value    id=days    10
    Select From List By Value    id=months    5
    Select From List By Value    id=years    1998

    Click Element    id=newsletter
    Click Element    id=optin

    # Scroll before address section
    Scroll Element Into View    id=first_name

    # Address information
    Input Text    id=first_name    Bhashkar
    Input Text    id=last_name     Mishra
    Input Text    id=company       ABC Company
    Input Text    id=address1      Kolkata Street
    Input Text    id=address2      Near Park

    Select From List By Label    id=country    India

    Input Text    id=state     West Bengal
    Input Text    id=city      Kolkata
    Input Text    id=zipcode   700001
    Input Text    id=mobile_number    9876543210

    # Create account
    Scroll Element Into View    xpath://button[@data-qa='create-account']
    Click Button    xpath://button[@data-qa='create-account']

    # STABLE SUCCESS CHECK
    Wait Until Element Is Visible    xpath://a[@data-qa='continue-button']    20s

    Click Element    xpath://a[@data-qa='continue-button']

    Wait Until Page Contains    Logged in as    20s

    Close Browser