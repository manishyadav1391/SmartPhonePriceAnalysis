import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load Data
df = pd.read_csv("amazon_smartphones.csv")

# Preprocessing
df["Price (₹)"] = df["Price (₹)"].astype(str).str.replace(",", "").astype(float)
df["Brand"] = df["Product Name"].fillna("Unknown").apply(lambda x: x.split()[0])

# Streamlit App
st.title("📊 Amazon Smartphone Data Analysis & Prediction Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
price_range = st.sidebar.slider("Select Price Range", min_value=int(df["Price (₹)"].min()),
                                max_value=int(df["Price (₹)"].max()), value=(5000, 50000))
brand_filter = st.sidebar.multiselect("Select Brand", df["Brand"].unique(), default=df["Brand"].unique())

# Apply Filters
filtered_df = df[(df["Price (₹)"] >= price_range[0]) & (df["Price (₹)"] <= price_range[1]) &
                 (df["Brand"].isin(brand_filter))]

st.write(f"Showing {len(filtered_df)} smartphones from {price_range[0]} to {price_range[1]} ₹")
st.dataframe(filtered_df)

# Data Visualization with Tabs
tab1, tab2, tab3 = st.tabs(["📈 Data Insights", "📊 Visualizations", "🤖 ML Model"])

with tab1:
    st.subheader("📌 Correlation Heatmap")
    numeric_df = df.select_dtypes(include=['number'])
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

with tab2:
    st.subheader("📌 Top 10 Most Expensive Smartphones")
    top_expensive = df.sort_values(by="Price (₹)", ascending=False).head(10)
    fig = px.bar(top_expensive, x="Price (₹)", y="Product Name", orientation='h',
                 title="Top 10 Most Expensive Smartphones", labels={'Price (₹)': 'Price (₹)', 'Product Name': 'Smartphone'})
    st.plotly_chart(fig)

    st.subheader("📌 Price Distribution Across Brands")
    fig = px.box(df, x="Brand", y="Price (₹)", title="Price Distribution by Brand")
    st.plotly_chart(fig)

    st.subheader("📌 Distribution of Ratings")
    fig = px.histogram(df, x="Rating", nbins=20, title="Distribution of Smartphone Ratings", labels={'Rating': 'Rating (Out of 5)'})
    st.plotly_chart(fig)

    st.subheader("📌 Top 10 Best Rated Smartphones")
    best_rated = df.sort_values(by="Rating", ascending=False).head(10)
    fig = px.bar(best_rated, x="Rating", y="Product Name", orientation='h',
                 title="Top 10 Best Rated Smartphones", labels={'Rating': 'Rating (Out of 5)', 'Product Name': 'Smartphone'})
    st.plotly_chart(fig)

    st.subheader("📌 Brand-wise Average Price")
    brand_avg_price = df.groupby("Brand")["Price (₹)"].mean().reset_index()
    fig = px.bar(brand_avg_price, x="Brand", y="Price (₹)", title="Average Price of Each Brand", labels={'Price (₹)': 'Average Price (₹)'})
    st.plotly_chart(fig)

    st.subheader("📌 Price vs. Rating Scatter Plot")
    fig = px.scatter(df, x="Rating", y="Price (₹)", title="Price vs. Rating Scatter Plot",
                     labels={'Rating': 'Rating (Out of 5)', 'Price (₹)': 'Price (₹)'})
    st.plotly_chart(fig)


with tab3:
    st.subheader("📌 Predict Smartphone Price")
# Feature Engineering
df['Rating'] = pd.to_numeric(df.get('Rating', pd.Series([0] * len(df))), errors='coerce')  # Convert to numeric
df['Rating'].fillna(df['Rating'].mean(), inplace=True)  # Fill missing values with mean

df = df.dropna(subset=['Price (₹)'])  # Ensure no NaN in target variable
X = df[['Rating']]
y = df['Price (₹)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_choice = st.selectbox("Choose a Machine Learning Model", ["Linear Regression", "Decision Tree", "KNN"])

if model_choice == "Linear Regression":
    model = LinearRegression()
elif model_choice == "Decision Tree":
    model = DecisionTreeRegressor()
else:
    model = KNeighborsRegressor()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

st.write(f"**Mean Absolute Error:** {mean_absolute_error(y_test, y_pred):.2f}")
st.write(f"**R² Score:** {r2_score(y_test, y_pred):.2f}")

st.subheader("📌 Predict a New Smartphone Price")
user_rating = st.number_input("Enter the Rating (out of 5)", min_value=0.0, max_value=5.0, step=0.1)

if st.button("Predict Price"):
    predicted_price = model.predict([[user_rating]])[0]
    st.success(f"Predicted Price: ₹{predicted_price:.2f}")
