import os
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.index, name='index'), 
    path('', views.home, name='home'),
    path('store/', views.store,name='store'),
    
    path('store/aipage.html', views.aipage,name='aipage'),
    path('store/fullstack.html', views.fullstack,name='fullstack'),
    path('store/trading.html', views.trading,name='trading'),
    path('store/free.html', views.free,name='free'),
    path('store/erp.html', views.erp,name='erp'),
    
    
    path('aipage.html/',views.aipage,name='aipage'),
    path('fullstack.html/',views.fullstack,name='fullstack'),
    path('trading.html/', views.trading,name='trading'),
    path('free.html/', views.free,name='free'),
    path('erp.html/', views.erp,name='erp'),
    
    
    path('search/',views.search,name='search'),
    path('search/aipage.html/',views.aipage,name='aipage'),
    path('search/fullstack.html/',views.fullstack,name='fullstack'),
    path('search/trading.html/',views.trading,name='trading'),
    path('search/free.html/', views.free,name='free'),
    path('search/erp.html/', views.erp,name='erp'),
    
    path('aipage.html/aisearch/',views.aisearch,name='aisearch'),
    path('fullstack.html/fullsearch',views.fullsearch,name='fullsearch'),    
    path('trading.html/tradesearch',views.tradesearch,name='tradesearch'),    
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


