from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    refresh["token_version"] = user.token_version  # 👈 custom claim
    access = refresh.access_token
    access["token_version"] = user.token_version  # also in access

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
