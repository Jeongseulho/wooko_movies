from django.urls import path

from . import views

app_name = 'community'
urlpatterns = [
    # # review
    # path('articles/', views.article_list),  # 모든 게시글 목록 조회
    # # 단일 게시글 조회 (수정삭제도 포함되어야할텐데 묻기가 싫음)
    # path('article/<int:article_pk>/', views.article_detail),
    # path('article/', views.article_create),  # 게시글 작성하기
    # path('article/<int:article_pk>/', views.article_update),  # 게시글 수정하기
    # path('article/<int:article_pk>/', views.article_delete),  # 게시글 삭제하기
    # path('<int:article_pk>/', views.comment_create),  # 댓글 작성하기
    # path('<int:article_pk>/comment/', views.comment_update),  # 댓글 수정하기
    # path('<int:article_pk>/comment/', views.comment_delete),  # 댓글 삭제하기
]