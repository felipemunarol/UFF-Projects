# -*- coding: utf-8 -*-
"""cpfl.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cGUSJKEkfZ4T9-7rvcFMM8xju6MCoul2

Filtra os conjunto somente da Distribuidora CPFL que tem área de concessão em parte do Rio de Janeiro (considerando 2023) para o teste da inferencia do modelo
"""

import csv
import pandas as pd
import os
import json

pd.set_option('display.max_columns', None)

# Conecta o serviço com o Drive
from google.colab import drive
drive.mount('/content/drive')

# Raiz
! ls '/content/drive/MyDrive/Mestrado/Ordens_servico/'

"""# Preprocess"""

year = 2022

interrupcoes_general = pd.read_csv("/content/drive/MyDrive/Mestrado/Ordens_servico/Ordens_servico/test_interrupcoes_collect_ckan_{}.csv".format(year))

interrupcoes_general

interrupcoes = interrupcoes_general[interrupcoes_general.NomAgenteRegulado.str.contains('COMPANHIA PAULISTA DE FORÇA E LUZ')]

"""Due to the high error on the prediction to this company. It's checked the distribuition statistics."""

interrupcoes_general_grouped_by_sets = interrupcoes_general.groupby("DscConjuntoUnidadeConsumidora")["_id"].count().reset_index()
print(interrupcoes_general_grouped_by_sets.describe())
interrupcoes_general_grouped_by_sets.plot.hist(bins=100)

interrupcoes_grouped_by_sets = interrupcoes.groupby("DscConjuntoUnidadeConsumidora")["_id"].count().reset_index()
print(interrupcoes_grouped_by_sets.describe())
interrupcoes_grouped_by_sets.plot.hist(bins=100)

"""Save the dict with the information of the unit sets of the company"""

interrupcoes_array = interrupcoes.DscConjuntoUnidadeConsumidora.values

interrupcoes_array

interrupcoes_dict = {}
interrupcoes_dict["conjuntos"] = list(interrupcoes_array)
interrupcoes_dict

with open("/content/drive/MyDrive/Mestrado/Ordens_servico/Ordens_servico/CONJUNTOS_CPFL.json", 'w') as f:
  json.dump(interrupcoes_dict, f)

