*** Settings ***
Resource    ../Variables.robot
Resource    ../Resources/Login.robot
Resource    ../Resources/Dashboard.robot

*** Test Cases ***

TC_01 Verify Successful Employee Login

    Open OrangeHRM Login Page
    Enter Username    ${VALID_USER}
    Enter Password    ${VALID_PASS}
    Click Login Button
    Verify User Logged In

    Close All Browsers