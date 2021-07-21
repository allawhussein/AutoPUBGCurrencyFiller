from selenium import webdriver #this is needed to basicly anything
from selenium.webdriver import ActionChains #this used to open some hover menus
from selenium.webdriver.support import expected_conditions as EC #this is used to prevent the driver form clicking unloaded elements
from selenium.webdriver.common.by import By #this used for element finding method
from selenium.webdriver.common.keys import Keys #this is used to simiulate keyboard keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

import time
from services.variables import *
from services import telegram_services

def refresh_xpath_midas_id_verifier(country_code):
    if country_code == "my":
        input_field_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div/div/div/div/div[1]/input"
        payment_completed_button_xpath = "/html/body/div[1]/div[3]/div[13]/div[1]/div[2]/div[1]"#these two buttons are for
        payment_completed_ok_button_xpath = "/html/body/div[1]/div[3]/div[13]/div[2]/div[3]/div"#previous opened payment windows
        edit_button_class = "link-mod-a"
        submit_button_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div/div/div/div/div[2]"
        pubg_name_holder = "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div/div/div/div/div[1]/div[1]/p"
        rejection_div_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div/div/div/p"
        payment_completed_button_2_xpath = '//*[@id="backBtn"]'
        return [input_field_xpath, payment_completed_button_xpath, payment_completed_ok_button_xpath, edit_button_class, submit_button_xpath, pubg_name_holder, rejection_div_xpath, payment_completed_button_2_xpath]
    elif country_code == "ot":
        input_field_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div/div/div/div/div[1]/input"
        payment_completed_button_xpath = "/html/body/div[1]/div[3]/div[13]/div[1]/div[2]/div[2]"
        payment_completed_ok_button_xpath = "/html/body/div[1]/div[3]/div[13]/div[2]/div[3]/div"
        edit_button_class = "link-mod-a"
        submit_button_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div/div/div/div/div[2]"
        pubg_name_holder = "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div/div/div/div/div[1]/div[1]/p"
        rejection_div_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div/div/div/p"
        payment_completed_button_2_xpath = '//*[@id="backBtn"]'
        return [input_field_xpath, payment_completed_button_xpath, payment_completed_ok_button_xpath, edit_button_class, submit_button_xpath, pubg_name_holder, rejection_div_xpath, payment_completed_button_2_xpath]
    else:
        print(" -RX-MIDV: country code is not recognized")
        return None

def refersh_xpath_midas_bundle_and_payment_method_chooser(country_code):
    if country_code == "my":
        payment_options_list_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/ul/span"
        bundle_list_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[5]/ul"
        return [payment_options_list_xpath, bundle_list_xpath]
    elif country_code == "ot":
        payment_options_list_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/ul/span"
        bundle_list_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[5]/ul"
        return [payment_options_list_xpath, bundle_list_xpath]
    else:
        print(" -RX-MBAPMC: country code is not recognized")

