# Imports
import streamlit as st
import google.generativeai as genai
import datetime
import time

# PART I: SETTING UP GOOGLE GEMINI 

with open(r"C:\Users\ganna\OneDrive\Desktop\keys.txt", "r") as f:  # Updated to the correct file path
    genai.configure(api_key=f.read())  # Replace with your API key

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# System Prompt
sys_prompt = """
You are FRIDAY: Your AI Code Reviewer. Analyze, debug, and optimize your scripts with AI assistance:
🐞 Bug Report: Identify potential bugs, syntax errors, and logical flaws in the code. Provide concise explanations for each issue in the form of a clear, numbered list.
🛠️ Fixed Code: Provide corrected or optimized code snippets, along with explanations of the changes made.
💡 Code Insights: Offer clear, concise, and helpful feedback suitable for developers with various levels of experience, in the form of a clear, numbered list.
"""

# Function - To get response
def get_response(sys_prompt, code_input):
    response = model.generate_content([sys_prompt, code_input])
    return response.text


# PART II: STREAMLIT UI - FRONTEND

# Set up the page configuration
st.set_page_config(
    page_title="FRIDAY: AI Code Reviewer",
    page_icon="🤖",
    layout="wide"
)

# Page Header
#st.title("🤖 FRIDAY: Your AI Code Reviewer")
st.markdown("<h1 style='text-align: center;'>🤖 <span style='color: red;'>FRIDAY:</span> Your AI Code Reviewer</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>Enhance Your Code with AI Analysis and Optimization </h3>", unsafe_allow_html=True)

# Page Footer
st.markdown("""
    <div style="position: fixed; bottom: 0; width: 100%; background-color: #2c3e50; color: white; padding: 3px 10px; font-size: 10px; display: flex; align-items: center;">
        <p style="margin: 0;"><strong>FRIDAY</strong> | Created by Vinay Kumar | Powered by Google Gemini AI and Streamlit</p>
    </div>
""", unsafe_allow_html=True)


# Navigation Bar

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar Navigation
#st.sidebar.title("DASHBOARD")
st.sidebar.markdown("""
    <h1 style='text-align: center;'><span style='color: red;'>DASHBOARD</span></h1>
    """, unsafe_allow_html=True)
st.sidebar.markdown("---")

# Sidebar with icons
if st.sidebar.button("🏠 Home"):
    st.session_state.page = "Home"
if st.sidebar.button("ℹ️ About"):
    st.session_state.page = "About"
if st.sidebar.button("📚 Resources"):
    st.session_state.page = "Resources"


# Content for Each Page
#1. HOME PAGE
if st.session_state.page == "Home":

    # Intro
    st.markdown("---")
    st.write("Review your code, resolve bugs, and uncover valuable insights!")
    st.markdown("FRIDAY is here to help! Paste your code, and let FRIDAY analyze and enhance it for you.")
    
    # Input Section
    st.write("📝 Code Input")
    code_input = st.text_area("Drop your code below:: ", placeholder="Enter your code")

    # Analyze button
    analyze_button = st.button("Analyze Code")

    if analyze_button:
        # Show the progress bar
        progress_bar = st.progress(0)

        # Simulate the code analysis process
        for i in range(100):
            # Update the progress bar
            progress_bar.progress(i + 1)
            time.sleep(0.05)  # Simulate processing delay (adjust as needed)

        try:
            response = get_response(sys_prompt, code_input)
            st.write(response)
        except Exception as e:
            print(e)

#2. ABOUT PAGE
elif st.session_state.page == "About":
    
    st.markdown("---")
    st.write("""**FRIDAY** was created to simplify code reviews and assist developers in enhancing the quality of their Python code. 
             Whether you're a beginner or an experienced developer, AlphaBot provides an efficient, user-friendly solution.""")
    
    st.write("")
    st.subheader("How to Use")
    st.write("""
    1. Navigate to the **Home** section of the app.
    2. Input your code: Paste your Python code into the provided text area.
    3. Submit for review: Click the "Analyze" button to initiate the review process.
    4. Receive Feedback: A **Bug Report**, **Fixed Code**, and **Insights** will be displayed.
    
    The app features an intuitive **Navigation Bar** on the sidebar, allowing you to switch between different sections like **Home**, **About**, and **Resources** for a seamless experience.
    """)
    
    # Feedback Section
    st.write("")
    st.subheader("Feedback")
    with st.expander("Submit Feedback"):
        feedback = st.text_area("Would love to hear your thoughts or suggestions:", height=150)
        submit_button = st.button("Submit Feedback")

        if submit_button:
            if feedback:
                # Save feedback to a text file (you can modify this part to save to an Excel file as well)
                with open("feedback.txt", "a") as file:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    file.write(f"Timestamp: {timestamp}\nFeedback: {feedback}\n\n")
                
                st.success("Thank you for your feedback!")
            else:
                st.warning("Please enter some feedback before submitting.")
    
    # Disclaimer Section (in italics)
    st.write("")
    st.subheader("Disclaimer")
    st.markdown("_FRIDAY is a **prototype** designed to assist with Python code reviews. While it aims to provide accurate and helpful feedback, it may not always be complete or error-free. Users are advised to use the insights with discretion._")
    

#3. RESOURCES PAGE
elif st.session_state.page == "Resources":

    st.markdown("---")

    st.write("Here are some helpful resources for getting started:")

    st.markdown("- [Python Documentation](https://docs.python.org/3/)")
    st.markdown("- [Streamlit Documentation](https://docs.streamlit.io/)")
    st.markdown("- [Google Gemini API Docs](https://developers.generativeai.google/)")

    st.write("")  
    
    # Community Resources 
    st.subheader("Community Resources")
    st.write("Join these communities to ask questions, share knowledge, and solve problems")

    st.markdown("- [Python Tag on Stack Overflow](https://stackoverflow.com/questions/tagged/python)")
    st.markdown("- [r/streamlit on Reddit](https://www.reddit.com/r/streamlit/)")
    st.markdown("- [r/Python on Reddit](https://www.reddit.com/r/Python/)")

    st.write("")  

    # Learning Resources 
    st.subheader("Learning Resources")
    st.write("Check out these tutorials, documentation, and courses to level up your skills")

    st.markdown("##### Python:")
    st.markdown("- [Real Python Tutorials](https://realpython.com/)")
    st.markdown("- [W3Schools Python Tutorial](https://www.w3schools.com/python/)")
    st.markdown("- [Python Cheat Sheet (DataCamp)](https://www.datacamp.com/cheat-sheet/category/python)")

    st.write("")
    st.markdown("##### Streamlit:")
    st.markdown("- [Streamlit Cheat Sheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)")