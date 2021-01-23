from selenium import webdriver #this is needed to basicly anything
from selenium.webdriver import ActionChains #this used to open some hover menus
from selenium.webdriver.support import expected_conditions as EC #this is used to prevent the driver form clicking unloaded elements
from selenium.webdriver.common.by import By #this used for element finding method
from selenium.webdriver.common.keys import Keys #this is used to simiulate keyboard keys
from selenium.common.exceptions import TimeoutException
from variables import *
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
    time_zero = time.time()
    while time.time() - time_zero < time_of_waiting:
        try:
            assert checkout_button_webelement.is_displayed()
            assert "PROCEED TO CHECKOUT" in checkout_button_webelement.text
            print(" -RGCB: balance is sufficeint, razer_gold_check_balance service is over")
            return "G"
        except:
            pass
    
        try:
            assert driver.find_element_by_xpath(balance_warning_xpath).is_displayed()
            print(" -RGCB: balance is not enough, razer_gold_check_balance() service is over")
            return "C"
        except:
            pass
    print(" -RGCB: niether checkout button is not found, insufficient funds banner is not found")
    choice = input(" -RGCB: enter (R) to repeat process with the same account or (C) to repeat it with a different account, (G) to continue")
    print(" -RGCB: razer_gold_check_balance service is over")
    return choice

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
    while time.time() - time_zero < time_of_waiting:
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