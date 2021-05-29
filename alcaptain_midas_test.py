from selenium import webdriver #this is needed to basicly anything
from selenium.webdriver import ActionChains #this used to open some hover menus
from selenium.webdriver.support import expected_conditions as EC #this is used to prevent the driver form clicking unloaded elements
from selenium.webdriver.common.by import By #this used for element finding method
from selenium.webdriver.common.keys import Keys #this is used to simiulate keyboard keys
from selenium.common.exceptions import TimeoutException
import os
import time

from services.variables import *
from services import alcaptain_services
from services import midasbuy_services
from services import razer_gold_services
from services import telegram_services

driver = webdriver.Firefox()

print(alcaptain_services.get_alcaptain_main_page(driver, driver.current_window_handle))
print(alcaptain_services.quick_accept_all_eligible_orders(driver, driver.current_window_handle))
order_tuple = alcaptain_services.select_order(driver, driver.current_window_handle)
print(order_tuple)
driver.execute_script('window.open("about:blank","_blank");')
print(midasbuy_services.midas_id_verifier(driver, driver.window_handles[1], order_tuple[1], 1, "my"))
print(midasbuy_services.midas_bundle_and_payment_method_chooser(driver, driver.window_handles[1], order_tuple[2], order_tuple[3],"Razer Gold", "my"))