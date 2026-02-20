*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://the-internet.herokuapp.com/download

*** Test Cases ***
Verify File Download Link
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    xpath://a[normalize-space()='sample-zip-file.zip']
    Click Element    xpath://a[normalize-space()='sample-zip-file.zip']

    Sleep    5s

    # Correct Downloads path
    ${files}=    List Files In Directory    C:/Users/bhash/Downloads
    List Should Contain Value   ${files}    sample-zip-file.zip

    Close Browser
