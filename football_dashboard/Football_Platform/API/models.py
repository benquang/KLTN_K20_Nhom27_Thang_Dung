# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class FbrefMatchgoalsModified(models.Model):
    match_id = models.CharField(db_column='Match_Id', 
                                max_length=100, db_collation='utf8mb3_general_ci', 
                                blank=True, null=True)  # Field name made lowercase.
    team = models.CharField(db_column='Team', 
                            max_length=100, db_collation='utf8mb3_general_ci', 
                            blank=True, null=True)  # Field name made lowercase.
    minute = models.CharField(db_column='Minute',
                              max_length=100, db_collation='utf8mb3_general_ci', 
                              blank=True, null=True)  # Field name made lowercase.
    player_name = models.CharField(db_column='Player_Name', 
                                   max_length=100, db_collation='utf8mb3_general_ci', 
                                   blank=True, null=True)  # Field name made lowercase.
    type_of_goal = models.CharField(db_column='Type_Of_Goal', 
                                    max_length=100, db_collation='utf8mb3_general_ci', 
                                    blank=True, null=True)  # Field name made lowercase.
    is_home_team = models.CharField(db_column='Is_Home_Team', 
                                    max_length=100, db_collation='utf8mb3_general_ci', 
                                    blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fbref_matchgoals_modified'


class FbrefMatchinfosModified(models.Model):
    match_id = models.CharField(db_column='Match_Id', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    league = models.CharField(db_column='League', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    season = models.CharField(db_column='Season', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    match_week = models.CharField(db_column='Match_Week',max_length=100, db_collation='utf8mb3_general_ci' ,blank=True, null=True)  # Field name made lowercase.
    home_team = models.CharField(db_column='Home_Team', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    away_team = models.CharField(db_column='Away_Team', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    match_date = models.DateField(db_column='Match_Date', blank=True, null=True)  # Field name made lowercase.
    venue_time = models.CharField(db_column='Venue_Time', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    attendance = models.IntegerField(db_column='Attendance', blank=True, null=True)  # Field name made lowercase.
    stadium = models.CharField(db_column='Stadium', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    officials = models.CharField(db_column='Officials', max_length=1000, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=200, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fbref_matchinfos_modified'


class FbrefMatchplayerstatsModified(models.Model):
    match_id = models.CharField(db_column='Match_Id', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    team = models.CharField(db_column='Team', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    player_name = models.CharField(db_column='Player_Name', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    player_kitnum = models.IntegerField(db_column='Player_Kitnum', blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    minutes = models.FloatField(db_column='Minutes', blank=True, null=True)  # Field name made lowercase.
    gls = models.FloatField(db_column='Gls', blank=True, null=True)  # Field name made lowercase.
    ast = models.FloatField(db_column='Ast', blank=True, null=True)  # Field name made lowercase.
    PK = models.FloatField(db_column='PK', blank=True, null=True)  # Field name made lowercase.
    pk_att = models.FloatField(db_column='PK_Att', blank=True, null=True)  # Field name made lowercase.
    sh = models.FloatField(db_column='Sh', blank=True, null=True)  # Field name made lowercase.
    sot = models.FloatField(db_column='SoT', blank=True, null=True)  # Field name made lowercase.
    crdy = models.FloatField(db_column='CrdY', blank=True, null=True)  # Field name made lowercase.
    crdr = models.FloatField(db_column='CrdR', blank=True, null=True)  # Field name made lowercase.
    touches = models.FloatField(db_column='Touches', blank=True, null=True)  # Field name made lowercase.
    tkl = models.FloatField(db_column='Tkl', blank=True, null=True)  # Field name made lowercase.
    int = models.FloatField(db_column='Int', blank=True, null=True)  # Field name made lowercase.
    blocks = models.FloatField(db_column='Blocks', blank=True, null=True)  # Field name made lowercase.
    xg = models.FloatField(db_column='xG', blank=True, null=True)  # Field name made lowercase.
    npxg = models.FloatField(db_column='npxG', blank=True, null=True)  # Field name made lowercase.
    xag = models.FloatField(db_column='xAG', blank=True, null=True)  # Field name made lowercase.
    sca = models.FloatField(db_column='SCA', blank=True, null=True)  # Field name made lowercase.
    gca = models.FloatField(db_column='GCA', blank=True, null=True)  # Field name made lowercase.
    passes_cmp = models.FloatField(db_column='Passes_Cmp', blank=True, null=True)  # Field name made lowercase.
    passes_att = models.FloatField(db_column='Passes_Att', blank=True, null=True)  # Field name made lowercase.
    passes_cmp_percentage = models.FloatField(db_column='Passes_Cmp_Percentage', blank=True, null=True)  # Field name made lowercase.
    passes_prgp = models.FloatField(db_column='Passes_PrgP', blank=True, null=True)  # Field name made lowercase.
    carries = models.FloatField(db_column='Carries', blank=True, null=True)  # Field name made lowercase.
    carries_prgc = models.FloatField(db_column='Carries_PrgC', blank=True, null=True)  # Field name made lowercase.
    take_ons_att = models.FloatField(db_column='Take_Ons_Att', blank=True, null=True)  # Field name made lowercase.
    take_ons_succ = models.FloatField(db_column='Take_Ons_Succ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fbref_matchplayerstats_modified'


class FbrefMatchsquadModified(models.Model):
    match_id = models.CharField(db_column='Match_Id', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    team = models.CharField(db_column='Team', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    is_home_team = models.CharField(db_column='Is_Home_Team', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    player_name = models.CharField(db_column='Player_Name', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    player_kitnum = models.IntegerField(db_column='Player_Kitnum', blank=True, null=True)  # Field name made lowercase.
    is_sub = models.CharField(db_column='Is_Sub', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fbref_matchsquad_modified'


class FbrefMatchstatsModified(models.Model):
    match_id = models.CharField(db_column='Match_Id', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    team = models.CharField(db_column='Team', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    is_home_team = models.CharField(db_column='Is_Home_Team', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    manager = models.CharField(db_column='Manager', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    captain = models.CharField(db_column='Captain', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    formation = models.CharField(db_column='Formation', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    possession = models.FloatField(db_column='Possession', blank=True, null=True)  # Field name made lowercase.
    fouls = models.FloatField(db_column='Fouls', blank=True, null=True)  # Field name made lowercase.
    corners = models.FloatField(db_column='Corners', blank=True, null=True)  # Field name made lowercase.
    crosses = models.FloatField(db_column='Crosses', blank=True, null=True)  # Field name made lowercase.
    aerials_won = models.FloatField(db_column='Aerials_Won', blank=True, null=True)  # Field name made lowercase.
    clearances = models.FloatField(db_column='Clearances', blank=True, null=True)  # Field name made lowercase.
    offsides = models.FloatField(db_column='Offsides', blank=True, null=True)  # Field name made lowercase.
    goal_kicks = models.FloatField(db_column='Goal_Kicks', blank=True, null=True)  # Field name made lowercase.
    throw_ins = models.FloatField(db_column='Throw_Ins', blank=True, null=True)  # Field name made lowercase.
    long_balls = models.FloatField(db_column='Long_Balls', blank=True, null=True)  # Field name made lowercase.
    total_players_stats = models.FloatField(db_column='Total_Players_Stats', blank=True, null=True)  # Field name made lowercase.
    minutes = models.FloatField(db_column='Minutes', blank=True, null=True)  # Field name made lowercase.
    gls = models.FloatField(db_column='Gls', blank=True, null=True)  # Field name made lowercase.
    ast = models.FloatField(db_column='Ast', blank=True, null=True)  # Field name made lowercase.
    PK = models.FloatField(db_column='PK', blank=True, null=True)  # Field name made lowercase.
    pk_att = models.FloatField(db_column='PK_Att', blank=True, null=True)  # Field name made lowercase.
    sh = models.FloatField(db_column='Sh', blank=True, null=True)  # Field name made lowercase.
    sot = models.FloatField(db_column='SoT', blank=True, null=True)  # Field name made lowercase.
    crdy = models.FloatField(db_column='CrdY', blank=True, null=True)  # Field name made lowercase.
    crdr = models.FloatField(db_column='CrdR', blank=True, null=True)  # Field name made lowercase.
    touches = models.FloatField(db_column='Touches', blank=True, null=True)  # Field name made lowercase.
    tkl = models.FloatField(db_column='Tkl', blank=True, null=True)  # Field name made lowercase.
    int = models.FloatField(db_column='Int', blank=True, null=True)  # Field name made lowercase.
    blocks = models.FloatField(db_column='Blocks', blank=True, null=True)  # Field name made lowercase.
    xg = models.FloatField(db_column='xG', blank=True, null=True)  # Field name made lowercase.
    npxg = models.FloatField(db_column='npxG', blank=True, null=True)  # Field name made lowercase.
    xag = models.FloatField(db_column='xAG', blank=True, null=True)  # Field name made lowercase.
    sca = models.FloatField(db_column='SCA', blank=True, null=True)  # Field name made lowercase.
    gca = models.FloatField(db_column='GCA', blank=True, null=True)  # Field name made lowercase.
    passes_cmp = models.FloatField(db_column='Passes_Cmp', blank=True, null=True)  # Field name made lowercase.
    passes_att = models.FloatField(db_column='Passes_Att', blank=True, null=True)  # Field name made lowercase.
    passes_cmp_percentage = models.FloatField(db_column='Passes_Cmp_Percentage', blank=True, null=True)  # Field name made lowercase.
    passes_prgp = models.FloatField(db_column='Passes_PrgP', blank=True, null=True)  # Field name made lowercase.
    carries = models.FloatField(db_column='Carries', blank=True, null=True)  # Field name made lowercase.
    carries_prgc = models.FloatField(db_column='Carries_PrgC', blank=True, null=True)  # Field name made lowercase.
    take_ons_att = models.FloatField(db_column='Take_Ons_Att', blank=True, null=True)  # Field name made lowercase.
    take_ons_succ = models.FloatField(db_column='Take_Ons_Succ', blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fbref_matchstats_modified'


class MatchsDatasetModel(models.Model):
    match_id = models.CharField(db_column='match_id', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    match_date = models.DateField(db_column='Match_Date', blank=True, null=True)  # Field name made lowercase.
    home_team = models.CharField(db_column='Home_Team', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    home_manager = models.CharField(db_column='Home_Manager', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    home_captain = models.CharField(db_column='Home_Captain', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    home_formation = models.CharField(db_column='Home_Formation', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    home_possession = models.FloatField(db_column='Home_Possession', blank=True, null=True)  # Field name made lowercase.
    home_fouls = models.FloatField(db_column='Home_Fouls', blank=True, null=True)  # Field name made lowercase.
    home_corners = models.FloatField(db_column='Home_Corners', blank=True, null=True)  # Field name made lowercase.
    home_crosses = models.FloatField(db_column='Home_Crosses', blank=True, null=True)  # Field name made lowercase.
    home_aerials_won = models.FloatField(db_column='Home_Aerials_Won', blank=True, null=True)  # Field name made lowercase.
    home_clearances = models.FloatField(db_column='Home_Clearances', blank=True, null=True)  # Field name made lowercase.
    home_offsides = models.FloatField(db_column='Home_Offsides', blank=True, null=True)  # Field name made lowercase.
    home_goal_kicks = models.FloatField(db_column='Home_Goal_Kicks', blank=True, null=True)  # Field name made lowercase.
    home_throw_ins = models.FloatField(db_column='Home_Throw_Ins', blank=True, null=True)  # Field name made lowercase.
    home_long_balls = models.FloatField(db_column='Home_Long_Balls', blank=True, null=True)  # Field name made lowercase.
    home_total_players_stats = models.FloatField(db_column='Home_Total_Players_Stats', blank=True, null=True)  # Field name made lowercase.
    home_minutes = models.FloatField(db_column='Home_Minutes', blank=True, null=True)  # Field name made lowercase.
    home_gls = models.FloatField(db_column='Home_Gls', blank=True, null=True)  # Field name made lowercase.
    home_ast = models.FloatField(db_column='Home_Ast', blank=True, null=True)  # Field name made lowercase.
    home_pk = models.FloatField(db_column='Home_PK', blank=True, null=True)  # Field name made lowercase.
    home_pk_att = models.FloatField(db_column='Home_PK_Att', blank=True, null=True)  # Field name made lowercase.
    home_sh = models.FloatField(db_column='Home_Sh', blank=True, null=True)  # Field name made lowercase.
    home_sot = models.FloatField(db_column='Home_SoT', blank=True, null=True)  # Field name made lowercase.
    home_crdy = models.FloatField(db_column='Home_CrdY', blank=True, null=True)  # Field name made lowercase.
    home_crdr = models.FloatField(db_column='Home_CrdR', blank=True, null=True)  # Field name made lowercase.
    home_touches = models.FloatField(db_column='Home_Touches', blank=True, null=True)  # Field name made lowercase.
    home_tkl = models.FloatField(db_column='Home_Tkl', blank=True, null=True)  # Field name made lowercase.
    home_int = models.FloatField(db_column='Home_Int', blank=True, null=True)  # Field name made lowercase.
    home_blocks = models.FloatField(db_column='Home_Blocks', blank=True, null=True)  # Field name made lowercase.
    home_xg = models.FloatField(db_column='Home_xG', blank=True, null=True)  # Field name made lowercase.
    home_npxg = models.FloatField(db_column='Home_npxG', blank=True, null=True)  # Field name made lowercase.
    home_xag = models.FloatField(db_column='Home_xAG', blank=True, null=True)  # Field name made lowercase.
    home_sca = models.FloatField(db_column='Home_SCA', blank=True, null=True)  # Field name made lowercase.
    home_gca = models.FloatField(db_column='Home_GCA', blank=True, null=True)  # Field name made lowercase.
    home_cmp_passes = models.FloatField(db_column='Home_Cmp_Passes', blank=True, null=True)  # Field name made lowercase.
    home_att_passes = models.FloatField(db_column='Home_Att_Passes', blank=True, null=True)  # Field name made lowercase.
    home_cmp_percent_passes = models.FloatField(db_column='Home_Cmp_percent_Passes', blank=True, null=True)  # Field name made lowercase.
    home_prgp_passes = models.FloatField(db_column='Home_PrgP_Passes', blank=True, null=True)  # Field name made lowercase.
    home_carries_carries = models.FloatField(db_column='Home_Carries_Carries', blank=True, null=True)  # Field name made lowercase.
    home_prgc_carries = models.FloatField(db_column='Home_PrgC_Carries', blank=True, null=True)  # Field name made lowercase.
    home_att_take_ons = models.FloatField(db_column='Home_Att_Take_Ons', blank=True, null=True)  # Field name made lowercase.
    home_succ_take_ons = models.FloatField(db_column='Home_Succ_Take_Ons', blank=True, null=True)  # Field name made lowercase.
    away_team = models.CharField(db_column='Away_Team', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    away_manager = models.CharField(db_column='Away_Manager', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    away_captain = models.CharField(db_column='Away_Captain', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    away_formation = models.CharField(db_column='Away_Formation', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    away_possession = models.FloatField(db_column='Away_Possession', blank=True, null=True)  # Field name made lowercase.
    away_fouls = models.FloatField(db_column='Away_Fouls', blank=True, null=True)  # Field name made lowercase.
    away_corners = models.FloatField(db_column='Away_Corners', blank=True, null=True)  # Field name made lowercase.
    away_crosses = models.FloatField(db_column='Away_Crosses', blank=True, null=True)  # Field name made lowercase.
    away_aerials_won = models.FloatField(db_column='Away_Aerials_Won', blank=True, null=True)  # Field name made lowercase.
    away_clearances = models.FloatField(db_column='Away_Clearances', blank=True, null=True)  # Field name made lowercase.
    away_offsides = models.FloatField(db_column='Away_Offsides', blank=True, null=True)  # Field name made lowercase.
    away_goal_kicks = models.FloatField(db_column='Away_Goal_Kicks', blank=True, null=True)  # Field name made lowercase.
    away_throw_ins = models.FloatField(db_column='Away_Throw_Ins', blank=True, null=True)  # Field name made lowercase.
    away_long_balls = models.FloatField(db_column='Away_Long_Balls', blank=True, null=True)  # Field name made lowercase.
    away_total_players_stats = models.FloatField(db_column='Away_Total_Players_Stats', blank=True, null=True)  # Field name made lowercase.
    away_minutes = models.FloatField(db_column='Away_Minutes', blank=True, null=True)  # Field name made lowercase.
    away_gls = models.FloatField(db_column='Away_Gls', blank=True, null=True)  # Field name made lowercase.
    away_ast = models.FloatField(db_column='Away_Ast', blank=True, null=True)  # Field name made lowercase.
    away_pk = models.FloatField(db_column='Away_PK', blank=True, null=True)  # Field name made lowercase.
    away_pk_att = models.FloatField(db_column='Away_PK_Att', blank=True, null=True)  # Field name made lowercase.
    away_sh = models.FloatField(db_column='Away_Sh', blank=True, null=True)  # Field name made lowercase.
    away_sot = models.FloatField(db_column='Away_SoT', blank=True, null=True)  # Field name made lowercase.
    away_crdy = models.FloatField(db_column='Away_CrdY', blank=True, null=True)  # Field name made lowercase.
    away_crdr = models.FloatField(db_column='Away_CrdR', blank=True, null=True)  # Field name made lowercase.
    away_touches = models.FloatField(db_column='Away_Touches', blank=True, null=True)  # Field name made lowercase.
    away_tkl = models.FloatField(db_column='Away_Tkl', blank=True, null=True)  # Field name made lowercase.
    away_int = models.FloatField(db_column='Away_Int', blank=True, null=True)  # Field name made lowercase.
    away_blocks = models.FloatField(db_column='Away_Blocks', blank=True, null=True)  # Field name made lowercase.
    away_xg = models.FloatField(db_column='Away_xG', blank=True, null=True)  # Field name made lowercase.
    away_npxg = models.FloatField(db_column='Away_npxG', blank=True, null=True)  # Field name made lowercase.
    away_xag = models.FloatField(db_column='Away_xAG', blank=True, null=True)  # Field name made lowercase.
    away_sca = models.FloatField(db_column='Away_SCA', blank=True, null=True)  # Field name made lowercase.
    away_gca = models.FloatField(db_column='Away_GCA', blank=True, null=True)  # Field name made lowercase.
    away_cmp_passes = models.FloatField(db_column='Away_Cmp_Passes', blank=True, null=True)  # Field name made lowercase.
    away_att_passes = models.FloatField(db_column='Away_Att_Passes', blank=True, null=True)  # Field name made lowercase.
    away_cmp_percent_passes = models.FloatField(db_column='Away_Cmp_percent_Passes', blank=True, null=True)  # Field name made lowercase.
    away_prgp_passes = models.FloatField(db_column='Away_PrgP_Passes', blank=True, null=True)  # Field name made lowercase.
    away_carries_carries = models.FloatField(db_column='Away_Carries_Carries', blank=True, null=True)  # Field name made lowercase.
    away_prgc_carries = models.FloatField(db_column='Away_PrgC_Carries', blank=True, null=True)  # Field name made lowercase.
    away_att_take_ons = models.FloatField(db_column='Away_Att_Take_Ons', blank=True, null=True)  # Field name made lowercase.
    away_succ_take_ons = models.FloatField(db_column='Away_Succ_Take_Ons', blank=True, null=True)  # Field name made lowercase.
    home_attack = models.FloatField(db_column='Home_Attack', blank=True, null=True)  # Field name made lowercase.
    home_midfield = models.FloatField(db_column='Home_Midfield', blank=True, null=True)  # Field name made lowercase.
    home_defense = models.FloatField(db_column='Home_Defense', blank=True, null=True)  # Field name made lowercase.
    away_attack = models.FloatField(db_column='Away_Attack', blank=True, null=True)  # Field name made lowercase.
    away_midfield = models.FloatField(db_column='Away_Midfield', blank=True, null=True)  # Field name made lowercase.
    away_defense = models.FloatField(db_column='Away_Defense', blank=True, null=True)  # Field name made lowercase.
    home_score = models.FloatField(db_column='Home_Score', blank=True, null=True)  # Field name made lowercase.
    away_score = models.FloatField(db_column='Away_Score', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'matchs_dataset_model'


class MatchsquadPlayers(models.Model):
    match_id = models.CharField(db_column='Match_Id', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    match_date = models.DateField(db_column='Match_Date', blank=True, null=True)  # Field name made lowercase.
    team = models.CharField(db_column='Team', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    player_name = models.CharField(db_column='Player_Name', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    player_kitnum = models.IntegerField(db_column='Player_Kitnum', blank=True, null=True)  # Field name made lowercase.
    is_sub = models.CharField(db_column='Is_Sub', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    sofifa_id = models.CharField(db_column='Sofifa_Id', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    player_position = models.CharField(db_column='Player_Position', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    player_overall_rating = models.FloatField(db_column='Player_Overall_Rating', blank=True, null=True)  # Field name made lowercase.
    player_update_date = models.DateField(db_column='Player_Update_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'matchsquad_players'


class SofifaPlayersAttrModified(models.Model):
    acceleration = models.FloatField(db_column='Acceleration', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    aggression = models.FloatField(db_column='Aggression', blank=True, null=True)  # Field name made lowercase.
    agility = models.FloatField(db_column='Agility', blank=True, null=True)  # Field name made lowercase.
    all_positions = models.CharField(db_column='All_Positions', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    attacking_work_rate = models.CharField(db_column='Attacking_Work_Rate', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    balance = models.FloatField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    ball_control = models.FloatField(db_column='Ball_Control', blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateField(db_column='Birthday', blank=True, null=True)  # Field name made lowercase.
    body_type = models.CharField(db_column='Body_Type', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    composure = models.FloatField(db_column='Composure', blank=True, null=True)  # Field name made lowercase.
    crossing = models.FloatField(db_column='Crossing', blank=True, null=True)  # Field name made lowercase.
    curve = models.FloatField(db_column='Curve', blank=True, null=True)  # Field name made lowercase.
    defensive_awareness = models.FloatField(db_column='Defensive_Awareness', blank=True, null=True)  # Field name made lowercase.
    defensive_work_rate = models.CharField(db_column='Defensive_Work_Rate', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    dribbling = models.FloatField(db_column='Dribbling', blank=True, null=True)  # Field name made lowercase.
    finishing = models.FloatField(db_column='Finishing', blank=True, null=True)  # Field name made lowercase.
    fk_accuracy = models.FloatField(db_column='Fk_Accuracy', blank=True, null=True)  # Field name made lowercase.
    gk_diving = models.FloatField(db_column='Gk_Diving', blank=True, null=True)  # Field name made lowercase.
    gk_handling = models.FloatField(db_column='Gk_Handling', blank=True, null=True)  # Field name made lowercase.
    gk_kicking = models.FloatField(db_column='Gk_Kicking', blank=True, null=True)  # Field name made lowercase.
    gk_positioning = models.FloatField(db_column='Gk_Positioning', blank=True, null=True)  # Field name made lowercase.
    gk_reflexes = models.FloatField(db_column='Gk_Reflexes', blank=True, null=True)  # Field name made lowercase.
    heading_accuracy = models.FloatField(db_column='Heading_Accuracy', blank=True, null=True)  # Field name made lowercase.
    height = models.CharField(db_column='Height', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    interceptions = models.FloatField(db_column='Interceptions', blank=True, null=True)  # Field name made lowercase.
    jumping = models.FloatField(db_column='Jumping', blank=True, null=True)  # Field name made lowercase.
    long_passing = models.FloatField(db_column='Long_Passing', blank=True, null=True)  # Field name made lowercase.
    long_shots = models.FloatField(db_column='Long_Shots', blank=True, null=True)  # Field name made lowercase.
    marking = models.FloatField(db_column='Marking', blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    overall_rating = models.FloatField(db_column='Overall_Rating', blank=True, null=True)  # Field name made lowercase.
    penalties = models.FloatField(db_column='Penalties', blank=True, null=True)  # Field name made lowercase.
    player_full_name = models.CharField(db_column='Player_Full_Name', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    player_name = models.CharField(db_column='Player_Name', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    positioning = models.FloatField(db_column='Positioning', blank=True, null=True)  # Field name made lowercase.
    potential = models.FloatField(db_column='Potential', blank=True, null=True)  # Field name made lowercase.
    preferred_foot = models.CharField(db_column='Preferred_Foot', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    reactions = models.FloatField(db_column='Reactions', blank=True, null=True)  # Field name made lowercase.
    real_face = models.CharField(db_column='Real_Face', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    reputation = models.FloatField(db_column='Reputation', blank=True, null=True)  # Field name made lowercase.
    short_passing = models.FloatField(db_column='Short_Passing', blank=True, null=True)  # Field name made lowercase.
    shot_power = models.FloatField(db_column='Shot_Power', blank=True, null=True)  # Field name made lowercase.
    skill_moves = models.FloatField(db_column='Skill_Moves', blank=True, null=True)  # Field name made lowercase.
    sliding_tackle = models.FloatField(db_column='Sliding_Tackle', blank=True, null=True)  # Field name made lowercase.
    sofifa_id = models.CharField(db_column='Sofifa_Id', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    specialities = models.CharField(db_column='Specialities', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    sprint_speed = models.FloatField(db_column='Sprint_Speed', blank=True, null=True)  # Field name made lowercase.
    stamina = models.FloatField(db_column='Stamina', blank=True, null=True)  # Field name made lowercase.
    standing_tackle = models.FloatField(db_column='Standing_Tackle', blank=True, null=True)  # Field name made lowercase.
    strength = models.FloatField(db_column='Strength', blank=True, null=True)  # Field name made lowercase.
    team1 = models.CharField(db_column='Team1', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    team1_contract = models.IntegerField(db_column='Team1_Contract', blank=True, null=True)  # Field name made lowercase.
    team1_joined = models.DateField(db_column='Team1_Joined', blank=True, null=True)  # Field name made lowercase.
    team1_kitnum = models.IntegerField(db_column='Team1_Kitnum', blank=True, null=True)  # Field name made lowercase.
    team1_loaned_from = models.CharField(db_column='Team1_Loaned_From', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    team1_position = models.CharField(db_column='Team1_Position', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    team1_rating = models.FloatField(db_column='Team1_Rating', blank=True, null=True)  # Field name made lowercase.
    team2 = models.CharField(db_column='Team2', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    team2_kitnum = models.IntegerField(db_column='Team2_Kitnum', blank=True, null=True)  # Field name made lowercase.
    team2_position = models.CharField(db_column='Team2_Position', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    team2_rating = models.FloatField(db_column='Team2_Rating', blank=True, null=True)  # Field name made lowercase.
    traits = models.CharField(db_column='Traits', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateField(db_column='Update_Date', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    vision = models.FloatField(db_column='Vision', blank=True, null=True)  # Field name made lowercase.
    volleys = models.FloatField(db_column='Volleys', blank=True, null=True)  # Field name made lowercase.
    wage = models.CharField(db_column='Wage', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    weak_foot = models.FloatField(db_column='Weak_Foot', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sofifa_players_attr_modified'


class SofifaPlayersInfosModified(models.Model):
    player_id = models.CharField(db_column='Player_Id', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateField(db_column='Birthday', blank=True, null=True)  # Field name made lowercase.
    player_full_name = models.CharField(db_column='Player_Full_Name', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    player_name = models.CharField(db_column='Player_Name', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    team_club = models.CharField(db_column='Team_Club', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    height = models.FloatField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sofifa_players_infos_modified'

class View_Scores_And_Fixtures(models.Model):
    match_id = models.CharField(max_length=255)
    league = models.CharField(db_column='League', max_length=255)
    season = models.CharField(db_column='Season',max_length=255)
    match_week = models.CharField(max_length=255)
    home_team = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)
    match_date = models.DateField()
    venue_time = models.CharField(max_length=255)
    attendance = models.IntegerField()
    stadium = models.CharField(max_length=255)
    officials = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    home_score = models.IntegerField()
    away_score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'view_scores_and_fixtures'

class FutureMatches(models.Model):
    match_id = models.CharField(db_column='match_id', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    match_date = models.DateField(db_column='Match_Date', blank=True, null=True)  # Field name made lowercase.
    home_team = models.CharField(db_column='Home_Team', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    home_manager = models.CharField(db_column='Home_Manager', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    home_captain = models.CharField(db_column='Home_Captain', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    home_formation = models.CharField(db_column='Home_Formation', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    home_possession = models.FloatField(db_column='Home_Possession', blank=True, null=True)  # Field name made lowercase.
    home_fouls = models.FloatField(db_column='Home_Fouls', blank=True, null=True)  # Field name made lowercase.
    home_corners = models.FloatField(db_column='Home_Corners', blank=True, null=True)  # Field name made lowercase.
    home_crosses = models.FloatField(db_column='Home_Crosses', blank=True, null=True)  # Field name made lowercase.
    home_aerials_won = models.FloatField(db_column='Home_Aerials_Won', blank=True, null=True)  # Field name made lowercase.
    home_clearances = models.FloatField(db_column='Home_Clearances', blank=True, null=True)  # Field name made lowercase.
    home_offsides = models.FloatField(db_column='Home_Offsides', blank=True, null=True)  # Field name made lowercase.
    home_goal_kicks = models.FloatField(db_column='Home_Goal_Kicks', blank=True, null=True)  # Field name made lowercase.
    home_throw_ins = models.FloatField(db_column='Home_Throw_Ins', blank=True, null=True)  # Field name made lowercase.
    home_long_balls = models.FloatField(db_column='Home_Long_Balls', blank=True, null=True)  # Field name made lowercase.
    home_total_players_stats = models.FloatField(db_column='Home_Total_Players_Stats', blank=True, null=True)  # Field name made lowercase.
    home_minutes = models.FloatField(db_column='Home_Minutes', blank=True, null=True)  # Field name made lowercase.
    home_gls = models.FloatField(db_column='Home_Gls', blank=True, null=True)  # Field name made lowercase.
    home_ast = models.FloatField(db_column='Home_Ast', blank=True, null=True)  # Field name made lowercase.
    home_pk = models.FloatField(db_column='Home_PK', blank=True, null=True)  # Field name made lowercase.
    home_pk_att = models.FloatField(db_column='Home_PK_Att', blank=True, null=True)  # Field name made lowercase.
    home_sh = models.FloatField(db_column='Home_Sh', blank=True, null=True)  # Field name made lowercase.
    home_sot = models.FloatField(db_column='Home_SoT', blank=True, null=True)  # Field name made lowercase.
    home_crdy = models.FloatField(db_column='Home_CrdY', blank=True, null=True)  # Field name made lowercase.
    home_crdr = models.FloatField(db_column='Home_CrdR', blank=True, null=True)  # Field name made lowercase.
    home_touches = models.FloatField(db_column='Home_Touches', blank=True, null=True)  # Field name made lowercase.
    home_tkl = models.FloatField(db_column='Home_Tkl', blank=True, null=True)  # Field name made lowercase.
    home_int = models.FloatField(db_column='Home_Int', blank=True, null=True)  # Field name made lowercase.
    home_blocks = models.FloatField(db_column='Home_Blocks', blank=True, null=True)  # Field name made lowercase.
    home_xg = models.FloatField(db_column='Home_xG', blank=True, null=True)  # Field name made lowercase.
    home_npxg = models.FloatField(db_column='Home_npxG', blank=True, null=True)  # Field name made lowercase.
    home_xag = models.FloatField(db_column='Home_xAG', blank=True, null=True)  # Field name made lowercase.
    home_sca = models.FloatField(db_column='Home_SCA', blank=True, null=True)  # Field name made lowercase.
    home_gca = models.FloatField(db_column='Home_GCA', blank=True, null=True)  # Field name made lowercase.
    home_cmp_passes = models.FloatField(db_column='Home_Cmp_Passes', blank=True, null=True)  # Field name made lowercase.
    home_att_passes = models.FloatField(db_column='Home_Att_Passes', blank=True, null=True)  # Field name made lowercase.
    home_cmp_percent_passes = models.FloatField(db_column='Home_Cmp_percent_Passes', blank=True, null=True)  # Field name made lowercase.
    home_prgp_passes = models.FloatField(db_column='Home_PrgP_Passes', blank=True, null=True)  # Field name made lowercase.
    home_carries_carries = models.FloatField(db_column='Home_Carries_Carries', blank=True, null=True)  # Field name made lowercase.
    home_prgc_carries = models.FloatField(db_column='Home_PrgC_Carries', blank=True, null=True)  # Field name made lowercase.
    home_att_take_ons = models.FloatField(db_column='Home_Att_Take_Ons', blank=True, null=True)  # Field name made lowercase.
    home_succ_take_ons = models.FloatField(db_column='Home_Succ_Take_Ons', blank=True, null=True)  # Field name made lowercase.
    away_team = models.CharField(db_column='Away_Team', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    away_manager = models.CharField(db_column='Away_Manager', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    away_captain = models.CharField(db_column='Away_Captain', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    away_formation = models.CharField(db_column='Away_Formation', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    away_possession = models.FloatField(db_column='Away_Possession', blank=True, null=True)  # Field name made lowercase.
    away_fouls = models.FloatField(db_column='Away_Fouls', blank=True, null=True)  # Field name made lowercase.
    away_corners = models.FloatField(db_column='Away_Corners', blank=True, null=True)  # Field name made lowercase.
    away_crosses = models.FloatField(db_column='Away_Crosses', blank=True, null=True)  # Field name made lowercase.
    away_aerials_won = models.FloatField(db_column='Away_Aerials_Won', blank=True, null=True)  # Field name made lowercase.
    away_clearances = models.FloatField(db_column='Away_Clearances', blank=True, null=True)  # Field name made lowercase.
    away_offsides = models.FloatField(db_column='Away_Offsides', blank=True, null=True)  # Field name made lowercase.
    away_goal_kicks = models.FloatField(db_column='Away_Goal_Kicks', blank=True, null=True)  # Field name made lowercase.
    away_throw_ins = models.FloatField(db_column='Away_Throw_Ins', blank=True, null=True)  # Field name made lowercase.
    away_long_balls = models.FloatField(db_column='Away_Long_Balls', blank=True, null=True)  # Field name made lowercase.
    away_total_players_stats = models.FloatField(db_column='Away_Total_Players_Stats', blank=True, null=True)  # Field name made lowercase.
    away_minutes = models.FloatField(db_column='Away_Minutes', blank=True, null=True)  # Field name made lowercase.
    away_gls = models.FloatField(db_column='Away_Gls', blank=True, null=True)  # Field name made lowercase.
    away_ast = models.FloatField(db_column='Away_Ast', blank=True, null=True)  # Field name made lowercase.
    away_pk = models.FloatField(db_column='Away_PK', blank=True, null=True)  # Field name made lowercase.
    away_pk_att = models.FloatField(db_column='Away_PK_Att', blank=True, null=True)  # Field name made lowercase.
    away_sh = models.FloatField(db_column='Away_Sh', blank=True, null=True)  # Field name made lowercase.
    away_sot = models.FloatField(db_column='Away_SoT', blank=True, null=True)  # Field name made lowercase.
    away_crdy = models.FloatField(db_column='Away_CrdY', blank=True, null=True)  # Field name made lowercase.
    away_crdr = models.FloatField(db_column='Away_CrdR', blank=True, null=True)  # Field name made lowercase.
    away_touches = models.FloatField(db_column='Away_Touches', blank=True, null=True)  # Field name made lowercase.
    away_tkl = models.FloatField(db_column='Away_Tkl', blank=True, null=True)  # Field name made lowercase.
    away_int = models.FloatField(db_column='Away_Int', blank=True, null=True)  # Field name made lowercase.
    away_blocks = models.FloatField(db_column='Away_Blocks', blank=True, null=True)  # Field name made lowercase.
    away_xg = models.FloatField(db_column='Away_xG', blank=True, null=True)  # Field name made lowercase.
    away_npxg = models.FloatField(db_column='Away_npxG', blank=True, null=True)  # Field name made lowercase.
    away_xag = models.FloatField(db_column='Away_xAG', blank=True, null=True)  # Field name made lowercase.
    away_sca = models.FloatField(db_column='Away_SCA', blank=True, null=True)  # Field name made lowercase.
    away_gca = models.FloatField(db_column='Away_GCA', blank=True, null=True)  # Field name made lowercase.
    away_cmp_passes = models.FloatField(db_column='Away_Cmp_Passes', blank=True, null=True)  # Field name made lowercase.
    away_att_passes = models.FloatField(db_column='Away_Att_Passes', blank=True, null=True)  # Field name made lowercase.
    away_cmp_percent_passes = models.FloatField(db_column='Away_Cmp_percent_Passes', blank=True, null=True)  # Field name made lowercase.
    away_prgp_passes = models.FloatField(db_column='Away_PrgP_Passes', blank=True, null=True)  # Field name made lowercase.
    away_carries_carries = models.FloatField(db_column='Away_Carries_Carries', blank=True, null=True)  # Field name made lowercase.
    away_prgc_carries = models.FloatField(db_column='Away_PrgC_Carries', blank=True, null=True)  # Field name made lowercase.
    away_att_take_ons = models.FloatField(db_column='Away_Att_Take_Ons', blank=True, null=True)  # Field name made lowercase.
    away_succ_take_ons = models.FloatField(db_column='Away_Succ_Take_Ons', blank=True, null=True)  # Field name made lowercase.
    home_attack = models.FloatField(db_column='Home_Attack', blank=True, null=True)  # Field name made lowercase.
    home_midfield = models.FloatField(db_column='Home_Midfield', blank=True, null=True)  # Field name made lowercase.
    home_defense = models.FloatField(db_column='Home_Defense', blank=True, null=True)  # Field name made lowercase.
    away_attack = models.FloatField(db_column='Away_Attack', blank=True, null=True)  # Field name made lowercase.
    away_midfield = models.FloatField(db_column='Away_Midfield', blank=True, null=True)  # Field name made lowercase.
    away_defense = models.FloatField(db_column='Away_Defense', blank=True, null=True)  # Field name made lowercase.
    home_score = models.FloatField(db_column='Home_Score', blank=True, null=True)  # Field name made lowercase.
    away_score = models.FloatField(db_column='Away_Score', blank=True, null=True)  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'future_matches'


class TeamOptimization(models.Model):
    sofifa_id = models.CharField(db_column='Sofifa_Id', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    team1 = models.CharField(db_column='Team1', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    team2 = models.CharField(db_column='Team2', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    player_name = models.CharField(db_column='Player_Name', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    all_positions = models.CharField(db_column='All_Positions', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    overall_rating = models.FloatField(db_column='Overall_Rating', blank=True, null=True)  # Field name made lowercase.
    potential = models.FloatField(db_column='Potential', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    team1_position = models.CharField(db_column='Team1_Position', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'team_optimization'