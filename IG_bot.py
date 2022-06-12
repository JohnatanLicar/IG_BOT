from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime, timedelta


navega = Firefox()

def start(browser: object, username: str,password: str, nicho: list, qtd: int):
    """Iniciar o BOT com as configurações corretas

    browser: navegador iniciado no selenium
    username: nome de usuario da conta
    password: senha para acessar a sua conta
    nicho: lista de nichos para seguir
    qtd: quantidade de seguidores que quer seguir/deixar de seguir ATENCAO: (maximo: 500, minimo: 50)
    primeira_vez: se o login da conta já foi feito antes
    
    """
    browser.delete_all_cookies()
    sleep(2)
    
    try:
        navega.get('https://www.instagram.com/')
        sleep(5)
        browser.find_element(by=By.NAME, value='username').send_keys(username) # campo usuario
        sleep(2)
        browser.find_element(by=By.NAME, value='password').send_keys(password) # campo senha
        sleep(6)
        browser.find_element(by=By.CSS_SELECTOR, value='.L3NKy').click() # botao de entrar
        sleep(10)
        browser.find_element(by=By.CSS_SELECTOR, value='._2dbep') # verifica se existe a imagem de perfil do usuario

    except:
        print('Usuario ou Senha incorreta, verifique os dados e tente novamente')
        return

    browser.get(f'https://www.instagram.com/{username}/saved/')
    sleep(10)
    try:

        browser.find_element(by=By.CSS_SELECTOR, value='div._ac7v:nth-child(1) > div:nth-child(1)').click()
    
    except:
        print(f'({str(datetime.today())[:19]}) não tem nichos salvos, vou buscar mais, aguarde...')
        buscar_nicho(browser,username,nicho)
        print(f'({str(datetime.today())[:19]}) Iniciando o Bot novamente...')
        start(browser,username,password,nicho,qtd)

    sleep(10)
    try:
        browser.find_element(by=By.CSS_SELECTOR, value='div._ab9o:nth-child(2) > div:nth-child(1) > a:nth-child(2) > div:nth-child(1)').click() # tente clicar em pessoas que curtiram
        # se nao der certo atualizar a pagina e tentar novamente
    
    except:
        browser.refresh()
        sleep(10)
        browser.find_element(by=By.CSS_SELECTOR, value='div._ab9o:nth-child(2) > div:nth-child(1) > a:nth-child(2) > div:nth-child(1)').click() # tentar clicar em pessoas que cirtiram
        sleep(10)
    sleep(5)
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
            curtidas = browser.find_element(by=By.CSS_SELECTOR, value='._ab9s > div:nth-child(1) > div:nth-child(1)')
            #salvar pessoas que curtiram a imagens ou video
            botoes = curtidas.find_elements(by=By.TAG_NAME, value='button')
            #salvar os botoes com nome de seguir ou seguindo
            
            if not clicou:
                curtidas.click()
                clicou = True

            for seguidor in botoes:
                try:
                    if (seguidor.text == 'Seguir') or (seguidor.text == 'Follow'):
                        seguidor.click()
                        conta_seguiu += 1
                        print(f'Seguiu +{conta_seguiu}')
                        sleep(2)
                except:
                    break

                if conta_seguiu == 30: # padrao é deixar == 30:
                    seguiu += conta_seguiu
                    if seguiu >= qtd: # padrao 200
                        status_do_while = False
                        break

                    print(f'({str(datetime.today())[:19]}) >> Entrei no break, ja seguir  {seguiu}, vou aguardar 1 hora!')
                    conta_seguiu = 0
                    sleep(3600) # padrao de 1 hora são sleep(3600)
                    passou_da_hora = datetime.today() + timedelta(minutes=5) # padrao é deixar timedelta(hours=1)
                
                elif datetime.today().time() > passou_da_hora.time():
                    status_do_while = False
                    break
                    
        except:
            browser.refresh()
            sleep(10)
            browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[2]/div/div[2]/a').click()
            sleep(10)
            
            

    if seguiu >= qtd:
        print(f'({str(datetime.today())[:19]}) Já atingiu o limite de seguidores [{seguiu}]')
        sleep(3600)
        deixar_seguir(browser,username,qtd)
        sleep(3600)
        print(f'({str(datetime.today())[:19]}) Iniciando o Bot novamente...')
        start(browser,username,password,nicho,qtd)
    else:
        print(f'({str(datetime.today())[:19]}) Não achei mais seguidores nessa pagina, vou procurar em outro nicho salvo!')
        apaga_salvo(browser,username)
        sleep(3600)
        print(f'({str(datetime.today())[:19]}) Iniciando o Bot novamente...')
        start(browser,username,password,nicho,qtd)

