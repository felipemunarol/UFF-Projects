# UFF-Projects

Esse repositório é destinado a projetos de pesquisa da UFF, tendo como objetivo o compartilhamento dos resultados, metodologias, códigos gerados e bases de dados. 


# Projeto de Projeção da Quantidade de Interrupções em Conjuntos Elétricos para Distribuidoras brasileiras

**Descriçao:**

**O projeto se destinou a criação de um modelo baseando-se em dados de livre acesso para a projeção da quantidade de interrupções em conjuntos de unidades consumidoras de distribuidoras do Brasil**. É criada, primeiramente, a etapa de ingestão de dados com um algoritmo
que realiza a coleta de diversas fontes de livre acesso por webscrapping e a inclusão manual de determinadas bases de informações.

Após, é estruturado o processamento dos dados, com o método de previsão e suporte a tomada de decisão desenvolvido. Sendo este caracterizado por um modelo de regressão linear múltipla, sendo comparados os seus resultados com um modelo sazonal ingênuo simples (este modelo considera que todas as interrupções
em anos anteriores serão iguais para o próximo ano, repetindo suas quantidades nos mesmos meses)

O resultado final é gerado para todas distribuidoras do Brasil e algumas destas empresas são selecionadas para realização de testes específicos.


**Breve Introdução ao Projeto**

A continuidade no fornecimento de energia elétrica é uma preocupação constante de autoridades, Operadores de Redes de Distribuição (Distribution System Operators  ̶  DSOs) e consumidores. À medida que cresce a dependência da sociedade em relação à eletricidade, interrupções do sistema de energia elétrica têm impactos sociais, políticos e econômicos cada vez maiores.  Nesse contexto, a elevada frequência e duração de eventos com implicação na operação do sistema elétrico, causados por fenômenos climáticos extremos, torna-se um risco para a segurança e qualidade do fornecimento de energia. 

Além disto, a não adequação aos indicadores de qualidade do serviço previamente definidos pelos agentes reguladores pode causar penalizações às distribuidoras. A previsão da quantidade de interrupções, portanto, é um importante insumo tanto para as companhias de distribuição quanto para as entidades que tem atuação direta ou indireta no acompanhamento e fiscalização do serviço que é prestado no sistema elétrico. 

Esta previsão pode servir de apoio à tomada de decisão em diversos processos e estudos que tem o potencial de mitigar os impactos da queda do fornecimento de energia. São exemplos desses estudos, a avaliação da manutenção dos indicadores de qualidade do fornecimento de energia (definidos pela regulamentação vigente), a alocação da força de trabalho para ação em casos de interrupções na rede elétrica, análise da confiabilidade de redes de distribuição e a estruturação de processos de reestabelecimento do fornecimento elétrico.   



## Bases de Dados

### 1. Dados Meteorológicos, socioeconômicos e de caracacterísticas geográficas regionais por unidade consumidora (ANEEL), em agregação mensal.

Estes [dados](https://github.com/felipemunarol/UFF-Projects/tree/main/data) são coletados de diversas fontes de dados públicas e são destinados ao exercicício de modelagem ou análise de dados. A base contém os dados de informações meteológicas, da geografica regional e índices econômicos por Conjunto Elétrico Brasileiro (ANEEL) e mês.
As fontes públicas em que são coletados, são:

- IBGE (Instituto Brasileiro de Geografia e Estatística) - Dados geográficas (características das regiões), Dados de Classificação de Vegetação e dados de litoraniedade;
- ANEEL (Agência Nacional de Energia Elétrica) - Dados de Interrupções;
- SIGEL/ANEEL (Sistema de Informações Georreferenciadas do Setor Elétrico) -  Informações da área geográfica de Conjuntos Elétricos;
- INMET (Instituto Nacional de Meteorologia) -  Dados Meteorológicos;
- INPE (Instituto Nacional de Pesquisas Espaciais) - Dados de Porcentagem de cobertura arbórea (em desenvolvimento).

Os dados apresentam estrutura temporal de agregação mensal e por conjuntos elétricos (estrutura SIGEL). Para serem requeridos dados em outras estruturas por favor, entrar em contato no email dos resposáveis.


## Códigos

Na pasta [src](https://github.com/felipemunarol/UFF-Projects/tree/main/src) encontram-se os códigos que foram utilizados para a criação da metologia. Sendo estes dividos entre i) coleta de dados ii) processamento dos dados iii) modelagem, previsão e simulação.
   
## Author Information

|               |               |
| ------------- | ------------- |
| Author        | Felipe Munaro |
| Content Cell  | felipemunarolima@gmail.com |
| Version  | As of 07/02/2024 |

