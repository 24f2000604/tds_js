# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "pandas",
#     "numpy",
# ]
# ///
#
# Author: 24f2000604@ds.study.iitm.ac.in
# Email: 24f2000604@ds.study.iitm.ac.in
# Contact: 24f2000604@ds.study.iitm.ac.in
#
# This Marimo notebook demonstrates:
# - Interactive slider widgets
# - Reactive cell dependencies
# - Dynamic markdown output
# - Data flow between cells

import marimo

__generated_with = "0.10.0"
app = marimo.App(width="medium")


# ============================================================================
# Cell 1: Setup and Introduction
# ============================================================================
# Data Flow: This cell initializes marimo and displays the title.
# No dependencies - this is the entry point.
# ============================================================================
@app.cell
def cell_introduction():
    import marimo as mo

    # Author: 24f2000604@ds.study.iitm.ac.in
    mo.md(
        """
        # Interactive Data Analysis Notebook

        **Author:** 24f2000604@ds.study.iitm.ac.in

        This notebook demonstrates the relationship between variables
        using interactive widgets. Change the sliders below to see
        how dependent cells update automatically.

        ---
        """
    )
    return (mo,)


# ============================================================================
# Cell 2: Interactive Slider Widgets
# ============================================================================
# Data Flow: This cell creates interactive sliders.
# Dependencies: Requires `mo` from cell_introduction
# Outputs: sample_size, noise_level sliders used by downstream cells
# ============================================================================
@app.cell
def cell_sliders(mo):
    # Email: 24f2000604@ds.study.iitm.ac.in
    # Create interactive slider for sample size
    sample_size = mo.ui.slider(
        start=10,
        stop=500,
        step=10,
        value=100,
        label="Sample Size (n)",
    )

    # Create interactive slider for noise level
    noise_level = mo.ui.slider(
        start=0.0,
        stop=2.0,
        step=0.1,
        value=0.5,
        label="Noise Level (σ)",
    )

    # Create slider for correlation strength
    correlation = mo.ui.slider(
        start=-1.0,
        stop=1.0,
        step=0.1,
        value=0.7,
        label="Correlation (r)",
    )

    # Display sliders with description
    mo.md(
        f"""
        ## Interactive Controls

        Adjust these parameters to explore the data:

        {sample_size}

        {noise_level}

        {correlation}

        ---
        """
    )
    return correlation, noise_level, sample_size


# ============================================================================
# Cell 3: Generate Data Based on Slider Values
# ============================================================================
# Data Flow: This cell DEPENDS on sample_size, noise_level, correlation
# from cell_sliders. When any slider changes, this cell re-executes.
# Outputs: x, y arrays and stats used by visualization cell
# ============================================================================
@app.cell
def cell_generate_data(sample_size, noise_level, correlation):
    # Contact: 24f2000604@ds.study.iitm.ac.in
    import numpy as np

    # Set seed for reproducibility
    np.random.seed(42)

    # Generate x values based on sample_size slider
    n = sample_size.value
    x = np.linspace(0, 10, n)

    # Generate y with correlation and noise based on sliders
    # y = r * x + noise, where r is correlation, noise is scaled by noise_level
    r = correlation.value
    sigma = noise_level.value
    noise = np.random.normal(0, sigma, n)
    y = r * x + noise

    # Calculate statistics
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    std_x = np.std(x)
    std_y = np.std(y)

    # Calculate actual correlation coefficient
    if std_x > 0 and std_y > 0:
        actual_corr = np.corrcoef(x, y)[0, 1]
    else:
        actual_corr = 0.0

    return actual_corr, mean_x, mean_y, n, std_x, std_y, x, y


