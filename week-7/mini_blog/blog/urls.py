
from django.urls import path

from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='posts'),
    path('blogs/<slug:slug>', views.BlogView.as_view(), name='post-detail'),
    path('blogger/', views.AuthorListView.as_view(), name='authors'),
    path('blogger/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    # path('blogs/<slug:slug>/create', views.CommentFormView.as_view(), name='add-comment'),
]

urlpatterns += [
    path('blogger/<slug:slug>/update', views.AuthorUpdateView.as_view(), name='author-update'),
]

urlpatterns += [
    path('blogger/<slug:slug>', views.AuthorProfileView.as_view(), name='author-profile'),
]

urlpatterns += [
    path('blogs/<slug:slug>/toggle-post', views.toggle_post, name='delete-restore-post'),
]


urlpatterns += [
    path('blogs/<slug:slug>/<int:pk>/toggle-comment', views.CommentDeleteView.as_view(), name='toggle-comment'),
]


# urlpatterns += [
#     path('blog/<slug:slug>/edit', ),
# ]
