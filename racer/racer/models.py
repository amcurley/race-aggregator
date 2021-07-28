from django.db import models


###########
# Race aggregator
# Scrape data from websites
# These posts will contain a title, date, and URL

class RaceTitle(models.Model):
    title = models.CharField(max_length=200)
    date = models.TextField()
    location = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.title
