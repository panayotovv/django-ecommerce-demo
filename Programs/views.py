from django.views.generic import DetailView
from Programs.models import Programs


class ProgramsDetailView(DetailView):
    template_name = 'plan-details.html'
    model = Programs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']

        return context