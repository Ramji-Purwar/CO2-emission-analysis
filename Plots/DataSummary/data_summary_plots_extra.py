import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.titleweight": "bold",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 120,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

OUT = Path("Plots/DataSummary")
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv("owid-co2-data.csv", low_memory=False)

# PLOT 7: Global CO₂ Emissions by Fuel Source (Stacked Area)
world_df = df[(df["country"] == "World") & (df["year"] >= 1900)]
sources = ["coal_co2", "oil_co2", "gas_co2", "cement_co2", "flaring_co2", "land_use_change_co2"]
labels = ["Coal", "Oil", "Gas", "Cement", "Flaring", "Land Use Change"]
colors = ["#264653", "#2A9D8F", "#E9C46A", "#F4A261", "#E63946", "#8AB17D"]

fig, ax = plt.subplots(figsize=(14, 7))
ax.stackplot(world_df["year"], [world_df[src].fillna(0) for src in sources], labels=labels, colors=colors, alpha=0.85)
ax.set_title("Global CO₂ Emissions by Source (1900–Present)")
ax.set_ylabel("Emissions (Mt)")
ax.legend(loc="upper left")
plt.savefig(OUT / "DS7_global_emissions_by_source.png")
plt.close()

# PLOT 8: Top 15 Cumulative Emitters (Latest Year)
country_df = df[df["iso_code"].notna() & (df["iso_code"] != "")]
latest = country_df["year"].max()
top_15 = country_df[country_df["year"] == latest].nlargest(15, "cumulative_co2")

fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(top_15["country"][::-1], top_15["cumulative_co2"][::-1] / 1000, color="#457B9D")
ax.set_title(f"Top 15 Countries by Cumulative CO₂ Emissions (through {latest})")
ax.set_xlabel("Cumulative CO₂ Emissions (Billion Tonnes / Gt)")
for bar in bars:
    ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2, f'{bar.get_width():.1f} Gt', va='center', fontsize=9)
plt.savefig(OUT / "DS8_cumulative_emitters.png")
plt.close()
