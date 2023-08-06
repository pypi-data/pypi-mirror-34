# SakaiAuthenticator

This is an authentication backend for Django that uses
[Sakai](https://sakaiproject.org/) to authenticate users. They are valid users
if their username and password match. Users can be granted roles based on a
specific site - all site owners will be given `superuser` permissions, while
support staff are given `staff` permissions. There is no way to determine if a
user is a participant or not when logged in as an user who only has participant
permissions, thus all users who successfully authenticate against the Sakai
instance, but are not support staff or site owners are given user accounts.

# Installation

To install SakaiAuthenticator run:

   pip install sakaiauthenticator

# Usage

In `settings.py` of your Django application, add the following:

```python
INSTALLED_APPS = [
    'sakaiauthenticator',
    ...
]

AUTHENTICATION_BACKENDS = [
    'sakaiauthenticator.sakaiauthenticator.SakaiAuthenticator',
    ...
]
SAKAI_URL = 'your.sakai.site';
USE_SAKAI_SITE = True                 # To enable site restricted authentication
SAKAI_SITE_ID = 'your_sakai_site_id'; # To enable site restricted authentication
```
