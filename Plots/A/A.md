# Plot A1 — GDP per Capita vs CO₂ per Capita (2022)
## Environmental Kuznets Curve Analysis

---

## 1. Chart Overview

**Chart type:** Log-log scatter plot (bubble chart)  
**Data:** OWID CO₂ dataset, 2022 cross-section  
**X-axis:** GDP per capita (USD, log scale) — measure of economic development  
**Y-axis:** CO₂ per capita (tonnes, log scale) — measure of individual carbon burden  
**Bubble size:** Total population  
**Highlighted countries:** United States, China, India, Brazil, Russia, Germany, United Kingdom, Japan, European Union (27), Indonesia

> Log scales are essential here — without them, the poorest countries collapse into a single corner and the relationship becomes unreadable. Each unit step on both axes represents a 10× change in value.

---

## 2. Key Findings

### Finding 1 — The General Pattern: Wealth and Emissions Rise Together

Across the full dataset, there is a clear positive correlation between income and per-capita CO₂ emissions. Countries with a GDP per capita below $5,000 typically emit less than 1 tonne per person annually, while those above $30,000 emit 5–15 tonnes. This confirms the foundational premise of the **Environmental Kuznets Curve (EKC) hypothesis**: in the early and middle stages of industrialisation, economic growth is fuelled by energy-intensive activities — manufacturing, construction, and freight — which drive carbon emissions upward in tandem with income.

---

### Finding 2 — The EKC Turning Point: Germany and UK Demonstrate Decoupling

The most important feature of the chart is not the trend line but the **deviations from it**. Germany (~$52,000 GDP per capita) and the United Kingdom (~$47,000 GDP per capita) both emit roughly 5–6 tonnes per capita — significantly below what their income levels would predict given the global trend.

This downward deviation is the empirical signature of **decoupling**: economies that have transitioned from heavy industry toward services, invested in renewable energy, and enacted strong carbon regulation can sustain high living standards at much lower emission intensities.

- Germany's *Energiewende* (energy transition policy) and its shift to renewables explain its position.
- The UK's early deindustrialisation followed by aggressive offshore wind deployment accounts for its similarly low intensity.

These two cases provide the strongest evidence in A1 that policy choices — not just income — determine a country's emission trajectory.

---

### Finding 3 — The United States as a High-Income Outlier

The United States sits conspicuously **above the trend** at approximately 14–15 tonnes per capita despite a GDP per capita of ~$76,000 — the highest among labelled countries. At the same income level, Germany emits less than half as much per person.

This gap cannot be explained by wealth alone. Structural factors include:

- Dominance of **car-dependent urban planning** and low public transport usage
- Historically **cheap domestic energy** (natural gas and oil)
- **Absence of a national carbon price** or equivalent regulatory mechanism
- Large, energy-intensive industrial and agricultural sectors
- Higher average living space per household driving residential energy demand

The US position in A1 is one of the most analytically rich data points in the entire dataset — it proves that policy choices, not just income, determine where a country lands on the scatter.

---

### Finding 4 — Russia: Resource-Intensity Above Its Income Class

Russia presents a strikingly different outlier case. With a GDP per capita of around $15,000 — placing it in the upper-middle income bracket — Russia emits approximately **12 tonnes per capita**, a level comparable to Japan despite earning roughly a third as much.

This reflects:

- The legacy of **Soviet-era energy infrastructure**, designed for volume rather than efficiency
- The continued dominance of **fossil fuel extraction** (oil, gas, coal) in the national economy
- **Chronically low domestic energy prices** that eliminate financial incentives for efficiency improvements

Russia's position in A1 anticipates what Plot C2 (gas flaring) will confirm: that resource endowment and regulatory failure — not income — are the primary drivers of its emission profile.

---

### Finding 5 — China and India: The Population Dimension

China (~$12,000 GDP per capita, ~8 tonnes per capita) and India (~$7,000 GDP per capita, ~1.8 tonnes per capita) both sit within the broad trend band — neither is a dramatic outlier in per-capita terms. However, their **exceptionally large bubbles** transform the analysis.

