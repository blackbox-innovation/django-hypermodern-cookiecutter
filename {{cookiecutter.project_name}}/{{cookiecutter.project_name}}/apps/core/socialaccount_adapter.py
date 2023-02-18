
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


LINKEDIN_OUATH2_PROFILE_PICTURE_URL = (
    "https://api.linkedin.com/v2/me?projection=(profilePicture("
    "displayImage~:playableStreams))&oauth2_access_token={access_token}"
)


class SocialaccountAdapter(DefaultSocialAccountAdapter):
    pass