from django.shortcuts import render,HttpResponse
from django.http.response import JsonResponse
from rest_framework import status
from .serializers import Matchs_Dataset_Serializer
from .models import MatchsDatasetModel
from API.models import *
from API.serializers import *
from rest_framework.views import APIView
# Create your views here.

def home(request):
    return HttpResponse("HelloWorld")
class Scores_And_Fixtures_List(APIView):
    def get(self, request, league = None,season=None):
        if league and season:
            league = league.replace("_"," ")
            season = season.replace("-","/")
            scores_and_fixtures = View_Scores_And_Fixtures.objects.all().order_by('-match_date',
                                                                                  "match_week").filter(league=league,season=season)
            scores_and_fixtures_serializer = View_Scores_And_Fixtures_Serializer(scores_and_fixtures, many=True)
        else:
            scores_and_fixtures = View_Scores_And_Fixtures.objects.all().order_by('-match_date',"match_week")
            scores_and_fixtures_serializer = View_Scores_And_Fixtures_Serializer(scores_and_fixtures, many=True)
        return JsonResponse(scores_and_fixtures_serializer.data, safe=False)

class Matchs_Detail_Infos_View(APIView):
    def get(self, request, match_id = None):
        if match_id:
            matchs_infos = FbrefMatchinfosModified.objects.all().filter(match_id=match_id)
            match_goals = FbrefMatchgoalsModified.objects.all().filter(match_id=match_id)
            match_player_stats = FbrefMatchplayerstatsModified.objects.all().filter(match_id=match_id)
            match_squad = FbrefMatchsquadModified.objects.all().filter(match_id=match_id)
            match_stats = FbrefMatchstatsModified.objects.all().filter(match_id=match_id)
            matchs_infos_serializer = FbrefMatchinfosModified_Serializer(matchs_infos, many=True)
            match_goals_serializer = FbrefMatchgoalsModified_Serializer(match_goals, many=True)
            match_player_stats_serializer = FbrefMatchplayerstatsModified_Serializer(match_player_stats, many=True)
            match_squad_serializer = FbrefMatchsquadModified_Serializer(match_squad, many=True)
            match_stats_serializer = FbrefMatchstatsModified_Serializer(match_stats, many=True)


            matchs_model = MatchsDatasetModel.objects.all().filter(match_id=match_id)
            matchs_model_serializer = Matchs_Dataset_Serializer(matchs_model, many=True)
            data = {
                "matchs_infos":matchs_infos_serializer.data,
                "match_goals":match_goals_serializer.data,
                "match_player_stats":match_player_stats_serializer.data,
                "match_squad":match_squad_serializer.data,
                "match_stats":match_stats_serializer.data,
                "matchs_model":matchs_model_serializer.data
            }
            return JsonResponse(data, safe=False)
        else:
            matchs_infos = FbrefMatchinfosModified.objects.all()
            matchs_infos_serializer = FbrefMatchinfosModified_Serializer(matchs_infos, many=True)
        return JsonResponse(matchs_infos_serializer.data, safe=False)

class FbrefMatchgoalsModifiedList(APIView):
    def get(self, request):
        match_id = request.GET.get('id')
        team = request.GET.get('team')
        player_name = request.GET.get('player')
        type_goal= request.GET.get('type')
        match_goals = FbrefMatchgoalsModified.objects.all()
        if match_id:
            match_goals = match_goals.filter(match_id=match_id)
        if team:
            match_goals = match_goals.filter(team=team)
        if player_name:
            match_goals = match_goals.filter(player_name=player_name)
        if type_goal:
            match_goals = match_goals.filter(type_of_goal=type_goal)
        match_goals_serializer = FbrefMatchgoalsModified_Serializer(match_goals, many=True)
        return JsonResponse(match_goals_serializer.data, safe=False) 

class MatchsDatasetList(APIView):
    def get(self,request):
        match_id = request.GET.get('id')
        home_team = request.GET.get('home')
        away_team = request.GET.get('away')
        date = request.GET.get('date')
        top_date = request.GET.get('top_date')
        matchs = MatchsDatasetModel.objects.all()
        if match_id:
            matchs = matchs.filter(match_id=match_id)

        if home_team:
            matchs = matchs.filter(home_team=home_team)

        if away_team:
            matchs = matchs.filter(away_team=away_team)

        if date:
            matchs = matchs.filter(match_date=date)

        if top_date:
            sorted_date = matchs.order_by('-match_date')
            matchs = sorted_date[:int(top_date)]

        matchs_serializer = Matchs_Dataset_Serializer(matchs, many=True)
        return JsonResponse(matchs_serializer.data, safe=False)

