-- ============================================================================
-- Project: Market Entry Strategy & Competitive Analysis
-- Target Sector: Battery Energy Storage Systems (BESS) - Indian Market
-- Component: 03_weighted_scoring_model.sql
-- Description: Production-ready Weighted Scoring Model using CTEs and Window Functions
-- ============================================================================

USE bess_market_entry;

WITH normalized_metrics AS (
    SELECT 
        region_id,
        state_name,
        grid_region,
        total_re_capacity_gw,
        avg_ci_peak_tariff_inr,
        demand_potential,
        competitive_intensity,
        expected_profitability,
        -- Weighted composite formula:
        -- Weightings: Demand (40%), Profitability (40%), Competition (-20% Penalty)
        -- Math formulation: (Demand * 0.40) + (Profitability * 0.40) + ((100 - Competition) * 0.20)
        -- Bounds ensure resulting composite score is strictly within [0, 100]
        ROUND(
            (demand_potential * 0.40) + 
            (expected_profitability * 0.40) + 
            ((100.0 - competitive_intensity) * 0.20),
            2
        ) AS composite_market_score
    FROM regional_bess_market_data
),
market_rankings AS (
    SELECT 
        region_id,
        state_name,
        grid_region,
        total_re_capacity_gw,
        avg_ci_peak_tariff_inr,
        demand_potential,
        expected_profitability,
        competitive_intensity,
        composite_market_score,
        -- Ordinal priority ranking using Window Functions
        RANK() OVER (ORDER BY composite_market_score DESC) AS entry_rank,
        DENSE_RANK() OVER (ORDER BY composite_market_score DESC) AS dense_entry_rank,
        -- Regional grid peer group ranking
        RANK() OVER (PARTITION BY grid_region ORDER BY composite_market_score DESC) AS regional_peer_rank,
        -- Portfolio Cohort Average Benchmark
        ROUND(AVG(composite_market_score) OVER (), 2) AS national_benchmark_avg,
        -- Relative performance spread vs national average
        ROUND(
            composite_market_score - AVG(composite_market_score) OVER (), 
            2
        ) AS spread_vs_national_avg
    FROM normalized_metrics
)
SELECT 
    entry_rank,
    state_name,
    grid_region,
    total_re_capacity_gw AS re_installed_gw,
    avg_ci_peak_tariff_inr AS peak_tariff_inr_kwh,
    demand_potential AS demand_score,
    expected_profitability AS profitability_score,
    competitive_intensity AS competition_score,
    composite_market_score,
    spread_vs_national_avg,
    regional_peer_rank,
    CASE 
        WHEN entry_rank = 1 THEN 'Wave 1: Anchor Market (Immediate Go-To-Market)'
        WHEN entry_rank <= 3 THEN 'Wave 2: High-Priority Secondary Expansion'
        ELSE 'Wave 3: Opportunistic / Regulatory Monitoring'
    END AS strategic_entry_phase
FROM market_rankings
ORDER BY entry_rank ASC;
