from django.contrib import admin

from Movieplatapp.models import Movie, Myrating, MyList

# Register your models here.
admin.site.register(Movie)
admin.site.register(Myrating)
admin.site.register(MyList)