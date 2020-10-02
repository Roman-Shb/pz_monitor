from django.conf.urls import url, include
from django.urls import path
from . import views
from machines import views
from rest_framework import routers
from .views import RawDataViewSet, EquipmentWorksDetailView, repair_equipment, all_complexes,complex_equipments,repair_view_data

router = routers.DefaultRouter()
router.register(r'^api/rawdata', RawDataViewSet, basename='RawData')

urlpatterns = [
                  url(r'^$', views.EqipmentFilteredListView.as_view(), name='equipment-list'),
                  url(r'^accounts/', include('django.contrib.auth.urls')),
                  url(r'^register$', views.register, name='register'),
                  url(r'^newdata/', views.RawDataUploadView.as_view()),
                  url(r'graph', views.APIGraphData.as_view(), name='graph-data'),
                  url(r'^ci$', views.ClassifiedIntervalsListView.as_view(), name='classifiedinterval-list'),
                  url(r'^stats', views.StatisticsView.as_view(), name='statistics-view'),
		  		  path('works/<int:pk>/', views.EquipmentWorksDetailView.as_view(), name='works-detail'),
		  		  path('workshop<int:workshop_numb>/area_stats/<int:area_numb>/',repair_equipment,name='post_new'),
		  		  path('complexes',all_complexes,name='all_complexes_name'),
		  		  path('complexes/equipment_complex/<int:complex_id>',complex_equipments,name='complex_equipments_name'),
            path('repair_view_data',repair_view_data,name='repair_view_data'),
                  #url(r'^ajax_stats/$', views.ajax_stats, name='ajax_stats'),
                  
              ] + router.urls