- China's 1.4 billion people mean that its moderate per-capita figure translates into the **world's largest absolute emitter**.
- India's low per-capita rate similarly multiplies into one of the **top five total emitters globally**.

This visual device — bubble size as population — is analytically essential. It warns against any policy framework that focuses solely on per-capita metrics and ignores total volume. A country can appear "efficient" per head while contributing massively to the global atmospheric burden.

---

### Finding 6 — The Bottom-Left Cluster: Low Income, Low Emissions — But for How Long?

The dense cloud of translucent dots in the lower-left corner represents predominantly low-income countries across Sub-Saharan Africa, South Asia, and parts of Southeast Asia. Their emissions are low — often below 0.5 tonnes per capita — but this is a function of **energy poverty**, not clean technology.

As these economies industrialise, the development path they take will be decisive for the global trajectory:

- If they replicate the **US model** (cheap fossil fuels, car-dependent growth), global emissions will rise sharply.
- If they can **leapfrog to renewables** — as early data from solar adoption in East Africa and India suggest — the EKC turning point could arrive at a much lower income threshold than historical precedent suggests.

This cluster is therefore the most consequential group on the chart for long-run climate projections, despite their current low absolute and per-capita emission levels.

---

## 3. The Core Argument A1 Makes

Plot A1 establishes the central analytical tension of this project:

> **Wealth is a necessary but not sufficient explanation for emissions.**

The US–Germany gap at the same income level proves that structural choices and policy ambition determine where a country lands. A1 sets up the questions that subsequent plots answer:

| Question raised by A1 | Answered by |
|---|---|
| Are rich countries becoming more efficient over time? | Plot B1 (CO₂/GDP trend) |
| Do rich countries hide emissions through trade? | Plots B2, B3 (trade CO₂) |
| Why does Brazil appear low here despite deforestation? | Plot A3 (CO₂ incl. land-use) |
| What explains Russia's position? | Plot C2 (gas flaring) |
| What accounts for the US–Germany gap? | Plot C4 (energy carbon intensity) |
| What has policy actually achieved? | Plots D2, D3 (policy section) |

---

## 4. Limitations

Three important caveats should be noted when interpreting A1 in a report:

1. **Production-based CO₂ only.** The chart measures emissions at the point of production, not consumption. Correcting for trade (as in Plots B2/B3) would shift the UK and Germany upward — they import manufactured goods whose production emissions are attributed to China — and would shift China downward.

2. **Single-year snapshot (2022).** A1 captures position, not trajectory. A country could be on a sharp declining path and still appear high in a single year. Plots A2 and B1 supply the essential temporal dimension.

3. **Land-use CO₂ excluded.** Brazil appears low on A1 — roughly 2.5 tonnes per capita — because fossil fuel emissions alone are modest. Once deforestation-driven emissions are added (Plot A3), Brazil's true footprint is dramatically higher, fundamentally changing its position relative to peers.

---

*Data source: Our World in Data (OWID) CO₂ and Greenhouse Gas Emissions dataset. Chart year: 2022.*



# Plot A2 — Annual CO₂ Growth: Absolute (Mt) & Percentage Change
## Growth Rate Analysis Across Major Economies (1988–2023)

---

## 1. Chart Overview

**Chart type:** Dual-panel bar chart grid (5 countries × 2 metrics)  
**Data:** OWID CO₂ dataset, annual observations  
**Left panels:** Absolute year-on-year change in CO₂ emissions (Mt CO₂)  
**Right panels:** Percentage year-on-year change (% YoY)  
**Countries covered:** United States, China, India, Germany, United Kingdom  
**Colour coding:** Positive bars (increases) in country colour; negative bars (decreases) in grey

> The dual-panel design is deliberate and important. Absolute change reveals *scale* — how many megatonnes were added or removed. Percentage change reveals *momentum* — how fast an economy is growing or shrinking its carbon output relative to its own base. A country can show a small absolute change but a large percentage swing (UK, Germany) or a massive absolute change but a moderate percentage shift (China). Reading both panels together is essential.

---

## 2. Country-by-Country Analysis

### United States — Structural Decline with Shock Events

The US panels tell a story of **long-run structural decline** interrupted by discrete economic shocks.

