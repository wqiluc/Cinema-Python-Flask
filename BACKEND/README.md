<h1 align="center">🏛️ Arquitetura Backend (Lógica de Negócio e Dados)</h1>
<pre>
Cinema-Python-Flask/
├── BACKEND<img src="https://img.shields.io/badge/-Python-111827?style=flat&logo=python&logoColor=3776AB"/><img src="https://img.shields.io/badge/-Flask-111827?style=flat&logo=flask&logoColor=white"/><img src="https://img.shields.io/badge/-JSON-111827?style=flat&logo=json&logoColor=white"/>/
│   ├── python<img src="https://img.shields.io/badge/-Python-111827?style=flat&logo=python&logoColor=3776AB"/>/
│   │   ├── cinema.py
│   │   ├── cinema_terminal.py
│   │   ├── cores.py
│   │   └── validacoes.py
│   ├── json<img src="https://img.shields.io/badge/-JSON-111827?style=flat&logo=json&logoColor=white"/>/
│   │       ├── dados_gerais.json
│   ├── app.py
│   ├── gerenciador_dados.py
│   └── main.py
</pre>

<h2 align="left">Núcleo de Lógica (Pasta <code>python/</code>) <br>
<img src="https://img.shields.io/badge/-Python-111827?style=flat&logo=python&logoColor=3776AB"/></h2>
Centraliza as regras de negócio e entidades (modelos) do sistema. Atua de forma independente da interface (CLI ou Web), garantindo a integridade dos dados através de validações e proporcionando feedback visual para o desenvolvedor.

---

<h2 align="left">Camada de Persistência <br>
<img src="https://img.shields.io/badge/-JSON-111827?style=flat&logo=json&logoColor=white"/></h2>
Desacopla a estrutura de dados da lógica do código. O arquivo `dados_gerais.json` serve como armazenamento, enquanto o `gerenciador_dados.py` funciona como uma camada de serviço (DAO), permitindo a troca do formato de banco de dados sem alterar o restante da aplicação.

---

<h2 align="left">Controller (<code>app.py</code>) <br>
<img src="https://img.shields.io/badge/-Flask-111827?style=flat&logo=flask&logoColor=white"/></h2>
Atua como o <b>Controller</b> do padrão MVC. É o maestro das requisições HTTP: recebe o input do usuário, invoca a lógica de negócio e as consultas de dados, e define a resposta (seja renderizando um template ou enviando JSON).

---

<h2 align="left">Orquestrador (<code>main.py</code>) <br>
<img src="https://img.shields.io/badge/-Runner-111827?style=flat&logo=python&logoColor=3776AB"/></h2>
O ponto de entrada para execução e configuração do servidor. Centraliza as definições de ambiente e inicialização da aplicação, garantindo que o servidor esteja pronto para ser operado, seja em ambiente de desenvolvimento ou produção.