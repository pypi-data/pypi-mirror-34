###########################################################################
# sakaiauthenticator is Copyright (C) 2018 Kyle Robbertze
# <krobbertze@gmail.com>
#
# sakaiauthenticator is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public
# License version 3 as published by the Free Software Foundation.
#
# sakaiauthenticator is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with sakaiauthenticator. If not, see
# <http://www.gnu.org/licenses/>.
###########################################################################

from SakaiPy import SakaiPy
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class SakaiAuthenticatorBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        info = {
            'username': username,
            'password': password,
            'baseurl': settings.SAKAI_URL
           }

        try:
            sak = SakaiPy.SakaiPy(info)
            user_info = sak.session.get_current_user_info()
        except:
            return None
        sak_username = user_info['eid']
        first_name = user_info['firstName']
        last_name = user_info['lastName']
        email = user_info['email']
        if sak_username is None:
            return None
        is_staff = False
        is_superuser = False
        if settings.USE_SAKAI_SITE:
            mem = sak.get_membership()
            try:
                # Sakai will only return membership if the current user is
                # support staff or the site owner, otherwise it returns nothing
                # and the json parsing errors.
                site_members = mem.getAllMembershipForSite(settings.SAKAI_SITE_ID)
                site_members = site_members['membership_collection']
                found = False
                for user in site_members:
                    if user['userId'] == user_info['id']:
                        role = user['memberRole']
                        is_staff = role == 'Support staff' or role == 'Site owner'
                        is_superuser = role == 'Site owner'
                        break
            except json.decoder.JSONDecodeError:
                # The current user does not have permission to view the
                # membership
                pass
        user, created = User.objects.get_or_create(username=sak_username)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user
