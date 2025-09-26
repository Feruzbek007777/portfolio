from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .models import Portfolio, Experience, Awards, Skills
from .forms import PortfolioForm


class HomeView(TemplateView):
    template_name = "news/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["portfolio"] = Portfolio.objects.first()
        context["experiences"] = Experience.objects.all()
        context["awards"] = Awards.objects.all()
        context["skills"] = Skills.objects.all()
        return context


class PortfolioCreateView(CreateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = "news/portfolio_form.html"
    success_url = reverse_lazy("home")
