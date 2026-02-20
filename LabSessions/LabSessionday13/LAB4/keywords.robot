*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${USERNAME}     standard_user
${PASSWORD}     secret_sauce

*** Keywords ***

Open Browser To SauceDemo
    Open Browser    https://www.saucedemo.com/    chrome
    Maximize Browser Window

Login To Application
    Input Text    id:user-name    ${USERNAME}
    Input Text    id:password     ${PASSWORD}
    Click Button  id:login-button

Add Product To Cart
    Click Button    id:add-to-cart-sauce-labs-backpack
    Click Element   class:shopping_cart_link

Checkout Product
    Wait Until Element Is Visible    id:checkout    10s
    Scroll Element Into View         id:checkout
    Click Element                    id:checkout

    Wait Until Page Contains Element    id:firstName    10s
    Input Text    id:firstName     Bhashkar
    Input Text    id:lastName      Mishra
    Input Text    id:postalCode    560001
    Click Element    id:continue


Finish Order
    Click Button    id:finish
    Page Should Contain    Thank you for your order!