def refresh_xpath_midas_razer_payment_initializer(country_code):
    if country_code == "my":
        pay_now_button_xpath = "/html/body/div[1]/div[3]/div[3]/div[3]/div[3]/div/div[2]"
        check_boxes_title_xpath = "/html/body/div[1]/div[3]/div[3]/div[3]/div[1]/div/p"
        date_of_birth_window_xpath = '//*[@id="confirmBirthdayTxt"]'
        pay_button_xpath = '/html/body/div[1]/div[3]/div[3]/div[3]/div[3]/div/div[2]'
        check_box_1_xpath = "/html/body/div[1]/div[3]/div[3]/div[3]/div[1]/div/div/div/div[1]/div"
        check_box_2_xpath = "/html/body/div[1]/div[3]/div[3]/div[3]/div[1]/div/div/div/div[2]/div"
        submit_pay_now_button_xpath = "/html/body/div[1]/div[3]/div[3]/div[3]/div[3]/div/div[2]" 
        pay_button_class = "pay-btn"
        check_box_class = "checkbox"
        check_box_class_2 = "check-box"
        date_of_birth_window_id = "birthdayLine"
        random_date_xpath = "/html/body/div[1]/div[2]/div[14]/div/div[3]/div/div[3]/div[3]/ul/li[4]"
        date_of_birth_confirmation = "btn"
        continue_button_class = "btn"
        birthday_popup_id = "birthday-pop"
        birthday_day_div = "time-picker-box"
        date_of_birth_css_selector = "div.bd:nth-child(3) > ul:nth-child(1) > li:nth-child(16) > span:nth-child(1)"
    elif country_code == "ot":
        pay_now_button_xpath = "/html/body/div[1]/div[3]/div[3]/div[3]/div[3]/div/div[2]"
        check_boxes_title_xpath = "/html/body/div[1]/div[3]/div[3]/div[3]/div[1]/div/p"
        date_of_birth_window_xpath = '//*[@id="confirmBirthdayTxt"]'
        pay_button_xpath = '/html/body/div[1]/div[3]/div[3]/div[3]/div[3]/div/div[2]'
        check_box_1_xpath = "/html/body/div[1]/div[3]/div[3]/div[3]/div[1]/div/div/div/div[1]/div"
        check_box_2_xpath = "/html/body/div[1]/div[3]/div[3]/div[3]/div[1]/div/div/div/div[2]/div"
        submit_pay_now_button_xpath = "/html/body/div[1]/div[3]/div[3]/div[3]/div[3]/div/div[2]"
        pay_button_class = "pay-btn"
        check_box_class = "checkbox"
        check_box_class_2 = "check-box"
        date_of_birth_window_id = "birthdayLine"
        random_date_xpath = "/html/body/div[1]/div[2]/div[14]/div/div[3]/div/div[3]/div[3]/ul/li[4]"
        date_of_birth_confirmation = "btn"
        continue_button_class = "btn"
        birthday_popup_id = "birthday-pop"
        birthday_day_div = "time-picker-box"
        date_of_birth_css_selector = "div.bd:nth-child(3) > ul:nth-child(1) > li:nth-child(16) > span:nth-child(1)"
    else:
        print(" -RX-MRPI: country code is not recognized")
        return None
    return [pay_now_button_xpath, 
            check_boxes_title_xpath, 
            date_of_birth_window_xpath, 
            pay_button_xpath, 
            check_box_1_xpath, 
            check_box_2_xpath, 
            submit_pay_now_button_xpath,
            pay_button_class,
            check_box_class,
            date_of_birth_window_id,
            random_date_xpath,
            date_of_birth_confirmation,
            check_box_class_2,
            continue_button_class,
            birthday_popup_id,
            birthday_day_div,
            date_of_birth_css_selector]

