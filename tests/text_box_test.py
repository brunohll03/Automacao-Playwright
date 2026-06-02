# Importa a função scenarios do pytest-bdd.
# Essa função é responsável por ler um arquivo .feature
# e transformar cada Scenario em um teste Pytest executável.
from pytest_bdd import scenarios


# Importa todos os steps definidos no arquivo text_box_steps.py.
#
# Os steps são as implementações dos Given, When e Then
# que existem dentro do arquivo text_box.feature.
#
# Exemplo:
# Given que acesso a página Text Box
# ↓
# @given("que acesso a página Text Box")
#
# Sem esse import, o pytest-bdd não conseguiria encontrar
# as funções que executam os passos do cenário.
from steps.text_box_steps import *


# Informa ao pytest-bdd qual arquivo .feature deve ser executado.
#
# O caminho é relativo ao local deste arquivo:
#
# ../features/text_box.feature
#
# O pytest-bdd irá:
# 1. Abrir o arquivo text_box.feature
# 2. Ler todos os cenários (Scenario)
# 3. Procurar os Given, When e Then correspondentes
#    dentro dos arquivos importados em steps
# 4. Criar automaticamente testes Pytest para cada cenário
#
# Exemplo:
#
# Scenario: Preencher formulário
#   Given que acesso a página Text Box
#   When preencho os dados
#   Then devo visualizar a confirmação
#
# Internamente será criado algo parecido com:
#
# def test_preencher_formulario():
#     executar_given()
#     executar_when()
#     executar_then()
#
# Tudo isso acontece automaticamente.
scenarios("../features/text_box.feature")
