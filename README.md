# 🗂️ cadastro-clientes-python 
<br/>
Um sistema simples de cadastro de clientes em Python, utilizando linha de comando (terminal) e persistência de dados com JSON. Permite cadastrar, listar, atualizar e deletar clientes, mantendo os dados salvos entre execuções.

---

📦 Tecnologias usadas <br/>
- Python 3.x
- Manipulação de arquivos .json
- Expressões regulares com re
- Módulo os para checar existência de arquivos
- Programação estruturada

---

⚙️ Funcionalidades <br/>
- ✅ Adicionar novos clientes com nome, idade e e-mail válido
- 📋 Listar todos os clientes cadastrados
- ✏️ Atualizar os dados de um cliente pelo ID
- ❌ Deletar um cliente pelo ID
- 💾 Dados salvos automaticamente no arquivo clientes.json
- 🧠 Retoma do ponto em que parou ao reiniciar o script

---

▶️ Como usar <br/>
1. Clone o repositório: <br/>
```bash
git clone git@github.com:LeonardDevv/cadastro-clientes-python.git
cd cadastro-clientes-python
```
2. Execute o programa: <br/>
```bash
python cadastro.py
```
3. Escolha uma das opções no menu: <br/>
```bash
[ 1 ] - Adicionar cliente
[ 2 ] - Listar clientes
[ 3 ] - Atualizar dados do cliente
[ 4 ] - Deletar cliente
[ 5 ] - Sair e salvar dados
```

---

```bash
Informe o nome do novo cliente: João
Informe a idade do novo cliente: 30
Informe o e-mail do novo cliente: joao@email.com
```
Ao listar:
```yaml
LISTA DE CLIENTES CADASTRADOS
Cliente 1:
Nome: João
Idade: 30
E-mail: joao@email.com
----------
```

---

📁 Estrutura de dados
Cada cliente é representado assim: <br/>
```json
{
  "Nome": "João",
  "Idade": 30,
  "E-mail": "joao@email.com",
  "Id": 1,
  "Status": false
}
```

---

🧠 Observações
- Ao fechar o programa, os dados são automaticamente salvos no arquivo clientes.json.
- Ao abrir novamente, os dados são carregados automaticamente e o contador de ID continua do último número.


---

🧑‍💻 Autor
- Leonardo Nascimento Fernandes
- 📧 leonardofernandespro@gmail.com
- 🔗 LinkedIn: https://www.linkedin.com/in/leonardopro
