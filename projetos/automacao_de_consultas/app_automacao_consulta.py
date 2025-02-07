from selenium import webdriver # modulo sobre automações na web, usando o google chrome

from selenium.webdriver.common.by import By

from time import sleep # função para poder pausar o código, (criar um timer)

from selenium.webdriver.support.select import Select

import openpyxl # módulo que permite a interação do python com tabelas do excel

# 1 - entrar no site: https://pje-consulta-publica.tjmg.jus.br/

driver = webdriver.Chrome()

driver.get('https://pje-consulta-publica.tjmg.jus.br/')

caminho_planilha = 'G:\\vs code codigos\\curso python\\projetos\\automacao_de_consultas\\dados_consulta.xlsx' # variavel para facilitar o acesso ao caminho da planilha.xlsx

planilha_dados_consulta = openpyxl.load_workbook(caminho_planilha) # load.workbook() é a função que atribui a uma variável as propriedades de uma planilha .xlsx

sleep(2)

# 2 - Clicar no campo de oab e digitar o número do advogado

numero_oab = 259155

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

links_processos = driver.find_elements(By.XPATH, "//a[@title='Ver Detalhes']") # retorna uma lista com todos os id='ver detalhes' da página

janela_principal = driver.current_window_handle # define uma janela, nesse caso a janela que está em execução, foi definida numa variavel chamada de janela principal

for link in links_processos: # laço para passar por todos os link de link_processos
    

    link.click()
    sleep(5)

    janelas_abertas = driver.window_handles # criar uma lista onde todos os valores são janelas diferentes

    
    
    for janela in janelas_abertas: # execução de tarefas em várias janelas abertas
        if janela != janela_principal:
            driver.switch_to.window(janela)
            sleep(2)
            numero_processo = driver.find_elements(By.XPATH, "//div[@class='value col-sm-12 ']//div[@class='col-sm-12 ']")[0]
            
            participantes = driver.find_elements(By.XPATH, "//tbody[contains(@id, 'processoPartesPoloAtivoResumidoList:tb')]//span[@class='text-bold']")

            lista_participantes = []

            for p in participantes: #adiciona todos os participantes ativos do processo em uma lista
                lista_participantes.append(p.text) # p.text é usado para que apenas o texto do elemento encontrado pelo xpath seja utilizado

            planilha_pagina_processos = planilha_dados_consulta['Planilha1']

            if len(lista_participantes) == 1:
                planilha_pagina_processos.append([numero_oab, numero_processo.text, lista_participantes[0]]) # adiciona valores às células da planilha de maneira sempre da esquerda para a direita
            else:
                planilha_pagina_processos.append([numero_oab, numero_processo.text, ', '.join(lista_participantes)])

            # 6 - salvar os dados para uma planilha

            planilha_dados_consulta.save('G:\\vs code codigos\\curso python\\projetos\\automacao_de_consultas\\dados_consulta - Copy.xlsx') # save() método utilizado para salvar o arquivo de planilha através do caminho do arquivo 

            """
            XPath Relativo: Utilize seletores que sejam menos dependentes de IDs dinâmicos. Por exemplo:
            elemento = driver.find_element_by_xpath("//div[contains(@id, 'processoPartesPoloPassivoResumidoList')]")

            """

            driver.switch_to.window(janela_principal) # Volta para a janela principal

            # Automação finalizada

