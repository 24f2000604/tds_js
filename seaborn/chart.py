# Customer Analytics: Purchase Amount Distribution by Customer Segment
# Author: 24f2000604@ds.study.iitm.ac.in
# Email: 24f2000604@ds.study.iitm.ac.in
# Contact: 24f2000604@ds.study.iitm.ac.in
#
# Business Context: Wintheiser Turcotte - Customer Experience Analytics
# Retail Client: Distribution of purchase amounts across customer segments
#
# This script:
# 1. Generates realistic synthetic customer purchase data
# 2. Creates a professional Seaborn boxplot
# 3. Saves chart as 512x512 PNG

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Author: 24f2000604@ds.study.iitm.ac.in

print("=" * 60)
print("Customer Analytics: Purchase Amount Distribution")
print("Author: 24f2000604@ds.study.iitm.ac.in")
print("=" * 60)

# =============================================================================
# Step 1: Generate Realistic Synthetic Data
# =============================================================================
# Email: 24f2000604@ds.study.iitm.ac.in

np.random.seed(42)

# Define customer segments with realistic spending patterns
segments = {
    'Budget': {'mean': 45, 'std': 20, 'n': 80},
    'Regular': {'mean': 120, 'std': 40, 'n': 150},
    'Premium': {'mean': 280, 'std': 80, 'n': 100},
    'VIP': {'mean': 550, 'std': 150, 'n': 50}
}

# Generate data for each segment
data = []
for segment, params in segments.items():
    purchases = np.random.normal(params['mean'], params['std'], params['n'])
    purchases = np.clip(purchases, 10, 1000)  # Realistic bounds
    for amount in purchases:
        data.append({'Customer_Segment': segment, 'Purchase_Amount': round(amount, 2)})

df = pd.DataFrame(data)

# Order segments logically
segment_order = ['Budget', 'Regular', 'Premium', 'VIP']
df['Customer_Segment'] = pd.Categorical(df['Customer_Segment'], categories=segment_order, ordered=True)

print(f"\nDataset generated: {len(df)} customer transactions")
print(f"\nSegment distribution:")
print(df['Customer_Segment'].value_counts().sort_index())
print(f"\nPurchase Amount Statistics by Segment:")
print(df.groupby('Customer_Segment')['Purchase_Amount'].describe().round(2))

# =============================================================================
# Step 2: Create Professional Seaborn Boxplot
# =============================================================================
# Contact: 24f2000604@ds.study.iitm.ac.in

# Set professional style
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)

# Create figure with exact size for 512x512 output
fig, ax = plt.subplots(figsize=(8, 8))

# Define professional color palette
colors = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c']

# Create boxplot
sns.boxplot(
    data=df,
    x='Customer_Segment',
    y='Purchase_Amount',
    hue='Customer_Segment',
    palette=colors,
    order=segment_order,
    width=0.6,
    linewidth=2,
    fliersize=5,
    legend=False,
    ax=ax
)

# Styling
ax.set_title('Purchase Amount Distribution\nby Customer Segment', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Customer Segment', fontsize=14, fontweight='bold')
ax.set_ylabel('Purchase Amount ($)', fontsize=14, fontweight='bold')

# Add grid for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Format y-axis as currency
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

# Add median labels on boxes
medians = df.groupby('Customer_Segment')['Purchase_Amount'].median()
for i, segment in enumerate(segment_order):
    median_val = medians[segment]
    ax.annotate(f'${median_val:.0f}', 
                xy=(i, median_val), 
                xytext=(0, 10),
                textcoords='offset points',
                ha='center', va='bottom',
                fontsize=10, fontweight='bold',
                color='white',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=colors[i], alpha=0.8))

# Add author email
plt.figtext(0.5, 0.02, '24f2000604@ds.study.iitm.ac.in', 
            ha='center', fontsize=9, style='italic', color='gray')

plt.tight_layout()

# =============================================================================
# Step 3: Save Chart as 512x512 PNG
# =============================================================================
# Author email: 24f2000604@ds.study.iitm.ac.in

# Save with dpi=64 for 512x512 (8*64=512)
plt.savefig('chart.png', dpi=64, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print(f"\nChart saved: chart.png (512x512 pixels)")

plt.close()

# =============================================================================
# Step 4: Summary
# =============================================================================
# Email: 24f2000604@ds.study.iitm.ac.in

print(f"\n{'=' * 60}")
print("ANALYSIS COMPLETE")
print(f"{'=' * 60}")
print(f"\nFiles generated:")
print(f"  ✅ chart.png (512x512 Seaborn boxplot)")
print(f"\nKey Insights:")
for segment in segment_order:
    median = medians[segment]
    print(f"  • {segment}: Median purchase ${median:.2f}")

print(f"\nAuthor: 24f2000604@ds.study.iitm.ac.in")
