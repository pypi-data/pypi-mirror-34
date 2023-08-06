Ressource Server Utilities
==========================

If you've read RFCs on OAuth or (more likely) the **django-oauth-toolkit** docs, you know that a *Ressource Server* sorts
of delegates user authentication to the *Authorization Server*.

But the current implementation in *Django OAuth Toolkit* only copies the username from the *Authorization Server* in its
database. This implies that all users have no special permissions, i.e. you lose administrator rights when you access
the *Ressource Server* !

The class FullUserOAuthBackend aims to fix this by fetching the full user model from the *Authorization Server* after
you've accessed the *Ressource Server*.

Installation
------------
`pip install oauth-slave-accounts`

Setup
-----
Authorization Server
~~~~~~~~~~~~~~~~~~~~
You need to create an endpoint that exposes user data in a json manner (or further override my methods), the easiest being
a DjangoRestFramework ModelViewset.
The current implementation uses the user's Authorization token as `lookup_field`.

.. code:: python

    class UserViewSet(viewset.ReadOnlyModelViewSet):
        queryset = User.objects.all()
        serializer_class = UserSerializer
        permission_classes = [ServerServerPermission]
        def get_object(self):
            return  AccessToken.objects.get(token=self.kwargs.get('pk')).user
..

 **pro tip:** you should exclude the password from the serializer, because its confidential even if salted, and furthermore its useability probably depends on the `SECRET_KEY`

Ressource Server
~~~~~~~~~~~~~~~~
Subclass `ressource_server_utils.backend.FullUserOAuthBackend` and override the following :
 * property fetch_url : a string that describes your *Authorization Server*'s endpoint to get User data e.g. `http://auth.srv/user/{}/`
 * property UserSerializer : a DjangoRestFramework Serializer that defines how to parse your *Authorization Server*'s response
 * And optionnally
    - method get_auth_token()
    - method refresh_auth_token()