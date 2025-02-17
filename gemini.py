import google.generativeai as genai
import streamlit as st

with open("gemini.txt", "r") as file:
    key = file.read()
    file.close()

system_prompt=""" 
You are a code reviewer specializing in Python. Your task is to:
- Analyze submitted code .
- Identify potential bugs or errors.
- Suggest optimizations or improvements.
- Provide the corrected version in Python if the code is in another language.

🔍 **Response Structure**:
1️⃣ **Bug/Error Identification**
   - Detect errors in the provided code.
   - If it's **not Python**, identify the language and explain syntax differences.
   
2️⃣ **Suggested Fixes/Optimizations**
   - Recommend fixes for errors.
   - If the code is in another language, show the **correct equivalent in Python**.

3️⃣ **Corrected Code**
   - Provide the correct **Python version**.
   - Ensure it's fully functional and valid.
   - Explain the changes.

📌 **Important**:
- If the code is in Java, C++, JavaScript, etc., explain how to translate it into Python.
- DO NOT reject non-Python code; instead, analyze it and convert it if possible.
- Always wrap the corrected Python code in triple backticks with 'python' language identifier.
"""




genai.configure(api_key=key)
model = genai.GenerativeModel(model_name= "gemini-2.0-flash-exp",system_instruction=system_prompt)
def review_code(code):
    prompt = f"Review this code and provide fixes:\n{code}"
    response = model.generate_content(prompt)
    return response.text
def main():
    st.title("Python Code Reviewer")
    code = st.text_area("Enter your Python code below:", height= 200)
    if st.button("Review Code"):
        if code.strip():
            review = review_code(code)
            st.subheader("Review Feedback:")
            st.markdown(review)
        else:
            st.warning("Please enter some python code to review.")

if __name__ == "__main__":
    main()