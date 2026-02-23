*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://automationexercise.com/

*** Test Cases ***
Search Product

    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

    # Home page verify
    Page Should Contain    Automation Exercise

    # Open Products page
    Click Element    xpath://a[contains(text(),'Products')]

    # Wait products page
    Wait Until Location Contains    products    20s
    Wait Until Element Is Visible    id=search_product    20s

    # Search product
    Input Text    id=search_product    Blue Top
    Click Button    id=submit_search

    # IMPORTANT FIX
    # Instead of checking text, check searched products container
    Wait Until Element Is Visible    xpath://div[@class='features_items']
    Sleep    20s

    # Verify product visible
    Wait Until Element Is Visible    xpath:(//div[@class='productinfo text-center'])[1]
    Sleep    20s

    Close Browser