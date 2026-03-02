# data_cleaner.py
import re
from typing import List, Dict


def clean_mod_name_for_url(name: str) -> str:
    """
    Converts a display name like 'Seeking Shuriken' or 'Calm & Frenzy'
    into a URL-friendly format like 'seeking_shuriken' or 'calm_and_frenzy'.
    Also handles specific API name overrides.
    """
    # 1. Lowercase and strip whitespace
    clean = name.strip().lower()

    # 2. Replace known special chars
    clean = clean.replace(" & ", " and ").replace("&", "and")
    clean = clean.replace("'", "")  # Remove apostrophes (Mesa's -> mesas)
    clean = clean.replace("-", "_")  # Hyphens to underscores

    # 3. Replace spaces with underscores
    clean = clean.replace(" ", "_")

    # 4. Specific API Overrides (Renaming logic)
    # These fix discrepancies between Wiki names and Warframe Market URL names
    if clean == 'teleport_rush':
        clean = 'fatal_teleport'
    elif clean == 'negation_armor':
        clean = 'negation_swarm'

    return clean


def parse_wiki_table(raw_text: str) -> List[Dict]:
    """
    Parses the MediaWiki format string to extract matching
    Warframes, Mods, and Syndicates.
    """
    # Remove the table header and footer syntax
    clean_text = raw_text.replace('{| class="wikitable" style="width:100%;" align="center"', '').replace('|}', '')

    # Split by rows (|- denotes a new row in wiki syntax)
    rows = clean_text.split('|-')

    parsed_data = []

    for row in rows:
        row = row.strip()
        if not row or row.startswith('!'):
            continue  # Skip header rows or empty lines

        # Extract Warframe {{WF|Name}}
        wf_match = re.search(r"{{WF\|([^}]+)}}", row)
        if not wf_match:
            continue
        warframe = wf_match.group(1).strip()

        # Extract Mods {{M|Mod Name}}
        mods_raw = re.findall(r"{{M\|([^}]+)}}", row)
        mods_list = [m.strip() for m in mods_raw]

        # Extract Syndicates {{Faction|Name}}
        syndicates_raw = re.findall(r"{{Faction\|([^}]+)}}", row)
        syndicates_list = [s.strip() for s in syndicates_raw]

        if warframe and mods_list:
            entry = {
                "warframe": warframe,
                "mods": mods_list,
                "syndicates": syndicates_list
            }
            parsed_data.append(entry)

    return parsed_data