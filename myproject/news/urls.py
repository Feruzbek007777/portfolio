from django.urls import path
from .views import HomeView, PortfolioCreateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add/", PortfolioCreateView.as_view(), name="portfolio_add"),
]
