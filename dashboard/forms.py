from django import forms
from datetime import datetime
from django.forms.widgets import DateTimeInput, Select, TextInput, Widget
import pytz
from .models import Review, Message


def get_now():
    return datetime.now(tz=pytz.timezone('Asia/Tehran')).strftime("%Y-%m-%d %H:%M:%S")


class NewTradeForm(forms.Form):
    symbol = forms.CharField(
        label='Symbol', max_length=200, required=True, strip=True, widget=forms.widgets.TextInput(attrs={
            'oninput': 'let p=this.selectionStart;this.value=this.value.toUpperCase();this.setSelectionRange(p, p);', 'id': 'symbol', 'spellcheck': 'False', 'class': 'text-center w-36 bg-color-darker m-2 p-2 text-gray-400 border-2 focus:border-blue-800 border-gray-700 border-opacity-60 rounded-3xl outline-none transition-all duration-200'}))

    date = forms.DateField(label="Date", widget=forms.widgets.DateInput(attrs={
        'type': 'date',  'spellcheck': 'False', 'class': 'text-center w-36 bg-color-darker p-2 m-2 text-gray-400 text-sm border-2 focus:border-blue-800 border-gray-700 border-opacity-60 rounded-3xl outline-none transition-all duration-200'}), initial=get_now)

    time = forms.TimeField(label="Time", widget=forms.widgets.TimeInput(attrs={
        'type': 'time',  'spellcheck': 'False', 'class': 'text-center w-36 bg-color-darker p-2 m-2 text-gray-400 border-2 focus:border-blue-800 border-gray-700 border-opacity-60 rounded-3xl outline-none transition-all duration-200'}), initial=get_now)

    price = forms.FloatField(widget=forms.widgets.NumberInput(attrs={
        'min':'0','spellcheck': 'False', 'class': 'text-center w-36 bg-color-darker m-2 p-2 text-gray-400 border-2 focus:border-blue-800 border-gray-700 border-opacity-60 rounded-3xl outline-none transition-all duration-200'}))

    side = forms.CharField(required=False, initial='Long',
                           widget=forms.widgets.TextInput(attrs={'id': 'SIDE', 'onclick': 'ChangeValueSide()', 'readonly': "readonly", 'class': 'leading-5 tracking-wider cursor-pointer bg-green-700 w-20 p-2 rounded-3xl text-center text-gray-200 outline-none '}))

    size = forms.FloatField(widget=forms.widgets.NumberInput(attrs={
        'min':'0','spellcheck': 'False', 'class': 'text-center w-36 bg-color-darker m-2 p-2 text-gray-400 border-2 focus:border-blue-800 border-gray-700 border-opacity-60 rounded-3xl outline-none transition-all duration-200'}))

    # leverage = forms.IntegerField(initial=1, widget=forms.widgets.NumberInput(attrs={
    #     'id': "slider", 'type': 'range', 'min': '1', 'max': '500', 'step': '1', 'oninput': "sliderChangeGet(this.value)", 'spellcheck': 'False', 'class': 'text-center w-36 bg-color-darker m-2 p-2 text-gray-400 border-2 focus:border-blue-800 border-gray-700 border-opacity-60 rounded-3xl outline-none transition-all duration-200'}))

    comment = forms.CharField(required=False, label="comment", widget=forms.widgets.TextInput(attrs={
        'class': 'text-center w-36 bg-color-darker m-2 p-2 text-gray-400 border-2 focus:border-blue-800 border-gray-700 border-opacity-60 rounded-3xl outline-none transition-all duration-200'}))


class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        fields = ['emotion', 'body']
        labels = {'emotion':'Place your emotion about this trade', 'body':'Explain your feeling .'}

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget = TextInput(attrs={
            'class' : 'my-4 border-2'
        })
        emotion_type = (('fear','Fear'),
               ('hope', 'Hope'),
               ('stress', 'Stress'),
               ('calm', 'Calm'),
               ('happy', 'Happy'),
               ('sad','Sad'))
        self.fields['emotion'].widget = Select(choices=emotion_type,attrs={
            'class' : 'my-4 bg-red-200 border-2'
        })

        
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'border border-gray-300'})