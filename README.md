# 🤖 Bot WhatsApp

Automação de envio de mensagens no WhatsApp utilizando Python e Selenium.

---

## 🚀 Funcionalidades

* 📩 Envio automático de mensagens
* 🖼️ Envio de imagens
* ⏰ Agendamento de horário
* 📂 Leitura de dados via arquivo `.env.config`
* 📂 codigo extra (opcional) para organizar fotos `rename_photos.py`

---

## 🛠️ Tecnologias

* Python
* Selenium

---

## ⚙️ Como usar

```bash
git clone https://github.com/seuusuario/bot-whatsapp
cd bot-whatsapp
```

---

## 📌 Configuração

Crie um arquivo `.env.config` baseado no `.env.example`:

```python
nomedogrupo="seu_grupo"
horario="00:00"
img="photos/sua_imagem.png"
```

### ⚠️ Regras importantes

* Informe apenas o nome da imagem (o código já resolve o caminho automaticamente)
* O nome do grupo deve ser **EXATO** (maiúsculas, minúsculas, acentos e espaços)
* Utilize apenas **1 horário**, a menos que modifique o código

---

## 🔐 Primeiro uso

* Na primeira execução, será necessário fazer login no WhatsApp Web
* O navegador abrirá automaticamente
* Caso seja deslogado, será necessário logar novamente

---

## ⚠️ Observações

* ❌ **Não compartilhe** seu `.env.config`

* ❌ **Não compartilhe** a pasta `chrome-data`

  * Ela contém dados sensíveis do navegador

* O projeto utiliza automação com navegador através do Selenium

---

## 📄 Licença

Uso livre para estudos e aprendizado.
