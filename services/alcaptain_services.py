from selenium import webdriver #this is needed to basicly anything
from selenium.webdriver import ActionChains #this used to open some hover menus
from selenium.webdriver.support import expected_conditions as EC #this is used to prevent the driver form clicking unloaded elements
from selenium.webdriver.common.by import By #this used for element finding method
from selenium.webdriver.common.keys import Keys #this is used to simiulate keyboard keys
from variables import *
import time

def open_dashboard_window(driver, window_handle):
    driver.switch_to.window(window_handle)
    dashboard_main_button_xpath = "/html/body/div[2]/div[1]/div/ul/li[1]/a"
    dashboard_main_button = driver.find_element_by_xpath(dashboard_main_button_xpath)
    close_all_alcaptain_tabs_xpath = "/html/body/div[2]/div[1]/div/ul/ul/a[3]"
    print(" -ODW: opening dashboard main menu")
    action_chains = ActionChains(driver)
    action_chains.context_click(dashboard_main_button)
    action_chains.move_to_element(driver.find_element_by_xpath(close_all_alcaptain_tabs_xpath))
    action_chains.click(on_element = driver.find_element_by_xpath(close_all_alcaptain_tabs_xpath))
    action_chains.click(on_element = driver.find_element_by_xpath(dashboard_main_button_xpath))
    action_chains.perform()

def get_alcaptain_main_page(driver, window_handle, force_refresh = 0):#this funciton will take as a parameter the driver, and the handle, it does what it says
    alcaptain_url = "https://" + alcaptain_prompt_username + ":" + alcaptain_prompt_password + "@alcaptainunlock.com/Chadid2020/main.php?page=home"
    print(" -GAMP: service get_alcaptain_main_page is initiated")
    #move the driver to the specified window handle
    driver.switch_to.window(window_handle)
    time_zero = time.time()
    first_loop = 1
    while time.time() - time_zero < time_of_waiting:
        #make sure we are in alcaptain unlock site
        if "alcaptainunlock.com" in driver.current_url and first_loop:
            print(" -GAMP: driver is at alcaptainunlock.com")
            first_loop = 0
            if force_refresh:
                print(" -GAMP: force reloading")
                driver.get(alcaptain_url)
        else:
            driver.get(alcaptain_url)
            print(" -GAMP: opening alcaptainunlock.com")
        if "404! File Not Found" in driver.find_element_by_tag_name("body").text:
            print(" -GAMP: probably PROMPT credentials are WRONG, if you see this text a lot, check these credentials")
            return get_alcaptain_main_page(driver, window_handle)
        
        try:#verifiy we are logged in, check if dashboard is present
            dhru_dashboard_xpath = '//*[@id="tabs-group"]'
            driver.find_element_by_xpath(dhru_dashboard_xpath)
            print(" -GAMP: we are signed in")
            open_dashboard_window(driver, driver.current_window_handle)
            return 1
        except:
            pass
        try:#checking for session-expired div
            driver.find_element_by_class_name("session-expired").click()#when the site loads it will show this a note, just click it
            print(" -GAMP: clicking for session-expired div")
            time_zero = time.time()
        except:
            pass
        try:#checking for login portal
            driver.find_element_by_id("username").send_keys(alcaptain_login_username)
            driver.find_element_by_class_name("passwordd").send_keys(alcaptain_login_password)
            print(" -GAMP: filled credentials")
            driver.find_element_by_css_selector(".btn").click()
            print(" -GAMP: clicked login button")
            time_zero = time.time()
        except:
            pass
        try:#checking if password is wrong
            driver.switch_to.alert.accept()
            print(" -GAMP: wrong DHRU credentials, if you see this messge a lot, check you credentials")
        except:
            pass
    return get_alcaptain_main_page(driver, window_handle)

