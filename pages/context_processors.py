from django.conf import settings


def site_settings(request):
    """
    Add site name and description to all templates
    """
    return {
        "site_name": getattr(settings, "SITE_NAME", "My Website"),
        "site_description": getattr(settings, "SITE_DESCRIPTION", "A personal website"),
    }
