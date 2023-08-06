![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# django-politico-fake-news

### Quickstart

1. Install the app.

  ```
  $ pip install django-politico-fake-news
  ```

2. Add the app and its dependencies to your Django project and configure settings.

  ```python
  INSTALLED_APPS = [
      # ...
      'taggit',
      'taggit_serializer',
      'rest_framework',
      'savepagenow',
      'fakenews',
  ]

  #########################
  # fakenews settings

  FAKENEWS_AUTH_DECORATOR = ''
  FAKENEWS_POLITICO_SERVICES_TOKEN = ''
  FAKENEWS_POLITICO_SERVICES_ROOT = ''
  FAKENEWS_API_TOKEN = ''
  FAKENEWS_SECRET_KEY = ''
  FAKENEWS_AWS_ACCESS_KEY_ID = ''
  FAKENEWS_AWS_SECRET_ACCESS_KEY = ''
  FAKENEWS_AWS_REGION = ''
  FAKENEWS_AWS_S3_BUCKET = ''
  FAKENEWS_CLOUDFRONT_ALTERNATE_DOMAIN = ''
  FAKENEWS_S3_UPLOAD_ROOT = ''
  ```

### Developing

##### Running a development server

Developing python files? Move into example directory and run the development server with pipenv.

  ```
  $ cd example
  $ pipenv run python manage.py runserver
  ```

Developing static assets? Move into the pluggable app's staticapp directory and start the node development server, which will automatically proxy Django's development server.

  ```
  $ cd fakenews/staticapp
  $ gulp
  ```

Want to not worry about it? Use the shortcut make command.

  ```
  $ make dev
  ```

##### Setting up a PostgreSQL database

1. Run the make command to setup a fresh database.

  ```
  $ make database
  ```

2. Add a connection URL to the `.env` file.

  ```
  DATABASE_URL="postgres://localhost:5432/fakenews"
  ```

3. Run migrations from the example app.

  ```
  $ cd example
  $ pipenv run python manage.py migrate
  ```
