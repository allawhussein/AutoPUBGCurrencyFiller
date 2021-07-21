from selenium import webdriver #this is needed to basicly anything
from selenium.webdriver import ActionChains #this used to open some hover menus
from selenium.webdriver.support import expected_conditions as EC #this is used to prevent the driver form clicking unloaded elements
from selenium.webdriver.common.by import By #this used for element finding method
from selenium.webdriver.common.keys import Keys #this is used to simiulate keyboard keys
from selenium.common.exceptions import TimeoutException
from services.variables import *
import time

def razer_gold_login(driver, window_handle, credentials, transaction_url):
    print(" -RGL: razer_gold_login() service is initiated")
    driver.switch_to.window(window_handle)
    
    print(" -RGL: getting transaction site")
    if transaction_url not in driver.current_url:
        print(" -RGL: reloading site")
        driver.get(transaction_url)

    razer_loading_logo_xpath = "/html/body/div/main/section/div/div/div/div[1]/div"
    webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.invisibility_of_element((By.XPATH, razer_loading_logo_xpath)))

    try:#re-call the function if it took to long to load the razer payment wall
        print(" -RGL: waiting for razer gold logo to appear")
        webdriver.support.ui.WebDriverWait(driver, razer_payment_wait).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/section/nav/div/div/img")))
    except:
        print(" -RGL: razer gold logo did not appear in " + str(razer_payment_wait))
        print(" -RGL: razer_gold_login() service will restart")
        driver.execute_script('window.localStorage.clear();')
        return razer_gold_login(driver, window_handle, credentials, transaction_url)
    
    print(" -RGL: starting login-procedure")
    time_zero = time.time()
    while time.time() - time_zero < time_of_waiting:
        try:#check for updates dialog
            webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dialogPanel1"]')))
            print(" -RGL: closing dialog")
            agree_button_xpath = "/html/body/div/div/div/div[4]/a"
            agree_button = driver.find_element_by_xpath(agree_button_xpath)
            webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.visibility_of_element_located((By.XPATH, agree_button_xpath)))
            webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.element_to_be_clickable((By.XPATH, agree_button_xpath)))
            driver.execute_script("arguments[0].click();", agree_button)
            time_zero = time.time()
        except:
            pass
        try:#hide every dialog
            i = 1
            while True:
                driver.execute_script("arguments[0].setAttribute('style','visibility:hidden;');",driver.find_element_by_id("dialogPanel"+str(i)))
                i += 1
        except:
            pass
        try:#this checks if we have an invalid link
            error_header = "/html/body/div/main/section/div/div/h4"
            driver.find_element_by_xpath(error_header)
            print(" -RGL: the link is invalid")
            return 0
        except:
            pass
        try:#verify successful login
            verifier_div_xpath = "/html/body/div/main/section/div/div/div/div[5]/div/div[1]/div[1]/div[1]/h5"
            assert driver.find_element_by_xpath(verifier_div_xpath).is_displayed()
            print(" -RGL: Logged in\n -RGL: razer_gold_login services is over")
            return 1
        except:
            pass
        try:#fill logging in information
            driver.find_element_by_xpath('//*[@id="loginEmail"]')
            print(" -RGL: filling login credentials")
            driver.find_element_by_xpath('//*[@id="loginEmail"]').send_keys(Keys.CONTROL + "a")
            driver.find_element_by_xpath('//*[@id="loginPassword"]').send_keys(Keys.CONTROL + "a")
            driver.find_element_by_xpath('//*[@id="loginEmail"]').send_keys(Keys.DELETE)
            driver.find_element_by_xpath('//*[@id="loginPassword"]').send_keys(Keys.DELETE)
            driver.find_element_by_xpath('//*[@id="loginEmail"]').send_keys(credentials[0])
            driver.find_element_by_xpath('//*[@id="loginPassword"]').send_keys(credentials[1])
            time_zero = time.time()
            form_filled = 1
        except:
            pass
        try:#pressing sign in button
            assert form_filled
            driver.find_element_by_id("btn-log-in")
            driver.find_element_by_id("btn-log-in").click()
            print(" -RGL: pressing for sign in button")
            time_zero = time.time()
        except:
            pass
        try:#checking for invalid credentials
            error_message = driver.find_element_by_id("errorMessageForLogin")
            assert error_message.is_displayed()
            assert error_message.text == "Invalid Username/account"
            print(" -RGL: invalid credentials")
            return None
        except:
            pass


    print(" -RGL: loggin in failed, restarting razer_gold_login() service")
    driver.execute_script('window.localStorage.clear();')
    driver.delete_all_cookies()
    return razer_gold_login(driver, window_handle, credentials, transaction_url)

