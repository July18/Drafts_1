from django.db import models
import numpy as np
# Create your models here.
class Wine(models.Model):
    name = models.CharField(max_length=200)

    def average_rating(self):
        # all_ratings = map(lambda x: x.rating,self.review_set.all())
        all_ratings = []
        for review in self.review_set.all():
            all_ratings.append(review.rating)
        return np.mean(all_ratings)

    def __str__(self):
        # 默认使用哪个属性，显示模型的简单表示
        return self.name

class Review(models.Model):
    RATING_CHOICES = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    )
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
