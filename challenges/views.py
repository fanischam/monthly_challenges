from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    'january': 'Eat no meat for the entire month',
    'february': 'Walk for at least 20 minutes a day',
    'march': 'Walk for at least 25 minutes a day',
    'april': 'Walk for at least 30 minutes a day',
    'may': 'Walk for at least 40 minutes a day',
}

# Create your views here.


def index(request):
    response_data = []
    months = list(monthly_challenges.keys())

    for month in months:
        month_path = reverse('month-challenge', args=[month])
        response_data.append(f'<h2><a href="{month_path}">{month}</a></h2>')

    return HttpResponse(response_data)


def monthly_challenge_by_num(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound(f'<h1>This month is not supported</h1>')