- Through the 1990s and early 2000s, the US shows mostly **positive but small absolute bars** — modest annual growth driven by GDP expansion and rising energy demand.
- From **2007–2009**, a sharp negative spike appears — the Global Financial Crisis triggered the largest single-year drop in US emissions in the modern record, reflecting collapsed industrial output and reduced transport activity.
- Post-2009, the trajectory shifts: the US enters a sustained period of **predominantly negative bars**, driven by the shale gas revolution displacing coal in power generation, improving vehicle fuel efficiency standards, and the growing share of renewables.
- **2020** shows another dramatic negative spike — the COVID-19 pandemic lockdowns — followed by a sharp positive rebound in 2021 as economic activity resumed.
- By the early 2020s, the US is on a declining absolute trend, though the pace of reduction remains insufficient relative to its 1.5°C-compatible pathway.

The percentage change panels confirm this: the US has not seen sustained positive percentage growth since the mid-2000s, making it one of the few large economies in confirmed long-run decline.

---

### China — The World's Growth Engine, Now Slowing

China's panels are the most dramatic in the entire chart and tell a three-act story of their own.

**Act 1 — Explosive growth (1990–2013):**  
Nearly every bar is positive, and the absolute bars are enormous — annual additions of 300–700 Mt CO₂ in peak years (2003–2011). This period corresponds to China's rapid industrialisation, infrastructure buildout, and entry into global manufacturing supply chains. The percentage bars confirm the pace: double-digit YoY growth in several years during the 2000s.

**Act 2 — Deceleration (2014–2019):**  
Absolute additions slow significantly. Percentage growth drops to 1–3% annually. This reflects China's deliberate rebalancing away from heavy industry toward services and domestic consumption, alongside early renewable energy deployment. China's coal consumption plateaued during this period.

**Act 3 — Pandemic and rebound (2020–present):**  
Like the US, China shows a negative bar in 2020, but its **2021 rebound is the largest absolute single-year increase of any country in the dataset** — over 700 Mt added in one year as China's economy recovered faster than peers. Post-2021, growth has resumed but at a slower rate than the pre-2014 period.

The critical question A2 raises about China — but cannot answer alone — is whether the post-2021 deceleration represents a genuine structural peak or a temporary plateau. Plot B1 (carbon intensity of GDP) provides partial evidence that China's economy is becoming more efficient; Plot C1 (fuel breakdown) shows coal still dominates.

---

### India — Consistent Growth, Moderate but Unbroken

India's panels present a strikingly different pattern from both the US and China: **almost uninterrupted positive growth** across the entire 35-year window.

- Absolute additions are modest in early years (10–30 Mt annually through the 1990s) but have grown steadily, reaching 100–200 Mt per year by the 2020s.
- Percentage growth has been consistently positive at 4–8% per year — the most stable growth profile of any country in the chart.
- The **only negative bar** appears in 2020 (COVID), and India's recovery in 2021 was swift and strong, with one of the largest percentage rebounds in the dataset (~10% YoY).
- Unlike China, India has shown **no sign of deceleration** in its growth trajectory. Its emissions are still rising at approximately the rate of its GDP growth, suggesting that decoupling has not yet begun.

This is the analytically most important observation about India in A2: at current growth rates, India will add more to global emissions over the next two decades than any other single country. The question Plot A1 raises — which development path will India follow — is answered in A2 with a clear current-trajectory answer: the high-growth path.

---

### Germany — Europe's Decarbonisation Benchmark

Germany's panels are the visual inverse of China's: a near-unbroken sequence of **negative bars** spanning more than three decades, with only occasional small positive interruptions.

- In absolute terms, Germany's changes are small — the bars rarely exceed ±50 Mt — but this reflects Germany's relatively modest total emissions base (~750 Mt at peak) rather than slow change.
- In percentage terms, Germany shows consistent annual declines of 2–6%, interrupted by the post-reunification spike in the early 1990s (when East German industrial capacity was absorbed and then restructured) and a brief positive period around 2010.
- The **steepest declines** appear after 2018, corresponding to Germany's accelerated coal phase-out and the rapid scaling of wind and solar capacity under the Energiewende.
- The **2020 COVID dip** is visible but relatively modest in percentage terms, as Germany's emissions had already fallen so far from their peak that the shock was proportionally smaller.

