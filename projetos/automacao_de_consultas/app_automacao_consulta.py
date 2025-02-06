
# 6 - salvar os dados para uma planilha

# 7 - repetir até finalizar todos os processos daquele advogado.


from selenium import webdriver # modulo sobre automações na web, usando o google chrome

from selenium.webdriver.common.by import By

from time import sleep

from selenium.webdriver.support.select import Select

# 1 - entrar no site: https://pje-consulta-publica.tjmg.jus.br/

driver = webdriver.Chrome()

driver.get('https://pje-consulta-publica.tjmg.jus.br/')

sleep(2)

# 2 - clicar no campo de oab e digitar o número do advogado

numero_oab = 25915

# estrutura para o MÉTODO (pois só é chamado a partir de uma classe) find_element() == driver.find_element(By.XPATH, "//tag[@atributo='valor_do_atributo'"])

campo_numero_oab = driver.find_element(By.XPATH, "//input[@id='fPP:Decoration:numeroOAB']") # procura um elemento HTML específico na pagina, obs.: se estiver utilizando By.XPATH

# Ctrl + F para !!! ABRIR A PROCURA POR XPATH NO CHROME DEVTOOLS !!!

sleep(2)

campo_numero_oab.click() # click(), autoexplicativo... clica no elemento.

sleep(1)

campo_numero_oab.send_keys(numero_oab) # send_keys('valor'), digita um valor em um campo HTML

# 3 - selecionar o estado daquele advogado

campo_estado = driver.find_element(By.XPATH, "//select[@id='fPP:Decoration:estadoComboOAB']") # seleciona o campo de selecionar o estado do advogado

sleep(2)

campo_estado.click()

sleep(1)

opcoes_estado = Select(campo_estado) # cria um objeto da classe select usando a variavel entre parenteses (q é um elemento HTML)

opcoes_estado.select_by_visible_text('SP') # select_by_visible_text() é um método acessado da clase Select, que permite selecionar um valor da tag select HTML, através do valor passado dentro dos parenteses

sleep(1)

# 4 - clicar em pesquisar

pesquisar = driver.find_element(By.XPATH, "//input[@id='fPP:searchProcessos']") # encontra o elemento botao submit (pesquisa) da pagina

sleep(1)

pesquisar.click()

sleep(5)

# 5 - entrar em cada um dos processos e extrair: número do advogado, número do processo e nome dos participantes

links_processos = driver.find_elements(By.XPATH, "//a[@title='Ver Detalhes']") # retorna uma lista com todos os a id='ver detalhes' da página

janela_principal = driver.current_window_handle # define uma janela, nesse caso a janela que está em execução, foi definida numa variavel chamada de janela principal

for link in links_processos: # laço para passar por todos os link de link_processos
    

    link.click()
    sleep(5)

    janelas_abertas = driver.window_handles # criar uma lista onde todos os valores são janelas diferentes
    
    for janela in janelas_abertas:
        if janela != janela_principal:
            driver.switch_to.window(janela)
            sleep(2)
            numero_processo = driver.find_elements(By.XPATH, "//div[@class='value col-sm-12 ']//div[@class='col-sm-12 ']")[0]
            print(f"numero do processo: {numero_processo.text}")

            participantes = driver.find_elements(By.XPATH, "//span[contains(@class, 'processoPartesPoloAtivoResumidoList:0:j_id271')]//span[@class='text-bold']")[0]
            lista_participantes = []

            for p in participantes: #adiciona todos os participantes ativos do processo em uma lista
                lista_participantes.append(p)

            input()
            print(f"nome do advogado: {nome_advogado.text}")

            """
            XPath Relativo: Utilize seletores que sejam menos dependentes de IDs dinâmicos. Por exemplo:
            elemento = driver.find_element_by_xpath("//div[contains(@id, 'processoPartesPoloPassivoResumidoList')]")

            """
            driver.switch_to.window(janela_principal)
input('digite enter para fechar ')