# ============================================================================
# Cell 4: Dynamic Markdown Output Based on Widget State
# ============================================================================
# Data Flow: DEPENDS on all outputs from cell_generate_data
# This cell updates automatically when sliders change.
# Demonstrates dynamic markdown with computed values.
# ============================================================================
@app.cell
def cell_dynamic_output(mo, actual_corr, mean_x, mean_y, n, std_x, std_y, sample_size, noise_level, correlation):
    # Author email: 24f2000604@ds.study.iitm.ac.in

    # Determine correlation strength description
    abs_corr = abs(actual_corr)
    if abs_corr >= 0.8:
        strength = "Strong"
        emoji = "🟢" * 5
    elif abs_corr >= 0.5:
        strength = "Moderate"
        emoji = "🟡" * 3
    else:
        strength = "Weak"
        emoji = "🔴" * 1

    # Dynamic markdown that updates when sliders change
    mo.md(
        f"""
        ## Data Summary

        | Parameter | Value |
        |-----------|-------|
        | Sample Size | **{n}** |
        | Target Correlation | **{correlation.value:.2f}** |
        | Actual Correlation | **{actual_corr:.4f}** |
        | Noise Level | **{noise_level.value:.2f}** |
        | Mean(X) | {mean_x:.2f} |
        | Mean(Y) | {mean_y:.2f} |
        | Std(X) | {std_x:.2f} |
        | Std(Y) | {std_y:.2f} |

        ### Correlation Strength: {strength}

        {emoji}

        ---

        *This output updates reactively when you move the sliders above.*

        Contact: 24f2000604@ds.study.iitm.ac.in
        """
    )
    return abs_corr, emoji, strength


# ============================================================================
# Cell 5: Visual Indicator with Dynamic Bars
# ============================================================================
# Data Flow: DEPENDS on sample_size slider
# Shows a visual bar that grows/shrinks with sample size
# ============================================================================
@app.cell
def cell_visual_indicator(mo, sample_size, noise_level):
    # 24f2000604@ds.study.iitm.ac.in
    # Create visual representation of sample size
    bar_length = sample_size.value // 10
    noise_bars = int(noise_level.value * 5)

    mo.md(
        f"""
        ## Visual Indicators

        **Sample Size:** {"█" * bar_length} ({sample_size.value})

        **Noise Level:** {"░" * noise_bars} ({noise_level.value:.1f})

        ---
        """
    )
    return bar_length, noise_bars


# ============================================================================
# Cell 6: Data Table Display
# ============================================================================
# Data Flow: DEPENDS on x, y arrays from cell_generate_data
# Displays first few rows of generated data
# ============================================================================
@app.cell
def cell_data_table(mo, x, y):
    # Email: 24f2000604@ds.study.iitm.ac.in
    import pandas as pd

    # Create DataFrame from generated data
    df = pd.DataFrame({
        "X": x,
        "Y": y,
    })

    mo.md(
        f"""
        ## Generated Data Preview

        Showing first 10 rows of {len(df)} total samples:
        """
    )

    # Return DataFrame for display (marimo auto-renders DataFrames)
    return (df,)


@app.cell
def cell_show_table(df):
    # Display the dataframe head
    # Contact: 24f2000604@ds.study.iitm.ac.in
    df.head(10)
    return ()


# ============================================================================
# Cell 7: Footer with Contact Info
# ============================================================================
# Data Flow: Final cell, no outputs consumed by other cells
# ============================================================================
@app.cell
def cell_footer(mo):
    # Author: 24f2000604@ds.study.iitm.ac.in
    mo.md(
        """
        ---

        ## Notebook Information

        - **Author:** 24f2000604@ds.study.iitm.ac.in
        - **Email:** 24f2000604@ds.study.iitm.ac.in
        - **Framework:** Marimo (Reactive Python Notebooks)

        ### Cell Dependencies in This Notebook:

        ```
        cell_introduction
              │
              ▼
        cell_sliders ──────────────────┐
              │                        │
              ▼                        ▼
        cell_generate_data      cell_visual_indicator
              │
              ▼
        cell_dynamic_output
              │
              ▼
        cell_data_table
              │
              ▼
        cell_show_table
              │
              ▼
        cell_footer
        ```

        *All cells with dependencies update reactively when upstream values change.*

        ---

        **Contact:** 24f2000604@ds.study.iitm.ac.in
        """
    )
    return ()


if __name__ == "__main__":
    app.run()