def razer_gold_sign_out(driver, window_handle):
    print(" -RGSO: razer_gold_sign_out() service initiated")

    driver.switch_to.window(window_handle)
    driver.quit()

    driver = webdriver.Firefox()
    print(" -RGSO: razer_gold_sign_out service is over")
    return driver
    
def razer_gold_check_balance(driver, window_handle, method):
    print(" -RGCB: razer_gold_check_balance() service initiated")
    print(" -RGCB: checking low balcance notification")

    checkout_button_xpath = '//*[@id="btn99"]'
    balance_warning_xpath = "/html/body/div/main/section/div/div/div/div[5]/div/div[1]/div[2]/div/ul/li/span[1]/i"
    checkout_button_webelement = driver.find_element_by_xpath(checkout_button_xpath)
    order_balance_number_id = "orderSummaryOrderTotal"
    time_zero = time.time()
    while time.time() - time_zero < time_of_waiting:
        try:
            assert checkout_button_webelement.is_displayed()
            assert "PROCEED TO CHECKOUT" in checkout_button_webelement.text
            print(" -RGCB: balance is sufficeint, razer_gold_check_balance service is over")
            return ("G", driver.find_element_by_id(order_balance_number_id).text)
        except:
            pass
    
        try:
            assert driver.find_element_by_xpath(balance_warning_xpath).is_displayed()
            print(" -RGCB: balance is not enough, razer_gold_check_balance() service is over")
            return ("C", 0)
        except:
            pass
    print(" -RGCB: niether checkout button is not found, insufficient funds banner is not found")
    choice = input(" -RGCB: enter (R) to repeat process with the same account or (C) to repeat it with a different account, (G) to continue")
    print(" -RGCB: razer_gold_check_balance service is over")
    return (choice, 0)

def razer_gold_proceed_to_check_out_legacy(driver, window_handle, credentials):
    print(" -RGPTCO: razer_gold_proceed_to_check_out service initiated")

    checkout_button_xpath = '//*[@id="btn99"]'
    checkout_button_webelement = driver.find_element_by_xpath(checkout_button_xpath)
    driver.execute_script("arguments[0].click();", checkout_button_webelement)
    print(" -RGPTCO: clicking proceed to checkout")

    print(" -RGPTCO: waiting for payment portal to appear")
    webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

    print(" -RGPTCO: waiting for tfa input field to appear")
    tfa_input_field_xpath = "/html/body/div[2]/div[1]/div/div/div/div[5]/input[1]"
    try:
        webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.element_to_be_clickable((By.XPATH, tfa_input_field_xpath)))
    except:
        print(" -RGPTCO: TFA Code Field is not found assuming TFA is not required")
    else:
        print(" -RGPTCO: entering TFA code")
        driver.find_element_by_xpath(tfa_input_field_xpath).send_keys(credentials[2].now())

    driver.switch_to.default_content()
    print(" -RGPTCO: waiting razer transaction page to load")
    try:
        razer_payment_loading_logo_xpath = "/html/body/div/main/section/div/div/div/div[1]/div"
        razer_payment_loading_logo_class_name = "loader-wrapper"
        webdriver.support.ui.WebDriverWait(driver, 10 * time_of_waiting).until(EC.invisibility_of_element_located((By.CLASS_NAME, razer_payment_loading_logo_class_name)))
    except:
        print(" -RGPTOC: the page took too long to load, the bot is blocked enter anything to stop quit the bot")
        x = input()
        return None
    else:
        print(" -RGPTCO: razer transaction page has loaded")

    print(" -RGPTCO: waiting for headers to show up")
    webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.invisibility_of_element_located((By.TAG_NAME, "h2")))
    payment_complete = 0
    print(" -RGPTCO: making sure the transaction is complete")
    start_time = time.time()
    time_out = 20
    try:
        while True:
            h2_header = driver.find_elements_by_tag_name("h2")
            for header in h2_header:
                if "Congratulations" in header.text:
                    print(" -RGPTOC: payment is complete collecting transaction id")
                    for div in driver.find_elements_by_tag_name("div"):
                        if "Transaction Id" in div.text and len(div.text) < 40:
                            return div.text.split("\n")[1]
            if time.time() - start_time > time_out:
                print(" -RGPTOC: razer site took too long to display the result of transaction")
                return None
    except Exception as error_message:
        print("error 102")
        print(error_message)
        
    try:
        while True:
            h4_headers = driver.find_elements_by_tag_name("h4")
            for header in h4_headers:
                    if "Error" in header.text or "error" in header.text:
                        print(" -RGPTOC: razer site have an error, service razer_gold_proceed_to_checkout is over")
                        return None
            if time.time() - start_time > time_out:
                print(" -RGPTOC: razer site took too long to display the result of transaction")
                return None

    except Exception as error_message:
        print("error 103")
        print(error_message)
        return None

