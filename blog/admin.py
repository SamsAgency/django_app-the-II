from django.contrib import admin
#importing models from the class we created
from .models import Post

# Registing the models
admin.site.register(Post)