Germany's A2 profile is the clearest example in the chart of what sustained, policy-driven decarbonisation looks like over time: not a single dramatic event, but a steady, compounding annual reduction over decades.

---

### United Kingdom — The Fastest Decarbonising Large Economy

The UK panels tell the most dramatic decarbonisation story in the chart when viewed through the percentage lens.

- Absolute changes are small (the UK is a relatively small economy in emissions terms), but **percentage declines are consistently among the largest** of any country shown.
- The UK has recorded annual percentage declines of 3–8% in most years since 2012, driven by the near-complete elimination of coal from electricity generation (from ~40% of the power mix in 2012 to under 2% by 2022) and the growth of offshore wind.
- Like Germany, the UK shows a **positive interruption around 2010** — the post-Global Financial Crisis recovery briefly pushed emissions up before the structural decline resumed.
- **2020** shows the largest single-year percentage drop in the UK's record, reflecting both COVID lockdowns and the continued coal phase-out coinciding with record renewable generation.

A critical caveat for the UK, however, is that its production-based emissions tell only part of the story. As Plot B3 demonstrates, the UK is the most extreme net carbon importer in the dataset — over 60% of its consumption-based footprint is embedded in imported goods. The rapid decline visible in A2 is partly a genuine decarbonisation achievement and partly a consequence of offshoring manufacturing to China and other high-emission economies.

---

## 3. Cross-Country Patterns and Key Observations

### The COVID signature is universal but asymmetric

Every country shows a negative bar in 2020. However, the recovery pattern differs sharply:
- **China** rebounded fastest and largest in absolute terms (2021).
- **India** rebounded fastest in percentage terms.
- **US, Germany, UK** show more muted rebounds, with the structural downward trend resuming quickly.

This asymmetry reflects the different roles of manufacturing versus services in each economy. COVID hit manufacturing-heavy economies harder and their recovery added more carbon.

### Scale vs. rate: the central analytical tension

The absolute and percentage panels together expose a fundamental tension in how to measure climate progress:

| Country | Absolute trend | % trend | Interpretation |
|---|---|---|---|
| United States | Declining | Declining | Genuine structural fall |
| China | Still rising (slowly) | Slowing | Deceleration, not yet peak |
| India | Rising | Stable growth | No decoupling yet |
| Germany | Declining | Declining fast | Policy-driven decarbonisation |
| United Kingdom | Declining | Declining fastest | Structural + policy shift |

### The baseline effect distorts percentage comparisons

Germany and the UK show large percentage declines partly because their absolute emission bases are now so low that any reduction looks large in proportional terms. China's percentage growth looks modest (2–3%) but represents hundreds of megatonnes in absolute terms — more than Germany's entire annual output. This is why the dual-panel design is essential: neither metric alone tells the full story.

---

## 4. Connection to Other Plots

| Question raised by A2 | Answered by |
|---|---|
| Is China's slowdown structural or cyclical? | Plot B1 (CO₂/GDP intensity), Plot C1 (fuel mix) |
| Why is the UK declining so fast in % terms? | Plot B3 (trade CO₂ — offshoring caveat) |
| What is driving Germany's consistent decline? | Plot C4 (energy carbon intensity) |
| Will India's growth rate eventually slow? | Plot A1 (EKC position), Plot C5 (energy vs CO₂) |
| What happened globally at these key dates? | Plot D3 (global trend with Kyoto/Paris annotations) |

---

## 5. Limitations

1. **Production-based only.** Annual growth rates in A2 measure domestic production emissions. Countries that offshore manufacturing (UK, Germany) will show faster apparent declines than their true consumption-based footprints warrant.

2. **Five-country selection.** The chart focuses on major economies. Notable omissions include Russia (whose post-1991 collapse and slow recovery is one of the most dramatic emission trajectories in the dataset) and Brazil (whose land-use emissions dominate over fossil fuels and follow a completely different cyclical pattern).

3. **No decomposition of drivers.** A2 shows *that* emissions changed but not *why* — whether from GDP growth, efficiency improvements, fuel switching, or structural economic change. Plot B1 begins to decompose this by isolating the carbon intensity of GDP.

