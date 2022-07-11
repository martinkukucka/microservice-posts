# microservice-posts
Python microservice that will provide a RESTful API for managing user posts

Database connection is required. Default database settings: <br />
  &ensp;'default': { <br />
  &ensp;&ensp;&ensp;    'ENGINE': 'django.db.backends.mysql', <br />
  &ensp;&ensp;&ensp;    'NAME': 'posts', <br />
  &ensp;&ensp;&ensp;    'USER': 'root', <br />
  &ensp;&ensp;&ensp;    'PASSWORD': 'root', <br />
  &ensp;&ensp;&ensp;    'HOST': 'localhost', <br />
  &ensp;&ensp;&ensp;    'PORT': '3306', <br />
  &ensp;} <br />

#### Installation:  <br />
  &ensp;&ensp;pip install -r .\requirements.txt <br />
  
#### Run:  <br />
  &ensp;&ensp;python3 manage.py runserver <br />

#### URLs: <br />
  &ensp;• all posts: <br />
  &ensp;&ensp;&ensp;    http://127.0.0.1:8000/api/posts/ <br />
  &ensp;• post with selected id: <br />
  &ensp;&ensp;&ensp;    http://127.0.0.1:8000/api/posts/postId/ <br />
  &ensp;• posts of selected user <br />
  &ensp;&ensp;&ensp;    http://127.0.0.1:8000/api/users/userId/ <br />
  
#### Path to run API documentation in web browser:  <br />
 &ensp;docs/_build/html/index.html