class Matches(APIView):
    def get(self, request, league = None, season = None):

        if league and season:
            league_new = league.replace("_"," ")
            season_new = season.replace("-","/")
            
            matchs_infos = FbrefMatchinfosModified.objects.all().order_by('-match_week').filter(league=league_new, season=season_new) 
            matchs_infos_serializer = FbrefMatchinfosModified_Serializer(matchs_infos, many=True)

            id_list = [obj["match_id"] for obj in matchs_infos_serializer.data]
            matchs_model = MatchsDatasetModel.objects.all().filter(match_id__in=id_list)
            matchs_model_serializer = Matchs_Dataset_Serializer(matchs_model, many=True)

            data = {
                "matchs_infos": matchs_infos_serializer.data,
                "matchs_model": matchs_model_serializer.data
            }
            return JsonResponse(data, safe=False)
        else:
            matchs_infos = FbrefMatchinfosModified.objects.all()
            matchs_infos_serializer = FbrefMatchinfosModified_Serializer(matchs_infos, many=True)
        return JsonResponse(matchs_infos_serializer.data, safe=False)
    
class Matches_WithMatchWeek(APIView):
    def get(self, request, league = None, season = None, matchweek = None):

        if league and season:
            league_new = league.replace("_"," ")
            season_new = season.replace("-","/")
            matchweek_new = matchweek.replace("_"," ")
            
            matchs_infos = FbrefMatchinfosModified.objects.all().filter(league=league_new, season=season_new, 
                                                                        match_week = matchweek_new) 
            matchs_infos_serializer = FbrefMatchinfosModified_Serializer(matchs_infos, many=True)

            id_list = [obj["match_id"] for obj in matchs_infos_serializer.data]
            matchs_model = MatchsDatasetModel.objects.all().filter(match_id__in=id_list)
            matchs_model_serializer = Matchs_Dataset_Serializer(matchs_model, many=True)

            data = {
                "matchs_infos": matchs_infos_serializer.data,
                "matchs_model": matchs_model_serializer.data
            }
            return JsonResponse(data, safe=False)
        else:
            matchs_infos = FbrefMatchinfosModified.objects.all()
            matchs_infos_serializer = FbrefMatchinfosModified_Serializer(matchs_infos, many=True)
        return JsonResponse(matchs_infos_serializer.data, safe=False)
    
class Match_Detail(APIView):
    def get(self, request, match_id = None):

        if match_id:
            
            matchs_infos = FbrefMatchinfosModified.objects.all().filter(match_id = match_id) 
            matchs_infos_serializer = FbrefMatchinfosModified_Serializer(matchs_infos, many=True)

            matchs_goals = FbrefMatchgoalsModified.objects.all().filter(match_id = match_id) 
            matchs_goals_serializer = FbrefMatchgoalsModified(matchs_goals)

            matchs_squad = FbrefMatchsquadModified.objects.all().filter(match_id = match_id) 
            matchs_squad_serializer = FbrefMatchsquadModified(matchs_squad)

            matchs_stats = FbrefMatchstatsModified.objects.all().filter(match_id = match_id) 
            matchs_stats_serializer = FbrefMatchstatsModified(matchs_stats)


            #id_list = [obj["match_id"] for obj in matchs_infos_serializer.data]
            matchs_model = MatchsDatasetModel.objects.all().filter(match_id=match_id)
            matchs_model_serializer = Matchs_Dataset_Serializer(matchs_model, many=True)

            data = {
                "matchs_infos": matchs_infos_serializer.data,
                "matchs_goals": matchs_goals_serializer.data,
                "matchs_squad": matchs_squad_serializer.data,
                "matchs_stats": matchs_stats_serializer.data,
                "matchs_model": matchs_model_serializer.data
            }
            return JsonResponse(data, safe=False)
        else:
            matchs_infos = FbrefMatchinfosModified.objects.all()
            matchs_infos_serializer = FbrefMatchinfosModified_Serializer(matchs_infos, many=True)
        return JsonResponse(matchs_infos_serializer.data, safe=False)
    
