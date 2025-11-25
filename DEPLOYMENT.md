# 🚀 Deployment Guide: Streamlit Community Cloud

This guide explains how to deploy your app so your team can use it **without entering an API key**.

## 1. Push to GitHub

1.  **Create a New Repository** on GitHub (e.g., `dognosis-finance-report`).
    *   Make it **Public** (easiest) or **Private**.
    *   Do *not* initialize with README/gitignore (we already have them).

2.  **Push your code**:
    Open your terminal in the `fin-report-agent` folder and run:
    ```bash
    git remote add origin https://github.com/YOUR_USERNAME/dognosis-finance-report.git
    git branch -M main
    git push -u origin main
    ```

## 2. Deploy to Streamlit Cloud

1.  Go to [share.streamlit.io](https://share.streamlit.io/).
2.  Click **"New app"**.
3.  Select your GitHub repository (`dognosis-finance-report`), branch (`main`), and file (`app.py`).
4.  Click **"Deploy!"**.

## 3. Configure Secrets (The Magic Step 🪄)

This is how your team uses the app without an API key.

1.  Once the app is deploying (or fails because of missing key), go to your App's **Dashboard** on Streamlit Cloud.
2.  Click the **Settings** menu (three dots) next to your app -> **Settings**.
3.  Go to the **Secrets** tab.
4.  Paste the content of your local `.streamlit/secrets.toml` file here:
    ```toml
    GOOGLE_API_KEY = "AIzaSyAK1SqewnXSUOVkkgjnjlhk9CMAupaZ3tM"
    ```
5.  Click **Save**.

## 🎉 Result

*   **Your Team**: They just visit the URL (e.g., `https://dognosis-finance.streamlit.app`). The app works instantly. No keys required.
*   **Security**: The key is stored safely in Streamlit's encrypted secrets manager, not in the code.
