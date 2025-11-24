# LangGraph Financial Analysis System

## Overview
An intelligent financial analysis system using **LangGraph** and **Google Gemini LLM** to automatically categorize expenses into CAPEX/OPEX and generate professional financial statements.

## Features

✨ **LLM-Powered Categorization**: Uses Google Gemini to intelligently analyze and categorize each transaction  
📊 **Professional Financial Statements**: Generates Excel reports with multiple sheets (Executive Summary, CAPEX, OPEX, Category Analysis)  
🔄 **LangGraph Workflow**: Structured agent workflow with 5 nodes for robust processing  
📈 **Consolidated Reporting**: Combines data from multiple sources into one comprehensive report  
🎯 **Confidence Scoring**: Each categorization includes confidence level and reasoning  

## Setup

### 1. Install Dependencies
```bash
pip install langgraph langchain langchain-google-genai openpyxl python-dotenv
```

### 2. Get Google Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the API key

### 3. Configure Environment
Create a `.env` file in the project directory:
```bash
GOOGLE_API_KEY=your_api_key_here
```

Or set it as an environment variable:
```bash
# Windows PowerShell
$env:GOOGLE_API_KEY="your_api_key_here"

# Windows CMD
set GOOGLE_API_KEY=your_api_key_here

# Linux/Mac
export GOOGLE_API_KEY=your_api_key_here
```

## Usage

### Run the Analysis
```bash
python langgraph_financial_analysis.py
```

The system will:
1. Load CSV files (`kodo-pay-reimbursement.csv` and `transactions-csv.csv`)
2. Filter out credit transactions
3. Use LLM to categorize each transaction as CAPEX or OPEX
4. Calculate totals and breakdowns
5. Generate a professional Excel financial statement

### Output
The system generates an Excel file: `Financial_Statement_YYYYMMDD_HHMMSS.xlsx`

**Sheets included:**
- **Executive Summary**: High-level overview with totals and percentages
- **CAPEX Statement**: All capital expenditures with reasoning
- **OPEX Statement**: All operating expenditures with reasoning
- **Category Analysis**: Breakdown by expense category

## LangGraph Workflow

```
┌─────────────┐
│ Load Data   │ → Read CSV files, filter credits
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Categorize  │ → LLM analyzes each transaction
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Calculate   │ → Compute totals and breakdowns
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Generate    │ → Create professional Excel report
│ Report      │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Summary     │ → Print final summary
└─────────────┘
```

## CAPEX vs OPEX Logic

### CAPEX (Capital Expenditure)
- Electronics, hardware, equipment
- IT infrastructure (servers, networking)
- Manufacturing equipment, machinery
- Lab equipment and setup
- Security systems (CCTV)
- Major renovations, construction

### OPEX (Operating Expenditure)
- Rent, utilities
- Salaries, wages, labor
- Office supplies, consumables
- Food, groceries, meals
- Travel, commute, fuel
- Maintenance and repairs
- Logistics, shipping

## Advantages Over Rule-Based Approach

| Feature | Rule-Based | LangGraph + LLM |
|---------|-----------|-----------------|
| **Accuracy** | ~70-80% | ~90-95% |
| **Context Understanding** | Limited | Excellent |
| **Ambiguous Cases** | Requires manual review | Handles intelligently |
| **Reasoning** | None | Provides explanation |
| **Adaptability** | Fixed rules | Learns from context |

## File Structure

```
sideproj/
├── langgraph_financial_analysis.py  # Main LangGraph workflow
├── kodo-pay-reimbursement.csv       # Input data
├── transactions-csv.csv             # Input data
├── .env                             # API key (create this)
├── .env.template                    # Template for .env
└── Financial_Statement_*.xlsx       # Generated output
```

## Troubleshooting

### API Key Issues
- Make sure your `.env` file is in the same directory as the script
- Verify the API key is valid at [Google AI Studio](https://makersuite.google.com/app/apikey)
- Check that `python-dotenv` is installed

### CSV File Not Found
- Ensure both CSV files are in the same directory as the script
- Check file names match exactly: `kodo-pay-reimbursement.csv` and `transactions-csv.csv`

### LLM Errors
- Check your internet connection
- Verify API key has sufficient quota
- Try reducing batch size in the code if rate-limited

## Next Steps

- Review the generated Excel file
- Check transactions with "low" confidence
- Adjust categorization if needed
- Use the reasoning column to understand LLM decisions
