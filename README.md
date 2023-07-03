# Newsletter Subscription
## Django Exercise

How to get and run:  
1. Clone the project: ```git clone https://github.com/CodingSummer23/newsletter.git```
1. Get in the new folder: ```cd newsletter``` 
1. Create a virtual environment: ```python -m venv venv```
1. Run the virtual environment: ```source venv/bin/activate``` (Mac/Linux), ```venv\Scripts\activate``` (Windows)
1. Install dependenies: ```pip install -r requirements.txt```
1. Get in the project's main folder: ```cd newsletter```
1. Migrate: ```python manage.py migrate```
1. Create super user: ```python manage.py createsuperuser```
1. Run the project: ```python manage.py runserver```


# Exercise:

Upon a new subscription a random token is created, to be used when someone wants to unsubscribe.  
Although it is almost impossible to have the same token twice, we never know. So, when creating a token, be sure that it has never been used before. 