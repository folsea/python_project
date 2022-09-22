from django.db import models


# Creates model of University Campuses
class UniversityCampus(models.Model):
    Campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    State = models.CharField(max_length=2, default="", blank=True, null=False)
    Campus_ID = models.IntegerField(default="", blank=True, null=False)

    #Creats model manager
    object = models.Manager()

    # Displays the object values in the form of a string
    def __str__(self):
        # Returns the input values of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_Campus = '{0.Campus_name}: {0.State}'
        return display_Campus.format(self)

    # Reomoves added 's' that Djangp adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"


