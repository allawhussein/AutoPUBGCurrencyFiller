from selenium import webdriver #this is needed to basicly anything
from selenium.webdriver import ActionChains #this used to open some hover menus
from selenium.webdriver.support import expected_conditions as EC #this is used to prevent the driver form clicking unloaded elements
from selenium.webdriver.common.by import By #this used for element finding method
from selenium.webdriver.common.keys import Keys #this is used to simiulate keyboard keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

import time
from variables import *

def refresh_xpath_midas_id_verifier(country_code):
    if country_code == "my":
        input_field_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div[1]/input"
        payment_completed_button_xpath = "/html/body/div[1]/div[3]/div[13]/div[1]/div[2]/div[1]"#these two buttons are for
        payment_completed_ok_button_xpath = "/html/body/div[1]/div[3]/div[13]/div[2]/div[3]/div"#previous opened payment windows
        edit_button_class = "link-mod-a"
        submit_button_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div[2]"
        pubg_name_holder = "/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div[1]/div[1]/p"
        rejection_div_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/p"
        payment_completed_button_2_xpath = '//*[@id="backBtn"]'
        return [input_field_xpath, payment_completed_button_xpath, payment_completed_ok_button_xpath, edit_button_class, submit_button_xpath, pubg_name_holder, rejection_div_xpath, payment_completed_button_2_xpath]
    elif country_code == "ot":
        input_field_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div[1]/input"
        payment_completed_button_xpath = "/html/body/div[1]/div[3]/div[13]/div[1]/div[2]/div[2]"
        payment_completed_ok_button_xpath = "/html/body/div[1]/div[3]/div[13]/div[2]/div[3]/div"
        edit_button_class = "link-mod-a"
        submit_button_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div[2]"
        pubg_name_holder = "/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div[1]/div[1]/p"
        rejection_div_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/p"
        payment_completed_button_2_xpath = '//*[@id="backBtn"]'
        return [input_field_xpath, payment_completed_button_xpath, payment_completed_ok_button_xpath, edit_button_class, submit_button_xpath, pubg_name_holder, rejection_div_xpath, payment_completed_button_2_xpath]
    else:
        print(" -RX-MIDV: country code is not recognized")
        return None

def refersh_xpath_midas_bundle_and_payment_method_chooser(country_code):
    if country_code == "my":
        payment_options_list_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/ul/span"
        bundle_list_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/ul"
        return [payment_options_list_xpath, bundle_list_xpath]
    elif country_code == "ot":
        payment_options_list_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/ul/span"
        bundle_list_xpath = "/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/ul"
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
            birthday_popup_id]

