from django.test import TestCase
from mammoth.models import Pattern, User, Comment
import os
from datetime import datetime
from django.conf import settings
import pytz
from django.db.models import Avg

class PatternMethodTests(TestCase): 

    def test_slug_line_creation(self):
        """
        Checks to make sure that when a pattern is created, an appropriate slug is created. 
        Example: "Random Pattern Name" should be "random-pattern-name".
        """
        user = User.objects.create(username='test_username', password='password')
        pattern = Pattern(title='Random Pattern Name', author=user)
        pattern.save()

        self.assertEqual(pattern.slug, 'random-pattern-name')

    def test_ensure_average_ratings_are_correct(self): 
        """ Ensures that all the average ratings of the patterns are between 0 and 5. """

        # Create a pattern
        user = User.objects.create(username='test_username', password='password')
        pattern = Pattern(title='test', author=user)
        pattern.save()
        
        # Create comments
        time = datetime(2019, 10, 3, 11, 30, 2, 0, tzinfo=pytz.UTC)
        for i in range(6):
            new_comment = Comment.objects.create(pattern=pattern, rating=str(i), text="Some text"+str(i), time=time, user=user)
            new_comment.save()

        # Get the average rating of all comments
        comments = Comment.objects.filter(pattern = pattern.pk)
        avg_rating = comments.aggregate(Avg('rating'))['rating__avg']

        self.assertEqual(( (avg_rating >= 0) and (avg_rating <= 5) ), True)

    def test_ensure_average_ratings_are_calculated_correctly(self): 
        """ Ensures that all the average ratings of the patterns are calculated correctly. """

        # Create a pattern
        user = User.objects.create(username='test_username', password='password')
        pattern = Pattern(title='test', author=user)
        pattern.save()
        
        # Create comments
        time = datetime(2019, 10, 3, 11, 30, 2, 0, tzinfo=pytz.UTC)
        
        for i in range(6):
            new_comment = Comment.objects.create(pattern=pattern, rating=str(i), text="Some text"+str(i), time=time, user=user)
            new_comment.save()

        # Get the average rating of all comments
        comments = Comment.objects.filter(pattern = pattern.pk)
        avg_rating = comments.aggregate(Avg('rating'))['rating__avg']

        self.assertEqual(avg_rating == sum(range(6))/len(range(6)), True)

    
