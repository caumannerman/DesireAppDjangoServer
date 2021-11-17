from django.contrib import admin

from design_fields.models import DesignField
from design_fields.user_design_fields.models import UserDesignField
from design_fields.question_design_fields.models import QuestionDesignField


class DesignFieldAdmin(admin.ModelAdmin):
    list_filter = ('id', 'name', )
    list_display = ('id', 'name', )


class UserDesignFieldAdmin(admin.ModelAdmin):
    list_filter = ('id', 'user', 'design_field', )
    list_display = ('id', 'user', 'design_field', )


class QuestionDesignFieldAdmin(admin.ModelAdmin):
    list_filter = ('id', 'question', 'design_field', )
    list_display = ('id', 'question', 'design_field', )


admin.site.register(DesignField, DesignFieldAdmin)
admin.site.register(UserDesignField, UserDesignFieldAdmin)
admin.site.register(QuestionDesignField, QuestionDesignFieldAdmin)
