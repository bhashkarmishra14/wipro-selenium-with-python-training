*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://automationexercise.com/

*** Test Cases ***
Verify All Products And Product Detail Page

    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

    # Verify home page
    Page Should Contain    Automation Exercise

    # Click Products
    Click Element    xpath://a[contains(text(),'Products')]

    # Verify products page
    Wait Until Location Contains    products    20s

    # Wait product list visible
    Wait Until Element Is Visible    xpath:(//div[@class='features_items'])[1]    20s

    # SAFE SCROLL (VALID KEYWORD)
    Scroll Element Into View    xpath:(//a[contains(text(),'View Product')])[1]
    Sleep    1s

    # Move mouse before click (Firefox fix)
    Mouse Over    xpath:(//a[contains(text(),'View Product')])[1]

    # Click view product
    Click Element    xpath:(//a[contains(text(),'View Product')])[1]

    # Verify product details page
    Wait Until Location Contains    product_details    20s

    Page Should Contain    Availability
    Page Should Contain    Condition
    Page Should Contain    Brand

    Close Browser