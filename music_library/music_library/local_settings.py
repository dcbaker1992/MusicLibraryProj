DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }

    }
}

SECRET_KEY = 'ry8jdiaz3g4s^9xej%ykimn)ide6_c*rs*e5$6waofoveyv4jm'