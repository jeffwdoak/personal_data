

#import floppyforms.__future__ as forms
import django.forms as forms

from .models import Exercise


class ListTextWidget(forms.TextInput):
    """
    Widget to provide drop down menu plus free text input for data entry.

    """
    def __init__(self, data_list, name, *args, **kwargs):
        """Initialize TextInput with additional list of choices."""
        super(ListTextWidget, self).__init__(*args, **kwargs)
        self._name = name
        self._list = data_list
        self.attrs.update({'list':'list__%s' % self._name})

    def render(self, name, value, attrs=None):
        """Add datalist onto back of TextInput rendered html."""
        text_html = super(ListTextWidget, self).render(name, value, attrs=attrs)
        data_list = '<datalist id="list__%s">' % self._name
        for item in self._list:
            data_list += '<option value="%s">' % item
        data_list += '</datalist>'
        return text_html+data_list


class ExerciseForm(forms.ModelForm):
    template_name = 'exercise/exercise_form.html'
    #char_field_with_list = forms.CharField(required=True)
    #time = DateTimeField(widget=forms.SplitDateTimeWidget)
    def __init__(self, *args, **kwargs):
        default_list = ['one', 'two']
        self.exercise_list = kwargs.pop('exercise_list', default_list)
        self.unit_list = kwargs.pop('unit_list', default_list)
        super(ExerciseForm, self).__init__(*args, **kwargs)
        self.fields['exercise'].widget = ListTextWidget(data_list=self.exercise_list, name='exercise-list')
        self.fields['units'].widget = ListTextWidget(data_list=self.unit_list, name='unit-list')
    class Meta:
        model = Exercise
        fields = ['time', 'exercise', 'amount', 'weight', 'units', 'notes']
        #all_exercises = Exercise.objects.values('exercise').distinct()
        #all_exercises = [query['exercise'] for query in all_exercises]
        #all_exercises = ['one', 'two', 'three']
        widgets = {
                'time': forms.SplitDateTimeWidget,
                }



