import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def login(driver, user, password):
    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.link'))
    )
    login.click()

    user_password = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.input-wrapper input'))
    )
    user_password_list = [up for up in user_password]
    user_password_list[0].send_keys(user)
    user_password_list[1].send_keys(password)

    submit = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.red.submit.shared-button-custom.css-12vlaew'))
    )
    submit.click()

    time.sleep(3)

    driver.refresh()