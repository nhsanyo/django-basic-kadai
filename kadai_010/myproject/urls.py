"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud import views #pythonのパッケージ、ライブラリを読み込む　　from　フォルダ名　import ファイル名

# 有効なURL ひとつめのパラメータ：パス, ふたつめのパラメータ：どのviewを返すのか　views.はimportのviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.Topview.as_view(), name="top"), #viewsファイルのTopViewクラスを返す as_viewは解析して返してくださいという意味
    path("crud/", views.ProductListView.as_view(), name="list"),
    path("abc/", views.ABCview.as_view(), name="abc"),
    path('crud/new/', views.ProductCreateView.as_view(), name="new"),
    path('crud/edit/<int:pk>', views.ProductUpdateView.as_view(), name="edit"),
    path('crud/delete/<int:pk>', views.ProductDeleteView.as_view(), name="delete"),
    path("crud/detail/<int:pk>", views.ProductDetailView.as_view(), name="detail"),
]

