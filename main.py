from itertools import count
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver = webdriver.Chrome(
    executable_path= 'D:\JetBrains\chromedriver\chromedriver.exe'
)

def send_wa_msg (phone_number, text, count):
    try:
        driver.get (url='https://web.whatsapp.com/')
        sleep(15)

        driver.get (url='https://web.whatsapp.com/send?phone={phone_number}')
        sleep(10)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')))
        text_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')

        for i in range(count):
            text_box.send_keys(text)
            text_box.send_keys('\n')

        print(f'Сообщение отправлено #{count} times.')
        sleep(5)

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()

        return 'Это работает!'

def main ():
    phone_number = input('Введи номер телефона:')
    text = input('Введи текст сообщения:')
    count = int (input('Сколько раз отрпавляем?:'))
    send_wa_msg(phone_number=phone_number, text=text, count=count)

if __name__ == '__main__':
    main()