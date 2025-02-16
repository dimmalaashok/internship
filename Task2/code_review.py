import streamlit as st
import google.generativeai as genai


genai.configure(api_key='AIzaSyAK7Np89oc0g4vJoxjmezwZWE8wYIQYzrM')

st.title("Python Code Review Tool (Vertex AI)")

code_input = st.text_area("Enter your Python code:", height=200)

if st.button("Review Code"):
    if not code_input:
        st.warning("Please enter some code to review.")
    else:
        try:
            model=genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp")

            prompt = f"Review the following Python code and identify potential issues, bugs, or areas for improvement. Provide suggested fixes:\n\n{code_input}"

            response = model.generate_text(
                prompt=prompt,
                max_output_tokens=500,
                temperature=0.5,
            )

            review_result = response.result.strip()

            st.subheader("Code Review Results:")
            st.write(review_result)
            if "Fixed Code:" in review_result:
                fixed_code = review_result.split("Fixed Code:")[1].strip()
                st.subheader("Suggested Fixed Code:")
                st.code(fixed_code, language="python")

        except Exception as e:
            st.error(f"An error occurred during code review: {e}")
