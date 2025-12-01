# Customer Journey Alluvial Diagram Generator
# Author: 24f2000604@ds.study.iitm.ac.in
# Email: 24f2000604@ds.study.iitm.ac.in
#
# This creates an Alluvial/Sankey-style diagram similar to RAWGraphs output

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.sankey import Sankey
import pandas as pd
import numpy as np

# Author: 24f2000604@ds.study.iitm.ac.in

print("=" * 60)
print("Customer Journey Alluvial Diagram")
print("Author: 24f2000604@ds.study.iitm.ac.in")
print("=" * 60)

# Load data
df = pd.read_csv('data.csv')
print(f"\nData loaded: {len(df)} rows")

# Create figure
fig, ax = plt.subplots(figsize=(8, 8))

# Define positions for each column
col_positions = {'Channel': 0, 'Stage': 1, 'Outcome': 2}

# Get unique values for each column
channels = df['Channel'].unique()
stages = df['Stage'].unique()
outcomes = df['Outcome'].unique()

# Color palettes
channel_colors = {'Social': '#3498db', 'Email': '#e74c3c', 'Organic': '#2ecc71', 'Paid': '#f39c12'}
outcome_colors = {'Converted': '#27ae60', 'Abandoned': '#c0392b', 'Pending': '#f39c12'}

# Calculate node positions
def get_node_positions(items, x_pos):
    n = len(items)
    y_positions = np.linspace(0.9, 0.1, n)
    return {item: (x_pos, y) for item, y in zip(items, y_positions)}

channel_pos = get_node_positions(channels, 0.1)
stage_pos = get_node_positions(stages, 0.5)
outcome_pos = get_node_positions(outcomes, 0.9)

# Aggregate flows
# Channel -> Stage flows
channel_stage = df.groupby(['Channel', 'Stage'])['Count'].sum().reset_index()
# Stage -> Outcome flows  
stage_outcome = df.groupby(['Stage', 'Outcome'])['Count'].sum().reset_index()

# Draw flows (simplified alluvial representation)
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.path import Path
import matplotlib.patches as patches

# Draw channel to stage flows
for _, row in channel_stage.iterrows():
    channel, stage, count = row['Channel'], row['Stage'], row['Count']
    start = channel_pos[channel]
    end = stage_pos[stage]
    
    # Draw curved connection
    alpha = min(count / 100, 0.8)
    width = count / 50
    
    verts = [
        (start[0] + 0.05, start[1]),
        (0.3, start[1]),
        (0.3, end[1]),
        (end[0] - 0.05, end[1]),
    ]
    codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor='none', edgecolor=channel_colors[channel], 
                               lw=width, alpha=alpha)
    ax.add_patch(patch)

# Draw stage to outcome flows
for _, row in stage_outcome.iterrows():
    stage, outcome, count = row['Stage'], row['Outcome'], row['Count']
    start = stage_pos[stage]
    end = outcome_pos[outcome]
    
    alpha = min(count / 100, 0.8)
    width = count / 50
    
    verts = [
        (start[0] + 0.05, start[1]),
        (0.7, start[1]),
        (0.7, end[1]),
        (end[0] - 0.05, end[1]),
    ]
    codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor='none', edgecolor=outcome_colors[outcome], 
                               lw=width, alpha=alpha)
    ax.add_patch(patch)

# Draw nodes
node_height = 0.08
node_width = 0.08

# Channel nodes
for channel, (x, y) in channel_pos.items():
    rect = FancyBboxPatch((x - node_width/2, y - node_height/2), node_width, node_height,
                          boxstyle="round,pad=0.01", facecolor=channel_colors[channel], 
                          edgecolor='white', linewidth=2)
    ax.add_patch(rect)
    ax.text(x, y, channel, ha='center', va='center', fontsize=9, fontweight='bold', color='white')

# Stage nodes
stage_colors = {'Awareness': '#9b59b6', 'Interest': '#3498db', 'Decision': '#1abc9c'}
for stage, (x, y) in stage_pos.items():
    rect = FancyBboxPatch((x - node_width/2, y - node_height/2), node_width, node_height,
                          boxstyle="round,pad=0.01", facecolor=stage_colors.get(stage, '#95a5a6'), 
                          edgecolor='white', linewidth=2)
    ax.add_patch(rect)
    ax.text(x, y, stage, ha='center', va='center', fontsize=9, fontweight='bold', color='white')

# Outcome nodes
for outcome, (x, y) in outcome_pos.items():
    rect = FancyBboxPatch((x - node_width/2, y - node_height/2), node_width, node_height,
                          boxstyle="round,pad=0.01", facecolor=outcome_colors[outcome], 
                          edgecolor='white', linewidth=2)
    ax.add_patch(rect)
    ax.text(x, y, outcome, ha='center', va='center', fontsize=8, fontweight='bold', color='white')

# Column headers
ax.text(0.1, 0.98, 'Channel', ha='center', va='bottom', fontsize=12, fontweight='bold')
ax.text(0.5, 0.98, 'Stage', ha='center', va='bottom', fontsize=12, fontweight='bold')
ax.text(0.9, 0.98, 'Outcome', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Title
ax.set_title('Customer Journey Flow\nAlluvial Diagram', fontsize=14, fontweight='bold', pad=10)

# Author
ax.text(0.5, 0.02, '24f2000604@ds.study.iitm.ac.in', ha='center', fontsize=8, style='italic', color='gray',
        transform=ax.transAxes)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.tight_layout()

# Save as 512x512
plt.savefig('chart.png', dpi=64, bbox_inches='tight', facecolor='white', edgecolor='none')
print("\nChart saved: chart.png")

plt.close()

# Resize to exact 512x512
import subprocess
subprocess.run(['magick', 'chart.png', '-resize', '512x512!', 'chart.png'], check=True)
print("Resized to 512x512 pixels")

print(f"\nAuthor: 24f2000604@ds.study.iitm.ac.in")
