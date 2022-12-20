from django.forms import ModelForm
from .models import Comment










class CommentFrom(ModelForm):
    class Meta:
        model= Comment
        fields('name','email','content','activate')
    