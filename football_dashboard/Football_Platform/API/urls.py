from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('matchs_dataset_model/', views.MatchsDatasetList.as_view(), name='matchs_dataset_model'),
    path('fbref_matchgoals_modified/', views.FbrefMatchgoalsModifiedList.as_view(), name='fbref_matchgoals_modified'),
    path('<str:league>/<str:season>/scores_and_fixtures/', views.Scores_And_Fixtures_List.as_view(), name='scores_and_fixtures'),
    
    
    


     path('scores_and_fixtures/',
         views.Scores_And_Fixtures_List.as_view(),name='scores_and_fixtures'),
     path('scores_and_fixtures/<str:team>/',
         views.Matchs_By_Team_Order_Desc.as_view(),name='scores_and_fixtures_by_team'),
     path('matches/<str:league>/<str:season>/',
         views.Matches.as_view(), name='matches'),
     path('matches/<str:league>/<str:season>/<str:matchweek>/',
         views.Matches_WithMatchWeek.as_view(), name='matches_withmatchweek'),
     path('match/<str:match_id>/', 
         views.Matchs_Detail_Infos_View.as_view(), name='match_detail'),
     path('match_future/<str:match_id>/', 
         views.Match_Future.as_view(), name='match_future'),
     path('team_optimization/<str:team>/', 
         views.Team_Optimization_View.as_view(), name='team_optimization'),
        
]
