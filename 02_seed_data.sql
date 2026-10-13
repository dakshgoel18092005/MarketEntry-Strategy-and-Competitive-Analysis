-- ============================================================================
-- Project: Market Entry Strategy & Competitive Analysis
-- Target Sector: Battery Energy Storage Systems (BESS) - Indian Market
-- Component: 02_seed_data.sql
-- Description: Benchmark Seed Data for 5 Key State Power Hubs
-- ============================================================================

USE bess_market_entry;

INSERT INTO regional_bess_market_data 
    (state_name, grid_region, demand_potential, competitive_intensity, expected_profitability, total_re_capacity_gw, avg_ci_peak_tariff_inr)
VALUES
    -- 1. Gujarat: Strongest overall target. High industrial demand, Grade A+ DISCOMs (GUVNL), favorable energy storage policies.
    ('Gujarat', 'Western', 92.50, 75.00, 88.00, 23.80, 11.20),

    -- 2. Maharashtra: Premier C&I manufacturing belt (Pune, Chakan, Aurangabad), highest peak Time-of-Day (ToD) tariffs in India.
    ('Maharashtra', 'Western', 85.00, 60.00, 82.50, 14.50, 13.40),

    -- 3. Karnataka: High installed solar base, mature Open Access market, but moderate incumbent saturation and wheeling charge uncertainties.
    ('Karnataka', 'Southern', 78.00, 80.00, 70.00, 17.20, 9.80),

    -- 4. Tamil Nadu: Massive wind energy penetration and seasonal grid curtailment, but counterparty risk due to historic DISCOM payment backlogs.
    ('Tamil Nadu', 'Southern', 88.00, 68.00, 65.00, 19.40, 10.50),

    -- 5. Rajasthan: Epicenter of utility-scale solar generation, but hyper-competitive bidding by global conglomerates and evacuation infrastructure bottlenecks.
    ('Rajasthan', 'Northern', 95.00, 85.00, 60.00, 25.10, 8.90);
