import csv
class Fbref_MatchSquad:
    def __init__(self):
        self.fbrefMatchId = None
        self.player_name = None
        self.player_kitnum = None
        self.team = None
        self.is_home_team = None
        self.is_sub = None
    
    def export_to_csv(self):
        with open('./fbref/fbref_MatchSquad.csv', 'a', newline='',encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['fbrefMatchId',
                                 'player_name',
                                 'player_kitnum',
                                 'team',
                                 'is_home_team',
                                 'is_sub'])
            writer.writerow([self.fbrefMatchId,
                             self.player_name,
                             self.player_kitnum,
                             self.team,
                             self.is_home_team,
                             self.is_sub])

class Fbref_MatchGoals:
    def __init__(self):
        self.fbrefMatchId = None
        self.player_name = None
        self.minute = None
        self.type_of_goal = None
        self.team = None
        self.is_home_team = None
    def export_to_csv(self):
        with open('./fbref/fbref_MatchGoals.csv', 'a', newline='',encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['fbrefMatchId',
                                 'player_name',
                                 'minute',
                                 'type_of_goal',
                                 'team',
                                 'is_home_team'])
            writer.writerow([self.fbrefMatchId,
                             self.player_name,
                             self.minute,
                             self.type_of_goal,
                             self.team,
                             self.is_home_team])
class Fbref_MatchStats:
    def __init__(self):
        self.fbrefMatchId = None
        self.team = None
        self.is_home_team = None
        self.score = None
        self.manager = None
        self.captain = None
        self.formation = None
        self.possession = None
        self.fouls = None
        self.corners = None
        self.crosses = None
        self.touches = None
        self.tackles = None
        self.interceptions = None
        self.aerials_won = None
        self.clearances = None
        self.offsides = None
        self.goal_kicks = None
        self.throw_ins = None
        self.long_balls = None
        self.total_players_stats = None
        self.minutes = None
        self.Gls = None
        self.Ast = None
        self.PK = None
        self.PKatt = None
        self.Sh = None
        self.SoT = None
        self.CrdY = None
        self.CrdR = None
        self.Touches = None
        self.Tkl = None
        self.Int = None
        self.Blocks = None
        self.xG = None
        self.npxG = None
        self.xAG = None
        self.SCA = None
        self.GCA = None
        self.Passes_Cmp = None
        self.Passes_Att = None
        self.Passes_CmpPercentage = None
        self.Passes_PrgP = None
        self.Carries = None
        self.Carries_PrgC = None
        self.Take_Ons_Att = None
        self.Take_Ons_Succ = None

    def export_to_csv(self):
        with open('./fbref/fbref_MatchStats.csv', 'a', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['fbrefMatchId', 'team', 'is_home_team', 'score', 'manager', 'captain',
                                 'formation', 'possession', 'fouls', 'corners', 'crosses', 'touches',
                                 'tackles', 'interceptions', 'aerials_won', 'clearances', 'offsides',
                                 'goal_kicks', 'throw_ins', 'long_balls', 'total_players_stats', 'minutes',
                                 'Gls', 'Ast', 'PK', 'PKatt', 'Sh', 'SoT', 'CrdY', 'CrdR', 'Touches',
                                 'Tkl', 'Int', 'Blocks', 'xG', 'npxG', 'xAG', 'SCA', 'GCA', 'Passes_Cmp',
                                 'Passes_Att', 'Passes_CmpPercentage', 'Passes_PrgP', 'Carries', 'Carries_PrgC',
                                 'Take_Ons_Att', 'Take_Ons_Succ'])
            writer.writerow([self.fbrefMatchId, self.team, self.is_home_team, self.score, self.manager,
                             self.captain, self.formation, self.possession, self.fouls, self.corners,
                             self.crosses, self.touches, self.tackles, self.interceptions, self.aerials_won,
                             self.clearances, self.offsides, self.goal_kicks, self.throw_ins, self.long_balls,
                             self.total_players_stats, self.minutes, self.Gls, self.Ast, self.PK, self.PKatt,
                             self.Sh, self.SoT, self.CrdY, self.CrdR, self.Touches, self.Tkl, self.Int, 
                             self.Blocks, self.xG, self.npxG, self.xAG, self.SCA, self.GCA, self.Passes_Cmp,
                             self.Passes_Att, self.Passes_CmpPercentage, self.Passes_PrgP, self.Carries, self.Carries_PrgC,
                             self.Take_Ons_Att, self.Take_Ons_Succ])

