# Data Quality Report
## Azerbaijan Cotton Yield Prediction Project
**Member 1 — Data Engineer**

---

## 1. Cotton Dataset

| Property | Value |
|---|---|
| Source | Course-provided Excel file |
| Original format | Wide (regions as rows, years as columns) |
| Reshaped format | Long (one row per region per year) |
| Rows after reshape | 725 |
| Districts | 29 |
| Year range | 2000 – 2024 |

### Missing Values
- **191 null values** found in yield_tonnes column
- **Fix applied:** deleted
- **Result:** 0 nulls remaining after cleaning 

---

## 2. Weather Dataset

| Property | Value |
|---|---|
| Source | Open-Meteo Historical Archive API |
| Locations | 5 (Ganja, Shamkir, Sabirabad, Lankaran, Nakhchivan) |
| Date range | 2000-01-01 – 2024-12-31 |
| Total rows | ~45,660 daily rows |
| Missing values | 0 (API fills gaps automatically) |

### Variables Collected
- temperature_2m_max / min / mean
- precipitation_sum
- relative_humidity_2m_max / min
- wind_speed_10m_max
- et0_fao_evapotranspiration

---

## 3. District to Weather Station Mapping

| Weather Zone | Districts Covered |
|---|---|
| Ganja | 16 districts (central and western Azerbaijan) |
| Sabirabad | 7 districts (Kür-Araz lowland) |
| Lankaran | 4 districts (southern humid zone) |

**Limitation:** 29 districts share only 5 weather stations.
Districts within the same zone receive identical weather features.
This is a known limitation documented for future improvement.

---

## 4. Alignment Check

| Check | Result |
|---|---|
| Year overlap (cotton vs weather) | 2000–2024 ✓ |
| All districts mapped | 22/22 ✓ |
| Nulls after cleaning | 0 ✓ |

---

## 5. Limitations

- No soil quality data available
- No irrigation or fertilizer records
- Weather station proximity varies by district
- 2024 partial year included in dataset