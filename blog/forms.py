from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Post

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'title',
            'slug',
            'text',
            'published_date',
            'image',
            Submit('submit', 'Submit', css_class='btn-success')
        )

    class Meta:
        model = Post
        fields = ('title', 'slug', 'text', 'published_date', 'image')
