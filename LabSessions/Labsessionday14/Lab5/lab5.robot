*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://practice.automationtesting.in/

*** Test Cases ***
Verify Complete Purchase Flow

    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

    # ---------- Go to Shop ----------
    Click Element    xpath://a[contains(text(),'Shop')]

    # ---------- Add Product ----------
    Wait Until Element Is Visible    xpath:(//a[contains(text(),'Add to basket')])[1]    10s
    Scroll Element Into View         xpath:(//a[contains(text(),'Add to basket')])[1]
    Click Element                    xpath:(//a[contains(text(),'Add to basket')])[1]

    Sleep    2s

    # ⭐ IMPORTANT: USE TOP MENU BASKET (NOT VIEW BASKET BUTTON)
    Click Element    xpath://a[contains(text(),'Basket')]

    # ---------- Checkout ----------
    Wait Until Element Is Visible    xpath://a[contains(@class,'checkout-button')]    10s
    Scroll Element Into View         xpath://a[contains(@class,'checkout-button')]
    Click Element                    xpath://a[contains(@class,'checkout-button')]

    # ---------- Billing ----------
    Wait Until Element Is Visible    id=billing_first_name    10s

    Input Text    id=billing_first_name    John
    Input Text    id=billing_last_name     Doe
    Input Text    id=billing_email         john@test.com
    Input Text    id=billing_phone         9999999999
    Input Text    id=billing_address_1     Test Street
    Input Text    id=billing_city          Hyderabad
    Input Text    id=billing_postcode      500001

    # ---------- Place Order ----------
    Scroll Element Into View    id=place_order
    Click Element               id=place_order

    Sleep    3s
    Close Browser