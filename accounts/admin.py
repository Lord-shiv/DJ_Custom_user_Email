from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, UserManager
from . forms import UserAdminCreationForm, UserAdminChangeForm


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    date_hierarchy = 'date_joined'

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username', 'admin', 'staff',
                    'date_joined', 'last_login',)
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('staff', 'active',
                                    'hide_email',)}),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions', )
        }),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email',)
    ordering = ('email',)
    filter_horizontal = ()

    def has_add_permission(self, request, obj=None):
        return True
        # request.user.id_admin

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name='Staff Head').exists():
            '''staff can't delete users'''
            return False
        return obj

    def has_change_permission(self, request, obj=None):
        return True
        # return request.user.is_admin or (obj and obj.id == request.user.id)

        # MAX_OBJECTS = 1
        # def has_add_permission(self, request):
        #     if self.model.objects.count() >= MAX_OBJECTS:
        #         return False
        #     return super().has_add_permission(request)

        # def has_module_permission(self, request):
        #     return request.user.is_admin

        # def get_queryset(self, request):  To only show the loged in user
        #     qs = super().get_queryset(request)
        #     user = request.user
        #     return qs if user.is_superuser else qs.filter(id=user.id)


admin.site.register(User, UserAdmin)
