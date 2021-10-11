# film_Web
Simple web service with DataBase using Django

![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/leszekgrechowicz/filmWeb)
![](film_web.png) 

## Preparation:

Python Installation is required !

- Crate new folder and new working environment using python/pip.
- Install requirements.txt using pip.
- Install PostgreSQL DataBase using pip `pip install psycopg2-binary`
- Run script create_db_postgre.py to crate `imdb` database under PostgreSQL
  - Go to the file located in filmWeb/settings.py and set your user_name and password to the database, 
  replacing DATABASE position with the code below.
   ```
    DATABASES = {
      'default': {
          'HOST': 'localhost',
          'NAME': '<db_name>',
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'USER': '<user_name>',
          'PASSWORD': '<db_password>',
      }
    }

- Run Django command `python3 manage.py makemigrations ` to make/prepare migrations
- Run Django command `python3 manage.py migrate ` to implement migrations
- Run Django command `python3 manage.py loaddata initial_data ` to load initial database data
- Lastly run App using `python3 manage.py runserver`