def quick_accept_all_eligible_orders(driver, window_handle, order_phrase_list = target_order_list):
    print(" -QAAEO: service quick_accept_all_eligible_orders() v1.0 is initiated, change log avilable in code")
    #added version number to aviod confusion with constant updates
    driver.switch_to.window(window_handle)

    print(" -QAAEO: opening alcatain dashboard page")
    open_dashboard_window(driver, window_handle)
    print(" -QAAEO: searching for iframe")
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    print(" -QAAEO: switching to iframe")
    while driver.execute_script("return document.readyState;") != "complete":
        pass
    table = driver.find_element_by_tag_name("table")
    print(" -QAAEO: searching for table rows and choosing the third one")
    third_row = table.find_elements_by_tag_name("td")[2]
    print(" -QAAEO: clicking accepted button")
    third_row.find_elements_by_tag_name("h3")[1].click()

    print(" -QAAEO: opening server order page")
    print(" -QAAEO: switching back to main page")
    driver.switch_to.default_content()
    print(" -QAAEO: searching for iframe")
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    print(" -QAAEO: switching to iframe")
    print(" -QAAEO: waiting for quick accept button to appear")
    webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.presence_of_element_located((By.ID, "tab34")))
    print(" -QAAEO: clicking quick accept button")
    driver.execute_script("arguments[0].click();", driver.find_element_by_id("tab33"))
    print(" -QAAEO: opeing new order page")
    print(" -QAAEO: starting to accept orders")
    try:
        print(" -QAAEO: waiting for table of orders to appear")
        webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.presence_of_element_located((By.ID, "_contentTable")))
        table_row = driver.find_element_by_id("row_0")#simple check for the presence of any usable data
        if table_row.text == 'No data found':
            print(" -QAAEO: New orders queue is empty")
            query = 0
        else: 
            query = 1
    except:
        query = 0
        print (" -QAAEO: New orders queue is empty")

    orders_clicked = 0
    if query > 0:
        print(" -QAAEO: caching all table rows")
        list_of_orders = driver.find_elements_by_class_name("dg_tr")
        print(" -QAAEO: removing table header")
        list_of_orders.pop(0)
        print(" -QAAEO: filtering orders")      
        for order_phrase in order_phrase_list:
            print(" -QAAEO: clicking valid orders for " + country_code_list[order_phrase_list.index(order_phrase)])
            for order in list_of_orders:
                if order_phrase in order.find_elements_by_tag_name("td")[2].find_element_by_tag_name("label").text:
                    order_box = order.find_elements_by_tag_name("td")[0]#click the check box of valid elements
                    driver.execute_script("arguments[0].click();", order_box)
                    orders_clicked += 1
        if orders_clicked:
            print(" -QAAEO: " + str(orders_clicked) + " orders accepted")
            print(" -QAAEO: pressing accept selected")
            accept_selected = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[5]/table/tbody/tr/td/div/table/tbody/tr/td/input[1]")#click accept selected
            driver.execute_script("arguments[0].click();", accept_selected)

    driver.switch_to.default_content()
    driver.find_element_by_tag_name("ul").find_element_by_tag_name("li").click()#return to dashboard
    print(" -QAAEO: returning to dashboard")

    print(" -QAAEO: closing quick accept tab")
    ActionChains(driver).context_click(driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[2]/a")).perform()

    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/ul/a[2]").click()
    print(" -QAAEO: page quick add orders tab is closed")
    print(" -QAAEO: quick_accept_all_eligible_orders() service is over")
    driver.switch_to.default_content()
    return orders_clicked
    
def select_order(driver, window_handle, order_phrase_list = target_order_list):
    time_of_waiting = 60
    print(" -SO: select_order() service is initiated")
    print(" -SO: opening dashboard window")
    open_dashboard_window(driver, driver.current_window_handle)

    print(" -SO: switching to iframe")
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

    print(" -SO: clicking server_orders->accepted_orders button")
    accepted_server_order_xpath = "/html/body/div[4]/div[2]/div[2]/div/div/table/tbody/tr/td[3]/div/div[3]/a/h3"
    orders_button = driver.find_element_by_xpath(accepted_server_order_xpath)
    orders_button.click()
    
    driver.switch_to.default_content()

    print(" -SO: switching to iframe")
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

    print(" -SO: waiting for table head to appear")
    table_head_xpath = "/html/body/div[4]/div/div[2]/div/form[2]/div[1]/table/thead"
    webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.presence_of_element_located((By.XPATH, table_head_xpath)))

    print(" -SO: starting to collect table rows")
    list_of_orders = driver.find_elements_by_tag_name("tr")
    list_of_orders.pop(0)
    list_of_valid_orders = []

    print(" -SO: " + str(len(list_of_orders)) + " orders are found")
    print(" -SO: searching for PUBG Mobile Orders, country codes: ", end="")
    print(country_code_list, sep = ", ")
    if len(list_of_orders) > 0:
        counter = 0
        print(" -SO: clearing non " + ", ".join(country_code_list) + " RAZER GOLD orders")
        for order in list_of_orders:
            for order_phrase in order_phrase_list:
                if order_phrase in order.find_elements_by_tag_name("td")[1].text:
                    row_id = order.find_element_by_tag_name("td").text
                    row_pubg_id = int(order.find_elements_by_tag_name("td")[4].text.split(">")[1])
                    if (row_id, str(row_pubg_id)) not in archive():
                        list_of_valid_orders.append(order)
                        break
        print(" -SO: " + str(len(list_of_valid_orders)) + " valid PUBG Mobile orders are found")
    order_chosen = 0
    if len(list_of_valid_orders) > 0:#if no requests are present, just keep refreshing
        for order in list_of_valid_orders:
            for order_phrase in order_phrase_list:
                if order_phrase in order.find_elements_by_tag_name("td")[1].text:
                    print(" -SO: collecting first player info")
                    order_id = order.find_element_by_tag_name("td").text#i will keep it is a string to make identifying it easier using "in"
                    order_uc = order.find_elements_by_tag_name("td")[1].text.split(" ")[0]
                    order_pubg_id = int(order.find_elements_by_tag_name("td")[4].text.split(">")[1])
                    country_code = country_code_list[order_phrase_list.index(order_phrase)]
                    order_chosen = 1
                    break
            if order_chosen == 1:
                break
        if "+" in order_uc:
            print(" -SO: new order UC style")
            offer_uc = int(order_uc.split("+")[1])
            order_uc = int(order_uc.split("+")[0]) + offer_uc
        else:
            try:
                offer_uc = int(order.find_elements_by_tag_name("td")[1].text.split("(")[1].split(" ")[0])
                offer_uc = offer_uc - int(order_uc)
                order_uc = int(order_uc)
            except Exception as error_message:
                print(" -SO: no offer UC included")
                offer_uc = 0
                order_uc = int(order_uc)
            else:
                print(" -SO: old order UC style")
        print(" -SO: order information")
        print("     |-alcaptainUnlock Order ID " + order_id)
        print("     |-required UC " + str(order_uc))
        print("     |-offer UC " + str(offer_uc))
        print("     |-Pubg ID " + str(order_pubg_id))
        print("     |-Country Code " + country_code)

        print(" -SO: opening order reply page")
        driver.execute_script("arguments[0].click();", order.find_element_by_tag_name("td").find_element_by_tag_name("a"))
        driver.switch_to.default_content()
        while driver.execute_script("return document.readyState;") != "complete":
            pass
        
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        while driver.execute_script("return document.readyState;") != "complete":
            pass

        driver.switch_to.default_content()
        print(" -SO: select_order() service is over")
        return (order_id, order_pubg_id, order_uc, offer_uc, country_code)
    else:
        return None

