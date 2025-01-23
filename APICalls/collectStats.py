import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
import time
from tqdm import tqdm
import logging

def setup_logging():
    """Configure logging for the script"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def get_active_players():
    """Retrieve list of all active NBA players"""
    try:
        return players.get_active_players()
    except Exception as e:
        logging.error(f"Error fetching active players: {e}")
        return []

def get_player_stats(player_id, retry_count=3):
    """
    Retrieve player statistics with retry mechanism
    Returns None if unsuccessful after retries
    """
    for attempt in range(retry_count):
        try:
            stats = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
            return stats.get_data_frames()[1]
        except Exception as e:
            if attempt == retry_count - 1:
                logging.error(f"Failed to fetch stats for player ID {player_id}: {e}")
                return None
            time.sleep(1)  # Wait before retry to avoid rate limiting

def collect_player_statistics():
    """
    Main function to collect statistics for all active players
    Returns a DataFrame with player stats
    """
    setup_logging()
    logging.info("Starting player statistics collection")
    
    # Get active players
    active_players = get_active_players()
    if not active_players:
        logging.error("No active players found")
        return pd.DataFrame()
    
    logging.info(f"Found {len(active_players)} active players")
    
    # Initialize lists to store player data
    all_stats = []
    
    # Process each player with progress bar
    for player in tqdm(active_players, desc="Collecting player stats"):
        player_id = player['id']
        player_stats = get_player_stats(player_id)
        
        if player_stats is not None:
            # Add player name to stats
            player_stats['PLAYER_NAME'] = player['full_name']
            all_stats.append(player_stats)
        
        # Add delay to avoid rate limiting
        time.sleep(0.6)
    
    # Combine all player stats into a single DataFrame
    if all_stats:
        final_df = pd.concat(all_stats, ignore_index=True)
        
        # Select relevant columns and rename them for clarity
        columns_of_interest = {
            'PLAYER_NAME': 'Player',
            'PTS': 'Points',
            'AST': 'Assists',
            'REB': 'Rebounds'
        }
        
        final_df = final_df[columns_of_interest.keys()].rename(columns=columns_of_interest)
        
        # Sort by points in descending order
        final_df = final_df.sort_values('Points', ascending=False)
        
        logging.info(f"Successfully collected stats for {len(final_df)} players")
        return final_df
    else:
        logging.error("No player statistics were collected")
        return pd.DataFrame()

if __name__ == "__main__":
    # Collect statistics
    stats_df = collect_player_statistics()
    
    # Display results if data was collected
    if not stats_df.empty:
        print("\nTop 10 Players by Points:")
        print(stats_df.head(10))
        
        # Save to CSV
        stats_df.to_csv('nba_player_stats.csv', index=False)
        print("\nData saved to 'nba_player_stats.csv'")