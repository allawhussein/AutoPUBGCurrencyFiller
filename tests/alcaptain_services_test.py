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

driver = webdriver.Firefox()

alcaptain_services.get_alcaptain_main_page(driver, driver.current_window_handle)
alcaptain_services.quick_accept_all_eligible_orders(driver, driver.current_window_handle)
alcaptain_services.select_order(driver, driver.current_window_handle)
alcaptain_services.get_list_of_active_archived_orders(driver, driver.current_window_handle)