def successful_order_reply(driver, window_handle, reply_message):
    print(" -SOR: successful_order_reply service initiated")
    print(" -SOR: checking if loaded page is valid")
    driver.switch_to.window(window_handle)
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    try:
        reply_page_title_xpath = "/html/body/div[4]/form/div/div/div[1]/div/div/div[1]/h2/span"
        webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.presence_of_element_located((By.XPATH, reply_page_title_xpath)))
    except:
        choice = input("either not reply page, or page took to long to open, enter (R) to reply the procedure, or anything to terminate the service ")
        if choice == "R" or choice == "r":
            driver.switch_to.default_content()
            successful_order_reply(driver, window_handle, reply_message)
    else:
        print(" -SOR: waiting for response box to load")
        webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.presence_of_element_located((By.XPATH, '//*[@id="replycode_ifr"]')))
        print(" -SOR: checking reply button")
        iframe = driver.find_element_by_xpath('//*[@id="replycode_ifr"]')
        print(" -SOR: switching to iframe of class name: " + str(iframe.get_attribute("class")))
        driver.switch_to.frame(iframe)
        print(" -SOR: wainting for text input to appear")
        webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tinymce"]')))
        print(" -SOR: writing response")
        driver.find_element_by_xpath('//*[@id="tinymce"]').send_keys(reply_message)
        driver.switch_to.default_content()
        iframe = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[1]/iframe")
        print(" -SOR: switching to iframe")
        driver.switch_to.frame(iframe)
        success_button = driver.find_element_by_xpath('//*[@id="btnsuccess"]')
        driver.execute_script("arguments[0].click();", success_button)
        print(" -SOR: success button pressed")

