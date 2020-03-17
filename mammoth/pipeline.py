from mammoth.models import UserProfile
def get_picture(backend, strategy, details, response,
        user=None, *args, **kwargs):
    url = None
    if backend.name == 'facebook':
        url = "http://graph.facebook.com/{0}/picture".format(response['id'])
    if backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal','')
    if backend.name == 'GoogleOAuth2':
        url = response['image'].get('url')
        ext = url.split('.')[-1]
    # if url:
    #     userprofile = UserProfile()
    #     userprofile.user = user
    #     userprofile.picture = url
    #     userprofile.save()
    
# def get_picture(backend, strategy, details, response,
#         user=None, *args, **kwargs):
#     url = None
#     if backend.name == 'facebook':
#         url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
#     if backend.name == 'twitter':
#         url = response.get('profile_image_url', '').replace('_normal','')
#     # if backend.name == 'google-oauth2':
#     #     url = response['image'].get('url')
#     #     ext = url.split('.')[-1]
#     if url:
#         user.avatar = url
#         user.save()