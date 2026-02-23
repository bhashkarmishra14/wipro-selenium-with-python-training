*** Settings ***
Resource    ../Variables.robot
Resource    ../Resources/Login.robot
Resource    ../Resources/PersonalDetails.robot

*** Test Cases ***
TC_03 Verify Personal Details Modification

    Open OrangeHRM Login Page
    Enter Username    ${VALID_USER}
    Enter Password    ${VALID_PASS}
    Click Login Button

    Open Personal Details Page
    Change First Name    BhashkarNew
    Change Last Name     TestLast
    Save Personal Details

    Verify First Name Updated    BhashkarNew

    Close All Browsers