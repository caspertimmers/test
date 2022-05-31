from wagtail.core.models import Page


class HomePage(Page):

    preview_modes = []

    class Meta:
        verbose_name = "Homepage"
