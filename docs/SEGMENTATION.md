# Customer segmentation analysis

I added a reproducible Python analysis to complement the Excel and Power BI files. It creates customer spending quartiles and compares spending, income, recency and campaign response **when those fields are available**.

```bash
pip install pandas openpyxl
python python/customer_segments.py
```

The script reads `data/Customer_Analysis.xlsx` and writes its outputs to `analysis/`.

**Interpretation:** The four spend groups are relative to this dataset, not universal customer tiers. The purchase-frequency proxy (if present) sums channel purchase counts; it is not a verified distinct-order count. `Response` is assumed to be binary and should be checked against the source definitions. A true RFM score needs reliable monetary, frequency and recency fields.

The script is supplied for reproducibility; the generated output files and any new numerical findings should be checked after running it on the workbook.
