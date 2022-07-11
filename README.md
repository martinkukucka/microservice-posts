# microservice-posts
Python microservice that will provide a RESTful API for managing user posts

Database connection is required. Default database settings:
  'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'posts',
      'USER': 'root',
      'PASSWORD': 'root',
      'HOST': 'localhost',
      'PORT': '3306',
  }

Installation: 
  pip install -r .\requirements.txt
  
Run: 
  python3 manage.py runserver

URLs:
  • all posts:
      http://127.0.0.1:8000/api/posts/
  • post with selected id:
      http://127.0.0.1:8000/api/posts/postId/
  • posts of selected user
      http://127.0.0.1:8000/api/users/userId/
