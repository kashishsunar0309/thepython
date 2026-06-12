#IN Terminal CMD:
"""cd Gitdemo\learning_log 
type: django-admin startproject pizzeria_project
type: cd pizzeria_project
type: python manage.py startapp pizzas"""

#ON CODE_RUNNER(create/edit these files)
"""
pizzas/models.py - edit it
pizzas/admin.py - edit it
pizzeria_project/settings.py - add
"""

#IN Terminal CMD:
"""
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
"""

#ON Browser
"""http://locathost:8000/admin
Add pizzas and toppings here.
"""

#ON Terminal shell
"""
python manage.py shell
from pizzas.models import Pizza, Topping
Pizza.objects.all()
Topping.objects.filter(pizza__name = 'Hawaiian')
"""