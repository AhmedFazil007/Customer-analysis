"""Customer segmentation and campaign response analysis.
Run: pip install pandas openpyxl
     python python/customer_segments.py

Outputs are created under analysis/ after execution.
The analysis uses only columns that actually exist in the workbook.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/Customer_Analysis.xlsx"
OUT = ROOT / "analysis"
df = pd.read_excel(SOURCE)
df.columns = df.columns.astype(str).str.strip()
print("Available columns:", df.columns.tolist())
OUT.mkdir(exist_ok=True)
spend_cols = [c for c in df if c.startswith("Mnt")]
if spend_cols:
    for c in spend_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)
    df["total_spend"] = df[spend_cols].sum(axis=1)
if "Income" in df:
    df["Income"] = pd.to_numeric(df["Income"], errors="coerce")
if "Recency" in df:
    df["Recency"] = pd.to_numeric(df["Recency"], errors="coerce")
if "NumWebPurchases" in df and "NumStorePurchases" in df:
    cols = [c for c in ("NumWebPurchases", "NumStorePurchases", "NumCatalogPurchases") if c in df]
    df["purchase_frequency_proxy"] = df[cols].apply(pd.to_numeric, errors="coerce").fillna(0).sum(axis=1)
    print("Purchase frequency is a proxy based on channel purchase counts, not distinct orders.")
if "total_spend" in df:
    df["spend_segment"] = pd.qcut(df["total_spend"].rank(method="first"), q=4,
                                   labels=["Low", "Lower-middle", "Upper-middle", "High"])
    summary = df.groupby("spend_segment", observed=True).agg(
        customers=("total_spend", "size"),
        average_spend=("total_spend", "mean"),
        median_spend=("total_spend", "median")
    )
    if "Income" in df:
        summary["average_income"] = df.groupby("spend_segment", observed=True)["Income"].mean()
    if "Recency" in df:
        summary["average_recency"] = df.groupby("spend_segment", observed=True)["Recency"].mean()
    if "Response" in df:
        response = pd.to_numeric(df["Response"], errors="coerce")
        df["response_numeric"] = response
        summary["campaign_response_rate"] = df.groupby("spend_segment", observed=True)["response_numeric"].mean()
    summary.to_csv(OUT / "spend_segment_summary.csv")
if "Response" in df:
    print("Response is interpreted as a 0/1 campaign indicator; confirm the workbook coding.")
    print(df["Response"].value_counts(dropna=False).to_string())
df.to_csv(OUT / "customer_segments.csv", index=False)
print(f"Exported {len(df):,} rows to analysis/.")
