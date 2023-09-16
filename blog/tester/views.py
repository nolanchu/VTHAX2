from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import json

def calculate_percentile(queryset, field_name, latest_survey):
    if not str(latest_survey.data[field_name]).isdecimal():
        return -1
    total = queryset.count()
    count_below = 0
    for e in queryset:
        if e.data[field_name] < latest_survey.data[field_name]:
            count_below += 1
    if total == 0:
        return 1
    return (count_below / total) * 100

class DisplayRecordsView(TemplateView):
    template_name = 'display_records_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get latest survey
        latest_survey = MyModel.objects.latest('id')
        print(latest_survey.data)
        percentiles = {}
        for attribute in latest_survey.data:
            percentiles[attribute] = calculate_percentile(MyModel.objects.exclude(id=latest_survey.id), attribute, latest_survey)

        context['data'] = json.dumps(percentiles)
        return context

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import PersonInfoForm, MiscInfoForm
from .models import PersonInfo, MiscInfo, MyModel

from django.core.serializers import serialize, deserialize

models = ['PersonInfo', "ConsumptionInfo", 'PhysicalActivityInfo', 'BiologicalInfo', 'MentalHealth', 'MiscInfo']
from .forms import *
def step(request, step_num):
    step_num = int(step_num)
    form = eval(f"{models[step_num]}Form")(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            serialized_data = serialize('json', [form.instance])
            request.session[models[step_num]] = serialized_data
            return HttpResponseRedirect(f'{step_num+1}')
        else:
            print(form.errors)
            print("nogood")
    return render(request, f'step{step_num}.html', {'form': form})
def last_in_gen(gen):
    data = None
    for obj in gen:
        data = obj.object
    return data
import json
def finished(request):
    all_fields = {}
    for string in models:
        all_fields.update(json.loads(request.session.get(string))[0]['fields'])
    m = MyModel(data=all_fields)
    m.save()
    return render(request, 'finished.html')
