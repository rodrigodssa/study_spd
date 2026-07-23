# Study_SPD

[![Python](https://img.shields.io/badge/Python-3.12-3776ab?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0.6-092e20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![pytest](https://img.shields.io/badge/pytest-8.2.2-0a9edc?style=flat-square&logo=pytest&logoColor=white)](https://docs.pytest.org/)

Repositório de estudos desenvolvido durante o programa de mentoria com **Marco Castro (DesenvolvendoMe)**. Reúne os exercícios, projetos e testes automatizados produzidos ao longo da formação, com foco em **Python**, **testes automatizados** e **boas práticas de desenvolvimento**.

---

## 📂 Projetos

O repositório agrupa quatro frentes de estudo independentes:

| Projeto | Descrição | Testes |
|---|---|---|
| [`bytebank-tdd/`](bytebank-tdd/) | Modelagem de uma classe `Funcionario` (idade, sobrenome, bônus, regra de sócio) desenvolvida com TDD e relatório de cobertura. | 5 testes (pytest + pytest-cov) |
| [`testes_fase1/`](testes_fase1/) | Implementação de algoritmos clássicos — busca binária e bubble sort — com testes cobrindo casos de borda. | 2 testes (pytest) |
| [`exercicios/`](exercicios/) | Sete exercícios de lógica: calculadora, IMC, número primo, par ou ímpar, classificação de idade, validação de senha e jogo de adivinhação. | — |
| [`alura-space/`](alura-space/) | Aplicação Django de galeria de imagens, com templates, rotas e configuração por variáveis de ambiente. | — |

---

## 🚀 Como executar

### Pré-requisitos
- Python 3.12 (ou superior)
- `pip` e `venv`

### Ambiente

```bash
git clone https://github.com/rodrigodssa/study_spd.git
cd study_spd

python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows
```

### bytebank-tdd

```bash
cd bytebank-tdd
pip install -r requirements.txt
pytest
```

A configuração em `pytest.ini` já executa a suíte em modo verboso e imprime o relatório de cobertura do pacote `codigo`, destacando as linhas não cobertas.

Para rodar apenas os testes de um marcador específico:

```bash
pytest -m calcular_bonus
```

### testes_fase1

```bash
cd testes_fase1
pytest
```

### alura-space

```bash
cd alura-space
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto com a chave do Django:

```env
SECRET_KEY=sua-chave-secreta-aqui
```

Em seguida:

```bash
python manage.py migrate
python manage.py runserver
```

A aplicação fica disponível em `http://127.0.0.1:8000/`.

> **Atenção:** `DEBUG` está ligado em `setup/settings.py`. A configuração atual é adequada apenas para desenvolvimento local.

---

## 🧪 Testes

Os projetos `bytebank-tdd` e `testes_fase1` seguem o padrão **Given/When/Then** (contexto, ação, desfecho), com nomes de teste descrevendo a expectativa verificada. A suíte do `bytebank-tdd` cobre desde o caminho feliz até o levantamento de exceção para salários acima do teto de bônus.

---

## 🛠️ Tecnologias e Ferramentas

| Categoria | Ferramentas |
|---|---|
| Linguagem | Python |
| Framework | Django |
| Testes | pytest, pytest-cov, coverage |
| Versionamento | Git, GitHub, Gitflow |
| Ambiente | Linux, macOS, Terminal, JetBrains IDE |
| Infraestrutura | Heroku, AWS, PostgreSQL |
| Integração | REST |
| Colaboração | Slack, Gather |

---

## 🎯 Competências desenvolvidas

### Hard Skills
- Projeto básico e planejamento de projeto ágil
- Desenvolvimento e análise de código
- Processo de desenvolvimento, entrega e qualidade de software
- Gestão de versionamento de código
- Gestão de qualidade de código
- Ferramentas para aumento de produtividade

### Soft Skills
Comunicação · Colaboração · Trabalho em equipe · Disciplina · Foco · Autogestão · Autodidatismo · Resolução de problemas · Qualidade · Empatia · Resiliência

---

## 📌 Sobre

Registro público da evolução prática ao longo da mentoria — dos primeiros exercícios de lógica até projetos com testes automatizados e cobertura de código.
