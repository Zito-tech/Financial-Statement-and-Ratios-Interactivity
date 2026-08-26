import streamlit as st

def show_ratios_dashboard():

    st.subheader("📊 Ratio Analysis Dashboard")

    # Dictionary storing ALL ratios
    ratios = {
        "Turnover Growth Ratio": {
            "formula": "(Current Year Turnover - Previous Year Turnover) / Previous Year Turnover × 100",
            "description": "Determines growth in sales turnover. Rapid growth may lead to cash flow problems."
        },
        "Gross Profit Margin": {
            "formula": "Gross Profit / Sales × 100",
            "description": "Shows percentage of sales available to cover operating expenses."
        },
        "Net Profit Margin": {
            "formula": "Net Profit After Tax / Sales × 100",
            "description": "Indicates percentage of revenue remaining after all expenses."
        },
        "Return on Investment (ROI)": {
            "formula": "Profit Before Interest and Tax / Total Liabilities & Equity × 100",
            "description": "Measures return on total funds invested by lenders and shareholders."
        },
        "Return on Equity (ROE)": {
            "formula": "Net Profit After Tax / Shareholder’s Equity × 100",
            "description": "Shows return earned on shareholder investment."
        },
        "Current Ratio": {
            "formula": "Current Assets / Current Liabilities",
            "description": "Measures ability to meet short-term obligations. Ideal: 2:1."
        },
        "Quick Ratio": {
            "formula": "(Current Assets - Inventory) / Current Liabilities",
            "description": "Measures immediate liquidity. Ideal: 1:1."
        },
        "Stock Turnover Days": {
            "formula": "Closing Inventory / Cost of Sales × 365",
            "description": "Shows how long stock takes to sell."
        },
        "Debtors Days": {
            "formula": "Accounts Receivable / Sales × 365",
            "description": "Shows how quickly customers pay."
        },
        "Creditors Days": {
            "formula": "Accounts Payable / Purchases × 365",
            "description": "Shows how long the business takes to pay suppliers."
        },
        "Gearing Ratio": {
            "formula": "Total Liabilities / Shareholder’s Equity × 100",
            "description": "Measures financial risk. Less than 100% is generally acceptable."
        },
        "Interest Coverage Ratio": {
            "formula": "Profit Before Interest and Tax / Interest Expense",
            "description": "Shows ability to pay interest. More than 3 times is good."
        }
    }

    # Layout
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("📌 Ratios")
        selected_ratio = st.radio(
            "Select a Ratio",
            list(ratios.keys())
        )

    with col2:
        st.subheader("📖 Details")
        st.markdown(f"### {selected_ratio}")
        st.write("**Formula:**")
        st.info(ratios[selected_ratio]["formula"])
        st.write("**What this ratio tells us:**")
        st.success(ratios[selected_ratio]["description"])

if __name__ == "__main__":
    show_ratios_dashboard()
