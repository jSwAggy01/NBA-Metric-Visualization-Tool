# Tutorial from Ken Jee with example use cases: https://youtu.be/NCyPY-jfb3I?si=AaBWg1l35LOcMLvn
import pandas as pd

# Create a dict for every NBA player ever (ID, playername)
from nba_api.stats.static import players
player_dict = players.get_players()

# Create a dict for a specific player
bron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
bron_id = bron['id']

# Create a dict for every NBA team
from nba_api.stats.static import teams
team_dict = teams.get_teams()

# Create a dict for a specific team
GSW = [team for team in team_dict if team['full_name'] == 'Golden State Warriors'][0]
GSW_id = GSW['id']

# Get stats for a specific player from a specified season
from nba_api.stats.endpoints import playergamelog
gamelog_bron = playergamelog.PlayerGameLog(player_id = '2544', season = '2017')
gamelog_bron_df = gamelog_bron.get_data_frames()[0]

# Get stats for all games played ever from a specific player
from nba_api.stats.library.parameters import SeasonAll
gamelog_bron_all = playergamelog.PlayerGameLog(player_id = '2544', season = SeasonAll.all)
gamelog_bron_df_all = gamelog_bron_all.get_data_frames()[0]

# Get stats for all games played ever from a specific team
from nba_api.stats.endpoints import leaguegamefinder
GSW_games = leaguegamefinder.LeagueGameFinder(team_id_nullable = GSW_id).get_data_frames()[0]