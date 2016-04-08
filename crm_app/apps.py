from __future__ import unicode_literals

from django.apps import AppConfig
from watson import search as watson


class CrmAppConfig(AppConfig):
    name = 'crm_app'

    def ready(self):
        Company = self.get_model("Company")
        watson.register(Company.objects.all())