class Match_Future(APIView):
    def get(self, request, match_id = None):
        if match_id:
            matchs_infos = FbrefMatchinfosModified.objects.all().filter(match_id=match_id)
            match_goals = FbrefMatchgoalsModified.objects.all().filter(match_id=match_id)
            match_player_stats = FbrefMatchplayerstatsModified.objects.all().filter(match_id=match_id)
            match_squad = FbrefMatchsquadModified.objects.all().filter(match_id=match_id)
            match_stats = FbrefMatchstatsModified.objects.all().filter(match_id=match_id)
            matchs_infos_serializer = FbrefMatchinfosModified_Serializer(matchs_infos, many=True)
            match_goals_serializer = FbrefMatchgoalsModified_Serializer(match_goals, many=True)
            match_player_stats_serializer = FbrefMatchplayerstatsModified_Serializer(match_player_stats, many=True)
            match_squad_serializer = FbrefMatchsquadModified_Serializer(match_squad, many=True)
            match_stats_serializer = FbrefMatchstatsModified_Serializer(match_stats, many=True)

            match_predict = FutureMatches.objects.all().filter(match_id=match_id)
            match_predict_serializer = Future_Matches_Serializer(match_predict, many=True)

            matchs_model = MatchsDatasetModel.objects.all().filter(match_id=match_id)
            matchs_model_serializer = Matchs_Dataset_Serializer(matchs_model, many=True)

            team1 = matchs_infos_serializer.data[0]["home_team"]
            team2 = matchs_infos_serializer.data[0]["away_team"]

            team_optimization1 = TeamOptimization.objects.all().filter(team1=team1) | TeamOptimization.objects.all().filter(team2=team1)
            team_optimization2 = TeamOptimization.objects.all().filter(team1=team2) | TeamOptimization.objects.all().filter(team2=team2)
            
            team_optimization1_serializer = Team_Optimization_Serializer(team_optimization1, many=True)
            team_optimization2_serializer = Team_Optimization_Serializer(team_optimization2, many=True)

            all_matchs_model1 = MatchsDatasetModel.objects.all().filter(home_team=team1) | MatchsDatasetModel.objects.all().filter(away_team=team1)
            all_matchs_model1_serializer = Matchs_Dataset_Serializer(all_matchs_model1[1:5], many=True)

            all_matchs_model2 = MatchsDatasetModel.objects.all().filter(home_team=team2) | MatchsDatasetModel.objects.all().filter(away_team=team2)
            all_matchs_model2_serializer = Matchs_Dataset_Serializer(all_matchs_model2[1:5], many=True)

            data = {
                "matchs_infos":matchs_infos_serializer.data,
                "match_goals":match_goals_serializer.data,
                "match_player_stats":match_player_stats_serializer.data,
                "match_squad":match_squad_serializer.data,
                "match_stats":match_stats_serializer.data,
                "matchs_model":matchs_model_serializer.data,
                "match_future":match_predict_serializer.data,

                "opti1":team_optimization1_serializer.data,
                "opti2":team_optimization2_serializer.data,

                "all_model_1":all_matchs_model1_serializer.data,
                "all_model_2":all_matchs_model2_serializer.data
            }
            return JsonResponse(data, safe=False)
        else:
            matchs_infos = FbrefMatchinfosModified.objects.all()
            matchs_infos_serializer = FbrefMatchinfosModified_Serializer(matchs_infos, many=True)
        return JsonResponse(matchs_infos_serializer.data, safe=False)
    
class Matchs_By_Team_Order_Desc(APIView):
    def get(self, request, team = None):
        if team:
            #team = team.replace("_"," ")

            matchs_model = MatchsDatasetModel.objects.all().order_by('-match_date').filter(home_team=team) | MatchsDatasetModel.objects.all().filter(away_team=team)

            matchs_model_serializer = Matchs_Dataset_Serializer(matchs_model, many=True)

            data = {
                "matchs_model":matchs_model_serializer.data
            }
            return JsonResponse(data, safe=False)
        else:
            matchs_infos = FbrefMatchinfosModified.objects.all()
            matchs_infos_serializer = FbrefMatchinfosModified_Serializer(matchs_infos, many=True)
        return JsonResponse(matchs_infos_serializer.data, safe=False)
    
class Team_Optimization_View(APIView):
    def get(self, request, team = None):
        if team:
            #team = "Tottenham Hotspur,Fulham"
            team_list = team.split(",")
            team1 = team_list[0]
            team2 = team_list[1]

            team_optimization1 = TeamOptimization.objects.all().filter(team1=team1) | TeamOptimization.objects.all().filter(team2=team1)
            team_optimization2 = TeamOptimization.objects.all().filter(team1=team2) | TeamOptimization.objects.all().filter(team2=team2)
            
            team_optimization1_serializer = Team_Optimization_Serializer(team_optimization1, many=True)
            team_optimization2_serializer = Team_Optimization_Serializer(team_optimization2, many=True)

            data = {
                team1:team_optimization1_serializer.data,
                team2:team_optimization2_serializer.data
            }
            return JsonResponse(data, safe=False)
        else:
            matchs_infos = FbrefMatchinfosModified.objects.all()
            matchs_infos_serializer = FbrefMatchinfosModified_Serializer(matchs_infos, many=True)
        return JsonResponse(matchs_infos_serializer.data, safe=False)