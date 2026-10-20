# Customer Analytics | Spending & Campaign Response

**Excel · Power BI · Customer segmentation**

I wanted to understand why a marketing team might treat customers differently instead of sending everyone the same campaign. I used a customer-spending dataset and a Power BI dashboard to explore **which groups spend more, which products they buy and what I would check before recommending a targeted campaign**.

## Dashboard

![Customer analysis dashboard](assets/Customer%20analysis.png)

## What I noticed

**Income and spending appear to move together.** Higher-income groups showed stronger spending patterns in the dashboard. That makes income worth investigating, but it doesn't tell me whether income alone predicts a response to marketing.

**Customers don't spend evenly across product categories.** Wine and meat products stood out in the analysis. I'd compare category preference with recency and purchase frequency before building any customer segments.

**Spending is not the same as campaign response.** A customer who buys more isn't automatically the most likely to respond to a promotion. I would check response rates by segment before deciding who should receive a campaign.

These are qualitative observations from the existing dashboard. I haven't added numerical segment comparisons here because the separate Python summaries still need to be run and verified.

## What I'd suggest

If I were working on this for a marketing team, I'd start with a simple comparison of customer groups by **spend, recency and recorded campaign response**. Then I'd test a targeted message against a general one.

I'd judge the result by **response rate and revenue per contacted customer**, and include campaign cost before claiming an improvement in marketing return.

## How I explored the data

The repository includes an [Excel workbook](data/Customer_Analysis.xlsx), the [Power BI report](powerbi/Customer_Analysis.pbix) and the dashboard screenshot above.

I've also included a [Python segmentation script](python/customer_segments.py) to group customers into spending quartiles and compare available income, recency and response fields.

```bash
pip install pandas openpyxl
python python/customer_segments.py
```

The script writes summaries to `analysis/` when run. See [segmentation notes](docs/SEGMENTATION.md) for definitions and limitations. Its outputs haven't been independently verified in this README.

## What I learned

The useful part of segmentation isn't giving customers labels. It's checking whether those groups behave differently enough to support a better decision. I'd want to test the campaign before saying the segmentation worked.

*Independent portfolio analysis, not a live marketing campaign or evidence of achieved revenue growth.*
