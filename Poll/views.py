from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import openpyxl
import os


def poll(request):
    return render(request, '../templates/PollApp/poll.html')

@csrf_exempt
@require_POST
def save(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        old = request.POST.get('old')
        question1 = request.POST.get('question1')
        question2 = request.POST.get('question2')
        question3 = request.POST.get('question3')
        question4 = request.POST.get('question4')
        question5 = request.POST.get('question5')
        question6 = request.POST.get('question6')
        question7 = request.POST.get('question7')
        question8 = request.POST.get('question8')
        question9 = request.POST.get('question9')
        question10 = request.POST.get('question10')
        question11 = request.POST.get('question11')
        
        excel_path = 'anket_sonuclari.xlsx'
        if os.path.exists(excel_path):
            workbook = openpyxl.load_workbook(excel_path)
            sheet = workbook.active
            sheet.append([id, name, gender, old, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11])
        else:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(["ID", "Ad Soyad", "Cinsiyet", "Yaş", "Soru 1", "Soru 2", "Soru 3", "Soru 4", "Soru 5", "Soru 6", "Soru 7", "Soru 8", "Soru 9", "Soru 10", "Soru 11"])
            sheet.append([id, name, gender, old, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11])
        
        workbook.save(excel_path)
        
        return render(request, '../templates/PollApp/poll.html')