def failed_order_reply(driver, window_handle, reply_message):
    print(" -FOR: failed_order_reply service initiated")
    print(" -FOR: checking if loaded page is valid")
    driver.switch_to.window(window_handle)
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    try:
        reply_page_title_xpath = "/html/body/div[4]/form/div/div/div[1]/div/div/div[1]/h2/span"
        webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.presence_of_element_located((By.XPATH, reply_page_title_xpath)))
    except:
        choice = input("either not reply page, or page took to long to open, enter (R) to reply the procedure, or anything to terminate the service ")
        if choice == "R" or choice == "r":
            driver.switch_to.default_content()
            successful_order_reply(driver, window_handle, reply_message)
    else:
        print(" -FOR: waiting rejection reason radio button to appear")
        webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/form/div/div/div[1]/div/div/div[5]/div/div[1]/div[1]/div[2]/div/label/input")))
        print(" -FOR: clicking reject order")
        driver.find_element_by_xpath("/html/body/div[4]/form/div/div/div[1]/div/div/div[5]/div/div[1]/div[1]/div[2]/div/label/input").click()
        print(" -FOR: submitting rejection reason")
        driver.find_element_by_xpath('//*[@id="rejectreason"]').send_keys(reply_message)
        print(" -FOR: clicking reject order")
        reject_button = driver.find_element_by_xpath('//*[@id="btnreject"]')
        driver.execute_script("arguments[0].click();", reject_button)

def get_list_of_active_archived_orders(driver, window_handle, order_phrase_list = target_order_list):
    print(" -GLOAAO: get_list_of_active_archived_orders() service is initiated")
    print(" -GLOAAO: opening dashboard window")
    open_dashboard_window(driver, driver.current_window_handle)

    print(" -GLOAAO: switching to iframe")
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

    print(" -GLOAAO: clicking server_orders->accepted_orders button")
    accepted_server_order_xpath = "/html/body/div[4]/div[2]/div[2]/div/div/table/tbody/tr/td[3]/div/div[3]/a/h3"
    orders_button = driver.find_element_by_xpath(accepted_server_order_xpath)
    orders_button.click()
    
    driver.switch_to.default_content()

    print(" -GLOAAO: switching to iframe")
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

    print(" -GLOAAO: waiting for table head to appear")
    table_head_xpath = "/html/body/div[4]/div/div[2]/div/form[2]/div[1]/table/thead"
    webdriver.support.ui.WebDriverWait(driver, time_of_waiting).until(EC.presence_of_element_located((By.XPATH, table_head_xpath)))

    print(" -GLOAAO: starting to collect table rows")
    list_of_orders = driver.find_elements_by_tag_name("tr")
    list_of_orders.pop(0)
    list_of_archived_orders = []

    print(" -GLOAAO: " + str(len(list_of_orders)) + " orders are found")
    print(" -GLOAAO: searching for archived PUBG Mobile Orders, country codes: ", end="")
    print(country_code_list, sep = ", ")
    if len(list_of_orders) > 0:
        counter = 0
        print(" -GLOAAO: clearing non " + ", ".join(country_code_list) + " RAZER GOLD orders")
        for order in list_of_orders:
            for order_phrase in order_phrase_list:
                if order_phrase in order.find_elements_by_tag_name("td")[1].text:
                    row_id = order.find_element_by_tag_name("td").text
                    row_pubg_id = int(order.find_elements_by_tag_name("td")[4].text.split(">")[1])
                    if (row_id, str(row_pubg_id)) in archive():
                        list_of_archived_orders.append((row_id, str(row_pubg_id)))
                        break
    if len(list_of_archived_orders):
        print(" -GLOAAO: " + str(len(list_of_archived_orders)) + " archived PUBG Mobile orders are found, sending new stall order to through telegram")
    else:
        print(" -GLOAAO: no duplicate archived orders are found")

    return list_of_archived_orders

if __name__ == "__main__":
    driver = webdriver.Firefox()
    get_alcaptain_main_page(driver, driver.window_handles[0])
    quick_accept_all_eligible_orders(driver, driver.window_handles[0], ["Pubg . Mobile"])
    print(select_order(driver, driver.window_handles[0], ["Pubg . Mobile"]))