4. **Short-term shocks vs. structural trends.** COVID (2020) and the Global Financial Crisis (2007–09) create large bars that can visually dominate the panels. Care should be taken not to mistake shock-driven reductions for structural decarbonisation — the post-shock rebound years are the diagnostic signal.

---

*Data source: Our World in Data (OWID) CO₂ and Greenhouse Gas Emissions dataset. Period: 1988–2023.*

# Plot A3 — CO₂ vs CO₂ Including Land-Use Change
## Hidden Deforestation Emissions Across Six Countries (1950–2023)

---

## 1. Chart Overview

**Chart type:** Small-multiple area chart (2×3 grid, six countries)  
**Data:** OWID CO₂ dataset, annual observations  
**Solid line:** CO₂ from fossil fuels and industry only (excl. LUC)  
**Dashed line:** CO₂ including land-use change (incl. LUC)  
**Shaded gap:** The hidden emissions — the difference between the two lines  
**Countries covered:** Brazil, Indonesia, United States, China, India, Democratic Republic of Congo

> The design is deliberately minimal. Each panel asks one question: *how much of a country's true carbon footprint disappears when land-use emissions are excluded from standard reporting?* The shaded gap is the answer. Where the two lines overlap almost perfectly, land-use change is irrelevant. Where the gap is large — sometimes larger than the fossil fuel baseline itself — the standard headline figure is a serious undercount.

---

## 2. Key Findings

### Finding 1 — Brazil: The Most Dramatic Distortion in the Dataset

Brazil's panel delivers the chart's central shock. From the 1950s through to around 2005, the **dashed line (incl. LUC) runs far above the solid line** — at peak, total emissions including land-use exceeded 3,200 Mt CO₂, while fossil fuel emissions alone were barely 500 Mt. The shaded gap between the two lines represents deforestation of the Amazon, which for decades was Brazil's dominant source of carbon output by a factor of 4–6×.

Two inflection points define Brazil's story:

- **~2005 peak:** The gap reaches its maximum. This corresponds to the height of Amazon deforestation rates under soy and cattle expansion.
- **Post-2005 collapse of the gap:** Brazil's deforestation crackdown — the 2004 Action Plan for the Prevention and Control of Deforestation in the Legal Amazon (PPCDAm) — produces one of the most dramatic emission reductions in any country's modern record. By 2012, the LUC gap had shrunk by over 70%.
- **Post-2019 resurgence:** Under relaxed enforcement, the gap widens again — a visible policy fingerprint on the chart.

**The takeaway for A1:** Brazil appeared to have modest per-capita emissions (~2.5 tonnes) on Plot A1 because that chart used production-based fossil fuel data. Plot A3 reveals that Brazil's *true* footprint at peak was among the highest in the world in absolute terms.

---

### Finding 2 — Indonesia: Volatile Spikes, Not a Smooth Curve

Indonesia's panel is the most visually dramatic in the chart — not because of a broad sustained gap, but because of **sharp, extreme spikes** in the LUC line, particularly in the late 1990s and again in the mid-2010s.

- The **1997–1998 spike** corresponds to the catastrophic El Niño–driven peatland fires, during which Indonesia briefly became one of the world's largest emitters. The dashed line shoots above 2,500 Mt CO₂ — more than triple its baseline — before collapsing back within two years.
- Subsequent spikes in the **2000s and 2015** reflect recurring peat fire events combined with deliberate forest clearance for palm oil expansion.
- Unlike Brazil, Indonesia has not achieved a sustained structural reduction in its LUC emissions — the spikes continue into the 2020s.

The irregular, event-driven pattern in Indonesia highlights an important methodological point: land-use CO₂ is not a smooth flow like fossil fuel combustion. It is episodic, driven by fire seasons, policy enforcement cycles, and commodity price incentives.

---

### Finding 3 — United States: A Narrow but Persistent Gap

The US panel presents a completely different picture from the tropical forest countries. The two lines track extremely closely throughout the entire 1950–2023 period, with only a **thin, consistent pink shading** between them.

This reflects the fact that by the mid-20th century, large-scale deforestation in the continental US had already occurred. What remains is a mix of:

