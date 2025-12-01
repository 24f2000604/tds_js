# Employee Performance Analysis
# Author: 24f2000604@ds.study.iitm.ac.in
# Email: 24f2000604@ds.study.iitm.ac.in
# Contact: 24f2000604@ds.study.iitm.ac.in
#
# Business Case: Analyze employee performance data for a Manufacturing company
# to understand departmental distributions and identify patterns.
#
# This script:
# 1. Loads employee data
# 2. Calculates frequency count for "Marketing" department
# 3. Prints the frequency count to console
# 4. Creates a histogram showing department distribution
# 5. Saves everything as an HTML file

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import base64
from io import BytesIO

# Author: 24f2000604@ds.study.iitm.ac.in

# Sample dataset (100 employees)
csv_data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,Operations,Africa,76.94,13,4.5
EMP002,Marketing,Africa,75.92,3,3.1
EMP003,Marketing,Latin America,78.01,11,3.0
EMP004,IT,Africa,73.25,11,3.2
EMP005,Sales,Latin America,70.58,1,4.3
EMP006,Marketing,Europe,82.15,7,4.1
EMP007,HR,Asia,69.42,5,3.8
EMP008,Operations,North America,85.33,15,4.7
EMP009,IT,Europe,77.89,9,3.5
EMP010,Sales,Africa,71.23,4,3.9
EMP011,Marketing,Asia,79.56,8,4.2
EMP012,Finance,Latin America,74.18,6,3.4
EMP013,Operations,Europe,81.67,12,4.4
EMP014,IT,North America,88.92,18,4.8
EMP015,HR,Africa,67.34,2,3.0
EMP016,Sales,Asia,73.45,7,3.7
EMP017,Marketing,North America,80.21,10,4.0
EMP018,Finance,Europe,76.78,8,3.6
EMP019,Operations,Asia,78.90,11,4.1
EMP020,IT,Latin America,75.12,6,3.3
EMP021,Sales,Europe,72.34,5,3.5
EMP022,Marketing,Africa,77.45,9,3.9
EMP023,HR,North America,70.89,4,3.2
EMP024,Finance,Asia,79.23,12,4.3
EMP025,Operations,Latin America,83.56,14,4.6
EMP026,IT,Africa,74.67,7,3.4
EMP027,Sales,North America,76.12,8,3.8
EMP028,Marketing,Europe,81.34,11,4.2
EMP029,HR,Latin America,68.45,3,2.9
EMP030,Finance,North America,82.78,13,4.5
EMP031,Operations,Europe,80.12,10,4.0
EMP032,IT,Asia,79.34,9,3.7
EMP033,Sales,Latin America,71.56,4,3.3
EMP034,Marketing,North America,78.67,8,3.8
EMP035,HR,Europe,72.89,6,3.5
EMP036,Finance,Africa,75.23,7,3.6
EMP037,Operations,North America,86.45,16,4.8
EMP038,IT,Europe,80.56,11,4.1
EMP039,Sales,Asia,74.67,6,3.6
EMP040,Marketing,Latin America,79.78,9,4.0
EMP041,HR,Asia,69.89,4,3.1
EMP042,Finance,Europe,77.12,8,3.7
EMP043,Operations,Africa,82.34,13,4.4
EMP044,IT,North America,84.45,14,4.5
EMP045,Sales,Europe,73.56,5,3.4
EMP046,Marketing,Asia,80.67,10,4.1
EMP047,HR,North America,71.78,5,3.3
EMP048,Finance,Latin America,76.89,7,3.5
EMP049,Operations,Asia,79.12,11,4.0
EMP050,IT,Africa,76.23,8,3.6
EMP051,Sales,North America,77.34,9,3.9
EMP052,Marketing,Europe,82.45,12,4.3
EMP053,HR,Africa,68.56,3,2.8
EMP054,Finance,Asia,78.67,9,3.8
EMP055,Operations,Latin America,81.78,12,4.2
EMP056,IT,Europe,79.89,10,3.9
EMP057,Sales,Africa,72.12,4,3.2
EMP058,Marketing,North America,80.23,11,4.0
EMP059,HR,Latin America,70.34,4,3.0
EMP060,Finance,North America,83.45,14,4.6
EMP061,Operations,Europe,84.56,15,4.7
EMP062,IT,Asia,78.67,9,3.7
EMP063,Sales,Latin America,74.78,6,3.5
EMP064,Marketing,Africa,77.89,8,3.7
EMP065,HR,Europe,73.12,6,3.4
EMP066,Finance,Africa,76.23,7,3.5
EMP067,Operations,North America,85.34,16,4.8
EMP068,IT,Latin America,77.45,8,3.6
EMP069,Sales,Europe,75.56,7,3.7
EMP070,Marketing,Asia,81.67,11,4.2
EMP071,HR,North America,72.78,5,3.3
EMP072,Finance,Europe,79.89,10,3.9
EMP073,Operations,Asia,80.12,11,4.1
EMP074,IT,North America,86.23,17,4.9
EMP075,Sales,Africa,73.34,5,3.4
EMP076,Marketing,Latin America,78.45,9,3.8
EMP077,HR,Asia,69.56,3,2.9
EMP078,Finance,Latin America,77.67,8,3.6
EMP079,Operations,Europe,82.78,13,4.4
EMP080,IT,Africa,75.89,7,3.5
EMP081,Sales,North America,76.12,8,3.8
EMP082,Marketing,Europe,83.23,13,4.4
EMP083,HR,Africa,67.34,2,2.7
EMP084,Finance,North America,81.45,12,4.3
EMP085,Operations,Latin America,79.56,10,4.0
EMP086,IT,Europe,80.67,11,4.0
EMP087,Sales,Asia,74.78,6,3.5
EMP088,Marketing,North America,79.89,10,3.9
EMP089,HR,Europe,71.12,4,3.1
EMP090,Finance,Asia,78.23,9,3.7
EMP091,Operations,North America,87.34,18,4.9
EMP092,IT,Asia,77.45,8,3.6
EMP093,Sales,Europe,75.56,7,3.6
EMP094,Marketing,Africa,78.67,9,3.8
EMP095,HR,Latin America,70.78,4,3.0
EMP096,Finance,Europe,80.89,11,4.1
EMP097,Operations,Africa,81.12,12,4.2
EMP098,IT,North America,83.23,13,4.4
EMP099,Sales,Latin America,72.34,4,3.2
EMP100,Marketing,Asia,80.45,10,4.0"""

# Email: 24f2000604@ds.study.iitm.ac.in

# =============================================================================
# Step 1: Load the employee data
# =============================================================================
print("=" * 60)
print("Employee Performance Analysis")
print("Author: 24f2000604@ds.study.iitm.ac.in")
print("=" * 60)

df = pd.read_csv(StringIO(csv_data))
print(f"\nDataset loaded successfully!")
print(f"Total employees: {len(df)}")
print(f"\nFirst 5 rows:")
print(df.head())

# =============================================================================
# Step 2: Calculate frequency count for "Marketing" department
# =============================================================================
# Contact: 24f2000604@ds.study.iitm.ac.in

department_counts = df['department'].value_counts()
marketing_count = department_counts.get('Marketing', 0)

print(f"\n{'=' * 60}")
print("DEPARTMENT FREQUENCY ANALYSIS")
print(f"{'=' * 60}")
print(f"\nFrequency count for 'Marketing' department: {marketing_count}")
print(f"\nAll department counts:")
print(department_counts)

# =============================================================================
# Step 3: Create histogram showing department distribution
# =============================================================================
# Author email: 24f2000604@ds.study.iitm.ac.in

# Set style
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))

# Create bar chart (histogram of categorical data)
colors = sns.color_palette("husl", len(department_counts))
ax = sns.barplot(x=department_counts.index, y=department_counts.values, palette=colors)

# Add value labels on bars
for i, v in enumerate(department_counts.values):
    ax.text(i, v + 0.5, str(v), ha='center', va='bottom', fontweight='bold', fontsize=12)

# Highlight Marketing bar
marketing_idx = list(department_counts.index).index('Marketing')
bars = ax.patches
bars[marketing_idx].set_edgecolor('red')
bars[marketing_idx].set_linewidth(3)

plt.title('Employee Distribution by Department\n(Marketing highlighted)', fontsize=16, fontweight='bold')
plt.xlabel('Department', fontsize=12)
plt.ylabel('Number of Employees', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save plot to base64 for HTML embedding
buffer = BytesIO()
plt.savefig(buffer, format='png', dpi=150, bbox_inches='tight')
buffer.seek(0)
plot_base64 = base64.b64encode(buffer.read()).decode('utf-8')
plt.close()

# Create second visualization - Performance by Department
plt.figure(figsize=(12, 6))
sns.boxplot(x='department', y='performance_score', data=df, palette="husl")
plt.title('Performance Score Distribution by Department', fontsize=16, fontweight='bold')
plt.xlabel('Department', fontsize=12)
plt.ylabel('Performance Score', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

buffer2 = BytesIO()
plt.savefig(buffer2, format='png', dpi=150, bbox_inches='tight')
buffer2.seek(0)
plot2_base64 = base64.b64encode(buffer2.read()).decode('utf-8')
plt.close()

# =============================================================================
# Step 4: Generate HTML file
# =============================================================================
# Email: 24f2000604@ds.study.iitm.ac.in

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Performance Analysis - 24f2000604@ds.study.iitm.ac.in</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #eaeaea;
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        header {{
            text-align: center;
            padding: 30px 0;
            border-bottom: 2px solid #f9ca24;
            margin-bottom: 30px;
        }}
        h1 {{
            color: #f9ca24;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .email {{
            color: #74b9ff;
            font-size: 1.1em;
        }}
        .section {{
            background: rgba(255,255,255,0.05);
            border-radius: 10px;
            padding: 25px;
            margin-bottom: 25px;
            border: 1px solid rgba(255,255,255,0.1);
        }}
        h2 {{
            color: #f9ca24;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid rgba(249,202,36,0.3);
        }}
        .highlight {{
            background: rgba(249,202,36,0.2);
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            margin: 20px 0;
        }}
        .highlight .count {{
            font-size: 3em;
            color: #f9ca24;
            font-weight: bold;
        }}
        .highlight .label {{
            font-size: 1.2em;
            color: #74b9ff;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        th {{
            background: rgba(249,202,36,0.2);
            color: #f9ca24;
        }}
        tr:hover {{
            background: rgba(255,255,255,0.05);
        }}
        .chart-container {{
            text-align: center;
            margin: 20px 0;
        }}
        .chart-container img {{
            max-width: 100%;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        .stat-card {{
            background: rgba(255,255,255,0.08);
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }}
        .stat-card .value {{
            font-size: 2em;
            color: #f9ca24;
            font-weight: bold;
        }}
        .stat-card .label {{
            color: #aaa;
            margin-top: 5px;
        }}
        footer {{
            text-align: center;
            padding: 30px 0;
            margin-top: 30px;
            border-top: 1px solid rgba(255,255,255,0.1);
            color: #888;
        }}
        code {{
            background: #2d3436;
            color: #81ecec;
            padding: 2px 8px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
        }}
        pre {{
            background: #2d3436;
            color: #81ecec;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
            margin: 15px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📊 Employee Performance Analysis</h1>
            <p class="email">Author: 24f2000604@ds.study.iitm.ac.in</p>
            <p style="margin-top: 10px; color: #888;">Manufacturing Company - HR Department Report</p>
        </header>

        <div class="section">
            <h2>📋 Dataset Overview</h2>
            <p>Analysis of employee performance data across multiple regions and departments.</p>
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="value">{len(df)}</div>
                    <div class="label">Total Employees</div>
                </div>
                <div class="stat-card">
                    <div class="value">{df['department'].nunique()}</div>
                    <div class="label">Departments</div>
                </div>
                <div class="stat-card">
                    <div class="value">{df['region'].nunique()}</div>
                    <div class="label">Regions</div>
                </div>
                <div class="stat-card">
                    <div class="value">{df['performance_score'].mean():.1f}</div>
                    <div class="label">Avg Performance</div>
                </div>
            </div>
        </div>

        <div class="section">
            <h2>🎯 Marketing Department Frequency</h2>
            <div class="highlight">
                <div class="count">{marketing_count}</div>
                <div class="label">Employees in Marketing Department</div>
            </div>
            <p style="text-align: center; color: #888;">
                Marketing represents <strong>{(marketing_count/len(df)*100):.1f}%</strong> of total workforce
            </p>
        </div>

        <div class="section">
            <h2>📈 Department Distribution</h2>
            <table>
                <thead>
                    <tr>
                        <th>Department</th>
                        <th>Employee Count</th>
                        <th>Percentage</th>
                        <th>Avg Performance</th>
                    </tr>
                </thead>
                <tbody>
                    {''.join(f"<tr><td>{dept}</td><td>{count}</td><td>{count/len(df)*100:.1f}%</td><td>{df[df['department']==dept]['performance_score'].mean():.2f}</td></tr>" for dept, count in department_counts.items())}
                </tbody>
            </table>
        </div>

        <div class="section">
            <h2>📊 Department Distribution Histogram</h2>
            <div class="chart-container">
                <img src="data:image/png;base64,{plot_base64}" alt="Department Distribution Histogram">
            </div>
            <p style="text-align: center; color: #888; margin-top: 15px;">
                <em>Marketing department highlighted with red border</em>
            </p>
        </div>

        <div class="section">
            <h2>📉 Performance Score Distribution by Department</h2>
            <div class="chart-container">
                <img src="data:image/png;base64,{plot2_base64}" alt="Performance by Department">
            </div>
        </div>

        <div class="section">
            <h2>💻 Python Code Used</h2>
            <pre><code># Email: 24f2000604@ds.study.iitm.ac.in
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('employee_data.csv')

# Calculate Marketing frequency
marketing_count = df[df['department'] == 'Marketing'].shape[0]
print(f"Marketing Department Count: {{marketing_count}}")

# Create histogram
department_counts = df['department'].value_counts()
sns.barplot(x=department_counts.index, y=department_counts.values)
plt.title('Employee Distribution by Department')
plt.show()</code></pre>
        </div>

        <div class="section">
            <h2>📝 Key Findings</h2>
            <ul style="line-height: 2;">
                <li><strong>Marketing Department:</strong> {marketing_count} employees ({(marketing_count/len(df)*100):.1f}% of workforce)</li>
                <li><strong>Largest Department:</strong> {department_counts.index[0]} with {department_counts.values[0]} employees</li>
                <li><strong>Smallest Department:</strong> {department_counts.index[-1]} with {department_counts.values[-1]} employees</li>
                <li><strong>Highest Avg Performance:</strong> {df.groupby('department')['performance_score'].mean().idxmax()} ({df.groupby('department')['performance_score'].mean().max():.2f})</li>
                <li><strong>Most Experienced Region:</strong> {df.groupby('region')['years_experience'].mean().idxmax()} (avg {df.groupby('region')['years_experience'].mean().max():.1f} years)</li>
            </ul>
        </div>

        <footer>
            <p><strong>Contact:</strong> 24f2000604@ds.study.iitm.ac.in</p>
            <p style="margin-top: 10px;">Employee Performance Analysis Report</p>
            <p style="margin-top: 5px; font-size: 0.9em;">Generated with Python, Pandas, Matplotlib & Seaborn</p>
        </footer>
    </div>
</body>
</html>"""

# Save HTML file
html_path = 'employee_analysis.html'
with open(html_path, 'w') as f:
    f.write(html_content)

print(f"\n{'=' * 60}")
print("OUTPUT FILES GENERATED")
print(f"{'=' * 60}")
print(f"\nHTML file saved: {html_path}")
print(f"\nAnalysis complete!")
print(f"\nAuthor: 24f2000604@ds.study.iitm.ac.in")
