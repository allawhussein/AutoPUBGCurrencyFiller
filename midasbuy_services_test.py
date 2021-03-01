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

if midasbuy_services.midas_id_verifier(driver, driver.window_handles[0], 5474774295, 1, "my"):
    print(midasbuy_services.midas_bundle_and_payment_method_chooser(driver, driver.window_handles[0], 600, 0,"Razer Gold", "my"))
    print(midasbuy_services.midas_razer_payment_initializer(driver, driver.window_handles[0], "my"))