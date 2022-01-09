from selenium import webdriver #this is needed to basicly anything
from selenium.webdriver import ActionChains #this used to open some hover menus
from selenium.webdriver.support import expected_conditions as EC #this is used to prevent the driver form clicking unloaded elements
from selenium.webdriver.common.by import By #this used for element finding method
from selenium.webdriver.common.keys import Keys #this is used to simiulate keyboard keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
import os
import time
import pickle
import datetime

from services.variables import *
from services import alcaptain_services
from services import midasbuy_services
from services import razer_gold_services
from services import telegram_services

print("Mobile PUBG Bot v3.0")
initialize_variables()

if browser == "firefox":
    driver = webdriver.Firefox()
    for country in country_code_list:
        pass
    driver.execute_script('window.open("https://www.midasbuy.com/midasbuy/ot/buy/pubgm","_blank");')#https://www.midasbuy.com/midasbuy/my/buy/pubgm
    driver.execute_script('window.open("https://www.midasbuy.com/midasbuy/sg/buy/pubgm","_blank");')#https://www.midasbuy.com/midasbuy/ot/buy/pubgm
    razer_driver = webdriver.Firefox()
    ot_window_handle = driver.window_handles[2]
    un_window_handle = driver.window_handles[1]
elif browser == "chrome":
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2, 
                                'plugins': 2, 'popups': 2, 'geolocation': 2, 
                                'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
                                'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 
                                'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
                                'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
                                'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
                                'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
                                'durable_storage': 2}}
    options.add_experimental_option('prefs', prefs)
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(chrome_options=options)
    driver.execute_script('window.open("about:blank","_blank");')
    razer_driver = webdriver.Chrome()

