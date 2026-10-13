-- ============================================================================
-- Project: Market Entry Strategy & Competitive Analysis
-- Target Sector: Battery Energy Storage Systems (BESS) - Indian Market
-- Component: 01_schema.sql
-- Description: MySQL Database Schema for Regional Market Attractiveness
-- ============================================================================

CREATE DATABASE IF NOT EXISTS bess_market_entry;
USE bess_market_entry;

DROP TABLE IF EXISTS regional_bess_market_data;

CREATE TABLE regional_bess_market_data (
    region_id INT AUTO_INCREMENT PRIMARY KEY,
    state_name VARCHAR(50) NOT NULL UNIQUE,
    grid_region ENUM('Northern', 'Western', 'Southern', 'Eastern', 'North-Eastern') NOT NULL,
    demand_potential DECIMAL(5, 2) NOT NULL 
        COMMENT 'Raw score (1-100): RE installed capacity, peak deficit, C&I power tariffs',
    competitive_intensity DECIMAL(5, 2) NOT NULL 
        COMMENT 'Raw score (1-100): Presence of incumbent EPCs, OEM aggregators, and tariff bidding wars',
    expected_profitability DECIMAL(5, 2) NOT NULL 
        COMMENT 'Raw score (1-100): DISCOM payment track record, banking charges, Open Access viability',
    total_re_capacity_gw DECIMAL(6, 2) DEFAULT 0.00 
        COMMENT 'Installed Solar + Wind Capacity in Gigawatts',
    avg_ci_peak_tariff_inr DECIMAL(5, 2) DEFAULT 0.00 
        COMMENT 'Average C&I Peak Tariff in INR/kWh',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_region (grid_region),
    INDEX idx_scores (demand_potential, expected_profitability, competitive_intensity)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
