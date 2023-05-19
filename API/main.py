# Build for a ATM API 
import json
import requests
import time

from fastapi import FastAPI
from pydantic import BaseModel

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

BNKRBankIP = '127.0.0.1'
BNKRGuiIP = '127.0.0.1'

accountInfo = {'Bank': 'value',
              'Iban': 'value',
              'Pincode': 'value',
              'Auth': 'value'}

bankInfo = {'Bank': 'value',
            'Name': 'value',
            'Iban': 'value',
            'Pincode': 'value',
            'Currency': 'value',
            'Status': 'value',
            'Time': time_string,
            'Auth': 'value'}


app = FastAPI()

# welcome page


app.post("/welcome")
async def welcome():
        return {"Welcome to BNKR ATM Services"}

# Login & Authentication


app.post("/login")
async def login ():
    # Account number
    # Iban info from the front-end
    Iban = requests.post(BNKRGuiIP, data = {'Iban': 'value'})
    Iban.text
    # Pincode info form the front-end
    pincode = requests.post(BNKRGuiIP, data = {'pincode': 'value'})
    pincode.text
    # Send Iban to the bank server to look for the pincode of that account.
    password = requests.post(BNKRBankIP, data = {'password': 'value'})
    password.text
    # Pincode Check
    falseCount = 0;
    if (pincode == password) :
            auth = "True";
            #response with acknowledgment massage
            r = requests.post(BNKRGuiIP, auth)
    elif (pincode != password & falseCount < 3) :
            auth = "False";
            #response with a denial & retry message
            r = requests.post(BNKRGuiIP, auth)
            falseCount += 1;
    else :
            # Reject user login with a error massage
            auth = "Blocked";
            #response with a denied & blocked warning
            r = requests.post(BNKRGuiIP, auth)

# Account conformation.


app.post("/account")
async def account():
    # get all the bank information from the bank database for the user
    bankInfo = requests.post(BNKRBankIP, params = bankInfo)
    bankInfo.text
    # sent account info to the front-end.
    bankInfo = requests.post(BNKRGuiIP, params = bankInfo)
    bankInfo .text
    # if there is a withdrawal
    # read the withdrawal amount
    withdrawal = requests.post(BNKRGuiIP, data = {"withdrawal": 'value'})
    withdrawal.text
    # request account currency amount form the bank info
    currency = requests.post(BNKRBankIP, data = {"currency": 'value'})
    currency.text
    # subtract the the withdrawal amount from the account amount
    currency = currency - withdrawal
    # update the from end with the new information
    withdrawal = requests.post(BNKRGuiIP, withdrawal)
    # send the new data to the bank server
    r = requests.post(BNKRBankIP, currency)
    # close the connection between the atm and the bank server.
    close = requests.post(BNKRGuiIP, data = {"close": "Thank you for using our services"})
    # -----------------------------------------------------------