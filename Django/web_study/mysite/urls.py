# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from mysite import views

# app_name = 'mysite'

# urlpatterns = [
#     path('', views.base1, name='base1'), 
#     path('blog/new_post/', views.new_post, name="new_post"),
#     path('blog/food_list/', views.food_list, name="food_list"),
#     path('blog/food_list1/', views.food_list1, name="food_list1"),
#     path('blog/map/', views.map, name='map'),
#     path('blog/base1/', views.base1, name='base1'),  
#     path('blog/molar/', views.molar, name='molar'),
#     path('blog/blog1/', views.blog1, name='blog1'),
#     #메뉴
#     path('blog/map/', views.map, name='map'),
#     path('blog/map/gotowork', views.gotowork, name='gotowork'),
#     path('blog/map/gotowork', views.gunae, name='gunae'),
#     path('blog/map/rol', views.rol, name='rol'),
#     path('blog/map/dol', views.dol, name='dol'),
#     path('blog/map/lee', views.lee, name='lee'),
#     path('blog/map/mak', views.mak, name='mak'),
#     path('blog/map/mij', views.mij, name='mij'),
#     path('blog/map/bac1', views.bac1, name='bac1'),
#     path('blog/map/bac2', views.bac2, name='bac2'),
#     path('blog/map/bac3', views.bac3, name='bac3'),
#     path('blog/map/bon', views.bon, name='bon'),
#     path('blog/map/bun', views.bun, name='bun'),
#     path('blog/map/bac4', views.bac4, name='bac4'),
#     path('blog/map/bac5', views.bac5, name='bac5'),
#     path('blog/map/sae', views.sae, name='sae'),
#     path('blog/map/sun', views.sun, name='sun'),
#     path('blog/map/yuk', views.yuk, name='yuk'),
#     path('blog/map/yeo', views.yeo, name='yeo'),
#     path('blog/map/one', views.one, name='one'),
#     path('blog/map/ins', views.ins, name='ins'),
#     path('blog/map/jes', views.jes, name='jes'),
#     path('blog/map/han', views.han, name='han'),
#     path('blog/map/hon', views.hon, name='hon'),

#     path('blog/show_food/', views.show_food, name='food'),
#     path('blog/show_post/', views.show_post, name='show'),

#     # path('blog/predict/', views.predict_model, name='predict_model'),

# ] 
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)




from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mysite import views

app_name = 'mysite'

urlpatterns = [
    path('', views.base1, name='base1'), 
    path('file_upload/', views.new_post, name="new_post"),
    path('recommend/', views.food_list, name="food_list"),
    path('recommend1/', views.food_list1, name="food_list1"),
    path('map/', views.map, name='map'),
    path('blank/', views.molar, name='molar'),

    #메뉴
    path('map/', views.map, name='map'),
    path('map/gotowork', views.gotowork, name='gotowork'),
    path('map/gunae', views.gunae, name='gunae'),
    path('map/rol', views.rol, name='rol'),
    path('map/dol', views.dol, name='dol'),
    path('map/lee', views.lee, name='lee'),
    path('map/mak', views.mak, name='mak'),
    path('map/mij', views.mij, name='mij'),
    path('map/bac1', views.bac1, name='bac1'),
    path('map/bac2', views.bac2, name='bac2'),
    path('map/bac3', views.bac3, name='bac3'),
    path('map/bon', views.bon, name='bon'),
    path('map/bun', views.bun, name='bun'),
    path('map/bac4', views.bac4, name='bac4'),
    path('map/bac5', views.bac5, name='bac5'),
    path('map/sae', views.sae, name='sae'),
    path('map/sun', views.sun, name='sun'),
    path('map/yuk', views.yuk, name='yuk'),
    path('map/yeo', views.yeo, name='yeo'),
    path('map/one', views.one, name='one'),
    path('map/ins', views.ins, name='ins'),
    path('map/jes', views.jes, name='jes'),
    path('map/han', views.han, name='han'),
    path('map/hon', views.hon, name='hon'),

    #네비바
    path('record/', views.show_food, name='food'),

    path('fchoice/', views.fchoice, name='choice'),
    path('foodview/', views.foodview, name='final'),

] 

# urlpatterns = [
#     path('', views.base1, name='base1'), 
#     path('file_upload/', views.new_post, name="new_post"),
#     path('recommand/', views.food_list, name="food_list"),
#     path('recommand1/', views.food_list1, name="food_list1"),
#     path('map/', views.map, name='map'),
#     path('blank/', views.molar, name='molar'),
    
#     #메뉴
#     path('map/', views.map, name='map'),
#     path('map/gotowork', views.gotowork, name='gotowork'),
#     path('map/gotowork', views.gunae, name='gunae'),
#     path('map/rol', views.rol, name='rol'),
#     path('map/dol', views.dol, name='dol'),
#     path('map/lee', views.lee, name='lee'),
#     path('map/mak', views.mak, name='mak'),
#     path('map/mij', views.mij, name='mij'),
#     path('map/bac1', views.bac1, name='bac1'),
#     path('map/bac2', views.bac2, name='bac2'),
#     path('map/bac3', views.bac3, name='bac3'),
#     path('map/bon', views.bon, name='bon'),
#     path('map/bun', views.bun, name='bun'),
#     path('map/bac4', views.bac4, name='bac4'),
#     path('map/bac5', views.bac5, name='bac5'),
#     path('map/sae', views.sae, name='sae'),
#     path('map/sun', views.sun, name='sun'),
#     path('map/yuk', views.yuk, name='yuk'),
#     path('map/yeo', views.yeo, name='yeo'),
#     path('map/one', views.one, name='one'),
#     path('map/ins', views.ins, name='ins'),
#     path('map/jes', views.jes, name='jes'),
#     path('map/han', views.han, name='han'),
#     path('map/hon', views.hon, name='hon'),
    
#     #추천기록
#     path('record', views.show_food, name='food'),
#     path('fchoice/', views.fchoice, name='choice'),
#     path('foodview/', views.foodview, name='fianl'),
#     # path('predict/', views.predict_model, name='predict_model'),

# ] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)