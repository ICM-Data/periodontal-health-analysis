# Data Dictionary

This project uses a synthetic periodontal-health dataset for portfolio demonstration.

| Column | Type | Description | Example |
|---|---|---|---|
| `patient_id` | string | Synthetic unique patient identifier | `P001` |
| `age` | integer | Patient age in years | `45` |
| `sex` | string | Sex recorded in the synthetic dataset | `F` |
| `smoker` | integer | Smoking indicator: 0 = no, 1 = yes | `1` |
| `diabetes` | integer | Diabetes indicator: 0 = no, 1 = yes | `0` |
| `bleeding_on_probing_pct` | float | Percentage of sites with bleeding on probing | `46.0` |
| `probing_depth_mm_mean` | float | Mean periodontal probing depth in millimeters | `4.0` |
| `clinical_attachment_loss_mm_mean` | float | Mean clinical attachment loss in millimeters | `2.3` |
| `periodontal_status` | string | Simplified analytical category derived by the project | `Moderate` |

## Validation rules
- `patient_id` must be present and unique after cleaning.
- `age` must be between 18 and 100.
- `bleeding_on_probing_pct` must be between 0 and 100.
- probing depth must be between 0 and 15 mm.
- clinical attachment loss must be between 0 and 15 mm.
- smoking and diabetes fields are normalized as binary integers.

## Clinical disclaimer
The derived periodontal-status field is intentionally simplified for analytics and software demonstration. It is not a clinical diagnostic classification and must not be used for patient care.
