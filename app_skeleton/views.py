#######
#
#   Django imports
#
####### 
from django import forms
from django.shortcuts import render, HttpResponse
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required


#######
#
#   Stdlib etc.. imports
#
#######
from wsgiref.util import FileWrapper
import glob
import pandas as pd
import datetime
import random
import os
import re

#######
#
#   This project imports
#
#######
import app_skeleton.helpers as helpers
import app_skeleton.unique_to_this_project as uttp


#######
#
#   Paths
#
#######
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIRECTORY = os.path.join(BASE_DIR, 'UPLOAD')


#######
#
#   Forms
#
#######
class UploadFileForm(forms.Form):
    file_1 = forms.FileField()
    file_2 = forms.FileField()
    #input_1 = forms.CharField(label='Some input field 1', max_length=100)
    #input_2 = forms.CharField(label='Some input field 2', max_length=100)


#######
#
#   Views
#
#######
@login_required
def first_page(request):
    if request.method == 'POST':
        upload_form = UploadFileForm(request.POST, request.FILES)
        if upload_form.is_valid():
            temp_directory = helpers.save_uploaded_files(request, UPLOAD_DIRECTORY)
            preliminary_results = uttp.produce_preliminary_results()
            return render(request,'second_page.html', {'results': preliminary_results, 'temp_directory': temp_directory})

    elif request.method == 'GET':
        helpers.remove_temp_files(UPLOAD_DIRECTORY)
        upload_form = UploadFileForm()
    
    return render(request, 'first_page.html',{'upload_form':upload_form})


@login_required
def second_page(request):
    param_1 = request.GET.get('param_1',None)
    param_2 = request.GET.get('param_2',None)
    temp_directory = request.GET.get('temp_directory',None)
    final_results = uttp.produce_final_results()
    return render(request,'last_page.html', {'results':final_results, 'temp_directory': temp_directory})

@login_required
def download_cleaned_file(request):
    wrapper = FileWrapper(open(os.path.join(UPLOAD_DIRECTORY, 'cleaned.csv'), "rb" ))
    response = HttpResponse(wrapper, content_type='application/csv')
    response['Content-Disposition'] = 'attachment; filename=CleanedList.csv'
    return response
