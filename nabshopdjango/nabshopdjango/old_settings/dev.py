from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qoqt=gb(b7^dquy$ohkpai2r-n79i9k%8qepgr#y6g4-%-bo66'

STRIPE_SECRET_KEY = 'sk_test_51MnI9lBwcqwfQakZcJKfr282Uh9fQqo9bjbxy8JYqVO2Xk3o9U69hmkrEUZVavTvzFfvozrvDWuChPJo2GV9Vclc00FzDbL7Ne'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nabshop',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'rootnabil'
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}