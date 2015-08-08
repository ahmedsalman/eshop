# eshop
git checkout code
create virtualenv
active the virtualenv
cd eshop
pip install -r requirement.txt
pip uninstall south

open settings.py

    PAYPAL_IDENTITY_TOKEN = "enter your token"                          #you may change these value as per your system settings
    PAYPAL_RECEIVER_EMAIL = "your paypal business email"                #you may change these value as per your system settings

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'       #you may change these value as per your system settings
    EMAIL_USE_TLS = True                                                #you may change these value as per your system settings
    EMAIL_HOST = 'smtp.gmail.com'                                       #you may change these value as per your system settings
    EMAIL_PORT = 587                                                    #you may change these value as per your system settings
    EMAIL_HOST_USER = 'email'
    EMAIL_HOST_PASSWORD = 'password'

if you are using the test database which is included in the package then no need to run migrate or syncdb

    python manage.py migrate
    python manage.py syncdb

python manage.py runserver

for demo https://test-eshoping.herokuapp.com/

admin username/password: ahmed/ahmed 
