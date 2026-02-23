*** Settings ***
Resource    ../Variables.robot
Resource    ../Resources/Login.robot

*** Test Cases ***
TC_02 Verify Invalid Login

    Open OrangeHRM Login Page
    Enter Username    ${VALID_USER}
    Enter Password    wrongpass

    Click Login Button

    Verify Invalid Login Error

    Close All Browsers