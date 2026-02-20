*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.saucedemo.com/
${browser}    firefox
${username}    standard_user
${password}    secret_sauce

*** Test Cases ***
Verify login scenario with valid credentials
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

    # wait until username field is visible
    Wait Until Element Is Visible    id:user-name

    # enter username
    Input Text    id:user-name    ${username}

    # enter password
    Input Text    id:password    ${password}

    # click login button
    Click Element    id:login-button

    # validate user is on home page (Products page)
    Wait Until Element Is Visible    xpath://span[text()='Products']
    Element Should Be Visible    xpath://span[text()='Products']

    Close Browser
