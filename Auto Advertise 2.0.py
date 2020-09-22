#Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import json

#get the right driver

driver = webdriver.Chrome(ChromeDriverManager().install())

#discord_email = 'sodium.uwu.meep@gmail.com'
#discord_password = 'Soccer0127'



startup = input('Add email and password to json file? y/n ')
if startup == 'y':
    print('Adding email and password...')
    User_and_pass_data = {}
    save_name = input('What do you want to save the username and password as? (For ex. 1)(Press enter for default save name) ')
    if save_name == '':
        save_name = 'tux'
    else:
        print('Saving to save name: ' + save_name)
    save_email = input("""What is the account's email? """)
    save_password = input("""What is the account's password? """)
    u = open('username_and_password_data.json')
    User_and_pass_data = json.load(u)
    User_and_pass_data[save_name] = {'email': save_email, 'password': save_password}
    with open('username_and_password_data.json', 'w') as u:
        json.dump(User_and_pass_data, u)
    print('Done')
else:
    print('Continuing...')

add_add_to_json_file = input('Do you want to add a advertisement to a json file? ')
if add_add_to_json_file == 'y':
    add_save_name = input('What save name do you want to save the advertisement as? (For ex. add1) ')
    add_line1 = input('What do you want line one to be? (there are 10 lines) ')
    add_line2 = input('What do you want line two to be? ')
    add_line3 = input('What do you want line three to be? ')
    add_line4 = input('What do you want line four to be? ')
    add_line5 = input('What do you want line five to be? ')
    add_line6 = input('What do you want line six to be? ')
    add_line7 = input('What do you want line seven to be? ')
    add_line8 = input('What do you want line eight to be? ')
    add_line9 = input('What do you want line nine to be? ')
    add_line10 = input('What do you want line ten to be? ')
    a = open('add.json')
    add_data = json.load(a)
    add_data[add_save_name] = {'line1': add_line1, 'line2': add_line2, 'line3': add_line3, 'line4': add_line4, 'line5': add_line5, 'line6': add_line6, 'line7': add_line7, 'line8': add_line8, 'line9': add_line9, 'line10': add_line10}
    print('Adding advertisement to json file...')
    with open('add.json', 'w') as a:
        json.dump(add_data, a)
    print('Done')
else:
    print('Continuing')

select_add = input('Which advertisement save name do you want to load? ')
a = open('add.json')
add_data = json.load(a)
line1 = (add_data[select_add]['line1'])
line2 = (add_data[select_add]['line2'])
line3 = (add_data[select_add]['line3'])
line4 = (add_data[select_add]['line4'])
line5 = (add_data[select_add]['line5'])
line6 = (add_data[select_add]['line6'])
line7 = (add_data[select_add]['line7'])
line8 = (add_data[select_add]['line8'])
line9 = (add_data[select_add]['line9'])
line10 = (add_data[select_add]['line10'])

print('This is your add:')
if line1 == '':
    print('line 1 is empty, not using it')
else:
    print(line1)
if line2 == '':
    print('line 2 is empty, not using it')
else:
    print(line2)
if line3 == '':
    print('line 3 is empty, not using it')
else:
    print(line3)
if line4 == '':
    print('line 4 is empty, not using it')
else:
    print(line4)
if line5 == '':
    print('line 5 is empty, not using it')
else:
    print(line5)
if line6 == '':
    print('line 6 is empty, not using it')
else:
    print(line6)
if line7 == '':
    print('line 7 is empty, not using it')
else:
    print(line7)
if line8 == '':
    print('line 8 is empty, not using it')
else:
    print(line8)
if line9 == '':
    print('line 9 is empty, not using it')
else:
    print(line9)
if line10 == '':
    print('line 10 is empty, not using it')
else:
    print(line10)

sstartup = input('import email and password from json file? y/n (It is recommended to say y) ')
if sstartup == 'y':
    load_name = input('What save name do you want to load? (Press enter for default save name) ')
    if load_name == '':
        load_name = 'tux'
        print('Logging in with default save')
    else:
        print('Logging in with save name: ' + load_name)
    u = open('username_and_password_data.json')
    User_and_pass_data = json.load(u)
    print('Using this to log in with:')
    print('Email: ' + User_and_pass_data[load_name]['email'])
    print('Password: ' + User_and_pass_data[load_name]['password'])
    discord_email = (User_and_pass_data[load_name]['email'])
    discord_password = (User_and_pass_data[load_name]['password'])
