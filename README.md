# Livraria Clean — Exercício 7.4

Aplicação web simples para cadastrar, listar e editar livros. O exercício demonstra Arquitetura Clean, o Princípio da Inversão de Dependência (DIP) e persistência em arquivo TXT.

## Funcionalidades

- Listar livros cadastrados.
- Cadastrar livro com título, gênero e preço.
- Editar título, gênero e preço de um livro existente.
- Persistir os dados no arquivo `dados.txt`, mantendo os dados após reiniciar a aplicação.
- Validar campos obrigatórios e impedir preços negativos.

## Tecnologias

- Python 3.10 ou superior.
- Flask para a interface web.
- `csv` da biblioteca padrão do Python para ler e escrever registros separados por ponto e vírgula.
- `unittest` da biblioteca padrão para os testes.

## Estrutura do projeto

```text
livraria-clean/
├── core/
│   ├── __init__.py
│   ├── entities.py
│   ├── repositories.py
│   └── use_cases.py
├── interface_adapters/
│   ├── __init__.py
│   └── txt_repository.py
├── frameworks/
│   ├── __init__.py
│   └── app.py
├── templates/
│   └── index.html
├── tests/
│   ├── __init__.py
│   ├── test_use_cases.py
│   └── test_txt_repository.py
├── dados.txt
├── requirements.txt
└── README.md
```

## Instalação

Na pasta raiz do projeto, crie e ative um ambiente virtual.

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Linux ou macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Executar a aplicação

Na raiz do projeto, execute:

```bash
python -m frameworks.app
```

Abra `http://127.0.0.1:5000` no navegador. A aplicação permite cadastrar livros e abrir a opção **Editar este livro** para alterar seus dados.

## Executar os testes

Na raiz do projeto, execute:

```bash
python -m unittest discover -v
```

Os testes cobrem listagem, cadastro, edição, validação de preço, leitura e gravação no arquivo TXT.

## Formato de persistência

Cada linha de `dados.txt` representa um livro no formato:

```text
O Hobbit;Fantasia;45.0
1984;Ficção;30.0
```

O repositório lê o formato original com três campos separados por ponto e vírgula. Se o arquivo ainda não existir, ele é criado com dois exemplos iniciais. Se já existir, o conteúdo não é substituído na inicialização. A edição regrava a lista completa após substituir o livro selecionado.

## Arquitetura Clean e DIP

- **Entidade (`core/entities.py`):** representa o livro e valida os dados essenciais do domínio.
- **Abstração (`core/repositories.py`):** define as operações de persistência que o núcleo precisa, sem mencionar TXT ou Flask.
- **Casos de uso (`core/use_cases.py`):** implementa listagem, cadastro e edição. Depende do contrato `LivroRepository`, não da implementação concreta.
- **Adaptador de persistência (`interface_adapters/txt_repository.py`):** implementa o contrato usando `dados.txt`.
- **Framework/interface (`frameworks/app.py` e `templates/index.html`):** recebe as requisições HTTP, chama os casos de uso e apresenta os resultados.

O DIP é aplicado porque o caso de uso depende da abstração `LivroRepository`. A implementação concreta `TxtRepository` é conectada na inicialização da aplicação. Assim, seria possível criar outro repositório — por exemplo, para banco de dados — sem reescrever as regras dos casos de uso.

## Observações

- Faça uma cópia de segurança de `dados.txt` antes de experimentar alterações.
- O servidor de desenvolvimento do Flask (`debug=True`) é apropriado para estudo local, não para produção.
