# PyQuillSSO

A Python library to facilitate single sign on authentication with quill.

## Usage

```python
from pyquillsso import QuillSSO
quill = QuillSSO(url="https://my.hackmit.org")

# To get the url for the sign-in button.
url = quill.get_signin_url("https://mycoolapp.com/login")

# Once the user has been redirected, get their details.
user_info = quill.get_user(token)  # Token is from url.
```

Check out the [example](example.py) for an example of a simple Flask app using this.