credentials = razer_accounts[0]
counter = 0
print("MainCode: using razer account: " + credentials[0])
last_order_tuple = [None, 0]
while True:
    try:
        order_tuple = None
        alcaptain_services.get_alcaptain_main_page(driver, driver.window_handles[0])
        try:
            order_clicked = alcaptain_services.quick_accept_all_eligible_orders(driver, driver.window_handles[0])
        except:
            pass
        order_tuple = alcaptain_services.select_order(driver, driver.window_handles[0])
        if order_tuple != None:
            country_code = order_tuple[4]
            try:
                order_tuple[1] = int(order_tuple[1])
            except:
                alcaptain_services.failed_order_reply(driver, driver.window_handles[0], "Your PUBG ID: " + str(order_tuple[1]) + " is invalid")
                reply_message = "💣PUBG Mobile Order Rejected❌\nOrder ID: " + str(order_tuple[0]).split("#")[1] + "\nPUBG ID: " + str(order_tuple[1]) + "\nis invalid and rejected (ID contains letters)"
                telegram_services.send_msg(reply_message)
            else:
                if country_code == "ot" or country_code == "check":
                    midasbuy_window_handle = ot_window_handle
                else:
                    midasbuy_window_handle = un_window_handle
                order_name = midasbuy_services.midas_id_verifier(driver, midasbuy_window_handle, order_tuple[1], 2, country_code)
                if order_name != None and country_code != "check":
                    if type(order_name) == int:
                        if order_name == -1:
                            print("Main Code: probably buttons' xpath changed CONTACT HUSSEIN ALLAW")
                        elif order_name == 0:
                            print("Main Code: Replying with Invalid Code")
                            alcaptain_services.failed_order_reply(driver, driver.window_handles[0], "Your PUBG ID: " + str(order_tuple[1]) + " is invalid")
                            reply_message = "PUBG Mobile Order Rejected❌\nOrder ID: " + str(order_tuple[0]).split("#")[1] + "\nPUBG ID: " + str(order_tuple[1]) + "\nis invalid and rejected (rejected by Midasbuy)"
                            telegram_services.send_msg(reply_message)
                    else:
                        output = midasbuy_services.midas_bundle_and_payment_method_chooser(driver, midasbuy_window_handle, order_tuple[2], order_tuple[3], "razer gold", country_code)
                        if output == None:
                            telegram_services.send_msg("⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️⚪️\nPUBG MOBILE BOT ERROR:\nEither Razer Gold is not avialable or NO suitable offer is available")
                            continue
                        print("Main Code: filling to the user :" + str(output))
                        razer_url = midasbuy_services.midas_razer_payment_initializer(driver, midasbuy_window_handle, country_code)
                        print("Main Code: razer url:" + str(razer_url))
                        if razer_url != None:
                            login_success = razer_gold_services.razer_gold_login(razer_driver, razer_driver.window_handles[0], credentials, razer_url)
                            if login_success != None:
                                balance, order_price = razer_gold_services.razer_gold_check_balance(razer_driver, driver.window_handles[0], 1)
                                if balance == "G":
                                    print("Main Code: archiving order")
                                    archive(str(order_tuple[0]))
                                    #Archive orderID, #PUBGM ID, Date&Time, OrderPrice, RazerAccount, Name, Filled UCs
                                    #transaction_id = razer_gold_services.razer_gold_proceed_to_check_out(razer_driver, razer_driver.window_handles[0], credentials)
                                    transaction_id = "None - Test Case by Hussein Allaw"
                                    with open("backup_transaction_numbers.txt", "a") as transaction_numbers_file:
                                        transaction_numbers_file.write(transaction_id + "\n")
                                    #transaction_id = "R"
                                    if transaction_id == None:
                                        print("Main Code: transaction id is not obtained")
                                        continue
                                    elif transaction_id == "R":
                                        print("Main Code: Simply Restarting")
                                    elif transaction_id == "S":
                                        print("Main Code: Bot will be Stoped")
                                        raise Exception
                                    else:
                                        reply_message = "The PUBG ID: " + str(order_tuple[1]) + "\nof Name: " + str(order_name) + "\nThe Transaction ID: " + str(transaction_id) + "\nHas filled: " + output
                                        alcaptain_services.successful_order_reply(driver, driver.window_handles[0], reply_message)
                                        reply_message = "💣PUBG Mobile Order Payed✅\nOrder ID: " + str(order_tuple[0]).split("#")[1] + "\nPUBG ID: " + str(order_tuple[1]) + "\nPUBG Name: " + str(order_name) + "\nTransaction ID: " + str(transaction_id) + "\nFilled UC: " + output + "\nConsumed Razer Gold: " + str(order_price)
                                        telegram_services.send_msg(reply_message)
                                        remove_last_order()
                                elif balance == "C":
                                    counter += 1
                                    print("Main Code: changing account")
                                    if (counter >= len(razer_accounts)):
                                        counter = 0
                                    credentials = razer_accounts[counter]
                                    rewrite_accounts(counter)
                                    print("Main Code: now using : " + credentials[0])
                                    razer_driver = razer_gold_services.razer_gold_sign_out(razer_driver, razer_driver.window_handles[0])
                                    print("insufficient funds, signing out, and restarting process")
                                elif balance == "R":
                                    pass
                                else:
                                    print("Main Code: Unkown Choice Inputed in RGS.RGCB service")
                                    assert False
                            else:
                                print("Main Code: Logging in razer account failed, simply restarting")
                                print("Main Code: changing account")
                                if (counter > len(razer_accounts)):
                                    counter = 0
                                credentials = razer_accounts[counter]
                                print("Main Code: now using : " + credentials[0])
                        else:
                            print("Main Code: Razer URL is not obtained, simply restarting")

                        print("MainCode: some error with Midasbuy, skipping")
                elif order_name != None and country_code == "check":
                    if type(order_name) == int:
                        if order_name == -1:
                            print("Main Code: probably buttons' xpath changed CONTACT HUSSEIN ALLAW")
                        elif order_name == 0:
                            print("Main Code: Replying with Invalid Code")
                            alcaptain_services.failed_order_reply(driver, driver.window_handles[0], "The PUBG ID: " + str(order_tuple[1]) + " is invalid")
                            reply_message = "🔍PUBG Mobile ID Check Invalid❌\nOrder ID: " + str(order_tuple[0]).split("#")[1] + "\nPUBG ID: " + str(order_tuple[1])
                            telegram_services.send_msg(reply_message)
                    else:
                        reply_message = "The PUBG ID: " + str(order_tuple[1]) + "is verified\nThe PUBG Name: " + str(order_name)
                        alcaptain_services.successful_order_reply(driver, driver.window_handles[0], reply_message)
                        reply_message = "🔍PUBG Mobile ID Check Verified✅\nOrder ID: " + str(order_tuple[0]).split("#")[1] + "\nPUBG ID: " + str(order_tuple[1]) + "\nPUBG Name: " + str(order_name)
                        telegram_services.send_msg(reply_message)
                else:
                    print("Main Code: some unknown None error")
        elif order_tuple == None:
            temp_sus_orders_list = alcaptain_services.get_list_of_active_archived_orders(driver, driver.current_window_handle)
            for order in temp_sus_orders_list:
                if order not in sus_orders_list:
                    sus_orders_list.append(order)
                    print(" -MainCode: sending sus order to telegram group")
                    telegram_services.send_msg("❌❌❌❌❌❌\n💣Duplicate Order Detected\nAlCaptain ID:%20" + order[0].split("#")[1] + "\nPUBG ID:+" + order[1] + "\nTimeAndDate: " + order[2])
            if len(sus_orders_list):
                sus_order = sus_order_list[0]
                transaction_numbers_file = open("transaction_numbers.txt", "r")
                transaction_numbers = transaction_numbers_file.readlines()
                for i in range(0, len(transaction_numbers)):
                    transaction_numbers[i] = transation_numbers[i].split("\n")[0]
                print("MainCode<DEBUG-DUPLICATE_ORDERS>: ", sus_order[0], sus_order[2], sus_order[3])
                if False:
                    order_status = razer_gold_services.razer_check_sus_order(razer_driver, razer_driver.window_handles[0], sus_order[2], sus_order[3], transaction_numbers)
                    print(order_status)
                    if type(order_status) == int:
                        if order_status == 1:
                            remove_order(sus_order[0])
                        else:
                            if alcaptain_services.select_specific_order(driver, driver.window_handles[0], sus_order[0]):
                                reply_message = "The PUBG ID: " + str(sus_order[1]) + "\nof Name: " + str(sus_order[-2]) + "\nThe Transaction ID: " + str(order_state) + "\nHas filled: " + sus_order[-1]
                                alcaptain_services.successful_order_reply(driver, driver.window_handles[0], reply_message)
                                reply_message = "💣PUBG Mobile Order Payed 🔁✅\nOrder ID: " + str(sus_order[0]).split("#")[1] + "\nPUBG ID: " + str(sus_order[1]) + "\nPUBG Name: " + str(sus_order[-2]) + "\nTransaction ID: " + str(order_state) + "\nFilled UC: " + sus_order[-1] + "\nConsumed Razer Gold: " + str(sus_order[3]) + "\nThis order was pulled from Razer Transaction List"
                                telegram_services.send_msg(reply_message)
                                remove_order(sus_order[0])
                                with open("trasaction_numbers.txt", "a") as transaction_numbers_file:
                                    transaction_numbers_file.append(order_status + "\n")
                    elif type(order_status) == list:
                        reply_message = "The PUBG ID: " + str(sus_order[1]) + "\nof Name: " + str(sus_order[-2]) + "\nThe Transaction ID: " + str(order_state[0]) + "\nHas filled: " + sus_order[-1]
                        alcaptain_services.successful_order_reply(driver, driver.window_handles[0], reply_message)
                        reply_message = "💣PUBG Mobile Order Payed 🔁✅\nOrder ID: " + str(sus_order[0]).split("#")[1] + "\nPUBG ID: " + str(sus_order[1]) + "\nPUBG Name: " + str(sus_order[-2]) + "\nTransaction ID: " + str(order_state[0]) + "\nFilled UC: " + sus_order[-1] + "\nConsumed Razer Gold: " + str(sus_order[3]) + "\nThis order was pulled from Razer Transaction List"
                        telegram_services.send_msg(reply_message)
                        with open("trasaction_numbers.txt", "a") as transaction_numbers_file:
                            transaction_numbers_file.append(order_status + "\n")

        if last_order_tuple == order_tuple:
            last_order_tuple[1] += 1
        else:
            last_order_tuple[0] = order_tuple
        if last_order_tuple[1] > 1:
            archive(str(order_tuple[0]), "stuck_archive.csv")
            reply_message = "❌❌❌❌❌❌\n💣Stuck Order Detected, and will be skipped\nAlCaptain ID: " + str(order_tuple[0]).split("#")[1] + "\nPUBG ID:+" + order_tuple[1]
            telegram_services.send_msg(reply_message)

    except Exception as error_message:
        print("MainCode: sending error message to Hussein Allaw")
        print(error_message)
        telegram_services.send_msg_dev(repr(error_message))
    except KeyboardInterrupt:
        print("MainCode: program ended by user")
        break