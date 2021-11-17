from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.contrib.auth.admin import UserAdmin as OrigUserAdmin
from django.utils.translation import gettext_lazy as _
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken

User = get_user_model()


class UserAdmin(OrigUserAdmin):
    list_display = ('id', 'email', 'acc_type', 'nickname',
                    'first_name', 'last_name',)
    search_fields = ('email', 'first_name', 'last_name',)
    list_filter = ('acc_type', 'is_active', 'is_superuser', 'is_staff',
                   'date_joined', 'last_login',)
    ordering = ('email',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password',
         'nickname', 'acc_type', 'profile_image')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, UserAdmin)


# # Unregister apps

# ## Django default apps

admin.site.unregister(Site)

# ## Third party apps

admin.site.unregister(EmailAddress)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)
