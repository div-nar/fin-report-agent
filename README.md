# 🐶 Dognosis Financial Spend Report

An intelligent financial analysis tool tailored for hardware companies. It categorizes expenses into CAPEX and OPEX using custom business rules and LLM-powered analysis.

## 🚀 Features

-   **Hardware Logic**: Automatically treats "Mechanical Hardware" as CAPEX.
-   **Custom Rules**: Handles specific vendor logic (e.g., Vishwanatha > 1000 = CAPEX).
-   **LLM Categorization**: Uses Gemini 2.5 Flash to intelligently categorize "Uncategorized" items.
-   **Interactive Reports**: Generates detailed Excel reports with Executive Summaries.

## 🛠️ Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configuration**:
    -   The app uses a secure `secrets.toml` file for the API key.
    -   **Sharing**: If you share this tool, you must include the `.streamlit/secrets.toml` file.
    -   **GitHub**: This file is ignored by git for security.

3.  **Run the App**:
    ```bash
    streamlit run app.py
    ```

## 📂 Project Structure

-   `app.py`: Main Streamlit application.
-   `requirements.txt`: Python dependencies.
-   `.streamlit/secrets.toml`: API Key storage (Keep private!).

