# <span style="color:#4CAF50">TOOLBOX</span>

**Toolbox** é um framework modular em <span style="color:#1976D2"><strong>Python</strong></span>, voltado ao desenvolvimento rápido de aplicações orientadas a dados.  
Ele fornece um conjunto de bibliotecas reutilizáveis organizadas por responsabilidade, facilitando a criação, manutenção e evolução de projetos.

---

## <span style="color:#FF9800">Objetivo</span>

Centralizar soluções comuns em um único repositório bem estruturado, reduzindo retrabalho e acelerando o desenvolvimento de novos projetos baseados em dados.

---

## <span style="color:#9C27B0">Funcionalidades</span>

O projeto oferece suporte para:

- Tratamento e análise de dados  
- Geração de gráficos e visualizações  
- Construção de APIs  
- Integração com bancos de dados  
- Interfaces gráficas e web  
- Execução via linha de comando (CLI)  

---

## <span style="color:#03A9F4">Como iniciar o projeto</span>

### <span style="color:#607D8B">1) Criar o ambiente virtual (venv)</span>

No diretório raiz do projeto (onde estão as pastas `api/`, `ui/`, `data/`, etc.):

**Linux / macOS**
```bash
python3 -m venv venv
``` 

**Windows**
```bash
python -m venv venv
```
### <span style="color:#607D8B"> 2) Ativar o ambiente virtual
</span>

**Linux / macOS**
```bash
source venv/bin/activate
```
**Windows (PowerShell)**
```bash
venv\Scripts\Activate.ps1
```
### <span style="color:#607D8B"> 3) Instalar as dependências do projeto
</span>

**Com o ambiente virtual ativo**
```bash
pip install -r requirements.txt
```
### <span style="color:#607D8B"> 4) Iniciar o projeto (interface gráfica)
</span>

**Ainda no diretório raiz do projeto**
```bash
python -m ui.app.main
```
---

Observações:
- O ambiente virtual deve estar ativo para executar o projeto
- Caso ocorram erros de importação, verifique se todas as dependências foram instaladas corretamente
- O comando deve ser executado a partir da raiz do projeto