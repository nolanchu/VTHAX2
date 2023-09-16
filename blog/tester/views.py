# from django.shortcuts import render, redirect
# from .forms import HealthSurveyForm
# from django.views.generic import TemplateView
# import json
# from .models import HealthSurvey

# def calculate_percentile(queryset, field_name, value):
#     filters = {f"{field_name}__lt": value}
#     count_below = queryset.filter(**filters).count()
#     total = queryset.count()


#     if total == 0:
#         return 0

#     return (count_below / total) * 100

# def health_survey(request):
#     if request.method == 'POST':
#         form = HealthSurveyForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('display_records')  # adjust as needed
#     else:
#         form = HealthSurveyForm()

#     return render(request, 'tester/health_survey_template.html', {'form': form})

# class DisplayRecordsView(TemplateView):
#     template_name = 'display_records_template.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Get latest survey
#         latest_survey = HealthSurvey.objects.latest('id')

#         # Calculate percentiles for latest survey
#         cigarettes_per_day_percentile = calculate_percentile(HealthSurvey.objects.exclude(id=latest_survey.id), "cigarettes_per_day", latest_survey.cigarettes_per_day)
#         exercise_per_week_percentile = calculate_percentile(HealthSurvey.objects.exclude(id=latest_survey.id), "exercise_per_week", latest_survey.exercise_per_week)
#         reaction_time_ms_percentile = calculate_percentile(HealthSurvey.objects.exclude(id=latest_survey.id), "reaction_time_ms", latest_survey.reaction_time_ms)
#         alcohol_per_week_percentile = calculate_percentile(HealthSurvey.objects.exclude(id=latest_survey.id), "alcohol_per_week", latest_survey.alcohol_per_week)
#         sitting_duration_per_day_percentile = calculate_percentile(HealthSurvey.objects.exclude(id=latest_survey.id), "sitting_duration_per_day", latest_survey.sitting_duration_per_day)

#         obj = latest_survey
#         context['data'] = json.dumps(
#             {
#                 'cigarettes': obj.cigarettes_per_day,
#                 'cigarettes_percentile': cigarettes_per_day_percentile,
#                 'exercise': obj.exercise_per_week.total_seconds(),
#                 'exercise_percentile': exercise_per_week_percentile,
#                 'reaction': obj.reaction_time_ms,
#                 'reaction_percentile': reaction_time_ms_percentile,
#                 'alcohol': obj.alcohol_per_week,
#                 'alcohol_percentile': alcohol_per_week_percentile,
#                 'sitting': obj.sitting_duration_per_day.total_seconds(),
#                 'sitting_percentile': sitting_duration_per_day_percentile,
#             }
#     )
#         return context

# def display_records(request):
#     # Get latest survey
#     latest_survey = HealthSurvey.objects.latest('id')

#     # Calculate percentiles for latest survey
#     cigarettes_per_day_percentile = calculate_percentile(HealthSurvey.objects.exclude(id=latest_survey.id), "cigarettes_per_day", latest_survey.cigarettes_per_day)
#     exercise_per_week_percentile = calculate_percentile(HealthSurvey.objects.exclude(id=latest_survey.id), "exercise_per_week", latest_survey.exercise_per_week)
#     reaction_time_ms_percentile = calculate_percentile(HealthSurvey.objects.exclude(id=latest_survey.id), "reaction_time_ms", latest_survey.reaction_time_ms)
#     alcohol_per_week_percentile = calculate_percentile(HealthSurvey.objects.exclude(id=latest_survey.id), "alcohol_per_week", latest_survey.alcohol_per_week)
#     sitting_duration_per_day_percentile = calculate_percentile(HealthSurvey.objects.exclude(id=latest_survey.id), "sitting_duration_per_day", latest_survey.sitting_duration_per_day)

#     # Get all data for template rendering as JSON
#     data = json.dumps(
#         [
#             {
#                 'cigarettes': obj.cigarettes_per_day,
#                 'cigarettes_percentile': cigarettes_per_day_percentile,
#                 'exercise': obj.exercise_per_week.total_seconds(),
#                 'exercise_percentile': exercise_per_week_percentile,
#                 'reaction': obj.reaction_time_ms,
#                 'reaction_percentile': reaction_time_ms_percentile,
#                 'alcohol': obj.alcohol_per_week,
#                 'alcohol_percentile': alcohol_per_week_percentile,
#                 'sitting': obj.sitting_duration_per_day.total_seconds(),
#                 'sitting_percentile': sitting_duration_per_day_percentile,
#             }
#             for obj in HealthSurvey.objects.all()
#         ]
#     )

#     return render(request, 'tester/display_records_template.html', {'records': records})
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import PersonInfoForm, HealthInfoForm, MiscInfoForm
from .models import PersonInfo, HealthInfo, MiscInfo

from django.core.serializers import serialize, deserialize

def step1(request):
    form = PersonInfoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            serialized_data = serialize('json', [form.instance])
            request.session['person_info'] = serialized_data
            return HttpResponseRedirect(reverse('step2'))
    return render(request, 'step1.html', {'form': form})

def step2(request):
    form = HealthInfoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            serialized_data = serialize('json', [form.instance])
            request.session['health_info'] = serialized_data
            return HttpResponseRedirect(reverse('step3'))
    return render(request, 'step2.html', {'form': form})
def step3(request):
    form = MiscInfoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            serialized_data = serialize('json', [form.instance])
            request.session['misc_info'] = serialized_data
            return HttpResponseRedirect(reverse('finished'))
            
            # request.session.clear()
            # return HttpResponseRedirect(reverse('finished'))
    return render(request, 'step3.html', {'form': form})
def last_in_gen(gen):
    data = None
    for obj in gen:
        data = obj.object
    return data
def finished(request):
    person_info = last_in_gen(deserialize('json', request.session.get('person_info')))
    health_info = last_in_gen(deserialize('json', request.session.get('health_info')))
    misc_info = last_in_gen(deserialize('json', request.session.get('misc_info')))
    print(person_info.__dict__, "a")
    print(health_info, "b")
    print(misc_info, "c")
    # for obj in deserialize('json', serialized_data):
        # person_info = obj.object
    return render(request, 'finished.html')
