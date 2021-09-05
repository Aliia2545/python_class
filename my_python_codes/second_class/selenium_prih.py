from time import sleep
from selenium import webdriver
import sqlite3
conn = sqlite3.connect(r'data.db')
cursor = conn.cursor()
browser = webdriver.Chrome(r'C:\Users\aliya\OneDrive\Рабочий стол\my_python_codes\chromedriver_win32\chromedriver.exe')
email = "aliya.beiwenalieva@gmail.com"
password = "2545Alii@"
try:
    browser.get(r'https://datamasters.ru/aianddata')
    sleep(5)
    browser.get(r'https://api.datamasters.ru/auth/login')
    sleep(5)
    email_input = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div/span/div[1]/span/div/input')
    password_input = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div/span/div[2]/span/div/input')


    email_input.clear()
    password_input.clear()
    email_input.send_keys(email)
    sleep(5)
    password_input.send_keys(password)
    sleep(5)
    browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div/span/div[4]/button').click()
    sleep(15)
    de = browser.find_element_by_css_selector('#tasks__list')
    sleep(10)
    print(de.text)
    de2 = browser.find_elements_by_css_selector('#task-247 > div > div:nth-child(3) > div')
    cursor.execute(f"""INSERT INTO data (страна) values (de2);""")
    result = cursor.fetchall()
    conn.commit()

    print('success')
    sleep(5)
    # for i in range(6):
    #     browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/main/main/div/div[3]/div[2]/div/div/a[2]').click()
    #     sleep(20)
    #     de2 = browser.find_element_by_css_selector('#tasks__list')
    #     sleep(10)
    #     print(de2.text)
    #     sleep(5)

    sleep(3000)
    browser.quit()
except Exception as ex:
    browser.quit()
    raise ex


# browser.get("https://metanit.com/python/tutorial/2.4.php")
# sleep(5)
#
# browser.execute_script("window.open('https://postgrespro.ru/docs/postgresql/9.4/sql-createtable/', 'new_window')")
# sleep(5)
# browser.close()
#
# # browser.quit()
#  f"""INSERT INTO numbers (first_n, second_n, third_n, firth_n, fifth_n, six_n, seven_n, pub_date) values ({(fresh_num_data[0])}, {fresh_num_data[1]}, {fresh_num_data[2]}, {fresh_num_data[3]}, {fresh_num_data[4]}, {fresh_num_data[5]}, {fresh_num_data[6]}, '{datetime.now()}');""")