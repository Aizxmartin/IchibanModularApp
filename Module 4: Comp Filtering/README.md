
# Module 4: Comparable Filtering

This module filters comparable properties based on a subject property's above-grade square footage (AG SF).

## Inputs
- Cleaned CSV from Module 1
- Subject AG SF from Module 2

## Logic
- Keeps comps where `ag_sf` is between 85% and 110% of subject AG SF
- Sorts output by `net_price`
- Allows downloading filtered comps for Module 5

---

⚠️ Columns Required in CSV:
- `ag_sf`
- `net_price`
