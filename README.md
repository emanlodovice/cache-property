# cache-property
A django model property decorator for caching the data returned by the decorated model property.


![screen shot](http://i.imgur.com/cDrSHL7.png)

## sample usage

```python
from django.db import models

from cache_property import cache_property


class Profile(models.Model):
    full_name = models.CharField(max_length=50)
    bio = models.TextField()

    @property
    def project_count(self):
        return self.projects.count()

    @property
    @cache_property(base_key='profile-')
    def cached_project_count(self):
        return self.projects.count()

    def __unicode__(self):
        return self.full_name


class Project(models.Model):
    owner = models.ForeignKey(Profile, related_name='projects')
    title = models.CharField(max_length=50)

    def owner_name(self):
        return self.owner.full_name

    def __unicode__(self):
        return self.title

```
