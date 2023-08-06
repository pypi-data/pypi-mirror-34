"""Provides the main class to interface with the
Quill SSO procedure.
"""

import requests
import jwt


class QuillSSO(object):
    def __init__(self, secret=None, url="https://my.hackmit.org"):
        """Initializes the QuillSSO object.

        Args:
            secret (string, optional): The shared SSO secret.
            url (string, optional): The Quill endpoint URL.

        Returns:
            A QuillSSO object.
        """

        self.secret = secret
        self.url = url.rstrip("/")  # Remove trailing slash.

    def get_signin_url(self, redirect_url):
        """Get the url for the sign-in button on your app.

        Args:
            redirect_url (string): Where quill will give the token.
        
        Returns:
            string: The url for the sign-in button.
        """

        return "{quill_url}/login?sso={redirect_url}".format(
            quill_url=self.url, redirect_url=redirect_url
        )

    def get_user(self, token):
        """Gets the user data from an SSO token.
        """

        if self.secret:
            jwt.decode(token, self.secret, algorithm="HS256")

        r = requests.post(self.url + "/auth/sso/exchange", data={"token": token})

        if r.status_code != 200:
            raise Exception(r.text)

        return r.json()
