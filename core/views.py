
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
    

class MenuView(TemplateView):
    template_name = 'menu/menu.html'
    
class AboutView(TemplateView):
    template_name = 'menu/about.html'
    
class BookView(TemplateView):
    template_name = 'menu/book.html'
    