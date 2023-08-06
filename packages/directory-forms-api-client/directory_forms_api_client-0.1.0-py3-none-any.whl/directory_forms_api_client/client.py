from django.conf import settings

from directory_client_core.base import BaseAPIClient


class DirectoryFormsAPIClient(BaseAPIClient):

    endpoints = {
        'ping': 'api/v1/healthcheck/ping/',
        'generic-submit': 'api/v1/generic/',
    }

    def ping(self):
        return self.get(url=self.endpoints['ping'])

    def submit_generic(self, data):
        return self.post(url=self.endpoints['generic-submig'], data=data)


forms_api_client = DirectoryFormsAPIClient(
    base_url=settings.DIRECTORY_FORMS_API_BASE_URL,
    api_key=settings.DIRECTORY_FORMS_API_API_KEY,
)
