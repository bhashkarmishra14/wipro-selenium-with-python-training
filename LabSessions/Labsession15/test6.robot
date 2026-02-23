*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://automationexercise.com/

*** Test Cases ***
Contact Us Form

    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    10s

    # Verify home page
    Page Should Contain    Automation Exercise

    # Click Contact Us
    Click Element    xpath://a[contains(text(),'Contact us')]

    # Verify GET IN TOUCH
    Wait Until Element Is Visible    xpath://h2[contains(text(),'Get In Touch')]    20s
    # Fill contact form
    Input Text    name=name       Bhashhkkar
    Input Text    name=email      bhashkkar912new@gmail.com
    Input Text    name=subject    Testing Contact Form
    Input Text    id=message      This is Robot Framework testing message

    # Upload file
    Choose File    name=upload_file    C:/Users/bhash/Downloads/Pytest_Scenario_Based_MCQ_Questions.docx

    # Submit form
    Click Button    name=submit

    # Handle alert popup
    Handle Alert    ACCEPT

    # Verify success message
    Wait Until Page Contains    Success! Your details have been submitted successfully.    20s

    # Click Home button
    Click Element    xpath://span[contains(text(),'Home')]

    # Verify home page
    Page Should Contain    Automation Exercise

    Close Browser