import pandas as pd
import numpy as np
from datetime import datetime

# File paths
KODO_PAY_FILE = "kodo-pay-reimbursement.csv"
TRANSACTIONS_FILE = "transactions-csv.csv"

# CAPEX categories - long-term investments and assets
CAPEX_CATEGORIES = {
    'Electronics', 'Mechanical hardware', 'IT', 'Housekeeping', 
    'Lab Work', 'Clinical Supplies'
}

# CAPEX keywords in comments/narration
CAPEX_KEYWORDS = [
    'manufacturing', 'equipment', 'cctv', 'voltage stabilizer',
    'extension room door', 'carpenter', 'wood', 'hardware',
    'laser', 'voltage', 'stabiliser', 'wifi setup'
]

# OPEX categories - day-to-day operational costs
OPEX_CATEGORIES = {
    'Food', 'Utilities', 'Office Supplies', 'Commute', 'Travel',
    'Rent', 'Logistics', 'Fuel', 'Hotel', 'Flight Booking',
    'Grocery', 'Stationery', 'Dog Food', 'Labour', 'Grass work',
    'Clinical Referee', 'Others'
}

def categorize_expense(category, comments, narration):
    """
    Categorize an expense as CAPEX or OPEX based on category and context.
    
    Args:
        category: Expense category
        comments: Maker comments or notes
        narration: Merchant/narration
    
    Returns:
        'CAPEX' or 'OPEX'
    """
    # Convert to string and lowercase for comparison
    category_str = str(category).strip() if pd.notna(category) else ''
    comments_str = str(comments).lower() if pd.notna(comments) else ''
    narration_str = str(narration).lower() if pd.notna(narration) else ''
    
    # Check if category is explicitly CAPEX
    if category_str in CAPEX_CATEGORIES:
        return 'CAPEX'
    
    # Check for CAPEX keywords in comments or narration
    combined_text = f"{comments_str} {narration_str}"
    for keyword in CAPEX_KEYWORDS:
        if keyword in combined_text:
            return 'CAPEX'
    
    # Check if category is explicitly OPEX
    if category_str in OPEX_CATEGORIES:
        return 'OPEX'
    
    # Default to OPEX for unclear cases (can be reviewed)
    return 'OPEX (Review)'

def analyze_kodo_pay(file_path):
    """Analyze kodo-pay sheet and categorize expenses."""
    print(f"\n{'='*80}")
    print("ANALYZING KODO-PAY SHEET")
    print(f"{'='*80}\n")
    
    # Read CSV
    df = pd.read_csv(file_path)
    print(f"Total transactions loaded: {len(df)}")
    
    # Filter out credit transactions (Cr)
    df_debit = df[df['Dr/Cr'] == 'Dr'].copy()
    print(f"Debit transactions (after filtering credits): {len(df_debit)}")
    
    # Categorize each transaction
    df_debit['Expense_Type'] = df_debit.apply(
        lambda row: categorize_expense(
            row['Category'], 
            row['Maker Comments'], 
            row['Narration on Kodo Pay']
        ), 
        axis=1
    )
    
    # Add source column
    df_debit['Source'] = 'Kodo-Pay'
    
    return df_debit

def analyze_transactions(file_path):
    """Analyze transactions sheet and categorize expenses."""
    print(f"\n{'='*80}")
    print("ANALYZING TRANSACTIONS SHEET")
    print(f"{'='*80}\n")
    
    # Read CSV
    df = pd.read_csv(file_path)
    print(f"Total transactions loaded: {len(df)}")
    
    # Filter out FUNDING and CARD_CREDIT transactions (these are credits)
    df_debit = df[~df['Txn Category'].isin(['FUNDING', 'CARD_CREDIT'])].copy()
    print(f"Debit transactions (after filtering credits): {len(df_debit)}")
    
    # Categorize each transaction
    df_debit['Expense_Type'] = df_debit.apply(
        lambda row: categorize_expense(
            row['Expense Category'], 
            row['Notes'], 
            row['Merchant/Narration']
        ), 
        axis=1
    )
    
    # Add source column
    df_debit['Source'] = 'Transactions'
    
    return df_debit

