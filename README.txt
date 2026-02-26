TOOLBOX

Toolbox é um framework modular em Python voltado ao desenvolvimento rápido de aplicações orientadas a dados, oferecendo um conjunto de bibliotecas reutilizáveis para:

Tratamento e análise de dados
Geração de gráficos
Construção de APIs
Integração com bancos de dados
Interfaces web
Execução via linha de comando

O projeto busca centralizar soluções comuns em um único repositório organizado, reduzindo retrabalho e acelerando novos projetos.

===========================
INSTRUÇÕES PARA INICIAR O PROJETO
===========================

1) Criar o ambiente virtual (venv)

No diretório raiz do projeto (onde estão as pastas api/, ui/, data/, etc):

Linux / macOS:
    python3 -m venv venv

Windows:
    python -m venv venv


2) Ativar o ambiente virtual

Linux / macOS:
    source venv/bin/activate

Windows (PowerShell):
    venv\Scripts\Activate.ps1


3) Instalar as dependências do projeto

Com o ambiente virtual ativo:

    pip install -r requirements.txt


4) Iniciar o projeto (interface gráfica)

Ainda no diretório raiz do projeto:

    python -m ui.app.main


Observações:
- O ambiente virtual deve estar ativo para executar o projeto
- Caso ocorram erros de importação, verifique se todas as dependências foram instaladas corretamente
- O comando deve ser executado a partir da raiz do projeto