def midas_id_verifier(driver, window_handle, order_pubg_id, max_verification_trails, country_code):#function will return None if ID is rejected
    print(" -MIDV: midas_id_verifier() service is initiated for country: " + country_code)
    print(" -MIDV: opening midas website, site loading timeout is 120 seconds")
    if country_code == "check":
        country_code = "ot"
    midas_url = "https://www.midasbuy.com/midasbuy/" + country_code + "/buy/pubgm"
    
    driver.switch_to.window(window_handle)
    driver.set_page_load_timeout(120)

    if midas_url not in driver.current_url:
        while True:            
            try:
                print(" -MIDV: loading midasbuy.com site")
                driver.get(midas_url)
            except TimeoutException:
                print(" -MIDV: midasbuy.com took too long to load")
                print(" -MIDV: reloading site")
            else:
                break
    else:
        print(" -MIDV: midasbuy.com is already loaded")
    
    while driver.execute_script("return document.readyState;") != "complete":
        pass

    input_field_visible = 0
    time_zero = time.time()
    while time.time() - time_zero < 20:
        print(" -MIDV: Main Loop, remaining time: ", str(20 - time.time() + time_zero)[:2])
        
        try:#check for input field if visible
            for input_field in driver.find_elements_by_tag_name("input"):
                if input_field.get_attribute("placeholder") == "Please enter Player ID":
                    print(" -MIDV: found the Player ID placeholder")
                    if input_field.get_attribute("value") != str(order_pubg_id):
                        input_field.send_keys(Keys.CONTROL + "a")
                        input_field.send_keys(Keys.DELETE)
                        input_field.send_keys(order_pubg_id)
                        print(" -MIDV: entered the player PUBG ID")
                    for button in driver.find_elements_by_tag_name("div"):
                        if button.get_attribute("class") == "btn" and button.text == "OK":
                            button.click()
                            time_zero = time.time()
                            print(" -MIDV: clicking submit button, waiting ID verification")
                            #time_zero = time.time()
        except Exception as err:
            print(" -MIDV<DEBUG>: ", err)

        try:#rest time_zero if button is loading
            if "loading-btn" in button.get_attribute("class"):
                time_zero = time.time()
        except:
            pass

        try:#check if player info are visible and valid
            for div in driver.find_elements_by_tag_name("div"):
                if len(div.find_elements_by_tag_name("*")) < 3:
                    for span in div.find_elements_by_tag_name("span"):
                        if span.text == "Player ID:":
                            print(" -MIDV<DEBUG> - PlayerID Text: ", span.text)
                            print(" -MIDV: found in Player info card the player ID field")
                            print(" -MIDV<DEBUG> - PlayerID: ", div.find_element_by_tag_name("p").text)
                            if div.find_element_by_tag_name("p").text == str(order_pubg_id):
                                print(" -MIDV: ID is successfully inputed")
                                for div in driver.find_elements_by_tag_name("div"):
                                    if len(div.find_elements_by_tag_name("*")) < 3:
                                        for span in div.find_elements_by_tag_name("span"):
                                            if span.text == "Nickname:":
                                                print(" -MIDV<DEBUG> - Nickname Text: ", span.text)
                                                print(" -MIDV: obtained the nickname MIDV is over")
                                                print(" -MIDV<DEBUG> - Nickname: ", div.find_element_by_tag_name("p").text)
                                                return div.find_element_by_tag_name("p").text
                            else:
                                print(" -MIDV: found in Player info card mismatch for the player ID")
                                for a_tag in driver.find_elements_by_tag_name("a"):
                                    if a_tag.text == "Edit":
                                        a_tag.click()
                                        time_zero = time.time()
                                        print(" -MIDV: pressed Edit Button")
        except Exception as err:
            print(" -MIDV<DEBUG>: ", err)

        for p_tag in driver.find_elements_by_tag_name("p"):
            if "invalid player id" in p_tag.text:
                if max_verification_trails < 1:
                    return 0
                return midas_id_verifier(driver, window_handle, order_pubg_id, max_verification_trails - 1, country_code)
        
    print(" -MIDV: Timeout")
    return None

def midas_bundle_and_payment_method_chooser(driver, window_handle, required_uc, offer_uc, payment_method, country_code):#function will return None if supplied payment method is not found
    print(" -MBAPMC: midas_bundle_and_payemnt_method_chooser() service is initiated")
    driver.switch_to.default_content()

    for li in driver.find_elements_by_tag_name("li"):
        if payment_method in li.text.lower():
            for li_child in li.find_elements_by_tag_name("*"):
                if li_child.text.lower() == payment_method:    
                    driver.execute_script("arguments[0].click();", li)
                    break
            else:
                continue
            break
    else:
        telegram_services.send_msg("❌❌❌❌❌❌\nMidasbuy Razer Gold is not found")
        return None

    bundle_choosen = False
    for li in driver.find_elements_by_tag_name("li")[::-1]:
        for p in li.find_elements_by_tag_name("p"):
            for char in p.text:
                if (char < "0" or char > "9") and char != "+":
                    break
            else:
                print('"' + p.text + '"')
                if "+" in p.text and p.text != "":
                    if str(required_uc) == p.text.split("+")[0] or str(required_uc + offer_uc) == p.text.split("+")[0]:
                        driver.execute_script("arguments[0].click();", li)
                        print(" -MBAPMC: bundle chosen: "+ p.text +" uc")
                        print(" -MBAPMC: midas_bundle_and_payment_method_chooser() service is over")
                        return p.text
                elif p.text != "":
                    if str(required_uc) == p.text or str(int(required_uc) + int(offer_uc)) == p.text:
                        driver.execute_script("arguments[0].click();", li)
                        print(" -MBAPMC: bundle chosen: "+ p.text +" uc")
                        print(" -MBAPMC: midas_bundle_and_payment_method_chooser() service is over")
                        return p.text

    return None

