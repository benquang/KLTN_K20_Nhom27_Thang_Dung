# Generated by Django 5.0 on 2023-12-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('API', '0004_delete_fbref_matchgoals_modified_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FbrefMatchgoalsModified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Match_Id', max_length=100, null=True)),
                ('team', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Team', max_length=100, null=True)),
                ('minute', models.FloatField(blank=True, db_column='Minute', null=True)),
                ('player_name', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Player_Name', max_length=100, null=True)),
                ('type_of_goal', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Type_Of_Goal', max_length=100, null=True)),
                ('is_home_team', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Is_Home_Team', max_length=100, null=True)),
            ],
            options={
                'db_table': 'fbref_matchgoals_modified',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FbrefMatchinfosModified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Match_Id', max_length=100, null=True)),
                ('league', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='League', max_length=100, null=True)),
                ('season', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Season', max_length=100, null=True)),
                ('match_week', models.IntegerField(blank=True, db_column='Match_Week', null=True)),
                ('home_team', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Home_Team', max_length=100, null=True)),
                ('away_team', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Away_Team', max_length=100, null=True)),
                ('match_date', models.DateField(blank=True, db_column='Match_Date', null=True)),
                ('venue_time', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Venue_Time', max_length=100, null=True)),
                ('attendance', models.IntegerField(blank=True, db_column='Attendance', null=True)),
                ('stadium', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Stadium', max_length=100, null=True)),
                ('officials', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Officials', max_length=1000, null=True)),
                ('link', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Link', max_length=200, null=True)),
            ],
            options={
                'db_table': 'fbref_matchinfos_modified',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FbrefMatchplayerstatsModified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Match_Id', max_length=100, null=True)),
                ('team', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Team', max_length=100, null=True)),
                ('player_name', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Player_Name', max_length=100, null=True)),
                ('player_kitnum', models.IntegerField(blank=True, db_column='Player_Kitnum', null=True)),
                ('nationality', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Nationality', max_length=100, null=True)),
                ('position', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Position', max_length=100, null=True)),
                ('age', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Age', max_length=100, null=True)),
                ('minutes', models.FloatField(blank=True, db_column='Minutes', null=True)),
                ('gls', models.FloatField(blank=True, db_column='Gls', null=True)),
                ('ast', models.FloatField(blank=True, db_column='Ast', null=True)),
                ('PK', models.FloatField(blank=True, db_column='PK', null=True)),
                ('pk_att', models.FloatField(blank=True, db_column='PK_Att', null=True)),
                ('sh', models.FloatField(blank=True, db_column='Sh', null=True)),
                ('sot', models.FloatField(blank=True, db_column='SoT', null=True)),
                ('crdy', models.FloatField(blank=True, db_column='CrdY', null=True)),
                ('crdr', models.FloatField(blank=True, db_column='CrdR', null=True)),
                ('touches', models.FloatField(blank=True, db_column='Touches', null=True)),
                ('tkl', models.FloatField(blank=True, db_column='Tkl', null=True)),
                ('int', models.FloatField(blank=True, db_column='Int', null=True)),
                ('blocks', models.FloatField(blank=True, db_column='Blocks', null=True)),
                ('xg', models.FloatField(blank=True, db_column='xG', null=True)),
                ('npxg', models.FloatField(blank=True, db_column='npxG', null=True)),
                ('xag', models.FloatField(blank=True, db_column='xAG', null=True)),
                ('sca', models.FloatField(blank=True, db_column='SCA', null=True)),
                ('gca', models.FloatField(blank=True, db_column='GCA', null=True)),
                ('passes_cmp', models.FloatField(blank=True, db_column='Passes_Cmp', null=True)),
                ('passes_att', models.FloatField(blank=True, db_column='Passes_Att', null=True)),
                ('passes_cmp_percentage', models.FloatField(blank=True, db_column='Passes_Cmp_Percentage', null=True)),
                ('passes_prgp', models.FloatField(blank=True, db_column='Passes_PrgP', null=True)),
                ('carries', models.FloatField(blank=True, db_column='Carries', null=True)),
                ('carries_prgc', models.FloatField(blank=True, db_column='Carries_PrgC', null=True)),
                ('take_ons_att', models.FloatField(blank=True, db_column='Take_Ons_Att', null=True)),
                ('take_ons_succ', models.FloatField(blank=True, db_column='Take_Ons_Succ', null=True)),
            ],
            options={
                'db_table': 'fbref_matchplayerstats_modified',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FbrefMatchsquadModified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Match_Id', max_length=100, null=True)),
                ('team', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Team', max_length=100, null=True)),
                ('is_home_team', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Is_Home_Team', max_length=100, null=True)),
                ('player_name', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Player_Name', max_length=100, null=True)),
                ('player_kitnum', models.IntegerField(blank=True, db_column='Player_Kitnum', null=True)),
                ('is_sub', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Is_Sub', max_length=100, null=True)),
            ],
            options={
                'db_table': 'fbref_matchsquad_modified',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FbrefMatchstatsModified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Match_Id', max_length=100, null=True)),
                ('team', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Team', max_length=100, null=True)),
                ('is_home_team', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Is_Home_Team', max_length=100, null=True)),
                ('manager', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Manager', max_length=100, null=True)),
                ('captain', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Captain', max_length=100, null=True)),
                ('formation', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Formation', max_length=100, null=True)),
                ('possession', models.FloatField(blank=True, db_column='Possession', null=True)),
                ('fouls', models.FloatField(blank=True, db_column='Fouls', null=True)),
                ('corners', models.FloatField(blank=True, db_column='Corners', null=True)),
                ('crosses', models.FloatField(blank=True, db_column='Crosses', null=True)),
                ('aerials_won', models.FloatField(blank=True, db_column='Aerials_Won', null=True)),
                ('clearances', models.FloatField(blank=True, db_column='Clearances', null=True)),
                ('offsides', models.FloatField(blank=True, db_column='Offsides', null=True)),
                ('goal_kicks', models.FloatField(blank=True, db_column='Goal_Kicks', null=True)),
                ('throw_ins', models.FloatField(blank=True, db_column='Throw_Ins', null=True)),
                ('long_balls', models.FloatField(blank=True, db_column='Long_Balls', null=True)),
                ('total_players_stats', models.FloatField(blank=True, db_column='Total_Players_Stats', null=True)),
                ('minutes', models.FloatField(blank=True, db_column='Minutes', null=True)),
                ('gls', models.FloatField(blank=True, db_column='Gls', null=True)),
                ('ast', models.FloatField(blank=True, db_column='Ast', null=True)),
                ('PK', models.FloatField(blank=True, db_column='PK', null=True)),
                ('pk_att', models.FloatField(blank=True, db_column='PK_Att', null=True)),
                ('sh', models.FloatField(blank=True, db_column='Sh', null=True)),
                ('sot', models.FloatField(blank=True, db_column='SoT', null=True)),
                ('crdy', models.FloatField(blank=True, db_column='CrdY', null=True)),
                ('crdr', models.FloatField(blank=True, db_column='CrdR', null=True)),
                ('touches', models.FloatField(blank=True, db_column='Touches', null=True)),
                ('tkl', models.FloatField(blank=True, db_column='Tkl', null=True)),
                ('int', models.FloatField(blank=True, db_column='Int', null=True)),
                ('blocks', models.FloatField(blank=True, db_column='Blocks', null=True)),
                ('xg', models.FloatField(blank=True, db_column='xG', null=True)),
                ('npxg', models.FloatField(blank=True, db_column='npxG', null=True)),
                ('xag', models.FloatField(blank=True, db_column='xAG', null=True)),
                ('sca', models.FloatField(blank=True, db_column='SCA', null=True)),
                ('gca', models.FloatField(blank=True, db_column='GCA', null=True)),
                ('passes_cmp', models.FloatField(blank=True, db_column='Passes_Cmp', null=True)),
                ('passes_att', models.FloatField(blank=True, db_column='Passes_Att', null=True)),
                ('passes_cmp_percentage', models.FloatField(blank=True, db_column='Passes_Cmp_Percentage', null=True)),
                ('passes_prgp', models.FloatField(blank=True, db_column='Passes_PrgP', null=True)),
                ('carries', models.FloatField(blank=True, db_column='Carries', null=True)),
                ('carries_prgc', models.FloatField(blank=True, db_column='Carries_PrgC', null=True)),
                ('take_ons_att', models.FloatField(blank=True, db_column='Take_Ons_Att', null=True)),
                ('take_ons_succ', models.FloatField(blank=True, db_column='Take_Ons_Succ', null=True)),
                ('score', models.FloatField(blank=True, db_column='Score', null=True)),
            ],
            options={
                'db_table': 'fbref_matchstats_modified',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MatchsDatasetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='match_id', max_length=100, null=True)),
                ('match_date', models.DateField(blank=True, db_column='Match_Date', null=True)),
                ('home_team', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Home_Team', max_length=100, null=True)),
                ('home_manager', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Home_Manager', max_length=100, null=True)),
                ('home_captain', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Home_Captain', max_length=100, null=True)),
                ('home_formation', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Home_Formation', max_length=100, null=True)),
                ('home_possession', models.FloatField(blank=True, db_column='Home_Possession', null=True)),
                ('home_fouls', models.FloatField(blank=True, db_column='Home_Fouls', null=True)),
                ('home_corners', models.FloatField(blank=True, db_column='Home_Corners', null=True)),
                ('home_crosses', models.FloatField(blank=True, db_column='Home_Crosses', null=True)),
                ('home_aerials_won', models.FloatField(blank=True, db_column='Home_Aerials_Won', null=True)),
                ('home_clearances', models.FloatField(blank=True, db_column='Home_Clearances', null=True)),
                ('home_offsides', models.FloatField(blank=True, db_column='Home_Offsides', null=True)),
                ('home_goal_kicks', models.FloatField(blank=True, db_column='Home_Goal_Kicks', null=True)),
                ('home_throw_ins', models.FloatField(blank=True, db_column='Home_Throw_Ins', null=True)),
                ('home_long_balls', models.FloatField(blank=True, db_column='Home_Long_Balls', null=True)),
                ('home_total_players_stats', models.FloatField(blank=True, db_column='Home_Total_Players_Stats', null=True)),
                ('home_minutes', models.FloatField(blank=True, db_column='Home_Minutes', null=True)),
                ('home_gls', models.FloatField(blank=True, db_column='Home_Gls', null=True)),
                ('home_ast', models.FloatField(blank=True, db_column='Home_Ast', null=True)),
                ('home_pk', models.FloatField(blank=True, db_column='Home_PK', null=True)),
                ('home_pk_att', models.FloatField(blank=True, db_column='Home_PK_Att', null=True)),
                ('home_sh', models.FloatField(blank=True, db_column='Home_Sh', null=True)),
                ('home_sot', models.FloatField(blank=True, db_column='Home_SoT', null=True)),
                ('home_crdy', models.FloatField(blank=True, db_column='Home_CrdY', null=True)),
                ('home_crdr', models.FloatField(blank=True, db_column='Home_CrdR', null=True)),
                ('home_touches', models.FloatField(blank=True, db_column='Home_Touches', null=True)),
                ('home_tkl', models.FloatField(blank=True, db_column='Home_Tkl', null=True)),
                ('home_int', models.FloatField(blank=True, db_column='Home_Int', null=True)),
                ('home_blocks', models.FloatField(blank=True, db_column='Home_Blocks', null=True)),
                ('home_xg', models.FloatField(blank=True, db_column='Home_xG', null=True)),
                ('home_npxg', models.FloatField(blank=True, db_column='Home_npxG', null=True)),
                ('home_xag', models.FloatField(blank=True, db_column='Home_xAG', null=True)),
                ('home_sca', models.FloatField(blank=True, db_column='Home_SCA', null=True)),
                ('home_gca', models.FloatField(blank=True, db_column='Home_GCA', null=True)),
                ('home_cmp_passes', models.FloatField(blank=True, db_column='Home_Cmp_Passes', null=True)),
                ('home_att_passes', models.FloatField(blank=True, db_column='Home_Att_Passes', null=True)),
                ('home_cmp_percent_passes', models.FloatField(blank=True, db_column='Home_Cmp_percent_Passes', null=True)),
                ('home_prgp_passes', models.FloatField(blank=True, db_column='Home_PrgP_Passes', null=True)),
                ('home_carries_carries', models.FloatField(blank=True, db_column='Home_Carries_Carries', null=True)),
                ('home_prgc_carries', models.FloatField(blank=True, db_column='Home_PrgC_Carries', null=True)),
                ('home_att_take_ons', models.FloatField(blank=True, db_column='Home_Att_Take_Ons', null=True)),
                ('home_succ_take_ons', models.FloatField(blank=True, db_column='Home_Succ_Take_Ons', null=True)),
                ('away_team', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Away_Team', max_length=100, null=True)),
                ('away_manager', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Away_Manager', max_length=100, null=True)),
                ('away_captain', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Away_Captain', max_length=100, null=True)),
                ('away_formation', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Away_Formation', max_length=100, null=True)),
                ('away_possession', models.FloatField(blank=True, db_column='Away_Possession', null=True)),
                ('away_fouls', models.FloatField(blank=True, db_column='Away_Fouls', null=True)),
                ('away_corners', models.FloatField(blank=True, db_column='Away_Corners', null=True)),
                ('away_crosses', models.FloatField(blank=True, db_column='Away_Crosses', null=True)),
                ('away_aerials_won', models.FloatField(blank=True, db_column='Away_Aerials_Won', null=True)),
                ('away_clearances', models.FloatField(blank=True, db_column='Away_Clearances', null=True)),
                ('away_offsides', models.FloatField(blank=True, db_column='Away_Offsides', null=True)),
                ('away_goal_kicks', models.FloatField(blank=True, db_column='Away_Goal_Kicks', null=True)),
                ('away_throw_ins', models.FloatField(blank=True, db_column='Away_Throw_Ins', null=True)),
                ('away_long_balls', models.FloatField(blank=True, db_column='Away_Long_Balls', null=True)),
                ('away_total_players_stats', models.FloatField(blank=True, db_column='Away_Total_Players_Stats', null=True)),
                ('away_minutes', models.FloatField(blank=True, db_column='Away_Minutes', null=True)),
                ('away_gls', models.FloatField(blank=True, db_column='Away_Gls', null=True)),
                ('away_ast', models.FloatField(blank=True, db_column='Away_Ast', null=True)),
                ('away_pk', models.FloatField(blank=True, db_column='Away_PK', null=True)),
                ('away_pk_att', models.FloatField(blank=True, db_column='Away_PK_Att', null=True)),
                ('away_sh', models.FloatField(blank=True, db_column='Away_Sh', null=True)),
                ('away_sot', models.FloatField(blank=True, db_column='Away_SoT', null=True)),
                ('away_crdy', models.FloatField(blank=True, db_column='Away_CrdY', null=True)),
                ('away_crdr', models.FloatField(blank=True, db_column='Away_CrdR', null=True)),
                ('away_touches', models.FloatField(blank=True, db_column='Away_Touches', null=True)),
                ('away_tkl', models.FloatField(blank=True, db_column='Away_Tkl', null=True)),
                ('away_int', models.FloatField(blank=True, db_column='Away_Int', null=True)),
                ('away_blocks', models.FloatField(blank=True, db_column='Away_Blocks', null=True)),
                ('away_xg', models.FloatField(blank=True, db_column='Away_xG', null=True)),
                ('away_npxg', models.FloatField(blank=True, db_column='Away_npxG', null=True)),
                ('away_xag', models.FloatField(blank=True, db_column='Away_xAG', null=True)),
                ('away_sca', models.FloatField(blank=True, db_column='Away_SCA', null=True)),
                ('away_gca', models.FloatField(blank=True, db_column='Away_GCA', null=True)),
                ('away_cmp_passes', models.FloatField(blank=True, db_column='Away_Cmp_Passes', null=True)),
                ('away_att_passes', models.FloatField(blank=True, db_column='Away_Att_Passes', null=True)),
                ('away_cmp_percent_passes', models.FloatField(blank=True, db_column='Away_Cmp_percent_Passes', null=True)),
                ('away_prgp_passes', models.FloatField(blank=True, db_column='Away_PrgP_Passes', null=True)),
                ('away_carries_carries', models.FloatField(blank=True, db_column='Away_Carries_Carries', null=True)),
                ('away_prgc_carries', models.FloatField(blank=True, db_column='Away_PrgC_Carries', null=True)),
                ('away_att_take_ons', models.FloatField(blank=True, db_column='Away_Att_Take_Ons', null=True)),
                ('away_succ_take_ons', models.FloatField(blank=True, db_column='Away_Succ_Take_Ons', null=True)),
                ('home_attack', models.FloatField(blank=True, db_column='Home_Attack', null=True)),
                ('home_midfield', models.FloatField(blank=True, db_column='Home_Midfield', null=True)),
                ('home_defense', models.FloatField(blank=True, db_column='Home_Defense', null=True)),
                ('away_attack', models.FloatField(blank=True, db_column='Away_Attack', null=True)),
                ('away_midfield', models.FloatField(blank=True, db_column='Away_Midfield', null=True)),
                ('away_defense', models.FloatField(blank=True, db_column='Away_Defense', null=True)),
                ('home_score', models.FloatField(blank=True, db_column='Home_Score', null=True)),
                ('away_score', models.FloatField(blank=True, db_column='Away_Score', null=True)),
            ],
            options={
                'db_table': 'matchs_dataset_model',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MatchsquadPlayers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Match_Id', max_length=100, null=True)),
                ('match_date', models.DateField(blank=True, db_column='Match_Date', null=True)),
                ('team', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Team', max_length=100, null=True)),
                ('player_name', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Player_Name', max_length=100, null=True)),
                ('player_kitnum', models.IntegerField(blank=True, db_column='Player_Kitnum', null=True)),
                ('is_sub', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Is_Sub', max_length=100, null=True)),
                ('sofifa_id', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Sofifa_Id', max_length=100, null=True)),
                ('player_position', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Player_Position', max_length=100, null=True)),
                ('player_overall_rating', models.FloatField(blank=True, db_column='Player_Overall_Rating', null=True)),
                ('player_update_date', models.DateField(blank=True, db_column='Player_Update_Date', null=True)),
            ],
            options={
                'db_table': 'matchsquad_players',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SofifaPlayersAttrModified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acceleration', models.FloatField(blank=True, db_column='Acceleration', null=True)),
                ('age', models.IntegerField(blank=True, db_column='Age', null=True)),
                ('aggression', models.FloatField(blank=True, db_column='Aggression', null=True)),
                ('agility', models.FloatField(blank=True, db_column='Agility', null=True)),
                ('all_positions', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='All_Positions', max_length=100, null=True)),
                ('attacking_work_rate', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Attacking_Work_Rate', max_length=100, null=True)),
                ('balance', models.FloatField(blank=True, db_column='Balance', null=True)),
                ('ball_control', models.FloatField(blank=True, db_column='Ball_Control', null=True)),
                ('birthday', models.DateField(blank=True, db_column='Birthday', null=True)),
                ('body_type', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Body_Type', max_length=100, null=True)),
                ('composure', models.FloatField(blank=True, db_column='Composure', null=True)),
                ('crossing', models.FloatField(blank=True, db_column='Crossing', null=True)),
                ('curve', models.FloatField(blank=True, db_column='Curve', null=True)),
                ('defensive_awareness', models.FloatField(blank=True, db_column='Defensive_Awareness', null=True)),
                ('defensive_work_rate', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Defensive_Work_Rate', max_length=100, null=True)),
                ('dribbling', models.FloatField(blank=True, db_column='Dribbling', null=True)),
                ('finishing', models.FloatField(blank=True, db_column='Finishing', null=True)),
                ('fk_accuracy', models.FloatField(blank=True, db_column='Fk_Accuracy', null=True)),
                ('gk_diving', models.FloatField(blank=True, db_column='Gk_Diving', null=True)),
                ('gk_handling', models.FloatField(blank=True, db_column='Gk_Handling', null=True)),
                ('gk_kicking', models.FloatField(blank=True, db_column='Gk_Kicking', null=True)),
                ('gk_positioning', models.FloatField(blank=True, db_column='Gk_Positioning', null=True)),
                ('gk_reflexes', models.FloatField(blank=True, db_column='Gk_Reflexes', null=True)),
                ('heading_accuracy', models.FloatField(blank=True, db_column='Heading_Accuracy', null=True)),
                ('height', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Height', max_length=100, null=True)),
                ('interceptions', models.FloatField(blank=True, db_column='Interceptions', null=True)),
                ('jumping', models.FloatField(blank=True, db_column='Jumping', null=True)),
                ('long_passing', models.FloatField(blank=True, db_column='Long_Passing', null=True)),
                ('long_shots', models.FloatField(blank=True, db_column='Long_Shots', null=True)),
                ('marking', models.FloatField(blank=True, db_column='Marking', null=True)),
                ('nationality', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Nationality', max_length=100, null=True)),
                ('overall_rating', models.FloatField(blank=True, db_column='Overall_Rating', null=True)),
                ('penalties', models.FloatField(blank=True, db_column='Penalties', null=True)),
                ('player_full_name', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Player_Full_Name', max_length=100, null=True)),
                ('player_name', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Player_Name', max_length=100, null=True)),
                ('positioning', models.FloatField(blank=True, db_column='Positioning', null=True)),
                ('potential', models.FloatField(blank=True, db_column='Potential', null=True)),
                ('preferred_foot', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Preferred_Foot', max_length=100, null=True)),
                ('reactions', models.FloatField(blank=True, db_column='Reactions', null=True)),
                ('real_face', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Real_Face', max_length=100, null=True)),
                ('reputation', models.FloatField(blank=True, db_column='Reputation', null=True)),
                ('short_passing', models.FloatField(blank=True, db_column='Short_Passing', null=True)),
                ('shot_power', models.FloatField(blank=True, db_column='Shot_Power', null=True)),
                ('skill_moves', models.FloatField(blank=True, db_column='Skill_Moves', null=True)),
                ('sliding_tackle', models.FloatField(blank=True, db_column='Sliding_Tackle', null=True)),
                ('sofifa_id', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Sofifa_Id', max_length=100, null=True)),
                ('specialities', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Specialities', max_length=100, null=True)),
                ('sprint_speed', models.FloatField(blank=True, db_column='Sprint_Speed', null=True)),
                ('stamina', models.FloatField(blank=True, db_column='Stamina', null=True)),
                ('standing_tackle', models.FloatField(blank=True, db_column='Standing_Tackle', null=True)),
                ('strength', models.FloatField(blank=True, db_column='Strength', null=True)),
                ('team1', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Team1', max_length=100, null=True)),
                ('team1_contract', models.IntegerField(blank=True, db_column='Team1_Contract', null=True)),
                ('team1_joined', models.DateField(blank=True, db_column='Team1_Joined', null=True)),
                ('team1_kitnum', models.IntegerField(blank=True, db_column='Team1_Kitnum', null=True)),
                ('team1_loaned_from', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Team1_Loaned_From', max_length=100, null=True)),
                ('team1_position', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Team1_Position', max_length=100, null=True)),
                ('team1_rating', models.FloatField(blank=True, db_column='Team1_Rating', null=True)),
                ('team2', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Team2', max_length=100, null=True)),
                ('team2_kitnum', models.IntegerField(blank=True, db_column='Team2_Kitnum', null=True)),
                ('team2_position', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Team2_Position', max_length=100, null=True)),
                ('team2_rating', models.FloatField(blank=True, db_column='Team2_Rating', null=True)),
                ('traits', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Traits', max_length=100, null=True)),
                ('update_date', models.DateField(blank=True, db_column='Update_Date', null=True)),
                ('value', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Value', max_length=100, null=True)),
                ('vision', models.FloatField(blank=True, db_column='Vision', null=True)),
                ('volleys', models.FloatField(blank=True, db_column='Volleys', null=True)),
                ('wage', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Wage', max_length=100, null=True)),
                ('weak_foot', models.FloatField(blank=True, db_column='Weak_Foot', null=True)),
                ('weight', models.FloatField(blank=True, db_column='Weight', null=True)),
            ],
            options={
                'db_table': 'sofifa_players_attr_modified',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SofifaPlayersInfosModified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Player_Id', max_length=100, null=True)),
                ('birthday', models.DateField(blank=True, db_column='Birthday', null=True)),
                ('player_full_name', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Player_Full_Name', max_length=100, null=True)),
                ('player_name', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Player_Name', max_length=100, null=True)),
                ('team_club', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Team_Club', max_length=100, null=True)),
                ('nationality', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Nationality', max_length=100, null=True)),
                ('height', models.FloatField(blank=True, db_column='Height', null=True)),
                ('weight', models.FloatField(blank=True, db_column='Weight', null=True)),
            ],
            options={
                'db_table': 'sofifa_players_infos_modified',
                'managed': False,
            },
        ),
    ]
