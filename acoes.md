# Playwright Python - Principais Ações Simulando um Usuário

## Navegação

```python
page.goto("https://demoqa.com")
# Abre uma página

page.reload()
# Atualiza a página (F5)

page.go_back()
# Volta para a página anterior

page.go_forward()
# Avança para a próxima página
```

---

## Cliques

```python
page.get_by_role("button").click()
# Clica em um botão

page.locator("#login").click()
# Clica em um elemento pelo seletor

page.get_by_text("Enviar").click()
# Clica em um texto visível

page.dblclick("#botao")
# Dá duplo clique

page.locator("#botao").click(button="right")
# Clique com botão direito
```

---

## Digitação

```python
page.get_by_label("Nome").fill("Bruno")
# Preenche um campo

page.fill("#email", "teste@email.com")
# Digita um valor

page.press("#senha", "Enter")
# Pressiona Enter no campo

page.keyboard.type("Olá Mundo")
# Digita usando o teclado
```

---

## Teclas de Teclado

```python
page.keyboard.press("Enter")
# Pressiona Enter

page.keyboard.press("Tab")
# Navega para o próximo campo

page.keyboard.press("Escape")
# Fecha modais ou cancela ações

page.keyboard.press("Control+A")
# Seleciona todo o conteúdo

page.keyboard.press("Control+C")
# Copia conteúdo

page.keyboard.press("Control+V")
# Cola conteúdo
```

---

## Checkbox e Radio Button

```python
page.get_by_role("checkbox").check()
# Marca um checkbox

page.get_by_role("checkbox").uncheck()
# Desmarca um checkbox

page.get_by_role("radio").check()
# Seleciona um radio button
```

---

## Dropdown (Select)

```python
page.select_option("#country", "Brazil")
# Seleciona pelo value

page.select_option("#country", label="Brazil")
# Seleciona pelo texto visível

page.select_option("#country", index=2)
# Seleciona pela posição
```

---

## Upload de Arquivos

```python
page.set_input_files("#upload", "arquivo.pdf")
# Faz upload de um arquivo

page.set_input_files("#upload", [])
# Remove o arquivo enviado
```

---

## Download de Arquivos

```python
with page.expect_download() as download_info:
    page.get_by_text("Download").click()

download = download_info.value
# Aguarda e captura o download
```

---

## Mouse

```python
page.mouse.move(100, 200)
# Move o mouse

page.mouse.down()
# Pressiona o botão do mouse

page.mouse.up()
# Solta o botão do mouse

page.mouse.wheel(0, 500)
# Faz scroll
```

---

## Drag and Drop

```python
page.drag_and_drop("#origem", "#destino")
# Arrasta um elemento para outro local
```

---

## Hover

```python
page.locator("#menu").hover()
# Passa o mouse sobre um elemento
```

---

## Scroll

```python
page.locator("#fim").scroll_into_view_if_needed()
# Rola a página até o elemento

page.mouse.wheel(0, 1000)
# Faz scroll para baixo
```

---

## Esperas

```python
page.wait_for_timeout(3000)
# Aguarda 3 segundos (não recomendado)

page.wait_for_selector("#login")
# Aguarda um elemento aparecer

page.wait_for_load_state("networkidle")
# Aguarda o carregamento da página terminar
```

---

## Captura de Evidências

```python
page.screenshot(path="evidencia.png")
# Screenshot da página inteira

page.locator("#form").screenshot(path="formulario.png")
# Screenshot de um elemento específico
```

---

## Leitura de Informações

```python
texto = page.locator("#mensagem").text_content()
# Obtém o texto do elemento

texto = page.inner_text("#mensagem")
# Obtém apenas o texto visível

valor = page.input_value("#email")
# Obtém o valor de um campo
```

---

## Validações com Expect

```python
expect(page).to_have_title("DemoQA")
# Valida o título da página

expect(page).to_have_url("https://demoqa.com")
# Valida a URL atual

expect(page.locator("#sucesso")).to_be_visible()
# Valida que o elemento está visível

expect(page.locator("#erro")).to_be_hidden()
# Valida que o elemento está oculto

expect(page.locator("#nome")).to_have_text("Bruno")
# Valida o texto de um elemento

expect(page.locator("#email")).to_have_value("teste@email.com")
# Valida o valor de um campo

expect(page.locator("#botao")).to_be_enabled()
# Valida que o botão está habilitado

expect(page.locator("#botao")).to_be_disabled()
# Valida que o botão está desabilitado
```

---

## Janelas e Abas

```python
with page.expect_popup() as popup_info:
    page.get_by_text("Nova Aba").click()

nova_aba = popup_info.value
# Captura uma nova aba aberta
```

---

## Alertas (Dialogs)

```python
page.on("dialog", lambda dialog: dialog.accept())
# Aceita um alerta

page.on("dialog", lambda dialog: dialog.dismiss())
# Cancela um alerta
```

---

## Iframes

```python
frame = page.frame_locator("#frame1")
# Acessa um iframe

frame.get_by_role("button").click()
# Interage com elementos dentro do iframe
```

---

## Localização de Elementos (Locators)

```python
page.get_by_role("button", name="Enviar")
# Localiza por role

page.get_by_text("Salvar")
# Localiza pelo texto

page.get_by_label("Nome")
# Localiza por label

page.get_by_placeholder("Digite seu nome")
# Localiza por placeholder

page.get_by_test_id("btn-salvar")
# Localiza por test id

page.locator("#login")
# Localiza por CSS Selector

page.locator("//button[@id='login']")
# Localiza por XPath
```

---

## Principais Ações Utilizadas por um QA no Dia a Dia

```python
page.goto()
# Navegar

page.get_by_role().click()
# Clicar

page.fill()
# Digitar

page.select_option()
# Selecionar opção

page.check()
# Marcar checkbox

page.hover()
# Passar o mouse

page.drag_and_drop()
# Arrastar elemento

page.screenshot()
# Gerar evidência

expect().to_have_text()
# Validar texto

expect().to_be_visible()
# Validar visibilidade

page.wait_for_selector()
# Esperar elemento

page.set_input_files()
# Upload de arquivo

page.expect_download()
# Download de arquivo

page.frame_locator()
# Trabalhar com iframe
```
