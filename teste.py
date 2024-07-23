import requests
import json
import time
import customtkinter as ctk
import globals
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from interface.aviso import show_aviso
from interface.login import interface_login
from login import login

def enter_clickable(selector):
        clickable = driver.find_element(By.CSS_SELECTOR, selector)
        if clickable.is_enabled():
            return True
        else:
            return False
        
def get_recent_colors():
    try:
        response = requests.get('https://blaze.com/api/roulette_games/recent')
        response.raise_for_status()
        jsonData = response.json()
        return [x['color'] for x in jsonData], [x['id'] for x in jsonData]
    except (requests.RequestException, ValueError) as e:
        print(f"Erro ao obter ou processar dados: {e}")
        return [], []
        
def place_bet(bet_input, enter_button, color, bet_amount, ids):

    if color == 0:
        colors_white, ids_white = get_recent_colors
        for c in colors_white:
            if c != 0:
                color = c
                break


    print(f'SEQUENCIA REALIZADA\ncolors: {colors}\n\n')
    
    
    bet_input.clear()

    color_map = {
        1: 'div.black',
        2: 'div.red'
    }

    # bet_input.send_keys('0.1')

    # white = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, 'div.white'))
    # )
    # white.click()
    # time.sleep(0.5)
    # enter_button.click()


    # print('APOSTA DE 0.1 NO BRANCO')


    # bet_input.clear()
    bet_input.send_keys(str(bet_amount))

    color_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, color_map[color]))
    )
    color_element.click()
    time.sleep(0.5)
    enter_button.click()


    print(f'APOSTA DE {bet_amount} NO {color_map[color]}\n')

    time.sleep(1)
    while enter_clickable('button.shared-button-custom.css-1apb7jj'):
        time.sleep(2)
    while not enter_clickable('button.shared-button-custom.css-1apb7jj'):
        time.sleep(2)

    colors_pb, ids_pb = get_recent_colors()

    if ids != ids_pb:
        if colors_pb[0] == colors_pb[1] or colors_pb[0] == 0:


            print(f'APOSTA NAO CONCRETIZADA\n\n')


            place_bet(bet_input, enter_button, colors_pb[0], bet_amount*2, ids_pb)

    
    print('APOSTA CONCRETIZADA\n\n')


try:
    driver = Driver(uc=True)
    driver.get(
        'https://blaze.com/en/games/double'
    )

    login(driver, globals.username, globals.password)

    
    print(f'INICIANDO MARTIN GALE\nbet_amount: {globals.bet_amount}\nreps: {globals.reps}\n\n')


    bet_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.input-field'))
    )
    enter_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.shared-button-custom.css-1apb7jj'))
    )

    while True:  
        bet_input.send_keys('0.1')  
        counter = 0
        colors, ids = get_recent_colors()
        bet_amount = globals.bet_amount

        if len(colors) >= globals.reps:
            color = colors[0]
            for i in range(globals.reps):
                if color == colors[globals.reps - i - 1]:
                    counter += 1
            if counter == globals.reps:
                if enter_clickable('button.shared-button-custom.css-1apb7jj'):
                    place_bet(bet_input, enter_button, color, bet_amount, ids)

        bet_input.clear()
    
except Exception as e:
    print(f"Erro ao processar a sequência da roleta: {e}")
    driver.quit()