- Ongoing agricultural land clearance (modest in global terms)
- Partially offset by forest regrowth in the northeastern and southeastern US, which acts as a **carbon sink** — occasionally pulling the LUC line *below* the fossil fuel line

The US panel confirms that for industrialised economies with stable land cover, the standard fossil fuel metric is a reasonably accurate representation of total emissions. The omission of LUC does not significantly distort the US headline figure.

---

### Finding 4 — China: Fossil Fuels Dominate, LUC Is Secondary

China's panel shows the smallest relative gap of any country in the chart — and for most of the period, the two lines are almost indistinguishable. This is not because China has no land-use emissions, but because its **fossil fuel trajectory is so steep** (rising from ~1,500 Mt in 1990 to over 12,000 Mt by 2023) that land-use change becomes a rounding error by comparison.

A small positive gap is visible in the 1950s–1970s, corresponding to agricultural expansion and the clearing of forests under collectivisation. By the reform era, however, China's LUC contribution becomes negligible relative to its industrial emissions.

**The implication:** For China, accurate climate accounting does not require LUC correction to any significant degree. The fossil fuel figure tells essentially the complete story.

---

### Finding 5 — India: A Closing Gap Over Time

India's panel shows a **moderate, gradually narrowing gap** between the two lines. In the 1950s–1970s, land-use emissions add a visible additional layer above India's fossil fuel baseline — reflecting the large-scale forest clearance that accompanied post-independence agricultural expansion.

Over time, as India's fossil fuel emissions grow rapidly (the solid line rising steeply from the 1990s onward), the proportional significance of LUC diminishes. By the 2010s, the two lines are nearly coincident.

This is a common pattern among developing economies undergoing industrialisation: early growth is partly land-use driven, but fossil fuel combustion eventually becomes dominant. India is currently in the transition phase between those two regimes.

---

### Finding 6 — Democratic Republic of Congo: Sporadic but Significant

The DRC panel is the least discussed in standard climate reporting but analytically important. The two lines diverge dramatically in **two distinct periods**:

- **Late 1950s–early 1960s:** A large LUC spike coincides with post-independence instability and forest clearance.
- **2000s–2010s:** A second, broader period of elevated LUC emissions reflects the Congo Basin deforestation surge — driven partly by charcoal production for urban cooking fuel, partly by agricultural encroachment.

What makes the DRC case analytically distinctive is that its fossil fuel emissions (the solid line) remain **extremely low throughout** — rarely exceeding 50 Mt. The LUC gap therefore represents not a correction to a large baseline, but *the entirety of the country's climate footprint*. In peak years, the DRC's land-use emissions spike above 1,000 Mt — 20× its fossil fuel level.

This panel is the clearest demonstration that for the world's poorest, most forest-rich nations, a standard fossil fuel metric is not merely incomplete — it is essentially meaningless as a measure of true climate impact.

---

## 3. Cross-Country Patterns

### The gap is inversely related to industrialisation

| Country | LUC significance | Primary driver |
|---|---|---|
| Brazil | Extreme (historically dominant) | Amazon deforestation |
| Indonesia | Extreme (episodic) | Peatland fires, palm oil |
| DRC | Total (fossil baseline negligible) | Forest clearance, charcoal |
| India | Moderate (declining) | Agricultural expansion, now fading |
| United States | Minimal | Historical deforestation complete |
| China | Negligible | Fossil fuels dominate absolutely |

### Policy is legible in the gap

The Brazil panel in particular demonstrates that land-use emissions are not natural or inevitable — they are directly policy-responsive. The 2004–2012 deforestation crackdown produced a visible, measurable, and sustained reduction in the shaded area. The post-2019 reversal is equally visible. No other panel in the chart shows such a direct mapping between political decisions and emission trajectories.

---

## 4. Connection to Other Plots

| Question raised by A3 | Answered by |
|---|---|
| Why did Brazil appear low in A1 (per-capita)? | A3 directly resolves this — fossil data alone undercounts Brazil by 4–6× at peak |
| Does the US gap affect its ranking among large emitters? | No — the US gap is negligible; C4 (energy intensity) is more relevant |
| What drives Indonesia's fossil baseline growth despite the LUC story? | C1 (fuel mix by country) |
| Is DRC's deforestation linked to poverty? | Implicit in A1's bottom-left cluster analysis |
| How does China's clean LUC profile connect to its policy trajectory? | D2, D3 (policy section) |