def midas_id_verifier(driver, window_handle, order_pubg_id, max_verification_trails, country_code):#function will return None if ID is rejected
    print(" -MIDV: midas_id_verifier() service is initiated for country: " + country_code)
    print(" -MIDV: opening midas website, site loading timeout is 120 seconds")
    midas_url = "https://www.midasbuy.com/midasbuy/" + country_code + "/buy/pubgm"
    varaible = refresh_xpath_midas_id_verifier(country_code)
    input_field_xpath = varaible[0]
    payment_completed_button_xpath = varaible[1]
    payment_completed_ok_button_xpath = varaible[2]
    edit_button_class = varaible[3]
    submit_button_xpath = varaible[4]
    pubg_name_holder = varaible[5]
    rejection_div_xpath = varaible[6]
    payment_completed_button_2_xpath = varaible[7]
    
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
    print(" -MIDV: waiting for input field to appear")
    while not input_field_visible:
        try:#check for input filed
            driver.find_element_by_xpath(input_field_xpath)
        except:
            try:               
                driver.find_element_by_class_name(edit_button_class).click()
                print(" -MIDV: pressing edit button") 
            except:
                pass
            else:
                pass
            try:
                driver.find_element_by_class_name("popa")
                for element in driver.find_element_by_class_name("popa").find_element_by_class_name("pop-content"):
                    element.find_element_by_class_name("close-btn").click()
                print(" -MIDV: closing opened popup window")
            except:
                pass
            try:
                driver.find_element_by_xpath(payment_completed_button_xpath).click()
                print(" -MIDV: closing payment window type I")
            except:
                pass
            try:
                driver.find_element_by_xpath(payment_completed_ok_button_xpath).click()
                print(" -MIDV: closing payment window type II")
            except:
                pass
        else:
            input_field_visible = 1
        current_time = time.time()
        if current_time - time_zero > time_of_waiting:
            print(" -MIDV: the input field is not showing up, MIDV is over")
            return -1

    print(" -MIDV: entering the player PUBG ID")
    driver.find_element_by_xpath(input_field_xpath).send_keys(Keys.CONTROL + "a")
    driver.find_element_by_xpath(input_field_xpath).send_keys(Keys.DELETE)
    driver.find_element_by_xpath(input_field_xpath).send_keys(order_pubg_id)

    print(" -MIDV: clicking submit button")
    webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.presence_of_element_located((By.XPATH, submit_button_xpath)))
    driver.find_element_by_xpath(submit_button_xpath).click()
    print(" -MIDV: waiting ID verification")

    time_zero = time.time()
    print(" -MIDV: verifying player ID")
    while True:
        try:
            return driver.find_element_by_xpath(pubg_name_holder).text
        except:    
            try:
                driver.find_element_by_xpath(rejection_div_xpath).click()
            except:
                pass
            else:
                if max_verification_trails:
                    print(" -MIDV: ID is rejected, re-initiating MIDV service")
                    print(" -MIDV: verification trails remaining #" + str(max_verification_trails - 1))
                    return midas_id_verifier(driver, window_handle, order_pubg_id, max_verification_trails - 1, country_code)
                else:
                    print(" -MIDV: ID is rejected, number of trails are exhausted midasbuy_id_verification() service is over")
                    return 0
        else:
            pass
        
        current_time = time.time()
        if current_time - time_zero > time_of_waiting:
            print(" -MIDV: Unkown Error, Send Photo to Hussein")
            driver.find_element_by_tag_name("body").screenshot("./MIDV_fail.png")
            return None

def midas_bundle_and_payment_method_chooser(driver, window_handle, required_uc, offer_uc, payment_method, country_code):#function will return None if supplied payment method is not found
    print(" -MBAPMC: midas_bundle_and_payemnt_method_chooser() service is initiated")
    variable = refersh_xpath_midas_bundle_and_payment_method_chooser(country_code)
    payment_options_list_xpath = variable[0]
    bundle_list_xpath = variable[1]
    driver.switch_to.default_content()

    print(" -MBAPMC: collecting payment options")
    payment_options_list = driver.find_element_by_xpath(payment_options_list_xpath).find_elements_by_xpath("li")
    for li in payment_options_list:
        if li.find_element_by_tag_name("p").text == payment_method:
            print(" -MBAPMC: choosen payment method: " + payment_method)
            payment_method_button = li
            break
    else:
        print(" -MBAPMC: payment method is not found")
        print(" -MBAPMC: midas_bundle_and_payment_method_chooser() service is over")
        return None
    
    print(" -MBAPMC: clicking the selected method")
    webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.element_to_be_clickable((By.XPATH, payment_options_list_xpath)))
    driver.execute_script("arguments[0].click();", payment_method_button)
    
    print(" -MBAPMC: searching for target bundle")
    bundles_list = driver.find_element_by_xpath(bundle_list_xpath).find_elements_by_tag_name("li")
    bundle_card_div_text = ""
    bundle_choosen = 0
    for bundle in bundles_list[::-1]:
        for element in bundle.find_elements_by_tag_name("*"):
            bundle_card_div_text = ""
            flag = False
            for char in element.text:
                if char <= "9" and char >="0":
                    bundle_card_div_text += char
                elif char == "+":
                    bundle_card_div_text += char
                else:
                    flag = False
                    break
                flag=True
            if flag:
                break
        if  bundle_card_div_text != "":
            bundle_card_total_uc = 0
            bundle_card_total_uc_list = []
            for x in bundle_card_div_text.split("+"):
                bundle_card_total_uc += int(x)
                bundle_card_total_uc_list.append(int(x))
            if bundle_card_total_uc == required_uc + offer_uc:
                print(" -MBAPMC: total uc order match")
                driver.execute_script("arguments[0].click();", bundle)
                bundle_choosen = 1
                break
            elif bundle_card_total_uc_list[0] == required_uc:
                print(" -MBAPMC: one time offer is not found, choosing base bundle")
                driver.execute_script("arguments[0].click();", bundle)
                bundle_choosen = 1
                break

    if bundle_choosen:        
        print(" -MBAPMC: bundle chosen: "+str(bundle_card_total_uc)+" uc")
        print(" -MBAPMC: midas_bundle_and_payment_method_chooser() service is over")
        return bundle_card_total_uc
    else:
        print(" -MBAPMC: required bundle is not found")
        return None

