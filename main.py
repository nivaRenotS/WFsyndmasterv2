# app.py
import streamlit as st
import pandas as pd
import config
import data_cleaner
import market_analyzer

# --- PAGE SETUP ---
st.set_page_config(page_title="Syndicate Mod Manager", layout="wide")


# --- DATA LOADING ---
@st.cache_data
def load_base_data():
    """Parses config data into a clean DataFrame."""
    parsed = data_cleaner.parse_wiki_table(config.RAW_WIKI_DATA)

    flat_data = []
    for entry in parsed:
        wf = entry['warframe']
        syndicates = entry['syndicates']
        for mod in entry['mods']:
            url_name = data_cleaner.clean_mod_name_for_url(mod)
            flat_data.append({
                "Warframe": wf,
                "Mod Name": mod,
                "URL Name": url_name,
                "Syndicates": syndicates
            })
    return pd.DataFrame(flat_data)


@st.cache_data
def get_live_market_data(url_names):
    """Fetches API data."""
    return market_analyzer.fetch_bulk_stats(url_names)


# Initialize Data
df_mods = load_base_data()

# --- SIDEBAR FILTERS (Dynamic) ---
st.sidebar.title("Market Filters")

# 1. SYNDICATE FILTER
all_syndicates = sorted(list(set([s for sublist in df_mods["Syndicates"] for s in sublist])))
selected_syndicates = st.sidebar.multiselect("1. Filter by Syndicate", all_syndicates)

# 2. DYNAMIC WARFRAME FILTER
# Logic: If syndicates are selected, limit the Warframe list to those syndicates.
if selected_syndicates:
    # Filter the base data temporarily to find matching Warframes
    # This checks if the row's syndicates overlap with the selected syndicates
    condition = df_mods["Syndicates"].apply(lambda x: any(s in selected_syndicates for s in x))
    available_warframes_df = df_mods[condition]

    # Get unique Warframes from this filtered set
    available_warframes = sorted(available_warframes_df["Warframe"].unique())
else:
    # If no syndicate selected, show ALL Warframes
    available_warframes = sorted(df_mods["Warframe"].unique())

selected_warframes = st.sidebar.multiselect("2. Filter by Warframe", available_warframes)

# --- APPLYING FINAL FILTERS ---
# We create a clean copy to filter for the final view
filtered_df = df_mods.copy()

# Apply Syndicate Filter
if selected_syndicates:
    filtered_df = filtered_df[filtered_df["Syndicates"].apply(lambda x: any(s in selected_syndicates for s in x))]

# Apply Warframe Filter
if selected_warframes:
    filtered_df = filtered_df[filtered_df["Warframe"].isin(selected_warframes)]

# --- MAIN CONTENT ---
st.title("Warframe Syndicate Analyzer Tool")
st.markdown(f"**Found {len(filtered_df)} mods** matching your criteria.")

if st.button("Fetch Market Data"):
    if len(filtered_df) == 0:
        st.warning("No mods match your current filters.")
    else:
        with st.spinner(f"Fetching live prices for {len(filtered_df)} mods..."):
            # Get stats
            mod_urls = filtered_df["URL Name"].tolist()
            stats_dict = get_live_market_data(mod_urls)

            # Merge stats
            stats_df = pd.DataFrame.from_dict(stats_dict, orient='index')
            stats_df.index.name = "URL Name"

            result_df = filtered_df.merge(stats_df, on="URL Name", how="left")


            # --- 1.4 BEST TIME TO SELL LOGIC ---
            def recommend_action(row):
                short = row['avg_price_48h']
                long_term = row['avg_price_90d']

                if short == 0 or long_term == 0: return "No Data"

                # If current price is 15% higher than 90d average -> Sell
                if short > long_term * 1.15:
                    return "🔥 SELL NOW (Price High)"
                # If current price is 15% lower than 90d average -> Hold
                elif short < long_term * 0.85:
                    return "🛑 HOLD (Price Low)"
                else:
                    return "✅ Normal"


            result_df["Action"] = result_df.apply(recommend_action, axis=1)

            # --- 1.3 BEST MOD TO SELL LOGIC ---
            if not result_df.empty:
                # Sort by Price (Profit) and Volume (Liquidity)
                best_price = result_df.sort_values(by="avg_price_48h", ascending=False).iloc[0]
                most_liquid = result_df.sort_values(by="volume_48h", ascending=False).iloc[0]

                # Display Metrics
                st.divider()
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("💎 Best Price Mod",
                              best_price["Mod Name"],
                              f"{best_price['avg_price_48h']:.1f} pl")
                    st.caption(f"For Warframe: {best_price['Warframe']}")

                with col2:
                    st.metric("🌊 Fastest Selling Mod",
                              most_liquid["Mod Name"],
                              f"{most_liquid['volume_48h']} sold/48h")
                    st.caption("Highest trading volume")

                with col3:
                    # Check for Arbitrage opportunities
                    trending = result_df[result_df["Action"].str.contains("SELL NOW")]
                    if not trending.empty:
                        top_trend = trending.sort_values(by="avg_price_48h", ascending=False).iloc[0]
                        diff = top_trend['avg_price_48h'] - top_trend['avg_price_90d']
                        st.metric("🚀 Trend Alert",
                                  top_trend["Mod Name"],
                                  f"+{diff:.1f} pl vs 90d Avg")
                    else:
                        st.metric("🚀 Trend Alert", "None", "Market Stable")

                # --- DATA TABLE ---
                st.divider()
                st.subheader("Market Data")

                display_cols = ["Mod Name", "Warframe", "avg_price_48h", "volume_48h", "Action"]
                st.dataframe(
                    result_df[display_cols].sort_values(by="avg_price_48h", ascending=False),
                    column_config={
                        "avg_price_48h": st.column_config.NumberColumn("Price (48h)", format="%.1f pl"),
                        "volume_48h": st.column_config.NumberColumn("Volume (48h)"),
                        "Action": st.column_config.TextColumn("Recommendation"),
                    },
                    use_container_width=True
                )
            else:
                st.warning("Data fetched, but no valid statistics found.")

else:
    st.info("Select filters on the left and click 'Fetch Market Data'.")


# Run
# streamlit run main.py
# on Terminal
