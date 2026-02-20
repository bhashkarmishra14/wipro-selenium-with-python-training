*** Settings ***
#setting we add the external library details,resources, set up and tear down commands

Library     SeleniumLibrary

*** Variables ***

#A scalar variable can only contain one value - $
#A list variable can contain multiple values @
#A dictionary variable can contain multiple key-value pairs - &

${name}        John
${city}        Hyderabad
${address}     St Peters Road

@{list1}       green    red    blue
@{list2}       apple    banana    grapes

&{creds}       username=admin    password=admin123
