def razer_gold_proceed_to_check_out(driver, window_handle, credentials):
    print(" -RGPTCO: razer_gold_proceed_to_check_out service initiated")
    tfa_input_field_xpath = "/html/body/div[2]/div[1]/div/div/div/div[5]/input[1]"
    razer_payment_loading_logo_xpath = "/html/body/div/main/section/div/div/div/div[1]/div"
    razer_payment_loading_logo_class_name = "loader-wrapper"
    checkout_button_xpath = '//*[@id="btn99"]'
    checkout_button_webelement = driver.find_element_by_xpath(checkout_button_xpath)

    driver.execute_script("arguments[0].click();", checkout_button_webelement)
    print(" -RGPTCO: clicking proceed to checkout")

    time_zero = time.time()
    while time.time() - time_zero < time_of_waiting*5:
        try:#restarting time_zero if razer loading logo is appearing
            driver.find_element_by_class_name(razer_payment_loading_logo_class_name)
            time_zero = time.time()
        except:
            pass
        try:#filling TFA codes
            driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
            driver.find_element_by_xpath(tfa_input_field_xpath).send_keys(credentials[2].now())
            print(" -RGL: entered TFA code")
            time_zero = time.time()
        except:
            pass
        finally:
            driver.switch_to.default_content()
        try:#checks for transaction ID
            h2_header = driver.find_elements_by_tag_name("h2")
            for header in h2_header:
                assert "Congratulations" in header.text
                for div in driver.find_elements_by_tag_name("div"):
                    if "Transaction Id" in div.text and len(div.text) < 40:
                        print(" -RGPTOC: payment is complete collecting transaction id")
                        return div.text.split("\n")[1]
        except:
            pass
        try:#check for failure in razer site
            h4_headers = driver.find_elements_by_tag_name("h4")
            for header in h4_headers:
                if "Error" in header.text or "error" in header.text:
                    print(" -RGPTOC: razer site have an error, or payment failed, service razer_gold_proceed_to_checkout is over")
                    return None
        except:
            pass
    
    print(" -RGPTOC: razer site took too long to display the result of transaction")
    return None

