from selenium import webdriver #this is needed to basicly anything
from selenium.webdriver import ActionChains #this used to open some hover menus
from selenium.webdriver.support import expected_conditions as EC #this is used to prevent the driver form clicking unloaded elements
from selenium.webdriver.common.by import By #this used for element finding method
from selenium.webdriver.common.keys import Keys #this is used to simiulate keyboard keys
from selenium.common.exceptions import TimeoutException
import os
import time

from variables import *
from services import alcaptain_services
from services import midasbuy_services
from services import razer_gold_services
from services import telegram_services

print("Mobile PUBG Bot v2.1.1")
print("v2.1.1:   <MainCode> added a non stopping condition")
print("V2.1:     <MainCode, TSM> added telegram reporting ability")
print("v2.0.8:   <RGL, MainCode> switch razer accoutn if credentials are invalid")
print("v2.0.7.1: <MainCode> added restart feature for QAAEO in case of failure")
print("v2.0.7:   <MRPI> new razer link parsing method")
print("v2.0.6:   <GAMP> new logging-in and verification method")
print("      :   <GAMP> new wrong password handling")
print("v2.0.5:   <RGPTC> new transaction id collection method")
print("      :   <MBAPMC> MBAPMC_OT is merged into MBAPMC")
print("v2.0.4:   <RGL> new razer login method")
print("v2.0.3:   <MainCode> added archiving ability with double order payment protection")
print("v2.0.2:   <MainCode> added ability to use chrome for better speed or firefox for better debugging and stability")
print("v2.0.1:   <MIDV> new waiting method for input field")
print("          <MIDV> new ID verification method")
print("          <MIDV> MIDV_OT is merged into MIDV")
print("v2.0.0:   <MainCode> Initial Refactor and Razer Account Switcher")
initialize_variables()

if browser == "firefox":
    driver = webdriver.Firefox()
    driver.execute_script('window.open("about:blank","_blank");')
    razer_driver = webdriver.Firefox()
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
try:
    while True:
        order_tuple = None
        alcaptain_services.get_alcaptain_main_page(driver, driver.window_handles[0])
        try:
            order_clicked = alcaptain_services.quick_accept_all_eligible_orders(driver, driver.window_handles[0])
        except:
            pass
        order_tuple = alcaptain_services.select_order(driver, driver.window_handles[0])
        if order_tuple != None:
            country_code = order_tuple[4]
            order_name = midasbuy_services.midas_id_verifier(driver, driver.window_handles[1], order_tuple[1], 2, country_code)
            if order_name != "fail":
                output = midasbuy_services.midas_bundle_and_payment_method_chooser(driver, driver.window_handles[1], order_tuple[2], order_tuple[3], "Razer Gold", country_code)
                if output == None:
                    print("Main Code: ")
                    raise Exception
                razer_url = midasbuy_services.midas_razer_payment_initializer(driver, driver.window_handles[1], country_code)
                print("Main Code: razer url:" + str(razer_url))
                if razer_url != None:
                    login_success = razer_gold_services.razer_gold_login(razer_driver, razer_driver.window_handles[0], credentials, razer_url)
                    if login_success != None:
                        balance = razer_gold_services.razer_gold_check_balance(razer_driver, driver.window_handles[0], 1)
                        if balance == "G":
                            print("Main Code: archiving order")
                            archive((str(order_tuple[0]), str(order_tuple[1])))
                            transaction_id = razer_gold_services.razer_gold_proceed_to_check_out(razer_driver, razer_driver.window_handles[0], credentials)
                            #transaction_id = "R"
                            if transaction_id == None:
                                print("Main Code: transaction id is not obtained, enter any thing to continue the bot")
                                x = input()
                                continue
                            elif transaction_id == "R":
                                print("Main Code: Simply Restarting")
                            elif transaction_id == "S":
                                print("Main Code: Bot will be Stoped")
                                raise Exception
                            else:
                                reply_message = "The PUBG ID: " + str(order_tuple[1]) + "\nof Name: " + order_name + "\nhas recharged: " + str(order_tuple[2]) + " UC\nThe Transaction ID: " + transaction_id
                                alcaptain_services.successful_order_reply(driver, driver.window_handles[0], reply_message)
                        elif balance == "C":
                            counter += 1
                            print("Main Code: changing account")
                            if (counter > len(razer_accounts)):
                                counter = 0
                            credentials = razer_accounts[counter]
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
            elif order_name != None:
                print("MainCode: some error with Midasbuy, skipping")
            else:
                print("Main Code: Replying with Invalid Code")
                alcaptain_services.failed_order_reply(driver, driver.window_handles[0], "Your PUBG ID: " + str(order_tuple[1]) + " is invalid")
        elif order_tuple == None:
            temp_sus_orders_list = alcaptain_services.get_list_of_active_archived_orders(driver, driver.current_window_handle)
            for order in temp_sus_orders_list:
                if order not in sus_orders_list:
                    sus_orders_list.append(order)
                    print(" -MainCode: sending sus order to telegram group")
                    telegram_services.send_msg("AlCaptain ID:%20" + order[0].split("#")[1] + "%0D%0Ahis PUBG ID:+" + order[1] + "%0D%0Ais active and archived")
                    telegram_services.send_msg_dev("AlCaptain ID:%20" + order[0].split("#")[1] + "%0D%0Ahis PUBG ID:+" + order[1] + "%0D%0Ais active and archived")
except Exception as error_message:
    print("ERROR MESSAGE")
    print(error_message)
    telegram_services.send_msg_dev(error_message)
    telegram_services.send_msg(error_message)
finally:
    x = input("bot is over, enter anything to exit")
    driver.quit()
    razer_driver.quit()
    time.sleep(1)
    if os.path.exists("geckodriver.log"):
        os.remove("geckodriver.log") 