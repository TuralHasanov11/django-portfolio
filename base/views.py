from django.shortcuts import render
import mimetypes
import os
from django.http.response import HttpResponse, FileResponse

from .models import *

contact = {
    'email' : 'hasanovtural11@gmail.com',
    'phone':'+994 51 3876332',
    'linkedin':'https://www.linkedin.com/in/tural-hasanov-1a5554204',
    'github':'https://github.com/TuralHasanov11',
}

education = [
    {
        'place':'Baku Higher Oil School',
        'title':'Bachelor in Process Automation Engineering',
        'dateFrom':'2017',
        'dateTo':'2022',
        'text':''
    },
    {
        'place':'Orient ITM',
        'title':'Web Development Student',
        'dateFrom':'February 2019',
        'dateTo':'August 2019',
        'text':'I took a 7-month full-stack web development course in Orient ITM training center. I was taught HTML5, CSS3, JavaScript, JQuery & Ajax for front-end programming, PHP for back-end, MySQL for database programming'
    }
]

def base(request):

    skills = Skill.objects.all()
    experience = Experience.objects.all()
    projects = Project.objects.order_by('-created_at').all().prefetch_related('technologies')

    return render(request, 'base/base.html',context={
        'skills':skills,
        'experience':experience,
        'projects':projects,
        'contact':contact,
        'education':education,
    })


def downloadCV(request):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    filename = 'Tural Hasanov DEV CV.pdf'

    filepath = BASE_DIR + '/static/files/' + filename
    
    return FileResponse(open(filepath, 'rb'))