class Fbref_MatchPlayerStats:
    def __init__(self):
        self.fbrefMatchId = None
        self.player_name = None
        self.player_kitnum = None
        self.team = None
        self.nationality = None
        self.position = None
        self.age = None
        self.minutes = None
        self.Gls = None
        self.Ast = None
        self.PK = None
        self.PKatt = None
        self.Sh = None
        self.SoT = None
        self.CrdY = None
        self.CrdR = None
        self.Touches = None
        self.Tkl = None
        self.Int = None
        self.Blocks = None
        self.xG = None
        self.npxG = None
        self.xAG = None
        self.SCA = None
        self.GCA = None
        self.Passes_Cmp = None
        self.Passes_Att = None
        self.Passes_CmpPercentage = None
        self.Passes_PrgP = None
        self.Carries = None
        self.Carries_PrgC = None
        self.Take_Ons_Att = None
        self.Take_Ons_Succ = None

    def export_to_csv(self):
        with open('./fbref/fbref_MatchPlayerStats.csv', 'a', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['fbrefMatchId', 'player_name', 'player_kitnum', 'team', 'nationality',
                                 'position', 'age', 'minutes', 'Gls', 'Ast', 'PK', 'PKatt', 'Sh', 'SoT',
                                 'CrdY', 'CrdR', 'Touches', 'Tkl', 'Int', 'Blocks', 'xG', 'npxG', 'xAG',
                                 'SCA', 'GCA', 'Passes_Cmp', 'Passes_Att', 'Passes_CmpPercentage',
                                 'Passes_PrgP', 'Carries', 'Carries_PrgC', 'Take_Ons_Att', 'Take_Ons_Succ'])
            writer.writerow([self.fbrefMatchId, self.player_name, self.player_kitnum, self.team,
                             self.nationality, self.position, self.age, self.minutes, self.Gls, self.Ast,
                             self.PK, self.PKatt, self.Sh, self.SoT, self.CrdY, self.CrdR, self.Touches,
                             self.Tkl, self.Int, self.Blocks, self.xG, self.npxG, self.xAG, self.SCA,
                             self.GCA, self.Passes_Cmp, self.Passes_Att, self.Passes_CmpPercentage,
                             self.Passes_PrgP, self.Carries, self.Carries_PrgC, self.Take_Ons_Att,
                             self.Take_Ons_Succ])


class Fbref_MatchInfos:
    def __init__(self):
        self.fbrefMatchId = None
        self.fbrefURL = None
        self.league = None
        self.season = None
        self.match_date = None
        self.match_date_str = None
        self.match_week = None
        self.venue_time = None
        self.attendance = None
        self.venue = None
        self.officials = None
        self.home_team = None
        self.away_team = None

    def export_to_csv(self):
        with open('./fbref/fbref_MatchInfos.csv', 'a', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['fbrefMatchId', 'fbrefURL', 'league', 'season', 'match_date', 'match_date_str',
                                 'match_week', 'venue_time', 'attendance', 'venue', 'officials', 'home_team',
                                 'away_team'])
            writer.writerow([self.fbrefMatchId, self.fbrefURL, self.league, self.season, self.match_date,
                             self.match_date_str, self.match_week, self.venue_time, self.attendance, self.venue,
                             self.officials, self.home_team, self.away_team])