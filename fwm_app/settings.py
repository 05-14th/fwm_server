import os

def env_var(name):
    try:
        return str(os.environ[name])
    except:
        raise KeyError

        # Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fwm_ai',
        'USER': 'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306'
    }
}

INSTALLED_APPS = [    
	'django.contrib.admin',    
	'django.contrib.auth',    
	'django.contrib.contenttypes',    
	'django.contrib.sessions',    
	'django.contrib.messages',    
	'django.contrib.staticfiles',    
	'employees_app',    
	'rest_framework',
]
