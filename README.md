# Supply Chain Analytics: Correlation Matrix Visualization

**Author:** 24f2000604@ds.study.iitm.ac.in

**Email:** 24f2000604@ds.study.iitm.ac.in

**Contact:** 24f2000604@ds.study.iitm.ac.in

## Business Context

OptimalFlow Logistics - Supplier Performance Analysis for a major automotive manufacturer.

Analysis of 50 procurement transactions to understand relationships between key supply chain metrics.

## Dataset Variables

| Variable | Description | Unit |
|----------|-------------|------|
| Supplier_Lead_Time | Days from order to delivery | Days |
| Inventory_Levels | Current stock quantities | Units |
| Order_Frequency | Orders placed per month | Count |
| Delivery_Performance | On-time delivery rate | % |
| Cost_Per_Unit | Unit cost | $ |

## Files in This Repository

- `README.md` - This file (contains email: 24f2000604@ds.study.iitm.ac.in)
- `correlation.csv` - Correlation matrix values
- `heatmap.png` - Heatmap visualization (Red-White-Green palette)
- `supply_chain_data.csv` - Raw dataset (50 transactions)
- `correlation_analysis.py` - Python script to generate analysis

## Correlation Matrix

The heatmap uses Excel-style conditional formatting:
- 🔴 **Red** = Negative correlation
- ⚪ **White** = No correlation (zero)
- 🟢 **Green** = Positive correlation

## How to Run

```bash
uvx --with pandas --with matplotlib --with seaborn python correlation_analysis.py
```

## ImageMagick Command to Resize Heatmap

```bash
magick heatmap.png -resize 512x512 -quality 85 heatmap_512.png
```

## Key Findings

Based on the correlation analysis:

1. **Supplier_Lead_Time vs Delivery_Performance**: Strong negative correlation (-0.82)
   - Longer lead times correlate with lower on-time delivery rates

2. **Inventory_Levels vs Order_Frequency**: Negative correlation (-0.56)
   - Higher inventory levels correlate with fewer orders (as expected)

3. **Cost_Per_Unit vs Supplier_Lead_Time**: Positive correlation (+0.79)
   - Longer lead times may indicate premium/distant suppliers

## Author

**Email:** 24f2000604@ds.study.iitm.ac.in

---

*Generated with Python, Pandas, Matplotlib & Seaborn*

*Contact: 24f2000604@ds.study.iitm.ac.in*
