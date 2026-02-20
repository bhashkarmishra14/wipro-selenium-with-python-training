*** Settings ***
Library    SeleniumLibrary
Resource   ./keywords.robot

*** Variables ***
${URL}      https://www.saucedemo.com/
${BROWSER}  chrome

*** Test Cases ***
Verify Complete Checkout Flow
            Open Browser To SauceDemo
            Login To Application
            Add Product To Cart
            Checkout Product
            Finish Order
            Close Browser

