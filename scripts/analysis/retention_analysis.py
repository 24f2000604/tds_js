"""
E-Commerce Customer Retention Analysis Script

This script analyzes quarterly customer retention rates and generates visualizations.
It was developed using an LLM-powered workflow (ChatGPT Codex / LLM) to generate code.

Author: 24f2000604@ds.study.iitm.ac.in
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Hard-coded quarterly retention values (%)
QUARTERLY_RETENTION = {
    'Q1': 72.26,
    'Q2': 71.57,
    'Q3': 74.89,
    'Q4': 77.52
}

# Industry benchmark target (%)
INDUSTRY_BENCHMARK = 85

def calculate_average_retention(retention_data):
    """
    Calculate the average retention rate across all quarters.
    
    Args:
        retention_data: Dictionary with quarter keys and retention values
        
    Returns:
        float: Average retention rate rounded to 2 decimal places
    """
    values = list(retention_data.values())
    average = sum(values) / len(values)
    return round(average, 2)

def create_retention_dataframe(retention_data):
    """
    Create a pandas DataFrame from the retention data.
    
    Args:
        retention_data: Dictionary with quarter keys and retention values
        
    Returns:
        pd.DataFrame: DataFrame with quarter and retention columns
    """
    df = pd.DataFrame({
        'quarter': list(retention_data.keys()),
        'retention': list(retention_data.values())
    })
    return df

def save_csv(df, filepath):
    """
    Save the DataFrame to a CSV file.
    
    Args:
        df: pandas DataFrame to save
        filepath: Path to save the CSV file
    """
    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"CSV saved to: {filepath}")

def create_retention_chart(df, average, benchmark, output_path):
    """
    Create a line chart showing quarterly retention trend with benchmark overlay.
    
    Args:
        df: DataFrame with quarter and retention data
        average: Average retention rate
        benchmark: Industry benchmark target
        output_path: Path to save the chart image
    """
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot quarterly retention trend line
    ax.plot(df['quarter'], df['retention'], marker='o', linewidth=2, 
            markersize=8, color='#2E86AB', label='Quarterly Retention Rate')
    
    # Add data point labels
    for i, (q, r) in enumerate(zip(df['quarter'], df['retention'])):
        ax.annotate(f'{r}%', (q, r), textcoords="offset points", 
                    xytext=(0, 10), ha='center', fontsize=10, fontweight='bold')
    
    # Add horizontal line for industry benchmark
    ax.axhline(y=benchmark, color='#E63946', linestyle='--', linewidth=2,
               label=f'Industry Benchmark ({benchmark}%)')
    
    # Add horizontal line for average retention
    ax.axhline(y=average, color='#457B9D', linestyle=':', linewidth=1.5,
               label=f'Average Retention ({average}%)')
    
    # Set chart properties
    ax.set_xlabel('Quarter', fontsize=12)
    ax.set_ylabel('Retention Rate (%)', fontsize=12)
    ax.set_title('E-Commerce Customer Retention Trend\nQuarterly Analysis', fontsize=14, fontweight='bold')
    
    # Set y-axis limits to provide context
    ax.set_ylim(65, 90)
    
    # Add grid for readability
    ax.grid(True, alpha=0.3)
    
    # Add legend
    ax.legend(loc='lower right', fontsize=10)
    
    # Tight layout for better spacing
    plt.tight_layout()
    
    # Save chart
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Chart saved to: {output_path}")
    plt.close()

def main():
    """Main function to run the retention analysis."""
    
    print("=" * 60)
    print("E-Commerce Customer Retention Analysis")
    print("=" * 60)
    
    # Calculate average retention
    average = calculate_average_retention(QUARTERLY_RETENTION)
    print(f"\nQuarterly Retention Rates:")
    for quarter, rate in QUARTERLY_RETENTION.items():
        print(f"  {quarter}: {rate}%")
    print(f"\nAverage Retention Rate: {average}%")
    print(f"Industry Benchmark Target: {INDUSTRY_BENCHMARK}%")
    print(f"Gap to Target: {round(INDUSTRY_BENCHMARK - average, 2)}%")
    
    # Create DataFrame
    df = create_retention_dataframe(QUARTERLY_RETENTION)
    
    # Define output paths (relative to repository root)
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, '..', '..'))
    
    csv_path = os.path.join(repo_root, 'data', 'retention_quarterly.csv')
    chart_path = os.path.join(repo_root, 'visuals', 'retention_trend.png')
    
    # Save CSV
    save_csv(df, csv_path)
    
    # Create and save chart
    create_retention_chart(df, average, INDUSTRY_BENCHMARK, chart_path)
    
    print("\n" + "=" * 60)
    print("Analysis complete!")
    print("=" * 60)

if __name__ == '__main__':
    main()
