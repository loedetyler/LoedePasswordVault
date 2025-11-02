# Loede Password Manager
I have decided to create and containerize a simple password manager/vault. Users will be able to create, store, access, and delete passwords using this top of the line vault. Users will have the ability to register and create an account from the main page, be shown the account or name of the passwords that they've stored, have the option to create a password, view their stored passwords, and in the case of needing to update or remove passwords, we have the option to doing both of those. 

# Installation
```bash
docker-build .
docker-compose run django bash
python manage.py migrate
python manage.py createsuperuser
```

# Getting Started
To run my top of the line password vault, simply use the following:
```bash
docker-compose up
```
# License

Copyright (c) Tyler P. Loede 2025
