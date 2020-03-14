from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from mammoth.models import Comment, Pattern
from mammoth.forms import UserForm, UserProfileForm, PatternForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.contenttypes.models import ContentType
# Add Avg pack
from django.db.models import Avg, Max, Min

def index(request):
    visitor_cookie_handler(request)

    response = render(request, 'mammoth/index.html', context={})
    return response

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'mammoth/register.html', context={'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                # Here: we can redirect the user to the page where they used to login
                # and if it cannot get previous page, it will redirect to mammoth:index
                refer = request.META.get("HTTP_REFERER","mammoth:index") 
                # return redirect(reverse('mammoth:index'))
                return redirect(refer)  
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'mammoth/login.html')

@login_required
def restricted(request):
    return render(request, 'mammoth/restricted.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('mammoth:index'))

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits
	
	
# -------------------------------------------------------
# --- Mammoth -------------------------------------------
# -------------------------------------------------------

def pattern(request, pattern_title_slug):
    context_dict = {}
    try:
        pattern = Pattern.objects.get(slug=pattern_title_slug)
        comments = Comment.objects.filter(pattern = pattern.pk)
        avg_rating = comments.aggregate(Avg('rating'))


        context_dict['pattern'] = pattern
        context_dict['comments'] = comments
        context_dict['AvgRating'] = avg_rating['rating__avg']
        context_dict['author'] = pattern.author
        context_dict['description'] = pattern.description
    except Pattern.DoesNotExist:
        context_dict['pattern'] = None
        
    return render(request, 'mammoth/pattern.html', context_dict)

def forum(request):
	return render(request, 'mammoth/forum.html')
	
def gallery(request):
    return render(request, 'mammoth/gallery.html', context={'all_patterns':Pattern.objects.all()})

def share_your_pattern(request):
    if request.method == 'POST':
        pattern_form = PatternForm(request.POST, request.FILES)

        if pattern_form.is_valid():
            if 'picture' in request.FILES:
                # user = request.user
                # pattern_form.picture = request.FILES['picture']
                # pattern_form.author = user
                # pattern_form.save()
                pattern = Pattern()
                pattern.title = pattern_form.cleaned_data['title']
                pattern.picture = request.FILES['picture']
                pattern.description = pattern_form.cleaned_data['description']
                pattern.author = request.user
                pattern.save()

            return render(request, 'mammoth/index.html', context={'pattern_uploaded':True})
        else:
            print(pattern_form.errors)
    else:
        pattern_form = PatternForm()
        user = request.user
    return render(request, 'mammoth/share_your_pattern.html', context={'pattern_form':pattern_form,'user':user})
	
def shop(request):
	return render(request, 'mammoth/shop.html')
	
def terms_and_conditions(request):
	return render(request, 'mammoth/terms_and_conditions.html')

def site_map(request):
	return render(request, 'mammoth/site_map.html')
	
def about_us(request):
	return render(request, 'mammoth/about_us.html')
	
def contact_us(request):
	return render(request, 'mammoth/contact_us.html')
	
def faq(request):
	return render(request, 'mammoth/faq.html')

def knit_kit(request):
    return render(request, 'mammoth/knit_kit.html')

#==============================================================
#====================== Comment function ======================
#==============================================================
def submit_comment(request):
    user = request.user
    text = request.POST.get('text','').strip() #''here means if there is nothing get from request, it will return ''
    rate = request.POST.get('rate',0)
    content_type = request.POST.get('content_type','')
    object_id = int(request.POST.get('object_id',''))
    model_class = ContentType.objects.get(model = content_type).model_class()
    model_obj = model_class.objects.get(pk = object_id)
    
    # if(isinstance(model_obj,'Pattern')):
    #     pattern_obj = Pattern(model_obj)
    #     commentList = Comment.objects.filter(object_id = pattern_obj.pk)

    #     pattern.avRate =
    #     pattern.save()
    
    #create a comment model
    comment = Comment() 
    comment.user = user
    comment.text = text
    comment.rating = rate
    comment.comment_type = model_class
    comment.content_object = model_obj
    comment.save()

    # Here: we can redirect the user to the page where they make comment
    # and if it cannot get previous page, it will redirect to mammoth:index
    refer = request.META.get("HTTP_REFERER","mammoth:index") 
        #for some special models (twittes? blog?) which might have comments for that model
    # , use this to show its comment
    # get all comment model : comments = Comment.objects.filter(object_id = pattern.pk )
    # and then return it to template page
    return redirect(refer)  

