{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "789541a2-c6f3-4354-9196-2c4166d1b52d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\MANISH YADAV\\AppData\\Local\\Temp\\ipykernel_21132\\617610996.py:14: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
      "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
      "\n",
      "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
      "\n",
      "\n",
      "  df[\"Price (₹)\"].fillna(0, inplace=True)\n",
      "C:\\Users\\MANISH YADAV\\AppData\\Local\\Temp\\ipykernel_21132\\617610996.py:15: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
      "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
      "\n",
      "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
      "\n",
      "\n",
      "  df[\"Brand\"].fillna(\"Unknown\", inplace=True)\n",
      "2025-03-31 15:52:53.767 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.769 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.773 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.779 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.782 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.787 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.789 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.796 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.806 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.833 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.839 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.851 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.857 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.861 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.871 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.875 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.878 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.882 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.892 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.899 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.901 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:53.904 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "C:\\Users\\MANISH YADAV\\AppData\\Local\\Temp\\ipykernel_21132\\617610996.py:40: FutureWarning: \n",
      "\n",
      "Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `y` variable to `hue` and set `legend=False` for the same effect.\n",
      "\n",
      "  sns.barplot(x=\"Price (₹)\", y=\"Product Name\", data=top_expensive, palette=\"coolwarm\", ax=ax)\n",
      "2025-03-31 15:52:54.269 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:55.455 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:55.457 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:55.459 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:55.460 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:55.514 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:55.903 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:55.906 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:55.910 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:55.913 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:55.915 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-31 15:52:55.917 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Load Data\n",
    "df = pd.read_csv(\"amazon_smartphones.csv\")\n",
    "\n",
    "# Preprocessing\n",
    "df[\"Price (₹)\"] = df[\"Price (₹)\"].astype(str).str.replace(\",\", \"\").astype(float)\n",
    "df[\"Brand\"] = df[\"Product Name\"].fillna(\"Unknown\").apply(lambda x: x.split()[0])  # Extract brand\n",
    "\n",
    "# Handle missing values\n",
    "df[\"Price (₹)\"].fillna(0, inplace=True)\n",
    "df[\"Brand\"].fillna(\"Unknown\", inplace=True)\n",
    "\n",
    "# Streamlit App\n",
    "st.title(\"📊 Amazon Smartphone Data Analysis Dashboard\")\n",
    "\n",
    "# Sidebar Filters\n",
    "st.sidebar.header(\"Filters\")\n",
    "price_range = st.sidebar.slider(\"Select Price Range\", min_value=int(df[\"Price (₹)\"].min()), \n",
    "                                 max_value=int(df[\"Price (₹)\"].max()), value=(5000, 50000))\n",
    "\n",
    "brand_filter = st.sidebar.multiselect(\"Select Brand\", df[\"Brand\"].unique(), default=df[\"Brand\"].unique())\n",
    "\n",
    "# Apply Filters\n",
    "filtered_df = df[(df[\"Price (₹)\"] >= price_range[0]) & (df[\"Price (₹)\"] <= price_range[1]) & \n",
    "                 (df[\"Brand\"].isin(brand_filter))].copy()\n",
    "\n",
    "# Show Data\n",
    "st.write(f\"Showing {len(filtered_df)} smartphones from {price_range[0]} to {price_range[1]} ₹\")\n",
    "st.dataframe(filtered_df)\n",
    "\n",
    "# Visualization: Top 10 Expensive Smartphones\n",
    "st.subheader(\"📌 Top 10 Most Expensive Smartphones\")\n",
    "top_expensive = df.sort_values(by=\"Price (₹)\", ascending=False).head(10)\n",
    "\n",
    "fig, ax = plt.subplots(figsize=(10, 5))\n",
    "sns.barplot(x=\"Price (₹)\", y=\"Product Name\", data=top_expensive, palette=\"coolwarm\", ax=ax)\n",
    "plt.xlabel(\"Price (₹)\")\n",
    "plt.ylabel(\"Smartphones\")\n",
    "st.pyplot(fig)\n",
    "\n",
    "# Visualization: Top 5 Most Common Brands\n",
    "st.subheader(\"📌 Top 5 Most Common Brands\")\n",
    "top_brands = df[\"Brand\"].value_counts().head(5)\n",
    "\n",
    "fig, ax = plt.subplots(figsize=(6, 4))\n",
    "top_brands.plot(kind=\"bar\", color=[\"blue\", \"red\", \"green\", \"purple\", \"orange\"], ax=ax)\n",
    "plt.xlabel(\"Brand\")\n",
    "plt.ylabel(\"Count\")\n",
    "plt.title(\"Most Common Smartphone Brands\")\n",
    "st.pyplot(fig)\n",
    "\n",
    "# Run the App\n",
    "st.sidebar.write(\"💡 Tip: Adjust the filters to analyze different segments of smartphones!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c38f5dfa-1c37-4639-a51c-b12d00ba7bc8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