def generate_summary(kodo_df, trans_df):
    """Generate summary statistics and reports."""
    print(f"\n{'='*80}")
    print("FINANCIAL ANALYSIS SUMMARY")
    print(f"{'='*80}\n")
    
    # Combine both datasets for summary
    all_expenses = []
    
    # Process Kodo-Pay data
    for _, row in kodo_df.iterrows():
        all_expenses.append({
            'Source': 'Kodo-Pay',
            'Date': row['Date (IST)'],
            'Amount': row['Net Txn Amount Debit (INR)'],
            'Category': row['Category'],
            'Expense_Type': row['Expense_Type'],
            'Description': f"{row['Outward Payment Beneficiary Name']} - {row['Maker Comments']}"
        })
    
    # Process Transactions data
    for _, row in trans_df.iterrows():
        all_expenses.append({
            'Source': 'Transactions',
            'Date': row['Txn Date'],
            'Amount': row['Net Txn Amount Debit (Rs.)'],
            'Category': row['Expense Category'],
            'Expense_Type': row['Expense_Type'],
            'Description': f"{row['Merchant/Narration']} - {row['Notes']}"
        })
    
    # Create summary DataFrame
    summary_df = pd.DataFrame(all_expenses)
    
    # Calculate totals
    total_capex = summary_df[summary_df['Expense_Type'] == 'CAPEX']['Amount'].sum()
    total_opex = summary_df[summary_df['Expense_Type'] == 'OPEX']['Amount'].sum()
    total_review = summary_df[summary_df['Expense_Type'] == 'OPEX (Review)']['Amount'].sum()
    total_all = summary_df['Amount'].sum()
    
    # Print summary
    print(f"Total Transactions Analyzed: {len(summary_df)}")
    print(f"\n{'─'*80}")
    print(f"{'EXPENSE TYPE':<30} {'COUNT':<15} {'AMOUNT (INR)':<20}")
    print(f"{'─'*80}")
    print(f"{'CAPEX (Capital Expenditure)':<30} {len(summary_df[summary_df['Expense_Type'] == 'CAPEX']):<15} ₹{total_capex:,.2f}")
    print(f"{'OPEX (Operating Expenditure)':<30} {len(summary_df[summary_df['Expense_Type'] == 'OPEX']):<15} ₹{total_opex:,.2f}")
    print(f"{'OPEX (Needs Review)':<30} {len(summary_df[summary_df['Expense_Type'] == 'OPEX (Review)']):<15} ₹{total_review:,.2f}")
    print(f"{'─'*80}")
    print(f"{'TOTAL':<30} {len(summary_df):<15} ₹{total_all:,.2f}")
    print(f"{'─'*80}\n")
    
    # Category breakdown
    print(f"\n{'='*80}")
    print("CAPEX BREAKDOWN BY CATEGORY")
    print(f"{'='*80}\n")
    capex_breakdown = summary_df[summary_df['Expense_Type'] == 'CAPEX'].groupby('Category')['Amount'].agg(['count', 'sum'])
    capex_breakdown = capex_breakdown.sort_values('sum', ascending=False)
    for category, row in capex_breakdown.iterrows():
        print(f"{category:<40} {int(row['count']):<10} ₹{row['sum']:,.2f}")
    
    print(f"\n{'='*80}")
    print("OPEX BREAKDOWN BY CATEGORY")
    print(f"{'='*80}\n")
    opex_breakdown = summary_df[summary_df['Expense_Type'].isin(['OPEX', 'OPEX (Review)'])].groupby('Category')['Amount'].agg(['count', 'sum'])
    opex_breakdown = opex_breakdown.sort_values('sum', ascending=False)
    for category, row in opex_breakdown.iterrows():
        print(f"{category:<40} {int(row['count']):<10} ₹{row['sum']:,.2f}")
    
    # Save detailed report
    output_file = f"financial_analysis_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    summary_df.to_csv(output_file, index=False)
    print(f"\n{'='*80}")
    print(f"Detailed report saved to: {output_file}")
    print(f"{'='*80}\n")
    
    return summary_df

def main():
    """Main execution function."""
    print("\n" + "="*80)
    print("FINANCIAL ANALYSIS: CAPEX vs OPEX CATEGORIZATION")
    print("="*80)
    
    # Analyze both sheets
    kodo_df = analyze_kodo_pay(KODO_PAY_FILE)
    trans_df = analyze_transactions(TRANSACTIONS_FILE)
    
    # Generate summary
    summary_df = generate_summary(kodo_df, trans_df)
    
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()
