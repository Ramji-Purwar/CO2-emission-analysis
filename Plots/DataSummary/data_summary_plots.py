"""
CO₂ Emission Analysis — Data Summary Plots
============================================
Generates 6 summary figures for the dataset overview section:
  1. Dataset dimensions & structure overview table
  2. Missing data heatmap for key columns
  3. Distribution histograms for core variables
  4. Correlation heatmap among emission indicators
  5. t-SNE plot — countries clustered by emission profile
  6. Global emissions timeline (world aggregate)

All outputs saved to  Plots/DataSummary/
"""

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from pathlib import Path

# ── Setup ────────────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family":       "DejaVu Sans",
    "font.size":         11,
    "axes.titlesize":    14,
    "axes.titleweight":  "bold",
    "axes.labelsize":    12,
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "figure.dpi":        120,
    "savefig.dpi":       300,
    "savefig.bbox":      "tight",
    "savefig.facecolor": "white",
})

OUT = Path("Plots/DataSummary")
OUT.mkdir(parents=True, exist_ok=True)

# ── Load data ────────────────────────────────────────────────────────────
df = pd.read_csv("owid-co2-data.csv", low_memory=False)
if "gdp_per_capita" not in df.columns:
    df["gdp_per_capita"] = df["gdp"] / df["population"]

country_df = df[df["iso_code"].notna() & (df["iso_code"] != "")].copy()
world_df   = df[df["country"] == "World"].copy()

