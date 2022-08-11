from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime
from news.models import Heading, Posts, Like, Comments
from accounts.models import User


def all_cat(request):
    all_categories = Heading.objects.all()
    return { 'cat': all_categories}


def get_weather(request):
    url = {'Киев': 'https://pogoda.co.il/ukraine/kiev', 'Лондон': 'https://pogoda.co.il/united_kingdom/london', 'Барселона': 'https://pogoda.co.il/spain/barcelona'}

    data = []

    for key, value in url.items():
        dic = {}
        page = requests.get(value)
        if page.status_code==200:
            soup = BeautifulSoup(page.text, "html.parser")
            allNews = soup.findAll('div', class_='now_block')
            picture = soup.findAll('img', class_='photo')
            url = str(picture[0]).split('<img alt="" class="photo" src="')
            picture = url[1].split('"/>')
            temp = str(soup.strong.text)
            all_data = str(BeautifulSoup(allNews[0].text, "html.parser"))
            all_data = all_data.split('\n\nОтметить Мой город\n\xa0\xa0')
            ful = 'https://pogoda.co.il' + picture[0]
            
            dic = {'city': key, 'pictures': ful, 'temperature': temp, 'all': all_data[1]}
            data.append(dic)
        else:
            continue
        date = datetime.now().date()
    return {'data': data, 'date': date}


def dashboard(request):
    ussss = User.objects.all()
    all_users = ussss.count()
    all_posts = Posts.objects.all().count()
    all_likes = Like.objects.all().count()
    all_comments = Comments.objects.all().count()

    count = 0
    now_date = datetime.now()
    now_date = now_date.replace(tzinfo=None)
    for i in ussss:
        if i.username:
            continue
        i = i.date_joined.replace(tzinfo=None)
        a = now_date - i
        if a.days < 7:
            count+=1
    return {'dash_users': all_users-1, 'dash_reg': count, 'dash_posts': all_posts, 'dash_likes': all_likes, 'dash_comments': all_comments}