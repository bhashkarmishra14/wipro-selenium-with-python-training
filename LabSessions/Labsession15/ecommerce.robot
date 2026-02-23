*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://automationexercise.com/

#test1

*** Test Cases ***
Register User Full Flow
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

    Click Element    xpath://a[contains(text(),'Signup / Login')]
    Input Text    xpath://input[@data-qa='signup-name']    Bhashhkkarir
    Input Text    xpath://input[@data-qa='signup-email']   bhashkkar9912noew@gmail.com
    Click Button  xpath://button[@data-qa='signup-button']

    Wait Until Element Is Visible    id=password    20s
    Click Element    id=id_gender1
    Input Text       id=password    123456

    Select From List By Value    id=days    10
    Select From List By Value    id=months    5
    Select From List By Value    id=years    1998

    Click Element    id=newsletter
    Click Element    id=optin

    Scroll Element Into View    id=first_name
    Input Text    id=first_name    Bhashkar
    Input Text    id=last_name     Mishra
    Input Text    id=company       ABC Company
    Input Text    id=address1      Kolkata Street
    Input Text    id=address2      Near Park
    Select From List By Label    id=country    India
    Input Text    id=state     West Bengal
    Input Text    id=city      Kolkata
    Input Text    id=zipcode   700001
    Input Text    id=mobile_number    9876543210

    Scroll Element Into View    xpath://button[@data-qa='create-account']
    Click Button    xpath://button[@data-qa='create-account']

    Wait Until Element Is Visible    xpath://a[@data-qa='continue-button']    20s
    Click Element    xpath://a[@data-qa='continue-button']

    Wait Until Page Contains    Logged in as    20s
    Close All Browsers

#test2

Login User With Correct Credentials
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

    Click Element    xpath://a[contains(text(),'Signup / Login')]
    Input Text    xpath://input[@data-qa='login-email']    bhashkkar912new@gmail.com
    Input Text    xpath://input[@data-qa='login-password']    123456
    Click Button    xpath://button[@data-qa='login-button']

    Wait Until Page Contains    Logged in as    10s
    Close All Browsers


#test3

Login User With Incorrect Credentials
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

    Click Element    xpath://a[contains(text(),'Signup / Login')]
    Input Text    xpath://input[@data-qa='login-email']    bhsdf@gmail.com
    Input Text    xpath://input[@data-qa='login-password']    hujhn123
    Click Button    xpath://button[@data-qa='login-button']

    Wait Until Page Contains    Your email or password is incorrect!    20s
    Close All Browsers


#test4

Logout User
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

    Click Element    xpath://a[contains(text(),'Signup / Login')]
    Input Text    xpath://input[@data-qa='login-email']    bhashkkar912new@gmail.com
    Input Text    xpath://input[@data-qa='login-password']    123456
    Click Button    xpath://button[@data-qa='login-button']

    Wait Until Page Contains    Logged in as
    Click Element    xpath://a[contains(text(),'Logout')]
    Wait Until Page Contains    Login to your account

    Close All Browsers


#test5

Register User With Existing Email
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

    Click Element    xpath://a[contains(text(),'Signup / Login')]
    Input Text    xpath://input[@data-qa='signup-name']    Bhashhkkar
    Input Text    xpath://input[@data-qa='signup-email']   bhashkkar912new@gmail.com
    Click Button    xpath://button[@data-qa='signup-button']

    Wait Until Page Contains    Email Address already exist!
    Close All Browsers


#test6

Contact Us Form
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

    Click Element    xpath://a[contains(text(),'Contact us')]
    Wait Until Element Is Visible    xpath://h2[contains(text(),'Get In Touch')]

    Input Text    name=name    Bhashhkkar
    Input Text    name=email   bhashkkar912new@gmail.com
    Input Text    name=subject    Testing Contact Form
    Input Text    id=message    This is Robot Framework testing message

    Choose File    name=upload_file    C:/Users/bhash/Downloads/Pytest_Scenario_Based_MCQ_Questions.docx
    Click Button    name=submit
    Handle Alert    ACCEPT

    Wait Until Page Contains    Success! Your details have been submitted successfully.
    Click Element    xpath://span[contains(text(),'Home')]

    Close All Browsers


#test7

Verify Test Cases Page
    Open Browser    ${url}    firefox
    Maximize Browser Window

    Click Element    xpath://a[contains(text(),'Test Cases')]
    Wait Until Location Contains    test_cases

    Close All Browsers


#test8

Verify All Products And Product Detail Page
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Click Element    xpath://a[contains(text(),'Products')]
    Wait Until Location Contains    products

    Scroll Element Into View    xpath:(//a[contains(text(),'View Product')])[1]
    Mouse Over    xpath:(//a[contains(text(),'View Product')])[1]
    Click Element    xpath:(//a[contains(text(),'View Product')])[1]

    Wait Until Location Contains    product_details
    Page Should Contain    Availability
    Page Should Contain    Condition
    Page Should Contain    Brand

    Close All Browsers


#test9

Search Product
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Click Element    xpath://a[contains(text(),'Products')]
    Wait Until Element Is Visible    id=search_product

    Input Text    id=search_product    Blue Top
    Click Button    id=submit_search

    Wait Until Element Is Visible    xpath://div[@class='features_items']
    Close All Browsers


#test 10

Verify Subscription In Home Page
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Execute Javascript    window.scrollTo(0, document.body.scrollHeight)
    Wait Until Element Is Visible    xpath://h2[contains(text(),'Subscription')]

    Input Text    id=susbscribe_email    bhashkar912new@gmail.com
    Click Element    id=subscribe

    Wait Until Page Contains    You have been successfully subscribed!

    Close All Browsers