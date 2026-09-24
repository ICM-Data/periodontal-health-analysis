-- 1. Number of patients by periodontal status
SELECT
    periodontal_status,
    COUNT(*) AS patient_count
FROM periodontal_patients
GROUP BY periodontal_status
ORDER BY patient_count DESC;

-- 2. Average clinical measurements by periodontal status
SELECT
    periodontal_status,
    ROUND(AVG(bleeding_on_probing_pct), 2) AS avg_bop_pct,
    ROUND(AVG(probing_depth_mm_mean), 2) AS avg_probing_depth_mm,
    ROUND(AVG(clinical_attachment_loss_mm_mean), 2) AS avg_attachment_loss_mm
FROM periodontal_patients
GROUP BY periodontal_status
ORDER BY avg_probing_depth_mm DESC;

-- 3. High-risk periodontal status by smoking status
SELECT
    smoker,
    COUNT(*) AS patients,
    SUM(CASE WHEN periodontal_status IN ('Moderate', 'Severe') THEN 1 ELSE 0 END) AS high_risk_patients,
    ROUND(
        100.0 * SUM(CASE WHEN periodontal_status IN ('Moderate', 'Severe') THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS high_risk_rate_pct
FROM periodontal_patients
GROUP BY smoker;

-- 4. High-risk periodontal status by diabetes
SELECT
    diabetes,
    COUNT(*) AS patients,
    SUM(CASE WHEN periodontal_status IN ('Moderate', 'Severe') THEN 1 ELSE 0 END) AS high_risk_patients,
    ROUND(
        100.0 * SUM(CASE WHEN periodontal_status IN ('Moderate', 'Severe') THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS high_risk_rate_pct
FROM periodontal_patients
GROUP BY diabetes;
