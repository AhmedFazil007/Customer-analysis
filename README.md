# Customer Analytics | Spending & Campaign Response

**Excel · Power BI · Customer segmentation**

I explored customer spending and campaign response to understand a practical marketing question: **Which customer groups and product categories deserve a closer look when planning campaigns?**

The project combines an Excel dataset with a Power BI dashboard. I focused on making spending patterns easier to compare, rather than treating every customer as part of the same audience.

## Dashboard preview

![Customer analytics dashboard](assets/Customer%20analysis.png)

## What stood out

- **Income and spending:** Higher-income customer groups showed stronger spending patterns in the analysis.
- **Product preferences:** Wine and meat products stood out among the higher-spending categories.
- **Campaign planning:** Looking at spending alongside customer characteristics can help form better targeting hypotheses.

These are descriptive findings. The dataset doesn't demonstrate that a campaign change improved revenue or marketing ROI.

## How I'd use these findings

If this were part of a marketing team's workflow, I'd start by comparing segments on **spend, recency and campaign response**. Then I'd test whether a more tailored message performs better than a general campaign.

I'd measure **response rate, conversion rate, revenue per contacted customer and acquisition cost** before claiming that a targeting strategy worked.

## Reproduce customer segmentation

I've included a [Python segmentation script](python/customer_segments.py) and [method notes](docs/SEGMENTATION.md) to compare spending quartiles, income, recency and campaign response when those columns are present. The script is ready to run against the Excel workbook; outputs and any resulting figures still need validation.

## Files

| File | Description |
|---|---|
| [Customer Analysis dashboard](powerbi/Customer_Analysis.pbix) | Power BI report |
| [Customer dataset](data/Customer_Analysis.xlsx) | Excel data and analysis |
| [Dashboard screenshot](assets/Customer%20analysis.png) | Quick preview |

## A note on interpretation

This is a portfolio analysis of customer behavior, not evidence of a live marketing campaign or an implemented business improvement. The recommendations are ideas to test, not measured outcomes.

---

[Ahmed Fazil](https://github.com/AhmedFazil007)
