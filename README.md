# UFF-Projects

Esse repositório é destinado a projetos de pesquisa da UFF, tendo como objetivo o compartilhamento dos resultados, metodologias, códigos gerados e bases de dados. 


# Projeto de Projeção da Quantidade de Interrupções em Conjuntos Elétricos para Distribuidoras brasileiras

# Pontos Abordados:

- [1.Descrição do Projeto](https://github.com/felipemunarol/UFF-Projects/blob/main/README.md#descri%C3%A7ao-do-projeto)
- [2.Breve Introdução ao Projeto](https://github.com/felipemunarol/UFF-Projects/blob/main/README.md#breve-introdu%C3%A7%C3%A3o-ao-projeto)
- [3.Bases de Dados](https://github.com/felipemunarol/UFF-Projects/blob/main/README.md#bases-de-dados)

### **1.Descriçao do Projeto:**

**O projeto se destinou a criação de um modelo baseando-se em dados de livre acesso para a projeção da quantidade de interrupções em conjuntos de unidades consumidoras de todas as distribuidoras de energia do Brasil**. É criada, primeiramente, a etapa de ingestão de dados com um algoritmo
que realiza a coleta de diversas fontes de livre acesso por webscrapping e com a inclusão manual de determinadas bases de informações.

Após, é estruturado o processamento dos dados, com o método de previsão e suporte a tomada de decisão que foi desenvolvido. Sendo este caracterizado por um modelo de regressão linear múltipla, sendo comparados os seus resultados com um modelo sazonal ingênuo simples (este último modelo considera que todas as interrupções
em anos anteriores serão iguais nos anos seguintes, repetindo-se suas quantidades de eventos de interrupções, nos mesmos meses).

O resultado final é gerado para todas distribuidoras do Brasil e algumas destas concessionárias são selecionadas para realização de testes específicos.


### **2.Breve Introdução ao Projeto**

A continuidade no fornecimento de energia elétrica é uma preocupação constante de autoridades, Operadores de Redes de Distribuição (Distribution System Operators  -  DSOs) e consumidores. À medida que cresce a dependência da sociedade em relação à eletricidade, interrupções do sistema de energia elétrica têm impactos sociais, políticos e econômicos cada vez maiores.  Nesse contexto, a elevada frequência e duração de eventos com implicação na operação do sistema elétrico, causados por fenômenos climáticos extremos, torna-se um risco para a segurança e qualidade do fornecimento de energia. 

Além disto, a não adequação aos indicadores de qualidade do serviço previamente definidos pelos agentes reguladores pode causar penalizações às distribuidoras. A previsão da quantidade de interrupções, portanto, é um importante insumo tanto para as companhias de distribuição quanto para as entidades que tem atuação direta ou indireta no acompanhamento e fiscalização do serviço que é prestado no sistema elétrico. 

Esta previsão pode servir de apoio à tomada de decisão em diversos processos e estudos que tem o potencial de mitigar os impactos da queda do fornecimento de energia. São exemplos desses estudos, a avaliação da manutenção dos indicadores de qualidade do fornecimento de energia (definidos pela regulamentação vigente), a alocação da força de trabalho para ação em casos de interrupções na rede elétrica, análise da confiabilidade de redes de distribuição e a estruturação de processos de reestabelecimento do fornecimento elétrico.   



### 3.Bases de Dados

### 1. Dados Meteorológicos, socioeconômicos e de caracacterísticas geográficas regionais por unidade consumidora (ANEEL), em agregação mensal.

Estes [dados](https://github.com/felipemunarol/UFF-Projects/tree/main/data) são coletados de diversas fontes de dados públicas e são destinados ao exercicício de modelagem ou análise de dados. A base contém os dados de informações meteológicas, da geografica regional e índices econômicos por Conjunto Elétrico Brasileiro (regulamentados pela ANEEL) e mês.

As fontes públicas em que são coletados, são:

- IBGE (Instituto Brasileiro de Geografia e Estatística) - Dados geográficas (características das regiões), Dados de Classificação de Vegetação e dados de litoraniedade;
- ANEEL (Agência Nacional de Energia Elétrica) - Dados de Interrupções;
- SIGEL/ANEEL (Sistema de Informações Georreferenciadas do Setor Elétrico) -  Informações da área geográfica de Conjuntos Elétricos;
- INMET (Instituto Nacional de Meteorologia) -  Dados Meteorológicos;
- INPE (Instituto Nacional de Pesquisas Espaciais) - Dados de Porcentagem de cobertura arbórea (em desenvolvimento).

Na pasta de dados existem os arquivos por Conjunto Elétrico Brasileiro (regulamentados pela ANEEL) e mês. Cada arquivo está separado por um ano, com a descrição base_{ano_de_referência}.xlsx.

Os dados apresentam estrutura temporal de agregação mensal e por conjuntos elétricos (na estrutura SIGEL). Para serem requeridos dados em outras estruturas por favor, entrar em contato no email dos resposáveis.


## Códigos Criados

Na pasta [src](https://github.com/felipemunarol/UFF-Projects/tree/main/src) encontram-se os códigos que foram utilizados para a criação da metologia. Sendo estes dividos entre **i) coleta de dados ii) processamento dos dados iii) modelagem, previsão e simulação.**

Obs. Alguns notebooks referentes ao webscrapping não estão na pasta. Por favor, entrar em contato com o reponsável, para solicitar sua utilização.
   
## Author Information

|      -      |        -       |
| ------------- | ------------- |
| Author        | Felipe Munaro |
| Content Cell  | felipemunarolima@gmail.com |
| Version  | As of 07/02/2024 |

## Dedicatória

Este trabalho é um esforço conjunto entre o Instituto INERGE, a Universidade Federal Fluminense (UFF) e o laboratório FRIENDS para o atendimento a necessidades de problemas atuais de empresas privadas de distribuição de Energia.

## Citação

Lima F. M. (2023). Modelo Baseado em Dados para Previsão do Número Mensal de Interrupções em Conjuntos Elétricos Utilizando Dados Públicos - Conjunto de Dados: v0 (Versão V0). Zenodo. https://doi.org/10.5281/zenodo.10033882

## Suporte

Qualquer suporte deve ser solicitado ao autor do conjunto de dados. Para utilizações empresariais é necessário ser solicitado.
