# market_analyzer.py
import pywmapi as wm
import time
from typing import List, Dict


def get_mod_statistics(mod_name):
    """Fetch statistics for a given mod from the Warframe Market API"""
    try:
        statistics = wm.statistics.get_statistic(mod_name)
        return statistics
    except Exception as e:
        # We catch the exception to allow the app to continue even if one item fails
        print(f"Error fetching statistics for {mod_name}: {e}")
        return None


def calculate_averages(stats):
    """Calculate average price and volume from a list of statistics"""
    if not stats or len(stats) == 0:
        return 0, 0, 0  # Return zeros if no data

    total_volume = sum(stat.volume for stat in stats)
    avg_price = sum(stat.avg_price * stat.volume for stat in stats) / total_volume if total_volume > 0 else 0

    # Calculate moving average if available
    moving_avgs = [stat.moving_avg for stat in stats if stat.moving_avg is not None]
    avg_moving_avg = sum(moving_avgs) / len(moving_avgs) if moving_avgs else None

    return avg_price, total_volume, avg_moving_avg


def fetch_bulk_stats(mod_url_list: List[str]) -> Dict[str, Dict]:
    """
    Fetches stats for a list of mods and returns a structured dictionary
    suitable for conversion into a Pandas DataFrame.
    """
    mod_stats = {}

    for mod_name in mod_url_list:
        # Default empty data structure
        data = {
            'avg_price_48h': 0.0, 'volume_48h': 0, 'moving_avg_48h': 0.0,
            'avg_price_90d': 0.0, 'volume_90d': 0, 'moving_avg_90d': 0.0
        }

        stats = get_mod_statistics(mod_name)

        if stats:
            p48, v48, m48 = calculate_averages(stats.closed_48h)
            p90, v90, m90 = calculate_averages(stats.closed_90d)

            data = {
                'avg_price_48h': p48,
                'volume_48h': v48,
                'moving_avg_48h': m48 if m48 else 0.0,
                'avg_price_90d': p90,
                'volume_90d': v90,
                'moving_avg_90d': m90 if m90 else 0.0
            }

        mod_stats[mod_name] = data

        # Small delay to respect API rate limits
        time.sleep(0.05)

    return mod_stats