from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name',)
    search_fields = ('email', 'first_name', 'last_name',)
    list_filter = ('is_active', 'is_superuser', 'is_staff',
                   'date_joined', 'last_login',)


admin.site.register(User, UserAdmin)


# # Unregister apps

# ## Django default apps

admin.site.unregister(Site)

# ## Third party apps

admin.site.unregister(EmailAddress)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)
