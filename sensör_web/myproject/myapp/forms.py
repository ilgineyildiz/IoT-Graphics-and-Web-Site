from django import forms

class DataOptionsForm(forms.Form):
    
    EXAMPLE_CHOICES = [
        ('Compare temperature data from three different days', 'Compare temperature data from three different days'),
        ('Plot temperature and wind speed on two different y-axes', 'Plot temperature and wind speed on two different y-axes'),
        ('Visualize correlation between temperature and humidity', 'Visualize correlation between temperature and humidity'),
        ('Use a histogram to understand variation in data', 'Use a histogram to understand variation in data')
    ]
    example = forms.ChoiceField(choices=EXAMPLE_CHOICES)
