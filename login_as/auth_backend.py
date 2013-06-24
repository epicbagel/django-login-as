from django.contrib.auth import get_user_model

class LoginAsBackend(object):
    def authenticate(self, from_user, to_username):
        if not from_user.is_superuser:
            return None
        try:
            user = get_user_model().objects.get(username=to_username)
        except get_user_model().DoesNotExist:
            return None
        return user

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None