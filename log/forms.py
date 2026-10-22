from django import forms
from .models import Log, Idea, Post

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['problem_name', 'what_i_didnt_know', 'solution', 'takeaway']
        widgets = {
            'problem_name': forms.TextInput(attrs={'class': 'w-full p-2 rounded text-black mb-4'}),
            'what_i_didnt_know': forms.Textarea(attrs={'class': 'w-full p-2 rounded text-black mb-4', 'rows': 3}),
            'solution': forms.Textarea(attrs={'class': 'w-full p-2 rounded text-black mb-4', 'rows': 3}),
            'takeaway': forms.Textarea(attrs={'class': 'w-full p-2 rounded text-black mb-4', 'rows': 2}),
        }

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'text', 'acted_on_it', 'is_it_bs']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 rounded text-black mb-4'}),
            'text': forms.Textarea(attrs={'class': 'w-full p-2 rounded text-black mb-4', 'rows': 3}),
            'acted_on_it': forms.CheckboxInput(attrs={'class': 'ml-2 mb-4 h-5 w-5'}),
            'is_it_bs': forms.CheckboxInput(attrs={'class': 'ml-2 mb-4 h-5 w-5'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'formatting']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 rounded text-black mb-4'}),
            'text': forms.Textarea(attrs={'class': 'w-full p-2 rounded text-black mb-4', 'rows': 6}),
            'formatting': forms.Select(attrs={'class': 'w-full p-2 rounded text-black mb-4'}),
        }