print(f"Full dataset   : {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"Country rows   : {country_df.shape[0]:,} rows | {country_df['country'].nunique()} countries")
print(f"Year range     : {df['year'].min()} – {df['year'].max()}")

# ═══════════════════════════════════════════════════════════════════════════
# PLOT 1 — Dataset Structure Summary Table
# ═══════════════════════════════════════════════════════════════════════════
print("\n[1/6] Dataset structure table …")

col_groups = {
    "Identifiers":       ["country", "year", "iso_code", "population", "gdp"],
    "Core CO₂":          ["co2", "co2_per_capita", "co2_per_gdp", "co2_growth_abs",
                          "co2_growth_prct", "co2_including_luc", "cumulative_co2"],
    "Fuel Sources":      ["coal_co2", "oil_co2", "gas_co2", "cement_co2",
                          "flaring_co2", "other_industry_co2"],
    "Land-Use":          ["land_use_change_co2", "co2_including_luc_per_capita"],
    "Trade / Consumption": ["consumption_co2", "trade_co2", "trade_co2_share"],
    "Energy":            ["primary_energy_consumption", "energy_per_capita",
                          "co2_per_unit_energy", "energy_per_gdp"],
    "GHG (non-CO₂)":    ["total_ghg", "methane", "nitrous_oxide",
                          "ghg_per_capita"],
    "Temperature":       ["temperature_change_from_co2", "temperature_change_from_ghg",
                          "share_of_temperature_change_from_ghg"],
    "Shares":            ["share_global_co2", "share_global_cumulative_co2"],
}

rows_tbl = []
for grp, cols in col_groups.items():
    valid_cols = [c for c in cols if c in df.columns]
    non_null = sum(df[c].notna().sum() for c in valid_cols)
    total    = len(valid_cols) * len(df)
    coverage = non_null / total * 100 if total > 0 else 0
    rows_tbl.append([grp, len(valid_cols), f"{coverage:.1f}%"])

fig, ax = plt.subplots(figsize=(10, 5))
ax.axis("off")
tbl = ax.table(
    cellText=rows_tbl,
    colLabels=["Column Group", "# Columns", "Data Coverage"],
    loc="center",
    cellLoc="center",
)
tbl.auto_set_font_size(False)
tbl.set_fontsize(11)
tbl.scale(1.2, 1.8)
for (r, c), cell in tbl.get_celld().items():
    if r == 0:
        cell.set_facecolor("#264653")
        cell.set_text_props(color="white", fontweight="bold")
    else:
        cell.set_facecolor("#F1FAEE" if r % 2 == 0 else "white")
    cell.set_edgecolor("#DDDDDD")

ax.set_title(
    f"Dataset Overview — {df.shape[0]:,} rows × {df.shape[1]} columns\n"
    f"{country_df['country'].nunique()} countries  |  {df['year'].min()}–{df['year'].max()}",
    fontsize=14, fontweight="bold", pad=20,
)
plt.savefig(OUT / "DS1_dataset_overview_table.png")
plt.close()
print("  ✓ Saved DS1")


# ═══════════════════════════════════════════════════════════════════════════
# PLOT 2 — Missing Data Heatmap
# ═══════════════════════════════════════════════════════════════════════════
print("[2/6] Missing data heatmap …")

key_cols = [
    "co2", "co2_per_capita", "co2_per_gdp", "gdp", "population",
    "coal_co2", "oil_co2", "gas_co2", "cement_co2", "flaring_co2",
    "consumption_co2", "trade_co2", "primary_energy_consumption",
    "total_ghg", "methane", "nitrous_oxide", "ghg_per_capita",
    "temperature_change_from_ghg", "co2_including_luc", "cumulative_co2",
]
key_cols = [c for c in key_cols if c in df.columns]

# Sample decades for readability
decades = list(range(1850, 2030, 10))
miss_data = []
for yr in decades:
    row_yr = country_df[country_df["year"] == yr]
    if row_yr.empty:
        miss_data.append([100.0] * len(key_cols))
    else:
        miss_data.append([(row_yr[c].isna().sum() / len(row_yr)) * 100 for c in key_cols])

miss_df = pd.DataFrame(miss_data, index=decades, columns=key_cols)

fig, ax = plt.subplots(figsize=(16, 8))
sns.heatmap(miss_df.T, cmap="YlOrRd", annot=False, linewidths=0.3,
            linecolor="white", cbar_kws={"label": "% Missing"}, ax=ax,
            vmin=0, vmax=100)
ax.set_title("Missing Data by Column & Decade\n"
             "Dark = mostly missing  |  Light = data available",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Decade"); ax.set_ylabel("")
ax.tick_params(axis="y", rotation=0)
plt.tight_layout()
plt.savefig(OUT / "DS2_missing_data_heatmap.png")
plt.close()
print("  ✓ Saved DS2")


# ═══════════════════════════════════════════════════════════════════════════
# PLOT 3 — Distribution Histograms for Core Variables (Latest Year)
# ═══════════════════════════════════════════════════════════════════════════
print("[3/6] Distribution histograms …")

latest = country_df["year"].max()
df_latest = country_df[country_df["year"] == latest].copy()

dist_cols   = ["co2", "co2_per_capita", "ghg_per_capita", "primary_energy_consumption"]
dist_labels = ["CO₂ (Mt)", "CO₂ per Capita (t)", "GHG per Capita (t)", "Energy (TWh)"]
dist_colors = ["#E63946", "#457B9D", "#F4A261", "#264653"]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(f"Distribution of Key Variables Across Countries ({latest})",
             fontsize=15, fontweight="bold", y=1.02)

for ax, col, label, colour in zip(axes.flat, dist_cols, dist_labels, dist_colors):
    data = df_latest[col].dropna()
    if data.empty:
        ax.text(0.5, 0.5, "No data", ha="center", va="center", transform=ax.transAxes)
        ax.set_title(label); continue
    # Use log scale if highly skewed
    skew = data.skew()
    plot_data = np.log10(data[data > 0]) if abs(skew) > 2 else data
    ax.hist(plot_data, bins=35, color=colour, alpha=0.85, edgecolor="white", linewidth=0.5)
    ax.set_xlabel(f"{'log₁₀ ' if abs(skew) > 2 else ''}{label}")
    ax.set_ylabel("Count")
    ax.set_title(f"{label}\n(n={len(data)}, median={data.median():.2f})", fontsize=11)
    ax.axvline(plot_data.median(), color="black", linewidth=1.5, linestyle="--", alpha=0.7,
               label=f"Median")
    ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig(OUT / "DS3_distributions.png")
plt.close()
print("  ✓ Saved DS3")


# ═══════════════════════════════════════════════════════════════════════════
# PLOT 4 — Correlation Heatmap
# ═══════════════════════════════════════════════════════════════════════════
print("[4/6] Correlation heatmap …")

corr_cols = [
    "co2", "co2_per_capita", "co2_per_gdp", "gdp_per_capita",
    "coal_co2", "oil_co2", "gas_co2",
    "primary_energy_consumption", "co2_per_unit_energy",
    "total_ghg", "methane", "ghg_per_capita",
    "temperature_change_from_ghg", "cumulative_co2",
]
corr_cols = [c for c in corr_cols if c in df_latest.columns]

corr_matrix = df_latest[corr_cols].corr()

# Pretty labels
pretty = {
    "co2": "CO₂", "co2_per_capita": "CO₂/cap", "co2_per_gdp": "CO₂/GDP",
    "gdp_per_capita": "GDP/cap", "coal_co2": "Coal CO₂", "oil_co2": "Oil CO₂",
    "gas_co2": "Gas CO₂", "primary_energy_consumption": "Energy",
    "co2_per_unit_energy": "CO₂/Energy", "total_ghg": "GHG",
    "methane": "CH₄", "ghg_per_capita": "GHG/cap",
    "temperature_change_from_ghg": "Temp Δ", "cumulative_co2": "Cum CO₂",
}
corr_matrix.index   = [pretty.get(c, c) for c in corr_matrix.index]
corr_matrix.columns = [pretty.get(c, c) for c in corr_matrix.columns]

mask = np.triu(np.ones_like(corr_matrix, dtype=bool), k=1)

fig, ax = plt.subplots(figsize=(13, 11))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt=".2f",
            cmap="RdBu_r", center=0, linewidths=0.5, linecolor="white",
            square=True, cbar_kws={"shrink": 0.75, "label": "Pearson r"},
            ax=ax, vmin=-1, vmax=1)
ax.set_title(f"Correlation Matrix of Emission Indicators ({latest})",
             fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig(OUT / "DS4_correlation_heatmap.png")
plt.close()
print("  ✓ Saved DS4")


# ═══════════════════════════════════════════════════════════════════════════
# PLOT 5 — t-SNE: Countries Clustered by Emission Profile
# ═══════════════════════════════════════════════════════════════════════════
print("[5/6] t-SNE embedding …")

# Use a compact feature set with high data coverage
tsne_cols = [
    "co2_per_capita", "co2_per_gdp", "coal_co2", "oil_co2", "gas_co2",
    "cumulative_co2", "share_global_co2",
]
tsne_cols = [c for c in tsne_cols if c in df_latest.columns]

df_tsne = df_latest[["country"] + tsne_cols].copy()
df_tsne = df_tsne.replace([np.inf, -np.inf], np.nan)

# Require at least co2_per_capita to be present
df_tsne = df_tsne.dropna(subset=["co2_per_capita"]).reset_index(drop=True)

# Fill remaining NaN with column median (so we don't lose countries)
for c in tsne_cols:
    med = df_tsne[c].median()
    df_tsne[c] = df_tsne[c].fillna(med if pd.notna(med) else 0)

print(f"  t-SNE using {len(df_tsne)} countries × {len(tsne_cols)} features")

X = df_tsne[tsne_cols].values.astype(np.float64)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Assign income groups by GDP per capita quartiles
gdp_vals = df_latest.set_index("country")["gdp_per_capita"]
df_tsne["gdp_pc"] = df_tsne["country"].map(gdp_vals)
q25, q50, q75 = df_tsne["gdp_pc"].quantile([0.25, 0.50, 0.75])
def income_group(g):
    if pd.isna(g): return "Unknown"
    if g < q25: return "Low Income"
    if g < q50: return "Lower-Middle"
    if g < q75: return "Upper-Middle"
    return "High Income"
df_tsne["income_group"] = df_tsne["gdp_pc"].apply(income_group)

# Run t-SNE
perplexity = min(30, len(df_tsne) - 1)
tsne = TSNE(n_components=2, perplexity=perplexity, random_state=42,
            learning_rate="auto", init="pca", max_iter=1500)
embedding = tsne.fit_transform(X_scaled)
df_tsne["x"] = embedding[:, 0]
df_tsne["y"] = embedding[:, 1]

# Plot
group_colours = {
    "Low Income":    "#2A9D8F",
    "Lower-Middle":  "#E9C46A",
    "Upper-Middle":  "#F4A261",
    "High Income":   "#E63946",
    "Unknown":       "#999999",
}

highlight = [
    "United States", "China", "India", "Brazil", "Russia", "Germany",
    "United Kingdom", "Japan", "Saudi Arabia", "South Africa",
    "Nigeria", "Australia", "France", "Indonesia", "Canada",
]

fig, ax = plt.subplots(figsize=(14, 10))

for grp, colour in group_colours.items():
    mask = df_tsne["income_group"] == grp
    ax.scatter(df_tsne.loc[mask, "x"], df_tsne.loc[mask, "y"],
               c=colour, s=70, alpha=0.65, edgecolors="white",
               linewidths=0.5, label=grp, zorder=3)

# Highlight and label major countries
for country in highlight:
    row = df_tsne[df_tsne["country"] == country]
    if row.empty: continue
    ax.scatter(row["x"], row["y"], s=200, facecolors="none",
               edgecolors="black", linewidths=1.8, zorder=5)
    ax.annotate(country, (row["x"].values[0], row["y"].values[0]),
                xytext=(7, 4), textcoords="offset points",
                fontsize=8, fontweight="bold", color="#222222",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#CCCCCC", alpha=0.85))

ax.set_xlabel("t-SNE Dimension 1", fontsize=12)
ax.set_ylabel("t-SNE Dimension 2", fontsize=12)
ax.set_title(
    f"t-SNE Embedding of Countries by Emission Profile ({latest})\n"
    f"Features: {len(tsne_cols)} emission indicators  |  Coloured by income group",
    fontsize=14, fontweight="bold",
)
ax.legend(title="Income Group", fontsize=10, title_fontsize=11,
          loc="upper left", framealpha=0.9)

# Remove axis ticks (t-SNE units are not meaningful)
ax.set_xticks([]); ax.set_yticks([])

plt.tight_layout()
plt.savefig(OUT / "DS5_tsne_country_clusters.png")
plt.close()
print("  ✓ Saved DS5")


# ═══════════════════════════════════════════════════════════════════════════
# PLOT 6 — Global CO₂ Emissions Timeline
# ═══════════════════════════════════════════════════════════════════════════
print("[6/6] Global emissions timeline …")

world_ts = world_df[["year", "co2"]].dropna()
world_ts = world_ts[world_ts["year"] >= 1850].copy()

fig, ax = plt.subplots(figsize=(15, 6))
ax.fill_between(world_ts["year"], world_ts["co2"], alpha=0.15, color="#E63946")
ax.plot(world_ts["year"], world_ts["co2"], color="#E63946", linewidth=2.5)

# Annotate key milestones
markers = {1950: "Post-WWII\nindustrialisation", 1973: "Oil\nCrisis",
           2008: "Financial\nCrisis", 2020: "COVID-19"}
for yr, label in markers.items():
    val = world_ts[world_ts["year"] == yr]["co2"]
    if val.empty: continue
    ax.annotate(label, (yr, val.values[0]),
                xytext=(0, 25), textcoords="offset points", ha="center",
                fontsize=8, color="#333333",
                arrowprops=dict(arrowstyle="->", color="#999999"),
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="#BBBBBB", alpha=0.9))

ax.set_xlabel("Year")
ax.set_ylabel("Global CO₂ Emissions (Mt)")
ax.set_title("Global CO₂ Emissions Timeline (1850–Present)\n"
             "From the Industrial Revolution to the Modern Era",
             fontsize=14, fontweight="bold")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1000:.0f}k"))
ax.set_xlim(1850, world_ts["year"].max() + 2)

plt.tight_layout()
plt.savefig(OUT / "DS6_global_timeline.png")
plt.close()
print("  ✓ Saved DS6")


print(f"\n✅ All 6 data-summary plots saved to: {OUT.resolve()}")
