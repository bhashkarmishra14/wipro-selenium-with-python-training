*** Settings ***
Library    Collections

*** Variables ***
${NAME}        Bhashkar
${CITY}        Hyderabad
${NUM1}        10
${NUM2}        20
@{FRUITS}      Apple    Banana    Mango
&{USER}        username=admin    password=admin123

*** Test Cases ***

Print Scalar Variable
    Log    ${NAME}

Print Sum Of Two Numbers
    ${sum}=    Evaluate    ${NUM1} + ${NUM2}
    Log    Sum is ${sum}

Use Variable Inside Sentence
    Log    I live in ${CITY}

Reassign Variable Inside Test Case
    ${NAME}=    Set Variable    John
    Log    Updated name is ${NAME}

Print First Item Of List
    Log    ${FRUITS}[0]

Loop Through List
    FOR    ${fruit}    IN    @{FRUITS}
        Log    ${fruit}
    END

Find Length Of List
    ${length}=    Get Length    ${FRUITS}
    Log    Length is ${length}

Print Dictionary Key Value
    Log    ${USER}[username]

Add New Key Value To Dictionary
    Set To Dictionary    ${USER}    role=admin
    Log    ${USER}[role]

Loop Through Dictionary
    FOR    ${key}    ${value}    IN    &{USER}
        Log    Key=${key} Value=${value}
    END



