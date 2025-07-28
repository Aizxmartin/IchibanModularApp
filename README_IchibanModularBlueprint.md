
# 📘 Ichiban Modular Valuation App — Blueprint

This document outlines the architecture and operational flow of the modular real estate valuation app, including each module’s purpose, inputs, outputs, and outstanding TODOs.

---

## ✅ Module 1: CSV Cleaner

**Purpose:** Load and sanitize comp data from uploaded CSV.

**Inputs:** CSV file with fields like: `Above Grade Finished Area`, `Net Close Price`, `Concessions Amount`, `Bedrooms Total`, `Bathrooms Total Integer`, and address parts.

**Core Tasks:**
- Clean data, convert to correct types
- Drop invalid rows
- Assemble address from parts
- Sort by Net Close Price

**Output:** Cleaned and sorted DataFrame saved as a CSV

**TODOs:** None

---

## ✅ Module 2: Subject Property Extractor

**Purpose:** Extract address, AVM, AG SF, beds, baths from a subject property PDF (or allow manual entry).

**Inputs:** PDF or manual

**Core Tasks:**
- Extract AVM using regex (or user input)
- Parse subject address from filename
- Display editable summary

**Output:** JSON/dict with subject property details

**TODOs:**
- Improve PDF parsing accuracy (deferred)
- Future: auto-recognition of beds/baths

---

## ✅ Module 3: Online Estimate Averaging

**Purpose:** Average the Zillow, Redfin, and Real AVM values.

**Inputs:** 2–3 values manually entered

**Core Tasks:**
- Accept inputs (Zillow, Redfin, Real AVM)
- Calculate average of non-zero values

**Output:** Single averaged float value

**TODOs:** None

---

## 🔄 Module 4: Comp Filtering by Above Grade SF

**Purpose:** Filter cleaned comps within 85–110% of subject AG SF

**Inputs:**
- Cleaned comp CSV (from Module 1)
- Subject AG SF (from Module 2)

**Core Tasks:**
- Apply AG SF range filter
- Display result

**Output:** Filtered DataFrame of comps

**TODOs:**
- ✅ Allow user input for subject AG SF
- 🔲 Show success message on screen (filtered count)
- 🔲 Show filtered table below input
- 🔲 Handle “no comps match” gracefully

---

## ⏳ Module 5: Adjustment Engine

**Planned Purpose:** Use JSON schema to apply $/sf and feature adjustments

**TODOs:**
- Load schema from file
- Apply line-by-line comp adjustments
- Add adjusted price field

---

## ⏳ Module 6: Summary Report

**Planned Purpose:** Generate final valuation summary and table

**TODOs:**
- Calculate PPSF, average
- Show adjusted comp table with pricing range
- Export to Word or PDF

---

© Ichiban ModularApp · Last updated automatically
