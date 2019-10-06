import datetime

from django.shortcuts import render
from django.conf import settings
import os


def file_list(request, date=None):
    template_name = 'index.html'
    files_list = os.listdir(path=settings.FILES_PATH)
    context_files = []
    for file in files_list:
        statinfo = os.stat(path=f'{settings.FILES_PATH}/{file}')
        c_time = datetime.datetime.fromtimestamp(statinfo.st_ctime)
        m_time = datetime.datetime.fromtimestamp(statinfo.st_mtime)
        context_files.append({'name': file, 'ctime': c_time, 'mtime': m_time})

    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        'files': context_files,
        'date': date  # Этот параметр необязательный
    }

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    content = ''
    with open(f'{settings.FILES_PATH}/{name}', encoding='utf8') as f:
        for line in f:
            content += f'{line}'
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )

