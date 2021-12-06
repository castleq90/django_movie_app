from django.http import Http404
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from .serializers import MovieSerializer
from movies.models import Movie

class MovieList(APIView):

    def get(self, request):

        year  = str(request.GET.get('year', None))       # 연도별 필터 기능
        sort  = str(request.GET.get('sort', 'id'))       # 별점 정렬 (sort의 값이 들어오지 않으면 id순서 정렬)
        title = request.GET.get('title', None)
        page  = int(request.GET.get('page', 1))          # pagination


        PAGE_SIZE = 10
        limit     = PAGE_SIZE * page
        offset    = limit - PAGE_SIZE

        # Q객체를 이용한 별점순 정렬
        q = Q()

        if year != str(None):       # year(o) True 반환 <-> year(x) False 반환
            q = Q(year=year)

        if title != None:
            q = Q(title__icontains=title)

        if year != str(None) and title != None:
            q = Q(year=year) & Q(title__icontains=title)

        movies     = Movie.objects.filter(q).order_by(sort)[offset:limit]
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