def razer_init_check_sus_order(driver, window_handle, credentials):
    driver.switch_to.window(window_handle)
    if driver.current_url != "https://gold.razer.com/transactions":
        driver.get("https://gold.razer.com/transactions")
    
    time_zero = time.time()
    while time.time() - time_zero < time_of_waiting:
        for a_link in driver.find_elements_by_tag_name("a"):
            if a_link.text == "I AGREE":
                a_link.click()
                print(" -RCSO: New Policy Notification is closed")
                time_zero = time.time()
        for span in driver.find_elements_by_tag_name("a"):
            if span.text == "SIGN IN":
                print(" -RCSO: Pressing Sign In button")
                span.click()
                time_zero = time.time()
        if driver.execute_script('return document.readyState;') != "complete":
            time_zero = time.time()
        for input_field in driver.find_elements_by_tag_name("input"):
            try:
                if input_field.get_attribute("placeholder") == "Email Address":
                    if input_field.get_attribute("value") != credentials[0]:
                        input_field.send_keys(credentials[0])
                        print(" -RGSO: entered Email Address")
                        time_zero = time.time()
                elif input_field.get_attribute("placeholder") == "Password":
                    if input_field.get_attribute("value") != credentials[1]:
                        input_field.send_keys(credentials[1])
                        print(" -RGSO: Entered Password")
                        time_zero = time.time()
            except:
                pass
        for button in driver.find_elements_by_tag_name("button"):
            try:
                if button.text == "LOG IN":
                    if "disabled" not in button.get_attribute("class"):
                        button.click()
                        time_zero = time.time()
                        print(" -RGSO: clicking log in")
                elif button.text == "CONNECT WITH ANOTHER ACCOUNT":
                    button.click()
                    time_zero = time.time()
                    print(" -RGSO: clicked connect with another account")
            except:
                pass
        try:
            account_options_button = driver.find_element_by_id("__BVID__62")
            if account_options_button.find_element_by_tag_name("a").get_attribute("aria-expanded") == "false":
                driver.find_element_by_id("__BVID__62").click()
                time_zero = time.time()
            if account_options_button.find_element_by_tag_name("a").get_attribute("aria-expanded") == "true":
                if credentials[0] in account_options_button.text:
                    return 1
                else:
                    for a_tag in account_options_button.find_elements_by_tag_name("a"):
                        if a_tag.text == "Sign Out":
                            a_tag.click()
                            driver.get("https://gold.razer.com/transactions")
        except:
            pass

    return 2

def razer_check_sus_order(driver, window_handle, date_time, price, list_of_successful_transaction_numbers):
    date = date_time.split(" ")[0].split("/")
    date[0] = month_numbers[date[0]]
    date = date[1] + "-" + date[0] + "-" + date[2]
    time = date_time.split(" ")[1].split(":")
    time = time[0] * 60 + time[1]
    passed_on_same_date = 0
    table_searches = 0
    list_of_possible_transactions = []
    while not passed_on_same_date:
        for table in driver.find_elements_by_tag_name("table"):
            if "TRANSACTION ID" in table.text:
                for trows in table.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr"):
                    if trows.find_element_by_tag_name("td").text.lower() in date:
                        passed_on_same_date = 1
                        print("-Date: ", end = "")
                        if trows.find_elements_by_tag_name("td")[1].text == "Razer Gold Purchase":
                            print("-Item: ", end = "")
                            if trows.find_elements_by_tag_name("td")[3].text == price:
                                print("-Price: ", end = "")
                                if  trows.find_elements_by_tag_name("td")[4].text not in list_of_successful_transaction_numbers:
                                    list_of_possible_transactions.append(trows.find_elements_by_tag_name("td")[4].text)
                                    print(trows.text, "\nTARGET")
                            else:
                                print(trows.text, "\nNOT TARGET")
                table_searches = 0
                break
        else:
            table_searches += 1
            if table_searches > 3:
                return 0
            continue
        for button in driver.find_element_by_tag_name("li"):
            if li.text == "›":
                li.click()

    if not len(list_of_possible_transactions):
        return 1
    list_of_highly_possible_transactions = []
    for transaction_number in list_of_possible_transactions:
        driver.get("https://gold.razer.com/transaction/zGold/" + transaction_number)
        transaction_date_found = 0
        for p_tag in driver.find_elements_by_tag_name("p"):
            if transaction_date_found:
                break
            elif p_tag.text == "TRANSACTION DATE":
                transaction_date_found = 1
        else:
            return 2
        
        transaction_time = p_tag.split(" ")[1].split(":")
        if time == transaction_time[0] * 60 + transaction_time[1] or time + 1 == transaction_number[0] * 60 + transaction_number:
            list_of_highly_possible_transactions.append(transaction_number)
    if not len(list_of_highly_possible_transactions):
        return 1
    if len(list_of_highly_possible_transactions) == 1:
        return list_of_highly_possible_transactions[0]
    return list_of_highly_possible_transactions
        
