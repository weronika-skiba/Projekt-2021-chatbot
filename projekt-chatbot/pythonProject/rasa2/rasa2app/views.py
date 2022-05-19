from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests

from .forms import SendForm
from .models import Question
from .models import Answer
from .models import SubmitCount


def index2(request):
    if request.method == "POST":
        form = SendForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            current_text = form.cleaned_data['q_text']
            response = requests.post('http://localhost:5005/webhooks/rest/webhook',
                                     json={"sender": "test_use", "message": current_text})
            json_response = response.json()
            json_r = json_response[0]
            a = Answer(a_text=json_r["text"])
            a.save()
            count_a = Answer.objects.all().count()
            count_q = Question.objects.all().count()
            latest_a = Answer.objects.get(id=(count_a - 1)).ret_string
            latest_q = Question.objects.get(id=(count_q - 1)).ret_string
            s_latest_a = Answer.objects.get(id=(count_a - 2)).ret_string
            s_latest_q = Question.objects.get(id=(count_q - 2)).ret_string
            json_r["s_latest_a"] = s_latest_a
            json_r["s_latest_q"] = s_latest_q
            json_r["latest_a"] = latest_a
            json_r["latest_q"] = latest_q
            json_r["form"] = form
            json_r["current_text"] = current_text
            return render(request, '..\\templates\\index.html', json_r)
    else:
        form = SendForm

    return render(request, '..\\templates\\index.html', {"form": form})


def index(request):
    if request.method == "POST":
        form = SendForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            current_text = form.cleaned_data['q_text']
            response = requests.post('http://localhost:5005/webhooks/rest/webhook',
                                     json={"sender": "test_use", "message": current_text})
            json_response = response.json()
            json_r = json_response[0]
            current_answer = json_r["text"]
            a = Answer(a_text=current_answer)
            a.save()
            count_s = SubmitCount.objects.all().count()
            latest_s_c = SubmitCount.objects.get(id=(count_s - 1)).ret_int() + 1
            submit_c = SubmitCount(s_count=latest_s_c)
            submit_c.save()
            if(latest_s_c == 1):
                text1 = current_text
                text2 = current_answer
                text3 = ""
                text4 = ""
                text5 = ""
                text6 = ""
            if (latest_s_c >= 2):
                count_a = Answer.objects.all().count()
                count_q = Question.objects.all().count()
                latest_a = Answer.objects.get(id=(count_a - 1)).ret_string
                latest_q = Question.objects.get(id=(count_q - 1)).ret_string
                if (latest_s_c == 2):
                    text1 = latest_q
                    text2 = latest_a
                    text3 = current_text
                    text4 = current_answer
                    text5 = ""
                    text6 = ""
                else:
                    text1 = Question.objects.get(id=(count_q - 2)).ret_string
                    text2 = Answer.objects.get(id=(count_a - 2)).ret_string
                    text3 = latest_q
                    text4 = latest_a
                    text5 = current_text
                    text6 = current_answer

            json_r["text1"] = text1
            json_r["text2"] = text2
            json_r["text3"] = text3
            json_r["text4"] = text4
            json_r["text5"] = text5
            json_r["text6"] = text6
            json_r["form"] = form
            return render(request, '..\\templates\\index.html', json_r)
    else:
        s_count = SubmitCount(s_count=0)
        s_count.save()
        form = SendForm
    return render(request, '..\\templates\\index.html', {"form": form})
