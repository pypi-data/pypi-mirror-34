from django_database_functions.utils import PrettyStringFormatting
from django.db.models.functions import Func


class TIMESTAMPDIFF(Func):
    def __init__(self, *expressions, **extra):
        unit = extra.pop('unit', 'day')
        self.template = self.template % PrettyStringFormatting({"unit": unit})
        super().__init__(*expressions, **extra)

    function = 'TIMESTAMPDIFF'
    template = "%(function)s(%(unit)s, %(expressions)s)"
