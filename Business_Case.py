import streamlit as st
from Easy_Ratios import show_ratios_dashboard

# --------------------------------
# Base Financial Data - ONE YEAR
# --------------------------------
BASE_DATA = {
    "sales": 50_000_000,
    "cost_of_sales": 20_000_000,
    "salaries": 15_000_000,
    "rent": 1_200_000,
    "marketing": 45_000,
    "admin_costs": 3_480_000,
    "tax_rate": 0.27,
    "fixed_assets": 10_411_000,
    "inventory": 450_000,
    "debtors": 435_000,
    "bank": 0,
    "long_term_liabilities": 1_500_000,
    "creditors": 46_000,
    "bank_overdraft": 0,
    "share_capital": 2_249_250,
}


# --------------------------------
# ONE-YEAR FUNCTION
# --------------------------------
def run_year(opening_balance, data):

    st.title("📊 Business Scenario Simulator - One Year")

    cash_from_operations = 0
    cash_from_investments = 0
    cash_from_financing = 0

    # --------------------------------
    # Sidebar - Annual Decisions
    # --------------------------------
    st.sidebar.header("Annual Business Decisions")

    s1 = st.sidebar.checkbox(
        "1. Move to cheaper rent",
        key="year_s1"
    )

    s2 = st.sidebar.checkbox(
        "2. Increase marketing",
        key="year_s2"
    )

    s3 = st.sidebar.checkbox(
        "3. Hire 2 employees",
        key="year_s3"
    )

    s4 = st.sidebar.checkbox(
        "4. New supplier",
        key="year_s4"
    )

    s5 = st.sidebar.checkbox(
        "5. Buy new computer",
        key="year_s5"
    )

    s6 = st.sidebar.checkbox(
        "6. L&D investment",
        key="year_s6"
    )

    s7 = st.sidebar.checkbox(
        "7. Consultant costs",
        key="year_s7"
    )

    # --------------------------------
    # Apply Annual Decisions
    # --------------------------------

    # 1. Move to cheaper rent
    if s1:
        data["rent"] -= 80_000
        data["bank"] += 80_000
        cash_from_operations += 80_000

    # 2. Increase marketing
    if s2:
        data["marketing"] += 50_000
        data["sales"] += 500_000
        data["bank"] += 450_000
        cash_from_operations += 450_000

    # 3. Hire 2 employees
    if s3:
        data["salaries"] += 500_000
        data["sales"] += 2_000_000
        data["bank"] += 1_500_000
        cash_from_operations += 1_500_000

    # 4. New supplier
    if s4:
        data["cost_of_sales"] -= 500_000
        data["bank"] += 500_000
        cash_from_operations += 500_000

    # 5. Buy new computer
    if s5:
        data["fixed_assets"] += 500_000
        data["bank_overdraft"] += 500_000
        cash_from_investments -= 500_000

    # 6. L&D investment
    if s6:
        data["admin_costs"] += 500_000
        data["sales"] += 1_000_000
        data["bank"] += 500_000
        cash_from_operations += 500_000

    # 7. Consultant costs
    if s7:
        data["admin_costs"] += 750_000
        data["cost_of_sales"] -= 1_000_000
        data["bank"] += 250_000
        cash_from_operations += 250_000

    # --------------------------------
    # Income Statement Calculations
    # --------------------------------

    gross_profit = (
        data["sales"] - data["cost_of_sales"]
    )

    expenses = (
        data["salaries"]
        + data["rent"]
        + data["marketing"]
        + data["admin_costs"]
    )

    ebt = gross_profit - expenses

    tax = ebt * data["tax_rate"]

    net_profit = ebt - tax

    # --------------------------------
    # Balance Sheet Calculations
    # --------------------------------

    current_assets = (
        data["inventory"]
        + data["debtors"]
        + data["bank"]
    )

    total_assets = (
        data["fixed_assets"]
        + current_assets
    )

    total_liabilities = (
        data["long_term_liabilities"]
        + data["creditors"]
        + data["bank_overdraft"]
    )

    equity = (
        data["share_capital"]
        + net_profit
    )

    total_equity_liabilities = (
        total_liabilities
        + equity
    )

    # --------------------------------
    # Cash Flow
    # --------------------------------

    closing_balance = (
        opening_balance
        + cash_from_operations
        + cash_from_investments
        + cash_from_financing
    )

    # --------------------------------
    # Ratios
    # --------------------------------

    gross_profit_ratio = (
        gross_profit / data["sales"]
        if data["sales"]
        else 0
    )

    net_profit_ratio = (
        net_profit / data["sales"]
        if data["sales"]
        else 0
    )

    roi = (
        net_profit / total_equity_liabilities
        if total_equity_liabilities
        else 0
    )

    current_ratio = (
        current_assets / data["creditors"]
        if data["creditors"]
        else 0
    )

    debtors_days = (
        data["debtors"] / data["sales"]
    ) * 365 if data["sales"] else 0

    debt_to_equity = (
        total_liabilities / equity
        if equity
        else 0
    )

    # --------------------------------
    # Display Results
    # --------------------------------

    st.header("📄 Income Statement")

    st.write(
        f"Sales: {data['sales']:,.0f}"
    )

    st.write(
        f"Cost of Sales: {data['cost_of_sales']:,.0f}"
    )

    st.write(
        f"Gross Profit: {gross_profit:,.0f}"
    )

    st.write(
        f"Total Expenses: {expenses:,.0f}"
    )

    st.write(
        f"Profit Before Tax: {ebt:,.0f}"
    )

    st.write(
        f"Tax: {tax:,.0f}"
    )

    st.write(
        f"Net Profit: {net_profit:,.0f}"
    )

    # --------------------------------
    # Balance Sheet
    # --------------------------------

    st.header("🏦 Balance Sheet")

    st.write(
        f"Fixed Assets: {data['fixed_assets']:,.0f}"
    )

    st.write(
        f"Inventory: {data['inventory']:,.0f}"
    )

    st.write(
        f"Debtors: {data['debtors']:,.0f}"
    )

    st.write(
        f"Bank: {data['bank']:,.0f}"
    )

    st.write(
        f"Total Assets: {total_assets:,.0f}"
    )

    st.write(
        f"Total Liabilities: {total_liabilities:,.0f}"
    )

    st.write(
        f"Equity: {equity:,.0f}"
    )

    st.write(
        f"Total Equity & Liabilities: "
        f"{total_equity_liabilities:,.0f}"
    )

    # --------------------------------
    # Cash Flow
    # --------------------------------

    st.header("💰 Cash Flow")

    st.write(
        f"Cash from Operations: "
        f"{cash_from_operations:,.0f}"
    )

    st.write(
        f"Cash from Investments: "
        f"{cash_from_investments:,.0f}"
    )

    st.write(
        f"Cash from Financing: "
        f"{cash_from_financing:,.0f}"
    )

    st.write(
        f"Opening Balance: "
        f"{opening_balance:,.0f}"
    )

    st.write(
        f"Closing Balance: "
        f"{closing_balance:,.0f}"
    )

    # --------------------------------
    # Ratios
    # --------------------------------

    st.header("📊 Financial Ratios")

    st.write(
        f"Gross Profit Ratio: "
        f"{gross_profit_ratio:.2%}"
    )

    st.write(
        f"Net Profit Ratio: "
        f"{net_profit_ratio:.2%}"
    )

    st.write(
        f"ROI: "
        f"{roi:.2%}"
    )

    st.write(
        f"Current Ratio: "
        f"{current_ratio:.2f}"
    )

    st.write(
        f"Debtors Days: "
        f"{debtors_days:.2f}"
    )

    st.write(
        f"Debt to Equity: "
        f"{debt_to_equity:.2f}"
    )

    # --------------------------------
    # Ratios Dashboard
    # --------------------------------

    st.markdown("---")

    try:
        show_ratios_dashboard(
            gross_profit_ratio,
            net_profit_ratio,
            roi,
            current_ratio,
            debtors_days,
            debt_to_equity
        )
    except TypeError:
        # If Easy_Ratios has a different function signature,
        # the main financial results above will still display.
        pass

    return closing_balance, data


# --------------------------------
# MAIN APP - ONE YEAR ONLY
# --------------------------------

data = BASE_DATA.copy()

opening_balance = data["bank"]

opening_balance, data = run_year(
    opening_balance,
    data
)
