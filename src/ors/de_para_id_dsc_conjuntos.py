# -*- coding: utf-8 -*-
"""de_para_id_dsc_conjuntos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rx1oawz4rDWV1oPthLIlgiD8h55kplCb

Descrição: Realiza o de-para de identificador do conjunto e a sua descricao unidade a partir dos dados de FEC e DEC
"""

import pandas as pd
import sys
import ast

import requests
import csv
import codecs

# Conecta o serviço com o Drive
from google.colab import drive
drive.mount('/content/drive')

# year = 2022

import urllib
url = 'https://dadosabertos.aneel.gov.br/api/3/action/datastore_search?resource_id=42d778de-4a10-4b54-a00a-87c8ff35db6f&limit=5'
fileobj = urllib.request.urlopen(url)
print (fileobj.read())

dir(fileobj)

# Pegar dados dos indicadores de qualidade DEC E FEC - tem a realção unidades consumidoras nomes e indicadores
# https://dadosabertos.aneel.gov.br/dataset/indicadores-coletivos-de-continuidade-dec-e-fec/resource/5d91171a-eb4e-4f66-8418-2833567123ae

! pip install selenium # && pip install BeautifulSoup

# Commented out IPython magic to ensure Python compatibility.
# %%shell
# # Codigo para utilizar o Selenium no Colab
# # Ubuntu no longer distributes chromium-browser outside of snap
# #
# # Proposed solution: https://askubuntu.com/questions/1204571/how-to-install-chromium-without-snap
# 
# # Add debian buster
# cat > /etc/apt/sources.list.d/debian.list <<'EOF'
# deb [arch=amd64 signed-by=/usr/share/keyrings/debian-buster.gpg] http://deb.debian.org/debian buster main
# deb [arch=amd64 signed-by=/usr/share/keyrings/debian-buster-updates.gpg] http://deb.debian.org/debian buster-updates main
# deb [arch=amd64 signed-by=/usr/share/keyrings/debian-security-buster.gpg] http://deb.debian.org/debian-security buster/updates main
# EOF
# 
# # Add keys
# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DCC9EFBF77E11517
# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 648ACFD622F3D138
# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 112695A0E562B32A
# 
# apt-key export 77E11517 | gpg --dearmour -o /usr/share/keyrings/debian-buster.gpg
# apt-key export 22F3D138 | gpg --dearmour -o /usr/share/keyrings/debian-buster-updates.gpg
# apt-key export E562B32A | gpg --dearmour -o /usr/share/keyrings/debian-security-buster.gpg
# 
# # Prefer debian repo for chromium* packages only
# # Note the double-blank lines between entries
# cat > /etc/apt/preferences.d/chromium.pref << 'EOF'
# Package: *
# Pin: release a=eoan
# Pin-Priority: 500
# 
# Package: *
# Pin: origin "deb.debian.org"
# Pin-Priority: 300
# 
# 
# Package: chromium*
# Pin: origin "deb.debian.org"
# Pin-Priority: 700
# EOF
# 
# # Install chromium and chromium-driver
# apt-get update
# apt-get install chromium chromium-driver
# 
# # Install selenium
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
# from BeautifulSoup import BeautifulSoup
import pandas as pd
import sys
import ast

import requests
import csv
import codecs

# Conecta o serviço com o Drive
from google.colab import drive
drive.mount('/content/drive')

year = 2021

# Inicializa o driver do Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.headless = True
wd = webdriver.Chrome('chromedriver',options=chrome_options)

# Faz a coleta dos dados do site da Aneel

wd.get("https://dadosabertos.aneel.gov.br/dataset/indicadores-coletivos-de-continuidade-dec-e-fec")

element = wd.find_element(By.XPATH, "//a[@href='https://dadosabertos.aneel.gov.br/dataset/d5f0712e-62f6-4736-8dff-9991f10758a7/resource/4493985c-baea-429c-9df5-3030422c71d7/download/indicadores-continuidade-coletivos-2020-2029.csv']")   # Inclui o ano para a coleta

url = element.get_attribute("href")

dados = []
with requests.get(url, stream=True, timeout=2) as r:
  lines = (line.decode('latin-1') for line in r.iter_lines())
  spamreader = csv.reader(lines, delimiter=';')
  for n, row in enumerate(spamreader):
    print(row)
    dados.append(row)

fec_dec = pd.DataFrame(dados[1:], columns=dados[0])

fec_dec

fec_dec.to_csv("/content/drive/MyDrive/Colab Notebooks/Religamentos/fec_dec.csv")

fec_dec = pd.read_csv("/content/drive/MyDrive/Mestrado/Ordens_servico/Ordens_servico/fec_dec.csv")

de_para_und_cons = fec_dec[["IdeConjUndConsumidoras","DscConjUndConsumidoras"]].drop_duplicates()

de_para_und_cons

de_para_und_cons.to_csv("/content/drive/MyDrive/Mestrado/Ordens_servico/Ordens_servico/de_para_und_cons.csv")