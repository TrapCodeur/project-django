from django.urls import path
from soccer.views import player_detail, index
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import signup, logout_user, login_user, verify, verification
from contact.views import contact, confirmation_view



urlpatterns = [ 
    path("", index, name="index"),
    path("player/<slug:slug>", player_detail, name="player_detail"),
    path("signup", signup, name="signup"),
    path("logout", logout_user, name="logout"),
    path("login", login_user, name="login"),
    path("contact", contact, name="contact"),
    path("confirmation", confirmation_view, name="confirmation"),
    path("verify", verify, name="verify"),
    path("verification", verification, name="verification"),




 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)