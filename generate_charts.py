"""
Project: Market Entry Strategy & Competitive Analysis
Sector: Battery Energy Storage Systems (BESS) - India
File: financial_model/generate_charts.py
Description: Generates executive presentation visual assets using Matplotlib
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def create_visuals():
    os.makedirs("financial_model/charts", exist_ok=True)
    
    # -------------------------------------------------------------------------
    # Chart 1: 3-Year Revenue Trajectory (Base vs Aggressive)
    # -------------------------------------------------------------------------
    years = ['Year 1', 'Year 2', 'Year 3']
    base_rev = [6.00, 18.20, 38.50]
    agg_rev = [7.20, 24.05, 58.80]
    
    x = np.arange(len(years))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
    fig.patch.set_facecolor('#0f172a') # Slate 900
    ax.set_facecolor('#1e293b')        # Slate 800
    
    rects1 = ax.bar(x - width/2, base_rev, width, label='Base Case ($62.7M Cum.)', color='#38bdf8', edgecolor='#0284c7')
    rects2 = ax.bar(x + width/2, agg_rev, width, label='Aggressive GTM ($90.1M Cum.)', color='#10b981', edgecolor='#059669')
    
    ax.set_ylabel('Annual Total Revenue ($ Millions)', color='#f8fafc', fontsize=12, fontweight='bold')
    ax.set_title('BESS India Market Entry: 3-Year Revenue Scaling by Scenario', color='#f8fafc', fontsize=14, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(years, color='#f8fafc', fontsize=11, fontweight='bold')
    ax.tick_params(colors='#94a3b8')
    ax.grid(axis='y', linestyle='--', alpha=0.25, color='#94a3b8')
    ax.legend(facecolor='#0f172a', edgecolor='#475569', labelcolor='#f8fafc', fontsize=10)
    
    # Add values on top of bars
    for rect in rects1:
        h = rect.get_height()
        ax.annotate(f'${h:.1f}M', xy=(rect.get_x() + rect.get_width()/2, h),
                    xytext=(0, 4), textcoords="offset points", ha='center', va='bottom',
                    color='#38bdf8', fontweight='bold', fontsize=10)
    for rect in rects2:
        h = rect.get_height()
        ax.annotate(f'${h:.1f}M', xy=(rect.get_x() + rect.get_width()/2, h),
                    xytext=(0, 4), textcoords="offset points", ha='center', va='bottom',
                    color='#10b981', fontweight='bold', fontsize=10)
                    
    plt.tight_layout()
    chart1_path = "financial_model/charts/revenue_trajectory.png"
    plt.savefig(chart1_path, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"[GENERATED]: {chart1_path}")

    # -------------------------------------------------------------------------
    # Chart 2: Sensitivity Heatmap (CAC vs Retention for Year 3)
    # -------------------------------------------------------------------------
    cacs = ['$30k', '$35k', '$40k', '$45k', '$50k', '$55k', '$60k']
    retentions = ['65%', '70%', '75%', '80%', '85%', '90%', '95%']
    
    # Load sensitivity dataframe
    df = pd.read_csv("financial_model/cac_retention_sensitivity.csv", index_col=0)
    data = df.values
    
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#1e293b')
    
    im = ax.imshow(data, cmap='YlGn', aspect='auto')
    
    ax.set_xticks(np.arange(len(retentions)))
    ax.set_yticks(np.arange(len(cacs)))
    ax.set_xticklabels(retentions, color='#f8fafc', fontsize=10)
    ax.set_yticklabels(cacs, color='#f8fafc', fontsize=10)
    
    ax.set_xlabel('Account Retention / Expansion Rate (%)', color='#f8fafc', fontsize=11, fontweight='bold', labelpad=10)
    ax.set_ylabel('Customer Acquisition Cost (CAC)', color='#f8fafc', fontsize=11, fontweight='bold', labelpad=10)
    ax.set_title('Year 3 Revenue Sensitivity Matrix ($ Millions)\nBudget: $1.5M | AOV: $700k', 
                 color='#f8fafc', fontsize=13, fontweight='bold', pad=15)
                 
    # Annotate numbers in heatmap cells
    for i in range(len(cacs)):
        for j in range(len(retentions)):
            val = data[i, j]
            color = 'black' if val > 44 else '#f8fafc'
            ax.text(j, i, f"${val:.1f}M", ha="center", va="center", color=color, fontsize=9, fontweight='bold')
            
    cbar = fig.colorbar(im, ax=ax, shrink=0.85)
    cbar.set_label('Revenue ($M)', color='#f8fafc', fontsize=10)
    cbar.ax.yaxis.set_tick_params(color='#f8fafc')
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='#f8fafc')
    
    plt.tight_layout()
    chart2_path = "financial_model/charts/sensitivity_heatmap.png"
    plt.savefig(chart2_path, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"[GENERATED]: {chart2_path}")

if __name__ == "__main__":
    create_visuals()
