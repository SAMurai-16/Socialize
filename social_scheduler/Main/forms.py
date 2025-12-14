from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Telegram, Reddit, ContentTemplate





class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email', 'password1','password2')



class TelegramForm(forms.ModelForm):
    class Meta:
        model = Telegram
        fields = ('BOT_id','chat_id','photo','content', 'scheduled_time',)
        widgets = {
            'scheduled_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            })
        }



class RedditForm(forms.ModelForm):
    class Meta:
        model = Reddit
        fields= ('subreddit_name','title','body','photo','scheduled_time')
        widgets = {
            'scheduled_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            })
        }




class CustomLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
    )


class ContentTemplateForm(forms.ModelForm):
    class Meta:
        model = ContentTemplate
        fields = [
            'content_type', 'topic', 'audience', 
            'tone', 'style', 'keywords', 
            'length', 'format', 'objective'
        ]
        widgets = {
            'content_type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select content type'
            }),
            'topic': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'What is the main topic or subject matter?',
                'rows': 3
            }),
            'audience': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Who is this content for?',
                'rows': 2
            }),
            'tone': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select tone'
            }),
            'style': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Any specific style requirements? (e.g., conversational, technical, storytelling)',
                'rows': 2
            }),
            'keywords': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter keywords or phrases (comma-separated)',
                'rows': 2
            }),
            'length': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., 500 words, 280 characters, 3 paragraphs'
            }),
            'format': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Any formatting requirements? (e.g., bullet points, headings, Q&A)',
                'rows': 2
            }),
            'objective': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'What should this content achieve? (e.g., inform, persuade, entertain, CTA)',
                'rows': 3
            })
        }
        labels = {
            'content_type': 'Content Type',
            'topic': 'Topic/Subject',
            'audience': 'Target Audience',
            'tone': 'Tone',
            'style': 'Writing Style',
            'keywords': 'Keywords/Phrases',
            'length': 'Length',
            'format': 'Format',
            'objective': 'Content Objective'
        }
        

