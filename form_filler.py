from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from utilities import code_to_state


def find_and_fill_names(driver, names: str, firstname_element_id: str, lastname_element_id: str) -> bool:
    names = names.split(' ')

    firstname = names[0]

    if len(names) == 1:
        lastname = "Kamau"
    else:
        # lastname is the last entry in the list
        lastname = names[-1]

    firstname_element = driver.find_element(By.ID, firstname_element_id)
    lastname_element = driver.find_element(By.ID, lastname_element_id)
    firstname_element.send_keys(firstname)
    lastname_element.send_keys(lastname)

    return True


def find_and_fill_email(driver, email: str, email_element_id: str, clear_element: bool = True) -> bool:

    if (email == "None\n") or (email == "None"):
        email = "tonykamau1996@gmail.com"

    email_element = driver.find_element(By.ID, email_element_id)

    if clear_element:
        email_element.clear()

    email_element.send_keys(email)

    # Check if the email entered is correct
    if email_element.get_attribute("value") != email:
        email_element.clear()
        email_element.send_keys(email)

    return True


def find_and_fill_phone(driver, phone: str, phone_element_id: str, clear_element: bool = True) -> bool:

    if (phone == "None\n") or (phone == "None"):
        phone = "795204551"
        find_and_select_country(driver, "Kenya", "CountryCodeId")

    phone_element = driver.find_element(By.ID, phone_element_id)

    if clear_element:
        phone_element.clear()

    phone_element.send_keys(phone)

    return True


def find_and_fill_accountnumber(driver, accountnumber: str, accountnumber_element_id: str) -> bool:

    accountnumber_element = driver.find_element(
        By.ID, accountnumber_element_id)
    accountnumber_element.send_keys(accountnumber)

    return True


def find_and_fill_amount(driver, amount: str, amount_element_id: str) -> bool:

    amount_element = driver.find_element(By.ID, amount_element_id)
    amount_element.send_keys(amount)

    return True


def find_and_click_continue(driver, continue_element_id: str) -> bool:

    continue_element = driver.find_element(By.ID, continue_element_id)
    continue_element.click()

    return True


def find_and_select_country(driver, country: str, country_element_id: str) -> bool:

    # Convert the country to lowercase and capitalize the first letter of each word
    country = country.title()

    country_element = Select(driver.find_element(By.ID, country_element_id))

    # Try to select the country, if it fails, return select Kenya
    try:
        country_element.select_by_visible_text(country)
        return True
    except NoSuchElementException:
        country_element.select_by_visible_text("Kenya")
        return False


def find_and_fill_address(driver, address: str, address_element_id: str) -> bool:

    if (address == "None\n") or (address == "None"):
        address = "316 Evergreen Mills Road"
    address_element = driver.find_element(By.ID, address_element_id)
    address_element.send_keys(address)

    return True


def find_and_fill_city(driver, city: str, city_element_id: str) -> bool:

    if (city == "None\n") or (city == "None"):
        city = "Nairobi"
    city_element = driver.find_element(By.ID, city_element_id)
    city_element.send_keys(city)

    return True


def find_and_fill_zipcode(driver, zipcode: str, zipcode_element_id: str) -> bool:

    if (zipcode == "None\n") or (zipcode == "None"):
        zipcode = "00100"
    zipcode_element = driver.find_element(By.ID, zipcode_element_id)
    zipcode_element.send_keys(zipcode)

    return True


def find_and_fill_state(driver, country: str, state: str, state_element_id: str) -> bool:

    try:
        state_element = driver.find_element(By.ID, state_element_id)
        if (state == "None\n") or (state == "None"):
            find_and_select_country(driver, "Kenya", "CountryCodeId")
            find_and_fill_phone(driver, "795204551", "cphonenumber")
            return False
    except NoSuchElementException:
        return True

    state_element = Select(state_element)
    country = country.title()
    state = code_to_state(country, state)
    if state:
        try:
            state_element.select_by_visible_text(state)
        except NoSuchElementException:
            find_and_select_country(driver, "Kenya", "CountryCodeId")
            find_and_fill_phone(driver, "795204551", "cphonenumber")
            return False
        return True
    else:
        find_and_select_country(driver, "Kenya", "CountryCodeId")
        find_and_fill_phone(driver, "795204551", "cphonenumber")
        return False


def find_and_fill_cardnumber(driver, cardnumber: str, cardnumber_element_id: str) -> bool:

    cardnumber_element = driver.find_element(By.ID, cardnumber_element_id)
    cardnumber_element.send_keys(cardnumber)

    # Check if the cardnumber entered is correct
    if cardnumber_element.get_attribute("value") != cardnumber:
        cardnumber_element.clear()
        cardnumber_element.send_keys(cardnumber)

    return True


def find_and_fill_cvv(driver, cvv: str, cvv_element_id: str) -> bool:

    cvv_element = driver.find_element(By.ID, cvv_element_id)
    cvv_element.send_keys(cvv)

    # Check if the cvv entered is correct
    if cvv_element.get_attribute("value") != cvv:
        cvv_element.clear()
        cvv_element.send_keys(cvv)

    return True


def find_and_fill_cardexpiry(driver, cardexpiry: str, expirymonth_element_id: str, expiryyear_element_id: str) -> bool:

    cardexpiry = cardexpiry.split('/')
    expirymonth = cardexpiry[0]
    expiryyear = cardexpiry[1]

    expirymonth_element = Select(
        driver.find_element(By.ID, expirymonth_element_id))
    expiryyear_element = Select(
        driver.find_element(By.ID, expiryyear_element_id))

    expirymonth_element.select_by_visible_text(expirymonth)
    expiryyear_element.select_by_visible_text(expiryyear)

    return True


def find_and_click_acceptterms(driver, acceptterms_element_id: str) -> bool:

    acceptterms_element = driver.find_element(
        By.ID, acceptterms_element_id)
    acceptterms_element.click()

    return True


def find_and_click_paynow(driver, paynow_element_id: str) -> bool:

    paynow_element = driver.find_element(By.ID, paynow_element_id)
    paynow_element.click()

    return True
