from django.views import generic
from .models import Character

class CharacterCreate(generic.CreateView):
    model = Character
    fields = ['name', 'char_class']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)