def midas_razer_payment_initializer(driver, window_handle, country_code):
    print(" -MRPI: service midas_razer_payment_initializer is initiated")
    driver.switch_to.window(window_handle)

    initial_number_of_windows = len(driver.window_handles)

    print(" -MRPI: starting payment procedure")
    check_box_first_click = 1
    pay_button_detected = 0
    pay_button_detected_first_time = 0
    pay_button_pressed = 0
    time_zero = time.time()
    while len(driver.window_handles) <= initial_number_of_windows:
        try:#locating pay-now button
            for element in driver.find_elements_by_class_name("pay-btn"):
                if "Pay now" in element.text:
                    pay_now_button = element
                    pay_button_detected = 1
                    break
                if pay_button_detected and not pay_button_detected_first_time:
                    print(" -MRPI: pay now button detected")
                    time_zero = time.time()
                    pay_button_detected_first_time = 1
        except:
            pass
        try:#pressing pay now button
            assert pay_now_button.is_enabled()
            pay_now_button.click()
            if not pay_button_pressed:
                print(" -MRPI: clicked pay now")
                time_zero = time.time()
                pay_button_pressed = 1
        except:
            pass
        try:#clicking checkboxes
            for check in driver.find_elements_by_class_name("check-box"):
                if check.is_displayed():
                    if "checked" not in check.get_attribute("class"):
                        check.click()
                        if check_box_first_click:
                            print(" -MRPI: checked all check boxes")
                            time_zero = time.time()
                        check_box_first_click = 0
        except:
            pass
        try:#submitting date
            for p_tag in driver.find_elements_by_tag_name("p"):
                if "Birthday" in p_tag.text:
                    p_tag.click()
            for div in driver.find_elements_by_tag_name("div")[::-1]:
                if div.text.replace("\n","").isnumeric():
                    break
            for li in div.find_elements_by_tag_name("li"):
                if li.text == "1":
                    li.click()
                    break
            for div in driver.find_elements_by_class_name("btn")[::-1]:
                if div.text == "OK":
                    div.click()
                    break
        except Exception as error:
            pass
        try:#clickng second pay now
            for div in driver.find_elements_by_class_name("btn"):
                if div.text == "Continue":
                    div.click()
        except:
            pass
        if time.time() - time_zero > time_of_waiting:
            print("Razer Window didn't open in time")
            return None
    
    print(" -MRPI: detecting opened tab containing razer gold site, this is a new feature, it can't be tested, for any errors contact the developer")
    print(" -MRPI: counting opened tabs after midasbuy tab")
    print(" -MRPI: currently " + str(len(driver.window_handles)) + " are opened")
    counter = 0
    
    for i in range(0, len(driver.window_handles)):
        if window_handle == driver.window_handles[i]:
            break

    driver.switch_to.window(driver.window_handles[i + 1])
    while "pay.gold.razer.com/order" not in driver.current_url:
        pass

    razer_payment_url = driver.current_url
    driver.close()
    
    driver.switch_to.window(window_handle)
    print(" -MRPI: reloading midaspage without blocking")
    driver.execute_script("location.reload();")
    print(" -MRPI: service midas_razer_payment_initializer is over")
    return razer_payment_url

if __name__ == "__main__":

    driver = webdriver.Firefox()
    country_code = "ot"

    if midas_id_verifier(driver, driver.window_handles[0], 5474774295, 1, "ot"):
        print(midas_bundle_and_payment_method_chooser(driver, driver.window_handles[0], 600, 0,"Razer Gold", "ot"))
        print(midas_razer_payment_initializer(driver, driver.window_handles[0], "ot"))