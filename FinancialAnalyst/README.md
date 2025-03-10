# Financial Analysis of a Company Stock
#### Using LlamaIndex 🦙 and Google Gemini ♊
This example shows you how you can use a LLM to analyze financial performance metrics of any company and give you an overall recommendation on the long term investment potential of the company. Such type of use-cases could be helpful to financial advisors making stock investment recommendations to pensioners or HNIs.

<table style="background-color:#ffe4e1; width:100%;">
  <tr>
    <td style="color:black; text-align:center;">
      <b>Warning:</b> This code is for illustration purposes only. It is not meant to
      replace or replicate the advise of a skilled Financial Advisor. <b>Do not make
      any financial investments decisions based on the recommendations you see here</b>.
      Always do your own independent research and seek professional advise before investing
      your hard-earned money.
    </td>
  </tr>
</table>

Analyzing a company as potential long term investment is a very tedious process. You have to pour through financial reports, read latest news and recommendatios, do your independent research before deciding on how to proceed. 

This example calculates various financial ratios, as detailed below, from data downloaded from Yahoo! Finance. It leverages Google Gemini LLM (we use `gemini-1.5-flash`) to analyze all the ratios we calculate and make an overall recommendation on the investment potential. All you do is provide the stock symbol used by Yahoo! Finance (such as AAPL for Apple, AMZN for Amazon, RELIANCE.NS for Reliance Industries and so on). <b>For now, analysis is limited to publicly traded companies</b>

### Financial Ratios Analyzed
1. **Liquidity Ratios**: such as Current Ratio, Quick Ratio and Cash Ratio, which help assess the short-term stability of a company.
2. **Profitability Ratios**": such as Return on Equity (RoE), Return on Assets (RoA), Return on Capital Employed (RoCE), Net Profit Margin, and Operating Margin, which help assess potential earnings and returns from the company.
3. **Efficiency Ratios**: such as Asset Turnover Ratio and Inventory Turnover, which measure operational efficiency of a company. **NOTE:** not all companies provide inventory information.
4. **Valuation Ratios**: such as Price-to-Earnings ratio (P/E), Price-to-Sales ratio (P/S), Price-to-Book ratio (P/B), EV/EBIDTA ratio, which is intended to measure stock price "fairness".
5. **Leverage Ratios**: 