elif sstartup == 'n':
    discord_email = input('What is the account email? ')
    discord_password = input('What us the account password? ')
    #discord_account_home_page = 'https://discord.com/channels/@me'
else:
    print('Please answer y or n')
    exit()

#print("""This is the login page of your account, if it isn't, then the script wont work.""" + discord_account_home_page)

#main

driver.get('https://discord.com/login')
time.sleep(5)

def login():
    global discord_ussername
    global discord_password
    print('loging in...')
    email = driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input""")
    email.send_keys(discord_email)
    time.sleep(5)
    password = driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input""")
    password.send_keys(discord_password)
    time.sleep(5)
    Login = driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]""")
    Login.click()
    time.sleep(15)
    print('Done')
    SwitchToTheServer()

def SwitchToTheServer():
    print('Checking login...')
    if driver.current_url == 'https://discord.com/channels/@me':
        print('Switching to the discord server...')
        driver.execute_script("window.open('https://discord.com/channels/302094807046684672/332967590685310978');")
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(0.1)
        driver.close()
        time.sleep(0.1)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(15)
        print('Done')
        Main()
    elif driver.current_url == 'https://discord.com/login':
        print('Check your accounts email')
    else:
        print('An error has occurred...')

def Main():
    PrintAvt = ['What is TraquilCraft?',
                'TraquilCraft is a non-toxic Minecraft Bedrock SMP server for you and your friends to play on!',
                'That means:',
                '- No Super complicated plugins',
                '- No Griefing',
                '- No toxicity',
                'If you are interested in TraquilCraft, Dm Me!']
    text_box = driver.find_element_by_xpath("""//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div[1]/div/div/div/div[1]/div[2]""")
    if line1 == '':
        print('line 1 is empty, not using it ')
    else:
        text_box.send_keys(line1)
        time.sleep(0.1)
        text_box.send_keys(Keys.SHIFT + Keys.RETURN)
        time.sleep(0.1)
    if line2 == '':
        print('line 2 is empty, not using it ')
    else:
        text_box.send_keys(line2)
        time.sleep(0.1)
        text_box.send_keys(Keys.SHIFT + Keys.RETURN)
        time.sleep(0.1)
    if line3 == '':
        print('line 3 is empty, not using it ')
    else:
        text_box.send_keys(line3)
        time.sleep(0.1)
        text_box.send_keys(Keys.SHIFT + Keys.RETURN)
        time.sleep(0.1)
    if line4 == '':
        print('line 4 is empty, not using it ')
    else:
        text_box.send_keys(line4)
        time.sleep(0.1)
        text_box.send_keys(Keys.SHIFT + Keys.RETURN)
        time.sleep(0.1)
    if line5 == '':
        print('line 5 is empty, not using it ')
    else:
        text_box.send_keys(line5)
        time.sleep(0.1)
        text_box.send_keys(Keys.SHIFT + Keys.RETURN)
        time.sleep(0.1)
    if line6 == '':
        print('line 6 is empty, not using it ')
    else:
        text_box.send_keys(line6)
        time.sleep(0.1)
        text_box.send_keys(Keys.SHIFT + Keys.RETURN)
        time.sleep(0.1)
    if line7 == '':
        print('line 7 is empty, not using it ')
    else:
        text_box.send_keys(line7)
        time.sleep(0.1)
        text_box.send_keys(Keys.SHIFT + Keys.RETURN)
    if line8 == '':
        print('line 8 is empty, not using it ')
    else:
        text_box.send_keys(line8)
        time.sleep(0.1)
        text_box.send_keys(Keys.SHIFT + Keys.RETURN)
    if line9 == '':
        print('line 9 is empty, not using it ')
    else:
        text_box.send_keys(line9)
        time.sleep(0.1)
        text_box.send_keys(Keys.SHIFT + Keys.RETURN)
    if line10 == '':
        print('line 10 is empty, not using it ')
    else:
        text_box.send_keys(line10)
        time.sleep(0.1)
        text_box.send_keys(Keys.SHIFT + Keys.RETURN)
    text_box.send_keys(Keys.RETURN)
    Tsleep = random.randint(2000, 2100)
    print('avetisment delay: ' + str(Tsleep / 60) + 'm')
    time.sleep(Tsleep)
    Main()

login()