from django.shortcuts import render
import requests

from .forms import SendForm
from .models import SessionText
from .models import SessionCount


def index(request):
    count_ses = SessionCount.objects.all().count()
    if request.method == "POST":
        # latest_ses = SubmitCount.objects.get(id=(count_ses - 1)).ret_int()
        latest_ses = count_ses - 1
        form = SendForm(request.POST, request.FILES)
        if form.is_valid():
            current_text = form.cleaned_data['q_text']
            response = requests.post('http://localhost:5005/webhooks/rest/webhook',
                                     json={"sender": "test_use", "message": current_text})
            json_response = response.json()
            json_r = json_response[0]
            current_answer = json_r["text"]
            t1 = SessionText(s_text=current_text, s_type="q", s_id=latest_ses, s_key=request.session.session_key)
            t2 = SessionText(s_text=current_answer, s_type="a", s_id=latest_ses, s_key=request.session.session_key)
            t1.save()
            t2.save()
            texts = SessionText.objects.filter(s_id=latest_ses)
            json_r["texts"] = texts
            json_r["form"] = form
            return render(request, '..\\templates\\index.html', json_r)
    else:
        if count_ses == 0:
            ses_count = SessionCount(s_count=0)
        else:
            latest_ses = count_ses - 1
            # latest_ses = SessionCount.objects.get(id=(count_ses - 1)).ret_int()
            ses_count = SessionCount(s_count=latest_ses + 1)
        ses_count.save()
        form = SendForm
    return render(request, '..\\templates\\index.html', {"form": form})
