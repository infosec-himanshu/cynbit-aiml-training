import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Performance Predictor", layout="wide")

st.title("🎓 Student Performance Predictor")
st.write("This machine learning tool helps teachers and students understand how habits affect results by predicting a future grade category (High, Medium, or Low).")

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Predict Performance", "Upload & Train Model"])

def train_model(df):
    required_cols = ['Attendance', 'Study_Hours', 'Grade_Category']
    if not all(col in df.columns for col in required_cols):
        st.error("Dataset must contain 'Attendance', 'Study_Hours', and 'Grade_Category' columns.")
        return None, None
    
    le = LabelEncoder()
    df['Grade_Category_Encoded'] = le.fit_transform(df['Grade_Category'])
    
    X = df[['Attendance', 'Study_Hours']]
    y = df['Grade_Category_Encoded']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    return model, le

if 'model' not in st.session_state:
    st.session_state.model = None
    st.session_state.le = None
    st.session_state.data = None

if page == "Upload & Train Model":
    st.header("📁 Upload Student Dataset")
    
    uploaded_file = st.file_uploader("Upload a CSV file with student data", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state.data = df
        st.success("File uploaded successfully!")
        
        st.subheader("Data Preview")
        st.dataframe(df.head())
        
        if st.button("Train Model"):
            with st.spinner("Training model... Please wait..."):
                model, le = train_model(df)
                if model is not None:
                    st.session_state.model = model
                    st.session_state.le = le
                    st.success("Model trained successfully! You can now go to the 'Predict Performance' page.")

elif page == "Predict Performance":
    st.header("🔮 Predict & Analyze Performance")
    
    if st.session_state.model is None:
        st.warning("⚠️ Please upload a dataset and train the model first in the 'Upload & Train Model' tab.")
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Enter Student Details")
            attendance = st.slider("Attendance (%)", min_value=0, max_value=100, value=75)
            study_hours = st.slider("Weekly Study Hours", min_value=0, max_value=50, value=15)
            
            if st.button("Predict Grade Category"):
                input_data = pd.DataFrame([[attendance, study_hours]], columns=['Attendance', 'Study_Hours'])
                prediction_encoded = st.session_state.model.predict(input_data)
                prediction = st.session_state.le.inverse_transform(prediction_encoded)[0]
                
                st.metric(label="Predicted Grade Category", value=prediction)
                
                st.subheader("Summary Report")
                if prediction == "High":
                    st.success("Excellent! Maintain this routine to secure a high grade.")
                elif prediction == "Medium":
                    st.info("Good job, but increasing study hours or attendance slightly could push you to a 'High' grade.")
                else:
                    st.error("Warning: High risk of low performance. Focus on increasing attendance and dedicated study hours.")
        
        with col2:
            st.subheader("📊 Data Visualization")
            df = st.session_state.data
            
            fig, ax = plt.subplots()
            colors = {'High': 'green', 'Medium': 'orange', 'Low': 'red'}
            
            for category, group in df.groupby('Grade_Category'):
                ax.scatter(group['Attendance'], group['Study_Hours'], label=category, color=colors.get(category, 'blue'), alpha=0.6)
            
            ax.scatter(attendance, study_hours, color='black', marker='X', s=200, label='Current Prediction Input')
            
            ax.set_xlabel('Attendance (%)')
            ax.set_ylabel('Study Hours')
            ax.set_title('Student Performance Distribution')
            ax.legend()
            
            st.pyplot(fig)