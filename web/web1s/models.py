from django.db import models

class Baby(models.Model):
    """A topic the user is learning about"""
    name = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Stuff(models.Model):
    baby = models.ForeignKey(Baby, on_delete=None)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.name) > 50:
            return self.name[:50] + "..."
        else:
            return self.name


class Pussy(models.Model):
    baby = models.ForeignKey(Baby, on_delete=None)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'pussyplays'

    def __str__(self):
        if len(self.name) > 50:
            return self.name[:50] + "..."
        else:
            return self.name