---

## 5. Limitations

1. **LUC data is the most uncertain in the OWID dataset.** Land-use emissions are estimated from satellite imagery, deforestation surveys, and land-cover models — all of which carry significant uncertainty bands, particularly for peat fires (Indonesia, DRC) where combustion volume is hard to measure directly.

2. **LUC can be negative (sequestration).** Forest regrowth, reforestation, and soil carbon accumulation can make LUC a net sink in some years and countries. The US panel shows occasional periods where the dashed line dips below the solid line for this reason.

3. **Single-country framing misses transnational drivers.** Brazil's and Indonesia's deforestation is substantially driven by global commodity demand — soy, beef, palm oil — originating in rich-country consumption. A consumption-based accounting framework (as in Plots B2/B3) would reallocate some of the LUC gap from producer to consumer nations.

4. **The y-axis scales differ across panels.** This is intentional — it allows each country's internal pattern to be visible — but it prevents direct visual size comparison across countries. China's near-invisible gap looks similar in height to Brazil's, yet the absolute scales are completely different.

---

*Data source: Our World in Data (OWID) CO₂ and Greenhouse Gas Emissions dataset. Period: 1950–2023.*

# Plot A4 — Cumulative CO₂ Emissions & Global Share (2024)
## Historical Responsibility Across Major Economies

---

## 1. Chart Overview

**Chart type:** Dual-panel — horizontal bar chart (left) + pie chart (right)  
**Data:** OWID CO₂ dataset, cumulative totals from industrialisation through 2024  
**Left panel X-axis:** Cumulative CO₂ in gigatonnes (Gt) — total carbon dioxide released
by each country across all years of recorded emissions  
**Left panel Y-axis:** Countries, ranked from highest to lowest cumulative emitter  
**Right panel:** Each slice = that country's percentage share of total global
cumulative CO₂ emissions  
**Countries covered:** United States, China, Russia, Germany, United Kingdom,
Japan, India, France, Canada, Poland + Rest of World

> The critical distinction this chart makes is between *current* emissions
> (who is polluting most *today*) and *cumulative* emissions (who has polluted
> most *across history*). Because CO₂ stays in the atmosphere for centuries,
> cumulative emissions are the correct metric for assigning historical
> responsibility for climate change — not annual snapshots.

---

## 2. Key Findings

### Finding 1 — The United States: Unmatched Historical Responsibility

At **435 Gt**, the United States has emitted more CO₂ cumulatively than any
other nation — by a large margin. Its 23.5% share of global cumulative
emissions means that nearly one quarter of all the industrial CO₂ currently
in the Earth's atmosphere was put there by a single country that holds
about 4% of the world's population.

This figure reflects the US's:
- Early and rapid industrialisation from the mid-19th century onward
- Dominance of coal-powered electricity and steel production through the
  20th century
- Consistently high per-capita emissions sustained over 150+ years
  (as established in Plot A1)
- Large absolute population combined with high per-capita output

The US bar is so dominant that it visually anchors the entire left panel —
every other country's bar is measured implicitly against it.

---

### Finding 2 — China: Large Total, but a Late Starter

China's **285 Gt** and 15.4% share place it firmly second. However, this
figure requires important context: the overwhelming majority of China's
cumulative emissions have been generated **since 1990**. China's
industrialisation accelerated dramatically later than the US, Europe, or
Russia, meaning its historical share understates its *current* annual
dominance (China is now the world's largest annual emitter by far, as
shown in Plot A2).

The implication is directional: China's cumulative share will continue
rising steeply in coming decades even if annual growth slows, while the
US share will grow only slowly as its annual emissions decline.

---

### Finding 3 — Europe's Outsized Historical Footprint

Russia (123 Gt, 6.6%), Germany (95 Gt, 5.1%), the United Kingdom
(80 Gt, 4.3%), France (40 Gt, 2.2%), and Poland (29 Gt) together
contribute approximately **18% of global cumulative emissions**.

