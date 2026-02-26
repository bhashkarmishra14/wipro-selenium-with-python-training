*** Settings ***
Library    SeleniumLibrary
Resource   locators.robot

*** Keywords ***

Open Browser And Launch App
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Set Selenium Timeout    10s

Login As Bank Manager
    Go To    ${URL}
    Wait Until Element Is Visible    ${BANK_MANAGER_LOGIN}
    Click Element    ${BANK_MANAGER_LOGIN}

Login As Customer
    Go To    ${URL}

    Wait Until Element Is Visible    ${CUSTOMER_LOGIN}    10s
    Click Element    ${CUSTOMER_LOGIN}


    Wait Until Element Is Visible    ${CUSTOMER_DROPDOWN}    10s

    Select From List By Index    ${CUSTOMER_DROPDOWN}    1
    Click Button    xpath=//button[text()='Login']

Add Customer
    Wait Until Element Is Visible    ${ADD_CUSTOMER_TAB}    10s
    Click Element    ${ADD_CUSTOMER_TAB}

    Wait Until Element Is Visible    ${FIRSTNAME}    10s

    Input Text    ${FIRSTNAME}    John
    Input Text    ${LASTNAME}    Wick
    Input Text    ${POSTCODE}    700001
    Click Button    ${ADD_CUSTOMER_BTN}
    Handle Alert    ACCEPT
Open Account
    Wait Until Element Is Visible    ${OPEN_ACCOUNT_TAB}    10s
    Click Element    ${OPEN_ACCOUNT_TAB}

    Wait Until Element Is Visible    ${CUSTOMER_DROPDOWN}    10s

    Select From List By Index    ${CUSTOMER_DROPDOWN}    1
    Select From List By Label    ${ACCOUNT_DROPDOWN}    Dollar
    Click Element    ${PROCESS_BTN}
    Handle Alert    ACCEPT

Deposit Amount
    Wait Until Element Is Visible    ${DEPOSIT_TAB}    10s
    Click Element    ${DEPOSIT_TAB}

    Wait Until Element Is Visible    ${AMOUNT_FIELD}    10s

    Input Text    ${AMOUNT_FIELD}    5000
    Click Button    ${SUBMIT_BTN}
Withdraw Amount
    Wait Until Element Is Visible    ${WITHDRAW_TAB}    10s
    Click Element    ${WITHDRAW_TAB}

    Wait Until Element Is Visible    ${AMOUNT_FIELD}    10s

    Input Text    ${AMOUNT_FIELD}    2000
    Click Button    ${SUBMIT_BTN}
Validate Balance
    ${balance}=    Get Text    ${BALANCE_TEXT}
    Log To Console    Current Balance is: ${balance}
    Should Not Be Empty    ${balance}

Suite Teardown       Close Browser