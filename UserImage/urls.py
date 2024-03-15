from rest_framework.urls import path
from .views import UserRegistrations,Userlogin,Userdetails,VerifyOTP,ResendOtp,ChangePassword,SendResetPasswordlinkView,UserPasswordResetView
urlpatterns = [
    path("api/register/",UserRegistrations.as_view()),
    path("api/login/",Userlogin.as_view()),
    path("api/details/",Userdetails.as_view()),
    path("api/otp/",VerifyOTP.as_view()),
    path("api/resentotp/",ResendOtp.as_view()),
    path("api/changepass/",ChangePassword.as_view()),
    path("api/send_reset_password_link-api/",SendResetPasswordlinkView.as_view()),
    path("api/reset_password-link/<uid>/<token>/",UserPasswordResetView.as_view())
]
