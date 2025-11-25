# 🔑 How to Add API Key on Streamlit Cloud

## Step-by-Step Visual Guide

### 1. Deploy Your App First
Go to https://share.streamlit.io/ and create a new app:
- **Repository**: `div-nar/fin-report-agent`
- **Branch**: `main`
- **Main file**: `app.py`
- Click **Deploy**

The app will start deploying but will show an error (missing secrets). That's expected!

### 2. Access App Settings
Once the app is deployed (even if it's showing an error):
1. You'll see your app in the Streamlit Cloud dashboard
2. Click the **⋮** (three vertical dots) next to your app name
3. Select **"Settings"** from the dropdown menu

### 3. Navigate to Secrets Tab
In the Settings panel:
1. You'll see several tabs at the top
2. Click on the **"Secrets"** tab

### 4. Add Your API Key
In the Secrets editor (it looks like a text box):
1. Paste this **EXACTLY** as shown:
   ```toml
   GOOGLE_API_KEY = "AIzaSyAK1SqewnXSUOVkkgjnjlhk9CMAupaZ3tM"
   ```
2. Make sure there are **no extra spaces** or quotes
3. Click the **"Save"** button at the bottom

### 5. App Restarts Automatically
- Streamlit will automatically restart your app
- Within 30 seconds, your app should be working!
- The error will disappear

### 6. Test It
- Visit your app URL (something like `https://your-app-name.streamlit.app`)
- Upload the CSV files
- Click "Analyze Expenses"
- It should work perfectly!

---

## ⚠️ Common Mistakes to Avoid

❌ **DON'T** add extra quotes: `GOOGLE_API_KEY = ""AIza...""` 
✅ **DO** use exactly: `GOOGLE_API_KEY = "AIza..."`

❌ **DON'T** forget the equals sign
✅ **DO** use: `GOOGLE_API_KEY = "..."`

❌ **DON'T** add spaces around the key
✅ **DO** paste it exactly as shown above

---

## 🎯 Quick Copy-Paste

Just copy this entire line and paste it into the Secrets box:

```
GOOGLE_API_KEY = "AIzaSyAK1SqewnXSUOVkkgjnjlhk9CMAupaZ3tM"
```

Then click Save. Done! 🎉
