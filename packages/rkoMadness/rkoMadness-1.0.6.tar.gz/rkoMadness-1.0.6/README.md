![pyRKO](https://raw.githubusercontent.com/Quantumke/files/master/pyRKO.png)

*There is always something that you can learn, and something you can teach - Roman Reigns*

rkoMADNESS 
=============

Why is django so popular? scaffolding, db management, routing properties?

Then there is *tornado* a simple async framework. This project allows
you to use tornado features with django scafolding and routing properties

*LETS GET STARTED*

installation
=============

`pip install rkoMadness`


Begining a new project

Move to the directory you would like to start your project.

then

` rkomadness newproject  projectname`

This will create a project with the following features:


```
projectname
    manage.py
    README.md
    .gitignore
    projectname
        routes.py
        settings.py

```

`manage.py` - this is the module that will allow you to run rkoFramework on

`routes.py` - write your routing properties here.

sample routes.py

```python
'''
import your class handler e.g
from app.views import Login

handlers=[
    (r'home/',Login)
]
'''
```

settings.py - This file will include settings variables
 
 CREATING A NEW APP
 ==================
 
 Run `python manage.py newapp appname`
 
 This will create a new app with
 ```
 projectname
    appname
        __init__.py
        controllers.py
 ```
 
 Sample Controller code:
 
 ```python
import json
from rkoMadness import BaseHandler
class SalesApi(BaseHandler):
    def post(self, *args, **kwargs):
        yield (json.dumps({}))
```

