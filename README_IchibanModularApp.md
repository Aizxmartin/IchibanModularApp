
# IchibanModularApp

A modular real estate market valuation tool built using Streamlit. This project separates each major function of the valuation process into independent modules for better structure, reusability, and debugging.

---

## 🔧 Modules Overview

### 🧼 Module 1: CSV Cleaner
Cleans raw MLS export data. It:
- Renames and sanitizes necessary fields
- Filters out incomplete or corrupt records
- Sorts comps by `Net Close Price`
- Displays clean comps for review

📁 Folder: `module1_csv_cleaner`

---

### 📄 Module 2: Subject Property Extractor
Uploads a PDF of the subject property and extracts:
- Address
- Real AVM value
- Above Grade Finished SF
- Bedrooms and Bathrooms

Allows manual override if any field is missing from the PDF.

📁 Folder: `module2_subject_extractor`

---

## ▶️ How to Run Locally

Each module is self-contained.

1. Navigate to a module directory:
```bash
cd module1_csv_cleaner
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Launch the module:
```bash
streamlit run main.py
```

Repeat for any other module.

---

## 🔜 Upcoming Modules

- Module 3: Online Estimate Averaging & Comp Filtering
- Module 4: Adjusted Value Calculation
- Module 5: Market Summary & Report Generation

---

## 🧠 Why Modular?

This structure makes it easier to:
- Debug isolated pieces
- Evolve components independently
- Replace or upgrade logic in any module without breaking the rest

---
