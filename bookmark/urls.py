from django.urls import path
from .views import *

urlpatterns = [
    # http://127.0.0.1/bookmark/ 까지는 config의 url.py에서 1차 필터링 되고
    # 그 이후값이 여기서 해석된다.
    path("",BookmarkListView.as_view(), name="list"),
    #as_view()는 제네릭뷰를 함수형뷰로 변환시켜 준다.
    path("add/", BookmarkCreateView.as_view(), name="add"),
    #name 은 나중에 template에서 이 주소 패턴을 불러오는데 사용한다.
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name = 'update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]

