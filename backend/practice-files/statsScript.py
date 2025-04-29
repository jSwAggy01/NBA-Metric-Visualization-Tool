# Get PTS/AST/REB averages for all active players in current season
'''
1) Get list of all active players
2) Save the IDs of all active players into a list
3) Iterate through that list and get all active players 'PlayerHeadlineStats'
4) Save the PTS/AST/REB into a new dataframe with corresponding players
'''

import pandas as pd

# Get all active players
from nba_api.stats.static import players
player_dict = players.get_active_players()

# Get PTS/AST/REB for a specific player in current season
from nba_api.stats.endpoints import commonplayerinfo
avg_bron = commonplayerinfo.CommonPlayerInfo(player_id = 2544)
avg_bron_df = avg_bron.get_data_frames()[1]