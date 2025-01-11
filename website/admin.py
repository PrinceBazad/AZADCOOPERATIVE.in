from django.contrib import admin

# Register your models here.
from .models import director
from .models import Product
from .models import Branch
from .models import AnnualReport
from .models import NewsandUpdate
from .models import HomeSlide
from .models import Aboutus
from .models import Byelaw
from .models import Announcement

admin.site.register(Byelaw)
admin.site.register(HomeSlide)
admin.site.register(director)
admin.site.register(Product)
admin.site.register(Branch)
admin.site.register(AnnualReport)
admin.site.register(NewsandUpdate)
admin.site.register(Aboutus)
admin.site.register(Announcement)