from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings


class Login(LoginView):
    template_name = "authen/login.html"

    def get_success_url(self):
        return "/"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({"company_name": settings.AUTHEN.get("COMPANY_NAME", "")})
        ctx.update({"login_title": settings.AUTHEN.get("LOGIN_TITLE", "")})
        return ctx


class Logout(LoginRequiredMixin, LogoutView):
    template_name = "authen/logout.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({"company_name": settings.AUTHEN.get("COMPANY_NAME", "")})
        ctx.update({"logout_title": settings.AUTHEN.get("LOGOUT_TITLE", "")})
        ctx.update({"logout_message": settings.AUTHEN.get("LOGOUT_MESSAGE", "")})
        return ctx


login_view = Login.as_view()
logout_view = Logout.as_view()
