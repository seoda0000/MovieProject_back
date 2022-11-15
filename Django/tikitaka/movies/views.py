# from django.shortcuts import render
# from rest_framework.response import Response
from django.http.response import JsonResponse


import requests



API_KEY = '90948a33935bf9b9275c46d36a90412c'


# 인기 영화 목록 가져오기
def popular_movie(request):
    payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'region': 'KR'
        }
    url = 'https://api.themoviedb.org/3/movie/popular'
    r = requests.get(url, params=payload)
    rdata = r.json()['results']
    return JsonResponse(rdata, safe=False) 


# 상위 영화 목록 가져오기
def top_rated_movie(request):
    payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'page': 1,
        'region': 'KR'
        }
    url = 'https://api.themoviedb.org/3/movie/top_rated'
    r = requests.get(url, params=payload)
    rdata = r.json()['results']
    return JsonResponse(rdata, safe=False)


# 상영 중인 영화 목록 가져오기
def now_playing_movie(request):
    payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'region': 'KR',
        'page': 1,
        }
    url = 'https://api.themoviedb.org/3/movie/now_playing'
    r = requests.get(url, params=payload)
    rdata = r.json()['results']
    return JsonResponse(rdata, safe=False)



# 상영 중인 영화 예고편 목록 가져오기
def now_playing_movie_video(request):

    # 상영 중인 영화 목록 가져오기
    p_payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'region': 'KR',
        'page': 1,
        }
    url = 'https://api.themoviedb.org/3/movie/now_playing'
    r = requests.get(url, params=p_payload)
    rdata = r.json()['results']

    video_list = []

    for data in rdata:
        title = data['title']
        backdrop_path = data['backdrop_path']
        movie_id = str(data['id'])
        video_payload = {
            'api_key': API_KEY,
            'language': 'ko-KR',
        }
        video_url = 'https://api.themoviedb.org/3/movie/' + movie_id + '/videos'
        video_r = requests.get(video_url, params=video_payload)
        video_rdata = video_r.json()['results']
        if video_rdata:
            if str(type(video_rdata)) == "<class 'list'>":
                video_rdata = video_rdata[0]
            video_rdata['title'] = title
            video_rdata['backdrop_path'] = backdrop_path
            
            video_list.append(video_rdata)

    return JsonResponse(video_list, safe=False)


# 키워드로 영화 검색
def search_movie(request):

    # 검색 키워드
    search_input = input()
    p = 1
    search_result = []

    # 영화 검색
    while True:
        p_payload = {
            'api_key': API_KEY,
            'language': 'ko-KR',
            'page': p,
            'include_adult': 'true',
            'query': search_input,
            # 'region': # 지역 설정 가능 ex. KR
            }
        url = 'https://api.themoviedb.org/3/search/movie'
        r = requests.get(url, params=p_payload)
        rdata = r.json()['results']

        if rdata:
            search_result += rdata
            p += 1
        else:
            break

    return JsonResponse(search_result, safe=False)


# 영화인 검색
def search_movie_people(request):

    # 검색 키워드
    search_input = input()
    p = 1
    search_result = []

    # 영화인 검색
    while True:
        payload = {
            'api_key': API_KEY,
            'language': 'ko-KR',
            'page': p,
            'include_adult': 'true',
            'query': search_input,
            # 'region': 'KR',
            }
        url = 'https://api.themoviedb.org/3/search/person'
        r = requests.get(url, params=payload)
        rdata = r.json()['results']

        if rdata:
            search_result += rdata
            p += 1
        else:
            break

    return search_result