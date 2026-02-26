*** Settings ***
Resource    ../resources/keywords.robot

Suite Setup       Open Browser And Launch App
Suite Teardown    Close Browser

*** Test Cases ***

Login Test
    Login As Bank Manager

Add Customer Test
    Login As Bank Manager
    Add Customer

Open Account Test
    Login As Bank Manager
    Open Account

Deposit Withdraw And Validate Balance
    Login As Customer
    Deposit Amount
    Withdraw Amount
    Validate Balance