from django.shortcuts import render
from dotenv import load_dotenv
import requests
import json
import os



def configure():
    load_dotenv()

def home(request):
    configure()
    if request.method == 'POST':
        search = request.POST['search']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + search, headers={'X-Api-Key': os.getenv('API_KEY')})
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Sorry! There was an error!"
            print(e)
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'search': 'Please enter a valid search'})