This is striking given their relatively modest populations and the fact
that Germany, the UK, and France have all significantly reduced annual
emissions in recent decades (as shown in Plot A2). Their cumulative
burden is the legacy of being the **birthplace of the Industrial
Revolution** — coal-powered industrialisation beginning in the
mid-1800s means over 150 years of high-intensity emissions are
already banked in the atmosphere.

The United Kingdom's position is particularly notable in the context
of Plot A3 and A2: while its *annual* emissions have fallen dramatically
(making it appear a climate success story), its *cumulative* 80 Gt
represents a historical debt that current reductions do not erase.

---

### Finding 4 — India and Japan: Large Absolutes, Small Shares

India (66 Gt, 3.8%) and Japan (70 Gt, 4.3%) both have significant
absolute cumulative totals, but their global shares are modest relative
to their population sizes.

India's case is the most analytically important:
- 66 Gt cumulative for a country of 1.4 billion people
- Compared to the US's 435 Gt for ~330 million people
- On a **per-person cumulative basis**, the average Indian has contributed
  roughly **10× less** to atmospheric CO₂ than the average American across
  history

This per-capita historical gap is the foundation of India's (and the
broader Global South's) argument that rich nations must bear
disproportionate responsibility for climate mitigation — they
filled the atmospheric carbon budget first.

---

### Finding 5 — Rest of World: The 31.9% Majority

The grey pie slice represents over 180 countries — the majority of
humanity — accounting for just 31.9% of cumulative emissions. This
group includes:
- All of Sub-Saharan Africa
- Most of Southeast Asia
- The entirety of Central America and the Caribbean
- Most of the Middle East (outside major oil producers)

These are predominantly the countries facing the *worst* climate
impacts (heat stress, flooding, drought, sea-level rise) while
having contributed the least to the problem. The gap between
contribution and consequence is the defining equity challenge of
climate policy — and this single grey slice makes it visible
more starkly than any other element of the chart.

---

## 3. Cross-Country Summary Table

| Country | Cumulative CO₂ (Gt) | Global Share (%) | Notes |
|---|---|---|---|
| United States | 435 | 23.5 | Largest historical emitter by far |
| China | 285 | 15.4 | Mostly post-1990; share still rising fast |
| Russia | 123 | 6.6 | Soviet-era heavy industry legacy |
| Germany | 95 | 5.1 | Industrial Revolution + 20th-century coal |
| United Kingdom | 80 | 4.3 | First industrial nation; now decarbonising |
| Japan | 70 | 4.3 | Post-WWII manufacturing expansion |
| India | 66 | 3.8 | Low per-capita historically; rising fast now |
| France | 40 | 2.2 | Partly offset by early nuclear adoption |
| Canada | 36 | 2.2 | High per-capita, small population |
| Poland | 29 | 1.6 | Coal-dependent economy |
| Rest of World | — | 31.9 | 180+ countries combined |

---

## 4. Connection to Other Plots

| Question raised by A4 | Answered by |
|---|---|
| Why does the US have such a high cumulative share? | A1 (high per-capita), A2 (slow to decline) |
| Is China's annual trajectory likely to increase its share further? | A2 (growth rate), B1 (carbon intensity) |
| Does the UK's rapid annual decline reduce its historical burden? | A2 (yes, annually) — A4 shows cumulative debt remains |
| Why does India argue for differentiated climate responsibility? | A4 directly — 3.8% share for 18% of world population |
| What does Europe's large share mean for climate finance obligations? | D2, D3 (policy section) |

---

## 5. Limitations

1. **Start date dependency.** Cumulative totals depend on when counting
   begins. Using 1750 (pre-industrial baseline) versus 1950 significantly
   changes relative shares, as early US and European emissions are heavily
   weighted by the longer window.

2. **Fossil fuels only.** Like Plot A1, this chart excludes land-use change
   emissions. Including LUC (as in A3) would raise Brazil and Indonesia
   significantly and lower the relative shares of the industrialised nations.

3. **Nation-state boundaries change over time.** Russia's figure includes
   emissions attributed to the Soviet Union. Germ