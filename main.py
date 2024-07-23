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

app = ctk.CTk()

show_aviso(app)

app.title('Blaze Assistant')
app.geometry('900x600')

interface_login(app)

app.mainloop()


def get_recent_colors():
    try:
        response = requests.get('https://blaze.com/api/roulette_games/recent')
        response.raise_for_status()
        jsonData = response.json()
        return [x['color'] for x in jsonData], [x['id'] for x in jsonData]
    except (requests.RequestException, ValueError) as e:
        print(f"Erro ao obter ou processar dados: {e}")
        return [], []

def place_bet(color, bet_amount):
    try:
        open = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.time-left'))
        )
        
        if 'In' in open.text:
            for i in range(1):
                bet_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'input.input-field'))
                )
                bet_input.clear()
                bet_input.send_keys('0.1')

                white = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.white'))
                )
                white.click()

                enter_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'button.shared-button-custom.css-1apb7jj'))
                )
                #enter_button.click()

                print(f'aposta de 0.1 na cor 0')

                color_map = {
                    1: 'div.black',
                    2: 'div.red'
                }

                time.sleep(1)
                
                if color in color_map:
                    color_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, color_map[color]))
                    )
                    color_element.click()

                    bet_input.clear()
                    bet_input.send_keys(str(bet_amount))
                    
                    enter_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.shared-button-custom.css-1apb7jj'))
                    )
                    #enter_button.click()

                    print(f'aposta de {bet_amount} na cor {color}')
                    
                    return True

    except Exception as e:
        print(f"Erro ao fazer a aposta: {e}")
        return False

def get_last_result():
    try:
        response = requests.get('https://blaze.com/api/roulette_games/recent')
        response.raise_for_status()
        jsonData = response.json()
        return jsonData[0]['color'], jsonData[0]['id']
    except (requests.RequestException, ValueError) as e:
        print(f"Erro ao obter ou processar dados: {e}")
        return None, None

try:
    driver = Driver(uc=True)  # Adicione os argumentos necessários aqui
    driver.get(
        'https://blaze.com/en/games/double'
    )

    login(driver, globals.username, globals.password)

    while True:
        counter = 0
        colors, bet_ids = get_recent_colors()
        if len(colors) >= globals.reps:
            color = colors[globals.reps - 1]
            for i in range(globals.reps):
                if color == colors[i]:
                    counter += 1
            if counter == int(globals.reps):
                bet_amount = globals.bet_amount
                bet_placed = False
                while not bet_placed:
                    print(f'Apostando {bet_amount} no {color}')
                    bet_success = place_bet(color, bet_amount)
                    if not bet_success:
                        break
                    
                    next_step = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.time-left'))
                    )
                    while 'In' in next_step.text:
                        time.sleep(3)

                    last_color, last_id = get_last_result()
                    if last_color == color:
                        print(f'Aposta ganha! Cor: {color}')
                        bet_placed = True
                        bet_amount = globals.bet_amount
                    else:
                        print(f'Aposta perdida. Cor: {color}, Último resultado: {last_color}')
                        bet_amount *= 2

except Exception as e:
    print(f"Erro ao processar a sequência da roleta: {e}")
    driver.quit()