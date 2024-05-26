## Deploy APi Vitinicultura Embrapa
O plano do deploy será feito em um servidor cloud AWS.

## Deploy da API na AWS

### 1. Preparar o Ambiente de Desenvolvimento

#### Estrutura do Projeto

Organizar o Projeto:
    Certifique-se de que todos os arquivos do projeto foram criados e estão seguindo a estrutura correta.
    Sua estrutura de diretórios deve estar semelhante a:

```markdown
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── comercialization.py
│   │   ├── exportation.py
│   │   ├── importation.py
│   │   ├── processing.py
│   │   ├── production.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── scraper.py
│   ├── requirements.txt
│   └── README.md
```

#### Arquivo `requirements.txt`

Certifique-se de incluir todas as dependências necessárias para execução do projeto:

```plaintext
fastapi
uvicorn
requests
beautifulsoup4
pydantic==1.10.7
fastapi-jwt-auth
```

### 2. Preparar o Ambiente AWS

#### Instalar AWS CLI e EB CLI

1. **Instalar AWS CLI:**
   - Siga o [guia de instalação](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
   - Configure o AWS CLI:
     ```sh
     aws configure
     ```

2. **Instalar Elastic Beanstalk CLI:**
   - Siga o [guia de instalação](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html).

### 3. Inicializar o Elastic Beanstalk

#### Estruturar o Projeto para Elastic Beanstalk

Crie a seguinte estrutura adicional no seu projeto:

```
├── .ebextensions
│   └── flask.config
```

#### Arquivo `.ebextensions/flask.config`

Crie o arquivo `.ebextensions/flask.config` com o seguinte conteúdo:

```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: app.main:app
```

#### Inicializar o Elastic Beanstalk

1. **Inicializar um Aplicativo Elastic Beanstalk:**
   ```sh
   eb init -p python-3.8 my-flask-app
   ```

2. **Criar um Ambiente de Deploy:**
   ```sh
   eb create my-flask-app-env
   ```

### 4. Fazer o Deploy da Aplicação

1. **Deploy da Aplicação:**
   ```sh
   eb deploy
   ```

2. **Verificar o Status:**
   ```sh
   eb status
   ```

3. **Abrir a Aplicação no Navegador:**
   ```sh
   eb open
   ```

### 5. Monitorar e Gerenciar o Ambiente

Use o Elastic Beanstalk Management Console para monitorar o desempenho do seu aplicativo, visualizar logs e gerenciar configurações.

2. **Configurar Regras de Segurança:**
   - Configure as regras de segurança para restringir o acesso às portas e serviços necessários.

### 6. Manter o Projeto

1. **Atualizar a Aplicação:**
   ```sh
   eb deploy
   ```

2. **Verificar Logs de Erro:**
   ```sh
   eb logs
   ```

Ferramentas de monitoramento adicionais serão sempre bem vindas para garantir a estabilidade da API.

