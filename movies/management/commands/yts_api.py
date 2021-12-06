import requests
import json

from django.core.management.base import BaseCommand

from movies.models import Movie

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        api_url = 'https://yts.mx/api/v2/list_movies.json?sort_by=download_count&limit=50'
        data = requests.get(api_url)
        json_data = json.loads(data.text)

        for data in json_data['data']['movies']:
            Movie.objects.create(
                title   = data.get('title'),
                year    = data.get('year'),
                rating  = data.get('rating'),
                genres  = data.get('genres'),
                summary = data.get('summary'),
            )
