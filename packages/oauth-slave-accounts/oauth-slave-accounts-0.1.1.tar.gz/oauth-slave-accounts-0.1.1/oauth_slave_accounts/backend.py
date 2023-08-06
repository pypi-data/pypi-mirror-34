import logging
import os

import requests
from django.contrib.auth import get_user_model
from oauth2_provider.oauth2_backends import get_oauthlib_core

from django.conf import settings


logger = logging.getLogger('introspector')

class FullUserOAuthBackend(object):
    """
    This authentification backend for Django apps extends django-oauth-toolkit's OAuth2Backend by downloading
    the full user data from a specified endpoint, in a DjangoRestFramework fashion

    Override properties UserSerializer, full_url and methods get_auth_token(), refresh_auth_token()
    """
    User = get_user_model()
    UserSerializer = None
    fetch_url = None #example "http://localhost:8080/oauth/user/{}/"

    def __init__(self):
        assert self.UserSerializer is not None, "Please define property UserSerializer for {}".format(self.__class__.__name__)
        assert self.fetch_url is not None, "Please define property full_url for {}".format(self.__class__.__name__)
        assert self.User().needs_update, "Please implement a property `needs_update` in you User model"

    def authenticate(self, request=None, **credentials):
        if request is not None:
            valid, r = get_oauthlib_core().verify_request(request, scopes=[])
            if valid and r.user is not None:
                if r.user.needs_update:
                    data = self.download_user(r)
                    return self.update_external_user(data, r.user)
            #else: test_token()
        return None

    def get_user(self, user_id): #en fait avec OAuth cette méthode est pas appelée
        try:
            return self.User.objects.get(pk=user_id)
        except self.User.DoesNotExist:
            return None

    def download_user(self, request, recursive=False):
        """
        Override this method to provide your own way of retrieving full user from master server
        :param r: the second value returned by verify_request()
        :return: a dict containing user model retrieved from server
        """


        response = self.perform_download(token=request.access_token.token, username=request.user.username)

        if response.status_code == 401: #refreshed token and retries
            if not recursive:
                self.refresh_auth_token()
                logger.info("Retrying user download")
                return self.download_user(request=request, recursive=True)
            else:
                logger.warning("Warn: unable to authenticate against remote server. Check your credentials")
        logger.debug("Response: " + str(response.status_code) + response.text + " \nfor " + response.url)
        return response.json()

    def perform_download(self, token=None, username=None):
        """
        Override this method
        :param token:
        :param username:
        :return:
        """
        logger.debug("using token {} to get full user data from external server".format(token))
        return requests.get(
            url=self.fetch_url.format(token),
            headers={
                'Authorization': 'Bearer ' + self.get_auth_token()
            }
        )


    def update_external_user(self, data, user):
        """
        :param data: a dict containing user data retrieved from server
        :param user:  the user instance to update with data
        :return: an updated User instance
        """
        serializer = self.UserSerializer(user, data=data) #on rajoute les nouvelles données au serializer
        if serializer.is_valid():
            logger.debug("External user data valid")
            return serializer.save() #on sauvegarde les modifications
            #logger.debug("User {} successfully updated".format(user.username))
        else:
            logger.warning("Deserialization errors: {}".format(serializer.errors))
            return None

    def get_auth_token(self):
        return os.environ.get('RESOURCE_SERVER_AUTH_TOKEN', '')

    def refresh_auth_token(self):
        logger.warning("You should override this method if your token expires")