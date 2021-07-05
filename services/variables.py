import pyotp#this library is used for the two factor authentication by razer
import os.path

alcaptain_login_username = "Auto_API"
alcaptain_login_password = "112233jj"
alcaptain_prompt_username = "Fawaz"
alcaptain_prompt_password = "Qwe123@$"

country_code = "my"
payment_method = "Razer Gold"
target_order = "Pubg . Mobile By ID"

country_code_list = ["my", "ot"]
target_order_list = ["Pubg . Mobile By ID", "Pubg Mobile By ID"]

pubg_id_verifier_wait = 10 #number of seconds to wait for correct ID verification
time_of_waiting = 15 #this number is based on internet speed, the lower the internet speed the higher the number
razer_payment_wait = 5

razer_email = "alcaptain.usa16@gmail.com"
razer_password = "112233jj"
razer_tfa = "JJUDKQRZJZYDO6CZGVYFGVCWJBBXC6TXNBAUY32FGJZUYWKP"

sleeping_time = 1 #number of seconds before refreshing
razer_payment_wait = 10

browser = "firefox"

account_pointer = 0

verification_trails = 2

sus_orders_list = []

totp = pyotp.TOTP(razer_tfa)#we can get the one time code using int(totp.now())

razer_accounts = []
def initialize_variables():
    with open("razer_accounts.txt", "r") as accounts_file:
        for account in accounts_file.readlines():
            razer_accounts.append(account.split("\n")[0].split(","))

    assert len(razer_accounts) > 0, "NO RAZER ACCOUNTS ARE FOUND"

    print(" -VS: using the follwing razer accounts")
    for i in range(len(razer_accounts)):
        print("  " + razer_accounts[i][0])
        razer_accounts[i][2] = pyotp.TOTP(razer_accounts[i][2])
    else:
        print(" -VS: seting up is complete launching bot")

def archive(order_data = None):
    if order_data == None:
        if os.path.isfile("archive.csv"):
            csv_file = open("archive.csv", "r")
            list_of_data = csv_file.readlines()
            for row in list_of_data:
                list_of_data[list_of_data.index(row)] = tuple(row.split("\n")[0].split(","))
            csv_file.close()
            return list_of_data
        else:
            return []
    else:
        csv_file = open("archive.csv", "a")
        csv_file.write(str(order_data[0]) + "," + str(order_data[1]) + "\n")
        csv_file.close()

def rewrite_accounts(counter):
    with open("razer_accounts.txt", "r") as accounts_file:
        accounts = accounts_file.readlines()
    with open("razer_accounts.txt", "w") as accounts_file:
        print(" -RA: reordring razer accounts")
        for line in accounts[counter:]:
            print("  " + line)
            accounts_file.write(line)
        for line in accounts[:counter]:
            print("  " + line)
            accounts_file.write(line)