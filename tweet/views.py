from django.shortcuts import render
from tweet.pycode import readtweet


def index(request):
    return render(request, 'tweet/home.html', readtweet.getTweets('accenture', 10))


