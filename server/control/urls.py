from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path(r'^login/?', obtain_jwt_token),
    path(r'^refresh-token/?', refresh_jwt_token),
]
