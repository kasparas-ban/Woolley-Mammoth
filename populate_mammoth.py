import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'woolly_mammoth.settings')

import django
django.setup()
from mammoth.models import Pattern, UserProfile, User, Comment
from django.conf import settings
from datetime import datetime
from django.contrib.contenttypes.models import ContentType
import pytz

def populate():
    # === Creating users =======================================================================================

    users = [
        {'username':"MrKnitter", 'picture':os.path.join(settings.BASE_DIR, 'media', 'profile_images', 'mr_knitter.jpg')},
        {'username':"Woolly", 'picture':os.path.join(settings.BASE_DIR, 'media', 'profile_images', 'woolly.jpg')},
        {'username':"Glasgow Grandma", 'picture':os.path.join(settings.BASE_DIR, 'media', 'profile_images', 'glasgow_grandma.jpg')},
        {'username':"Sandy", 'picture':os.path.join(settings.BASE_DIR, 'media', 'profile_images', 'sandy.jpg')},
        {'username':"Nicolas", 'picture':os.path.join(settings.BASE_DIR, 'media', 'profile_images', 'nicolas.jpg')},
        {'username':"Old Hag", 'picture':os.path.join(settings.BASE_DIR, 'media', 'profile_images', 'old_hag.jpg')},
        {'username':"Your Niece", 'picture':os.path.join(settings.BASE_DIR, 'media', 'profile_images', 'your_niece.jpg')},
        {'username':"Karen", 'picture':os.path.join(settings.BASE_DIR, 'media', 'profile_images', 'karen.jpg')},
        {'username':"Cinderella", 'picture':os.path.join(settings.BASE_DIR, 'media', 'profile_images', 'cinderella.jpg')}
    ]

    for u in users:
        add_user(u['username'], u['picture'])

    # === Creating patterns ======================================================================================

    comments = [
        {'user':users[0], 'rating':5, 'time':datetime(2019, 10, 3, 11, 30, 2, 0, tzinfo=pytz.UTC), 'comment':
            "I love this patttern! I have to say, I put off knitting for a long time now, \
            but seeing this pattern inspired me to come back to it!"},

        {'user':users[1], 'rating':3, 'time':datetime(2018, 12, 4, 14, 22, 45, 0, tzinfo=pytz.UTC), 'comment':
            "I guess it's alright."},

        {'user':users[2], 'rating':2, 'time':datetime(2019, 6, 12, 20, 11, 7, 0, tzinfo=pytz.UTC), 'comment':
            "The pattern is too basic. I've seen way better ones."},

        {'user':users[3], 'rating':5, 'time':datetime(2020, 1, 3, 21, 14, 55, 0, tzinfo=pytz.UTC), 'comment':
            "This pattern is so cool! This is exactly the kind of quality content I signed up for."},

        {'user':users[4], 'rating':4, 'time':datetime(2020, 3, 14, 15, 19, 17, 0, tzinfo=pytz.UTC), 'comment':
            "It’s my first time seeing a knitting pattern. I guess it's alright."},
        
        {'user':users[5], 'rating':1, 'time':datetime(2019, 9, 9, 23, 59, 59, 0, tzinfo=pytz.UTC), 'comment':
            "Sloppy work. Get good or don't post your garbage rags."},

        {'user':users[6], 'rating':5, 'time':datetime(2020, 2, 29, 6, 15, 1, 0, tzinfo=pytz.UTC), 'comment':
            "I've never seen such a wonderful pattern in my whole life. Thank you for showing me a whole new form of fiber art."},

        {'user':users[7], 'rating':2, 'time':datetime(2018, 10, 19, 10, 22, 40, 0, tzinfo=pytz.UTC), 'comment':
            "The pattern looks too complicated. It's straining my eyes just to look at it."},

        {'user':users[8], 'rating':5, 'time':datetime(2018, 7, 18, 13, 15, 1, 0, tzinfo=pytz.UTC), 'comment':
            "What a wonderful pattern! I'd love to use it to knit socks for my cat."}
    ]

    patterns = [
        {'title':'Pattern 1', 'picture':os.path.join(settings.BASE_DIR, 'media', 'pattern_images', 'pattern_1.jpg'),
         'comments':comments[:3], 'author':users[6], 'description':
            "It's a quick pattern I did in my spare time."},

        {'title':'Pattern 2', 'picture':os.path.join(settings.BASE_DIR, 'media', 'pattern_images', 'pattern_2.jpg'),
         'comments':comments[3:4], 'author':users[2], 'description':
            "Easy pattern that doesn't require much time to make."},

        {'title':'Pattern 3', 'picture':os.path.join(settings.BASE_DIR, 'media', 'pattern_images', 'pattern_3.jpg'),
         'comments':comments[4:6], 'author':users[1], 'description':
            "An expertly knitted pattern from yours truly."},

        {'title':'Pattern 4'[1:3], 'picture':os.path.join(settings.BASE_DIR, 'media', 'pattern_images', 'pattern_4.jpg'),
         'comments':comments, 'author':users[1], 'description':
            "Beautiful pattern that anyone can knit."},

        {'title':'Pattern 5', 'picture':os.path.join(settings.BASE_DIR, 'media', 'pattern_images', 'pattern_5.jpg'),
         'comments':comments[7], 'author':users[1], 'description':
            "A simple retro style pattern that looks good on everyone."},

        {'title':'Pattern 6', 'picture':os.path.join(settings.BASE_DIR, 'media', 'pattern_images', 'pattern_6.jpg'),
         'comments':comments[8:9], 'author':users[1], 'description':
            "A three dimensional pattern for exquisite look."},

        {'title':'Pattern 7', 'picture':os.path.join(settings.BASE_DIR, 'media', 'pattern_images', 'pattern_7.jpg'),
         'comments':comments[2:5], 'author':users[1], 'description':
            "A fun pattern for children."},

        {'title':'Pattern 8', 'picture':os.path.join(settings.BASE_DIR, 'media', 'pattern_images', 'pattern_8.jpg'),
         'comments':comments[1:6], 'author':users[1], 'description':
            "Yet another pattern."},
        
        {'title':'Pattern 9', 'picture':os.path.join(settings.BASE_DIR, 'media', 'pattern_images', 'pattern_9.jpg'),
         'comments':comments[6:9], 'author':users[1], 'description':
            "Just another pattern that I knitted in my spare time."}
    ]

    for pattern in patterns:
        add_pattern_and_comments(pattern['title'], pattern['picture'], pattern['description'], pattern['author'], pattern['comments'])

def add_pattern_and_comments(title, picture, description, author, comments):

    auth = User.objects.get(username=author['username'])
    p = Pattern.objects.get_or_create(title=title, author=auth)[0]
    p.picture = picture
    p.description = description

    try:
        auth = User.objects.get(username=author['username'])
        p = Pattern.objects.get_or_create(title=title, author=auth)[0]
        p.picture = picture
        p.description = description

        # Create comments for the pattern
        for c in comments:
            try:
                comment_author = User.objects.get(username=c['user']['username'])
                new_comment = Comment.objects.get_or_create(pattern=p, rating=c['rating'], text=c['comment'], time=c['time'], user=comment_author)
                new_comment.save()
            except:
                print("This comment already exists.")
                
        p.save()
        return p
    except:
        print("This pattern already exist.")


def add_user(username, picture):
    try:
        new_user = User.objects.get_or_create(username=username, password="password")[0]
        user_profile = UserProfile.objects.get_or_create(user=new_user, picture="")[0]
        user_profile.picture = picture
        user_profile.save()
        print("Added user: ", username)
        return user_profile
    except:
        print("The user ", username," already exist.")

if __name__ == '__main__':
    print('Starting Mammoth population script...')
    populate()
