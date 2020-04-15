from django import forms
from .models import Review, RatingStar, Rating

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['name', 'email', 'text']


class RatingForm(forms.ModelForm):
	star = forms.MoelChoiceField(
		queryset = RatingStar.objects.all(),
		widget = forms.RadioSelect(),
		empty_label = None
		)

	class Meta:
		model = Rating
		fields = ['star',]