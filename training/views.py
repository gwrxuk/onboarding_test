from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from training.models import do_training
import random

# Create your views here.
def leaderboard(request):
    samples = []

    for i in range(0, 4):
        r = lambda: random.randint(0,255)
        samples.append({"name": "User %s" % chr(i+65), "score": do_training(), "rank": i,  "color": "#%02X%02X%02X" % (r(),r(),r())})

    samples = sorted(samples, key=lambda x: -1*x["score"])
    
    for i in range(0, len(samples)):
        samples[i]["rank"] = 4-i;

    return render(request, 'leaderboard.html', {
        'samples': samples,
    })