from django.views.generic.base import TemplateView
from notes.models import Note
from video_archive.video import Video


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notes"] = Note.objects.all()
        context["videos"] = Video.objects.all()
        return context
