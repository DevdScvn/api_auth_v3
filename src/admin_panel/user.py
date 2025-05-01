from sqladmin import ModelView

from admin_panel.utils import get_sqladmin_mixin
from users.models import User


class UserAdmin(get_sqladmin_mixin(User), ModelView, model=User):

    column_list = [
        User.id,
        User.email,
        User.username,
        # User.password,
        User.created_at,
        User.updated_at,
        User.deleted_at,
    ]
    column_searchable_list = [User.id, User.email, User.username]

    name = "User"
    name_plural = "Users"