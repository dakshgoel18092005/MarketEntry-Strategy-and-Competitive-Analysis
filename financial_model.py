"""
Project: Market Entry Strategy & Competitive Analysis
Sector: Battery Energy Storage Systems (BESS) - India
File: financial_model/financial_model.py
Description: 3-Year Financial Projection & Sensitivity Analysis Model
"""

import pandas as pd
import numpy as np

def calculate_projections():
    years = ['Year 1', 'Year 2', 'Year 3']
    
    # Core Budget & AOV Assumptions
    mktg_budget = [600_000, 1_000_000, 1_500_000]
    aov = [600_000, 650_000, 700_000] # In USD (translates to ~₹5.0 Cr to ₹5.8 Cr B2B industrial systems)
    
    # 1. Base Case Assumptions
    base_cac = [60_000, 50_000, 45_000]
    base_retention = [0.70, 0.75, 0.80]
    
    # 2. Aggressive Case Assumptions
    agg_cac = [50_000, 38_000, 30_000]
    agg_retention = [0.85, 0.90, 0.92]
    
    def simulate_scenario(cac_list, retention_list, scenario_name):
        new_cust = []
        retained_cust = []
        active_cust = []
        revenue = []
        
        prev_active = 0
        for i in range(3):
            # New accounts acquired from budget
            new = round(mktg_budget[i] / cac_list[i])
            new_cust.append(new)
            
            # Retained accounts from previous year
            if i == 0:
                retained = 0
            else:
                retained = round(prev_active * retention_list[i])
            retained_cust.append(retained)
            
            total_active = new + retained
            active_cust.append(total_active)
            prev_active = total_active
            
            rev = total_active * aov[i]
            revenue.append(rev)
            
        df = pd.DataFrame({
            'Scenario': scenario_name,
            'Year': years,
            'Budget ($)': mktg_budget,
            'CAC ($)': cac_list,
            'Retention Rate (%)': [f"{int(r*100)}%" for r in retention_list],
            'AOV ($)': aov,
            'New Customers': new_cust,
            'Retained Customers': retained_cust,
            'Total Active Customers': active_cust,
            'Total Revenue ($M)': [r / 1_000_000 for r in revenue]
        })
        return df, revenue

    base_df, base_rev = simulate_scenario(base_cac, base_retention, 'Base Case')
    agg_df, agg_rev = simulate_scenario(agg_cac, agg_retention, 'Aggressive')
    
    combined_df = pd.concat([base_df, agg_df], ignore_index=True)
    
    # Print formatted table
    print("=" * 95)
    print("   BESS INDIA MARKET ENTRY: 3-YEAR REVENUE PROJECTIONS")
    print("=" * 95)
    print(combined_df.to_string(index=False))
    print("=" * 95)
    print(f"Base Case 3-Year Cumulative Revenue:        ${sum(base_rev)/1_000_000:,.2f} M")
    print(f"Aggressive Scenario 3-Year Cumulative Rev:  ${sum(agg_rev)/1_000_000:,.2f} M")
    print(f"Incremental Revenue Delta (Optimized GTM): +${(sum(agg_rev) - sum(base_rev))/1_000_000:,.2f} M (+{(sum(agg_rev)-sum(base_rev))/sum(base_rev)*100:.1f}%)")
    print("=" * 95)
    
    # Save to CSV
    combined_df.to_csv("financial_model/3_year_financial_projections.csv", index=False)
    
    # Sensitivity Analysis: Year 3 Revenue varying CAC vs Retention Rate
    # Year 3 Budget = $1.5M, Year 3 AOV = $700k
    # Assume base active accounts entering Y3 = 28 (from Base Case Y2)
    y3_budget = 1_500_000
    y3_aov = 700_000
    base_y2_accounts = 28
    
    cacs = [30_000, 35_000, 40_000, 45_000, 50_000, 55_000, 60_000]
    retentions = [0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]
    
    sensitivity_matrix = np.zeros((len(cacs), len(retentions)))
    
    for r_idx, cac in enumerate(cacs):
        for c_idx, ret in enumerate(retentions):
            new_acc = y3_budget / cac
            ret_acc = base_y2_accounts * ret
            total_acc = new_acc + ret_acc
            rev = (total_acc * y3_aov) / 1_000_000 # in $M
            sensitivity_matrix[r_idx, c_idx] = round(rev, 2)
            
    sensitivity_df = pd.DataFrame(
        sensitivity_matrix,
        index=[f"CAC ${c//1000}k" for c in cacs],
        columns=[f"Ret {int(r*100)}%" for r in retentions]
    )
    
    print("\n" + "=" * 80)
    print("   YEAR 3 REVENUE SENSITIVITY MATRIX ($ Millions)")
    print("   (Testing CAC vs Customer Retention on $1.5M spend & $700k AOV)")
    print("=" * 80)
    print(sensitivity_df)
    print("=" * 80)
    
    sensitivity_df.to_csv("financial_model/cac_retention_sensitivity.csv")
    print("\n[SAVED]: 3_year_financial_projections.csv & cac_retention_sensitivity.csv generated successfully.")

if __name__ == "__main__":
    calculate_projections()
