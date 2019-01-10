# from .models import Socials

def socials(request):
    # context = dict()
    # for item in Socials.objects.all().values():
    #     context = item
    # return context

    context = {
        'social_vk': 'https://vk.com/',
        'social_facebook': 'https://facebook.com/',
        # 'social_twitter': 'https://twitter.com/',
        'social_instagram': 'https://www.instagram.com/',
        # 'social_google_plus': 'https://plus.google.com/',
        'social_youtube': 'https://www.youtube.com/',
        'social_whatsapp': 'https://www.whatsapp.com/'
    }
    return context