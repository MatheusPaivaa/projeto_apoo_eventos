<h1 align="center">Sistema de Gerenciamento de Eventos 🎟️💻</h1>
<p align="center"> Projeto desenvolvido para a disciplina de Análise e Projeto Orientados a Objetos (SSC0124)</p>

<p align="center">
  <a href="#projeto">Projeto</a> • 
  <a href="#instalacao">Instalação e uso</a> • 
  <a href="#tecnologias">Tecnologias</a> • 
  <a href="#contribuindo">Contribuição</a> •
  <a href="#licenca">Licença</a> •
  <a href="#agradecimentos">Agradecimentos</a>
</p>

<p align="center">
   <img align="center" text-align="center" width="45%" style="margin-right:50px;" src="https://github.com/MatheusPaivaa/projeto_apoo_eventos/blob/main/assets/disp_eventos.png">
   <img align="center" text-align="center" width="50%" src="https://github.com/MatheusPaivaa/projeto_apoo_eventos/blob/main/assets/login.png">
</p>


## <div id="projeto"></div>Projeto

O **Sistema de Gerenciamento de Eventos** é uma solução tecnológica que moderniza e otimiza a organização de conferências, seminários e workshops. Ele integra e automatiza etapas como inscrições, controle de participantes, envio de convites, geração de certificados e coleta de feedback, reduzindo o tempo gasto e minimizando falhas comuns nos processos manuais. Essa ferramenta atende à crescente demanda por eventos presenciais e online, oferecendo uma experiência mais fluida para organizadores e participantes.

Com foco em simplificar o planejamento e automatizar tarefas repetitivas, o sistema centraliza todas as funcionalidades necessárias em uma única plataforma. Assim, permite uma gestão eficiente de eventos, facilitando a comunicação com os inscritos, garantindo maior precisão nos processos e melhorando a experiência geral para todos os envolvidos.

## <div id="instalacao"></div>Instalação e uso

Siga os passos abaixo para configurar e executar o projeto:

---

#### **Pré-requisitos**
- Python 3.8 ou superior instalado
- Pip (gerenciador de pacotes do Python)
- Git (opcional, para clonar o repositório)

---

#### **Passo 1: Clonar o repositório (opcional)**
Se ainda não baixou o projeto, use o comando:
```bash
git clone https://github.com/MatheusPaivaa/projeto_apoo_eventos
cd https://github.com/MatheusPaivaa/projeto_apoo_eventos
```

---

#### **Passo 2: Criar ambiente virtual**
Crie e ative um ambiente virtual:
```bash
python -m venv venv
# No Windows:
.venv\Scripts\activate
# No Linux/Mac:
source .venv/bin/activate
```

---

#### **Passo 3: Instalar dependências**
Instale as dependências listadas no arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

#### **Passo 4: Configurar o banco de dados**
Realize as migrações para configurar o banco de dados SQLite3:
```bash
python manage.py migrate
```

---

#### **Passo 5: Executar o servidor**
Inicie o servidor local:
```bash
python manage.py runserver
```
Acesse o projeto em [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

#### **Passo 6: Configurar o Front-End**
Certifique-se de que os arquivos HTML, CSS e jQuery estejam na pasta correta e funcionando conforme esperado no navegador.

---

#### **Passo 7: Gerar arquivos estáticos (opcional)**
Para produção, colete os arquivos estáticos:
```bash
python manage.py collectstatic
```

---

A própria disciplina disponibilizou um arquivo com as intruções de como começar a utilizar o Django: [LINK](https://edisciplinas.usp.br/pluginfile.php/8680583/mod_resource/content/1/traduzido_Tutorial_django_si_controleBancario.pdf)


## <div id="tecnologias"></div>Tecnologias

O projeto combina tecnologias eficientes para garantir um desenvolvimento ágil e um sistema funcional.

- **Linguagem de Programação: Python**  
  Utilizada pela sua simplicidade e suporte à Programação Orientada a Objetos, essencial para a estrutura do sistema.

- **Framework: Django**  
  Escolhido pelo padrão *"batteries-included"*, que oferece funcionalidades prontas, como autenticação, administração, ORM e segurança integrada.

- **Banco de Dados: SQLite3**  
  Implementado por sua leveza e facilidade de configuração, ideal para o desenvolvimento.

- **Front-End: HTML, CSS e jQuery**  
  HTML e CSS foram usados para estruturação e estilo, enquanto jQuery facilitou interações dinâmicas e comunicação assíncrona.

## <div id="contribuindo"></div>Contribuição
Contribuições são bem-vindas! Por favor, faça um fork do repositório e envie um pull request com suas alterações.

## <div id="licenca"></div>Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## <div id="acknowledgements"></div>Agradecimentos
Gostaríamos de agradecer a Profa. Lina Garcés pela sua orientação e apoio ao longo deste projeto.

## Alunos
- Felipe de Castro Azambuja - **14675437** ([Github](https://github.com/DeguShi))
- Guilherme Pascoale Godoy - **14576277** ([Github](https://github.com/))
- Leonardo Marangoni - **14747614** ([Github](https://github.com/leomarangonii))
- Matheus Paiva Angarola - **12560982** ([Github](https://github.com/MatheusPaivaa))
