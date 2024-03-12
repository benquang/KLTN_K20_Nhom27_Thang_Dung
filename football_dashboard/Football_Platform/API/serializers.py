from rest_framework import serializers
from .models import *

class FbrefMatchgoalsModified_Serializer(serializers.ModelSerializer):
    class Meta:
        model = FbrefMatchgoalsModified
        fields = '__all__'

class FbrefMatchinfosModified_Serializer(serializers.ModelSerializer):
    class Meta:
        model = FbrefMatchinfosModified
        fields = '__all__'

class FbrefMatchplayerstatsModified_Serializer(serializers.ModelSerializer):
    class Meta:
        model = FbrefMatchplayerstatsModified
        fields = '__all__'
class FbrefMatchsquadModified_Serializer(serializers.ModelSerializer):
    class Meta:
        model = FbrefMatchsquadModified
        fields = '__all__'

class FbrefMatchstatsModified_Serializer(serializers.ModelSerializer):
    class Meta:
        model = FbrefMatchstatsModified
        fields = '__all__'


class Matchs_Dataset_Serializer(serializers.ModelSerializer):
    class Meta:
        model = MatchsDatasetModel
        fields = '__all__'
class MatchsquadPlayers_Serializer(serializers.ModelSerializer):
    class Meta:
        model = MatchsquadPlayers
        fields = '__all__'
class SofifaPlayersAttrModified_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SofifaPlayersAttrModified
        fields = '__all__'

class SofifaPlayersInfosModified_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SofifaPlayersInfosModified
        fields = '__all__'


class View_Scores_And_Fixtures_Serializer(serializers.ModelSerializer):
    class Meta:
        model = View_Scores_And_Fixtures
        fields = '__all__'

class Future_Matches_Serializer(serializers.ModelSerializer):
    class Meta:
        model = FutureMatches
        fields = '__all__'

class Team_Optimization_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TeamOptimization
        fields = '__all__'