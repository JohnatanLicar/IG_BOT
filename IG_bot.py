from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

def start(browser, username, password, nicho, qtd):
    """Inicia o BOT com as configurações corretas"""

    def login():
        try:
            username_field = browser.find_element(By.NAME, 'username')
            password_field = browser.find_element(By.NAME, 'password')
            username_field.send_keys(username)
            password_field.send_keys(password)
            login_button = browser.find_element(By.CSS_SELECTOR, '.L3NKy')
            login_button.click()
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._2dbep')))
        except:
            print('Usuário ou senha incorreta, verifique os dados e tente novamente')
            return False
        return True

    def click_saved():
        try:
            saved_button = browser.find_element(By.CSS_SELECTOR, 'div._ac7v:nth-child(1) > div:nth-child(1)')
            saved_button.click()
        except:
            print(f'({str(datetime.today())[:19]}) Não há nichos salvos, buscando mais, aguarde...')
            buscar_nicho(browser, username, nicho)
            print(f'({str(datetime.today())[:19]}) Iniciando o BOT novamente...')
            start(browser, username, password, nicho, qtd)

    def click_likers():
        try:
            likers_button = browser.find_element(By.CSS_SELECTOR, 'div._ab9o:nth-child(2) > div:nth-child(1) > a:nth-child(2) > div:nth-child(1)')
            likers_button.click()
        except:
            browser.refresh()
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div._ab9o:nth-child(2) > div:nth-child(1) > a:nth-child(2) > div:nth-child(1)')))
            likers_button = browser.find_element(By.CSS_SELECTOR, 'div._ab9o:nth-child(2) > div:nth-child(1) > a:nth-child(2) > div:nth-child(1)')
            likers_button.click()

    def follow_users(qtd):
        pg_dw = ActionChains(browser)
        conta_seguiu = 0
        seguiu = 0
        clicou = False
        passou_da_hora = datetime.today() + timedelta(minutes=5)
        status_do_while = True

        while status_do_while:
            try:
                pg_dw.key_down(Keys.DOWN).key_up(Keys.UP).perform()
                sleep(3)
                curtidas = browser.find_element(By.CSS_SELECTOR, '._ab9s > div:nth-child(1) > div:nth-child(1)')
                botoes = curtidas.find_elements(By.TAG_NAME, 'button')

                if not clicou:
                    curtidas.click()
                    clicou = True

                for seguidor in botoes:
                    try:
                        if seguidor.text in ['Seguir', 'Follow']:
                            seguidor.click()
                            conta_seguiu += 1
                            print(f'Seguiu +{conta_seguiu}')
                            sleep(2)
                    except:
                        break

                    if conta_seguiu == 30:
                        seguiu += conta_seguiu
                        if seguiu == qtd:
                            status_do_while = False
                            break
                        conta_seguiu = 0
                        sleep(1800)

                if datetime.today() >= passou_da_hora:
                    status_do_while = False
                    break
            except:
                status_do_while = False
                break

    def buscar_nicho(browser, username, nicho):
        try:
            search_input = browser.find_element(By.CSS_SELECTOR, 'input._9x5sw')
            search_input.clear()
            search_input.send_keys(nicho)
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.FuwoR:nth-child(1) > div:nth-child(1)')))
            sleep(1)

            # Clicar no primeiro resultado da busca
            result = browser.find_element(By.CSS_SELECTOR, 'div.FuwoR:nth-child(1) > div:nth-child(1)')
            result.click()
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.Nnq7C')))
            sleep(1)

            # Clicar no botão de seguidores
            followers_button = browser.find_element(By.CSS_SELECTOR, 'li.Y8-fY:nth-child(2) > a:nth-child(1)')
            followers_button.click()
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._ab9o')))
        except:
            print(f'({str(datetime.today())[:19]}) Não foi possível buscar o nicho, verifique os dados e tente novamente')

    browser.get('https://www.instagram.com/')
    sleep(2)

    logged_in = login()
    if logged_in:
        click_saved()
        click_likers()
        follow_users(qtd)

    browser.quit()

# Configurações do BOT
username = 'seu_usuario'
password = 'sua_senha'
nicho = 'seu_nicho'
quantidade_seguir = 100

# Inicializar o navegador Firefox
browser = Firefox()
start(browser, username, password, nicho, quantidade_seguir)
