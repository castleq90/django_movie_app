# django_movie_app

본 프로젝트는 미니콘다 가상환경 및 python=3.8 버전 django=2.2 버전을 사용하였습니다.

## api 명세

### Movie(영화) 리스트 조회 API

http://127.0.0.1:8000/movie/list?page=1 (Pagination (limit=10) 기능)  
http://127.0.0.1:8000/movie/list?page=1&year=2018   (연도 별 필터 기능)   
http://127.0.0.1:8000/movie/list?page=1&sort=-rating (별점 높은 순 정렬)  
http://127.0.0.1:8000/movie/list?page=1&sort=rating  (별점 낮은 순 정렬)  
http://127.0.0.1:8000/movie/list?title= (title={검색어} 입력 기능)

### Movie(영화) 디테일 조회 API
http://127.0.0.1:8000/movie/detail/1/ (영화 DetailView)  
http://127.0.0.1:8000/movie/list/ (영화 생성 /아래의 Json 형식으로 입력)
```py
{
  "title": "AAA",
  "year": "2016",
  "genres": "['Action', 'Adventure', 'Animation', 'Comedy', 'Family', 'Fantasy', 'Musical', 'Thriller']",
  "summary": "요약 내용"
}
```
### Movie Review(영화리뷰) API

http://127.0.0.1:8000/movie/review/1 (리뷰 Detail조회, 수정, 삭제 가능)   
http://127.0.0.1:8000/movie/review/ (리뷰 생성 /아래의 Json 형식으로 입력)
```py
{
    "movie": "51",
    "text": "힘내자 아자 아자",
    "rating": "9.0",
}
```
