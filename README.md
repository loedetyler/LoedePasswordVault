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
# User Stories
As a **user**, I want to **securely store my passwords** so I can **easily access and add passwords** </br>
As an **admin**, I want to **be able to view and manage logs** so I can **watch for misuse and would be able to deactivate/delete malicious user accounts**. (Additional note: admins will **not** be able to see users' passwords.)</br>
As a **developer**, I want to **update and maintain the code** so I can **keep the users's passwords secure**.</br>
As a **support role**, I want to **be able to reset users' passwords if they forget them** so **the user can have access to their password vault**.

# Acceptance Criteria
As a **user**, the acceptance criteria would be **not allowing other users to see my passwords**.</br>
As an **admin**, the acceptance criteria would be **the ability to delete or deactivate users' accounts without being able to see their passwords**.</br>
As a **developer**, the acceptance criteria would be **regularly maintaining and updating the code**.</br>
As a **support role**, the acceptance criteria would be **being able to reset users' passwords and getting them access back into their vaults**. 

# Mis-user Stories
As a **misuser**, I want to **access other users' passwords** so I can **steal their passwords**.</br>
As a **misuser**, I want to **change other users' stored passwords** so I can **cause chaos**.</br>
As a **misuser**, I want to **change other users' account emails and passwords** so I can **potentially ransom their account**.</br>
As a **misuser**, I want to **access other users' passwords** so I can **sell access to their accounts**.

# Mitigation Criteria
In order to prevent a **misuser** from **accessing other users' passwords**, I want to use **authentication of users**.</br>
In order to prevent a **misuser** from **changing other users' passwords**, I think using **authentication** will still prevent malicious action to users' accounts.</br>
As a **role**, the acceptance criteria would be **line**. 

# License

Copyright (c) Tyler P. Loede 2025