def deixar_seguir(browser: object, username: str, qtd: int):
    browser.get(f'https://www.instagram.com/{username}/following/') #Pagina de pessoas que eu sigo
    sleep(10)
    conta = 0
    conta_total = 0
    clicou = False
    acao = ActionChains(browser)
    while True:
        try:
            seguindo = browser.find_element(by=By.CSS_SELECTOR, value='._aae-')# recebe os elementos onde estão os botões
            buttons = seguindo.find_elements(by=By.TAG_NAME, value='button') # recebe os botões
            if not clicou:
                seguindo.click()
                clicou = True
            for button in buttons:
                if (button.text == 'Seguindo') or (button.text == 'Following'):
                    button.click()
                    sleep(3)
                    box_seguidor = browser.find_element(by=By.CSS_SELECTOR, value='._a9-v')
                    box_seguidor.find_element(by=By.CSS_SELECTOR, value='button._a9--:nth-child(1)').click()
                    #box_seguidor.find_element_by_css_selector('.aOOlW.-Cab_.focus-visible').click() # Confirma deixar de seguir
                    conta += 1
                    print(f'Deixou de seguir {conta}')
                    sleep(1.5)
                if conta == 30:
                    conta_total += conta
                    if conta_total >= qtd:
                        print(f'({str(datetime.today())[:19]}) Já atingiu o limite de deixar de seguir [{conta_total}]')
                        return
                    print(f'({str(datetime.today())[:19]}) >> Entrei no break, Deixei de seguir {conta_total}, vou aguardar 1 hora!')
                    conta = 0
                    sleep(3600)
        except:
            if not clicou:
                seguindo.click()
                clicou = True
            acao.key_down(Keys.DOWN).key_up(Keys.UP).perform()
            sleep(3)


def apaga_salvo(browser: object, username: str):
    browser.get(f'https://www.instagram.com/{username}/saved/')
    sleep(10)
    browser.find_element(by=By.CSS_SELECTOR, value="div._ac7v:nth-child(1) > div").click()
    sleep(5)
    try:
        browser.find_element_by_css_selector('._aamz > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)').click()
                
    except:
        browser.refresh()
        sleep(10)
        browser.find_element_by_css_selector('._aamz > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)').click()
    sleep(5)

def buscar_nicho(browser: object, username: str, nicho: list):
    acao = ActionChains(browser)
    for buscar in nicho:
        browser.get(f"https://instagram.com/explore/tags/{buscar.replace(' ','')}")
        sleep(10)
        try:
            for l in range(1,4):
                for c in range(1,4):
                    browser.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[{l}]/div[{c}]').click()
                    #selecionar a imagem por imagens
                    sleep(5)
                    try:
                        browser.find_element(by=By.CSS_SELECTOR, value='a.qu0x051f:nth-child(2)')
                        #Se existir o link de muitas curtidas
                        browser.find_element(by=By.CSS_SELECTOR, value='._aamz > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)').click()
                        #salvar a imagens
                        sleep(2)
                        acao.key_down(Keys.ESCAPE).key_up(Keys.ESCAPE).perform()
                        sleep(2)

                    except:
                        acao.key_down(Keys.ESCAPE).key_up(Keys.ESCAPE).perform()
                        #browser.get(f"https://instagram.com/explore/tags/{buscar.replace(' ','')}")
        except:
            print(f"({str(datetime.today())[:19]}) Não existi nicho para: '{buscar}' ou pagina não encontrada")
        print(f"({str(datetime.today())[:19]}) Não existi mais nicho para: '{buscar}'")






if __name__ == '__main__':
    username = input('Digite seu nome de usuaruio: ')
    password = input('Digite sua senha: ')
    nicho = []
    n =  input('Deseja adcionar quantos nichos de pesquisa? [DIGITE SOMENTE NUMEROS]')
    for n in q:
        nicho.append(input(f'Digite o nicho numero {q} :'))
    start(navega,username,password,nicho,150)
    
    