from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import ReportForm
from .models import Report, ReportItemEvaluation
import json


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('report_create')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

@login_required(login_url='login')
def report_create_view(request):
    from .models import Location
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            
            # Save individual items from evaluation_data
            eval_data_raw = request.POST.get('evaluation_data')
            if eval_data_raw:
                try:
                    evaluations = json.loads(eval_data_raw)
                    for item_name, data in evaluations.items():
                        # data can be a string (old format) or dict (new format)
                        if isinstance(data, dict):
                            status = data.get('status')
                        else:
                            status = data
                            
                        if status:
                            ReportItemEvaluation.objects.create(
                                report=report,
                                item_name=item_name,
                                status=status
                            )
                except json.JSONDecodeError:
                    pass
            
            return redirect('success')
        else:
            print(f"Form Errors: {form.errors}")
    else:
        form = ReportForm()
    
    # Build dynamic location mapping from database
    locations = Location.objects.all()
    location_mapping = {}
    for loc in locations:
        if loc.region not in location_mapping:
            location_mapping[loc.region] = {}
        if loc.site_type not in location_mapping[loc.region]:
            location_mapping[loc.region][loc.site_type] = []
        location_mapping[loc.region][loc.site_type].append(loc.name)
    
    context = {
        'form': form,
        'location_mapping_json': json.dumps(location_mapping, ensure_ascii=False)
    }
    return render(request, 'core/report_form.html', context)

def success_view(request):
    return render(request, 'core/success.html')
