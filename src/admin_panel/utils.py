

from sqladmin import ModelView
from database.base import TimeStampModel

def get_sqladmin_mixin(model: TimeStampModel) -> ModelView:
    class SQLAdminMixin(ModelView):
        form_excluded_columns = [model.created_at, model.updated_at, model.deleted_at]

    return SQLAdminMixin
