import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(page_title="Madrid Real Estate Analysis", layout="wide")

st.title("🏠 Madrid Real Estate Market Analysis")
st.write("Analys av 21 000+ bostäder i Madrid — prisutveckling, stadsdelar och vad som påverkar priset.")

conn = duckdb.connect("madrid_dbt/madrid_warehouse.duckdb")

# --- TAB-LAYOUT ---
tab1, tab2 = st.tabs(["📍 Pris per stadsdel", "🔑 Vad påverkar priset?"])

with tab1:
    st.subheader("Genomsnittspris per stadsdel")
    df_hood = conn.execute("SELECT * FROM mart_price_by_neighborhood").df()
    
    # Förkorta långa namn
    df_hood['neighborhood_short'] = df_hood['neighborhood_id'].str.extract(r'Neighborhood \d+: ([^(]+)')
    df_hood['neighborhood_short'] = df_hood['neighborhood_short'].str.strip()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Antal stadsdelar", len(df_hood))
    col2.metric("Dyraste stadsdel", df_hood.iloc[0]['neighborhood_short'])
    col3.metric("Högsta snittspris", f"{int(df_hood.iloc[0]['avg_price']):,} €")
    
    st.bar_chart(df_hood.set_index('neighborhood_short')['avg_price_per_sqm'].head(15))
    
    st.subheader("Detaljerad data")
    st.dataframe(df_hood[['neighborhood_short', 'total_listings', 'avg_price', 'avg_price_per_sqm', 'avg_size_sqm', 'avg_rooms']].head(20))

with tab2:
    st.subheader("Hur mycket påverkar olika faktorer priset?")
    df_drivers = conn.execute("SELECT * FROM mart_price_drivers").df()
    
    factors = {
        "Pool": (df_drivers['avg_price_with_pool'][0], df_drivers['avg_price_without_pool'][0]),
        "Parkering": (df_drivers['avg_price_with_parking'][0], df_drivers['avg_price_without_parking'][0]),
        "Terrass": (df_drivers['avg_price_with_terrace'][0], df_drivers['avg_price_without_terrace'][0]),
        "AC": (df_drivers['avg_price_with_ac'][0], df_drivers['avg_price_without_ac'][0]),
        "Nybyggt": (df_drivers['avg_price_new'][0], df_drivers['avg_price_old'][0]),
        "Exteriör": (df_drivers['avg_price_exterior'][0], df_drivers['avg_price_interior'][0]),
    }
    
    rows = []
    for factor, (with_val, without_val) in factors.items():
        if pd.isna(with_val) or pd.isna(without_val) or without_val == 0:
            continue
        diff = with_val - without_val
        diff_pct = round((diff / without_val) * 100, 1)
        rows.append({"Faktor": factor, "Med": int(with_val), "Utan": int(without_val), "Skillnad €": int(diff), "Skillnad %": diff_pct})
    
    df_factors = pd.DataFrame(rows).sort_values("Skillnad %", ascending=False)
    st.dataframe(df_factors, use_container_width=True)
    
    st.bar_chart(df_factors.set_index("Faktor")["Skillnad %"])

conn.close()