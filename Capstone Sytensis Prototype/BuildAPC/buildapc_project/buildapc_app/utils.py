from django.contrib.auth.models import Group, Permission

def create_user_groups():
    # Administrator Groups 
    admin_group, _ = Group.objects.get_or_create(name='Administrator')

    # Optionally assign permissions, for example:
    # permissions = Permission.objects.filter(codename__in=['add_logentry', 'change_logentry'])
    # admin_group.permissions.set(permissions)



    user_group, _ = Group.objects.get_or_create(name='User')
    # Minimal permissions to be provided
