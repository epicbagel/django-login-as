from django.contrib.auth import get_user_model

class LoginAsBackend(object):
	def authenticate(self, from_user, to_user_id):
		if not from_user.is_superuser:
			return None
		try:
			user = get_user_model().objects.get(pk = to_user_id)
			#user = get_user_model().objects.get(email = to_username)
		except get_user_model().DoesNotExist:
			return None
		return user

	def get_user(self, user_id):
		try:
			return get_user_model().objects.get(pk = user_id)
		except get_user_model().DoesNotExist:
			return None