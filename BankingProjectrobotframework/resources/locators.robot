*** Variables ***

${URL}    https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login

# Login Buttons (Angular stable locators)
${BANK_MANAGER_LOGIN}    xpath=//button[@ng-click='manager()']
${CUSTOMER_LOGIN}        xpath=//button[@ng-click='customer()']

# Manager Page Tabs
${ADD_CUSTOMER_TAB}      xpath=//button[@ng-click='addCust()']
${OPEN_ACCOUNT_TAB}      xpath=//button[@ng-click='openAccount()']

# Add Customer
${FIRSTNAME}             xpath=//input[@ng-model='fName']
${LASTNAME}              xpath=//input[@ng-model='lName']
${POSTCODE}              xpath=//input[@ng-model='postCd']
${ADD_CUSTOMER_BTN}      xpath=//button[@type='submit']

# Open Account
${CUSTOMER_DROPDOWN}     id=userSelect
${ACCOUNT_DROPDOWN}      id=currency
${PROCESS_BTN}           xpath=//button[contains(text(),'Process')]

# Customer Actions
${DEPOSIT_TAB}           xpath=//button[@ng-click='deposit()']
${WITHDRAW_TAB}          xpath=//button[@ng-click='withdrawl()']

${AMOUNT_FIELD}          xpath=//input[@ng-model='amount']
${SUBMIT_BTN}            xpath=//button[@type='submit']

# Balance
${BALANCE_TEXT}          xpath=(//strong[@class='ng-binding'])[2]