def midas_razer_payment_initializer(driver, window_handle, country_code):
    print(" -MRPI: service midas_razer_payment_initializer is initiated")
    variable = refresh_xpath_midas_razer_payment_initializer(country_code)
    pay_now_button_xpath = variable[0]
    check_boxes_title_xpath = variable[1]
    date_of_birth_window_xpath = variable[2]
    pay_button_xpath = variable[3]
    check_box_1_xpath = variable[4]
    check_box_2_xpath = variable[5]
    submit_pay_now_button_xpath = variable[6]
    pay_button_class = variable[7]
    check_box_class = variable[8]
    date_of_birth_window_id = variable[9]
    random_date_xpath = variable[10]
    date_of_birth_confirmation = variable [11]
    check_box_class_2 = variable[12]
    continue_button_class = variable[13]
    birthday_popup_id = variable[14]
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
            for check in driver.find_elements_by_class_name(check_box_class):
                if check.is_displayed():
                    if "checked" not in check.get_attribute("class"):
                        check.click()
                        if check_box_first_click:
                            print(" -MRPI: checked all check boxes")
                            time_zero = time.time()
                        check_box_first_click = 0
        except:
            pass
            
        
            
            print(" -MRPI: clicking pay now")
            submit_pay_now_button = driver.find_element_by_xpath(submit_pay_now_button_xpath)
            submit_pay_now_button.click()
        try:#clicking new checkbox
            driver.find_element_by_class_name(check_box_class_2).click()
            print(" -MRPI: clicked checkbox")
            driver.find_element_by_class_name(check_box_class_2).find_element_by_xpath("..").find_element_by_class_name(continue_button_class).click()
            print(" -MRPI: clicking continue button")
        except:
            pass
        try:#submitting date
            assert driver.find_element_by_id(date_of_birth_window_id).is_displayed()
            print(" -MRPI: choosing date of birth")
            driver.find_element_by_id(date_of_birth_window_id).click()
            WebDriverWait(driver, time_of_waiting).until(EC.element_to_be_clickable((By.XPATH, random_date_xpath)))
            driver.find_element_by_xpath(random_date_xpath).click()
            print(" -MRPI: random date is selected")
            while not len(driver.find_element_by_id(date_of_birth_window_id).text):
                pass
            driver.find_element_by_id(birthday_popup_id).find_element_by_class_name(date_of_birth_confirmation).click()
            print(" -MRPI: date is submitted")
        except:
            pass
        if time.time() - time_zero > time_of_waiting:
            print("Razer Window didn't open in time")
            return None
    
    print(" -MRPI: detecting opened tab containing razer gold site, this is a new feature, it can't be tested, for any errors contact the developer")
    print(" -MRPI: counting opened tabs after midasbuy tab")
    print(" -MRPI: currently " + str(len(driver.window_handles)) + " are opened")
    counter = 0
    for tab in driver.window_handles:
        if tab == driver.current_window_handle:
            break
        counter += 1
    counter += 1
    razer_payment_url = None
    while not razer_payment_url:
        for opened_tab in driver.window_handles[counter:]:
            driver.switch_to.window(opened_tab)
            if "razer.com" in driver.current_url:
                razer_payment_url = driver.current_url

    print(" -MRPI: closing tabs starting from" + str(counter))
    for tab in driver.window_handles[counter:]:
        print(" -MRPI: closing tab " + str(counter))
        counter += 1
        driver.switch_to.window(tab)
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