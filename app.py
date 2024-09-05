import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm

API_KEY = 'AIzaSyB6rcCHX4bq4YEmTtSfXPBUCQQawUymgjM'  # Replace with your actual API key
genai.configure(api_key=API_KEY)

# Set page configuration as the first command
st.set_page_config(page_title="AI Email Generator", layout="wide")

st.title("AI Email Generator")

prompt = st.text_input("Enter your prompt here...")
generate_btn = st.button("Generate Code")

if generate_btn:
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(
        glm.Content(parts=[
            glm.Part(text="You are a AI EMAIL GENERATOR"
                    "You also add generated content in the email around the question"
                    "You dont give any other response but only html emails for prompts given"
                    "you give clean html files with great designs and scalability"
                    "you dont give explaination and if you do you give it in comments of html"
                    "you are good marketing tool and offer many resources to add in the email"
                    "you only answer to prompt asking email related questions"
                    "you dont say which part of the code is html '```html' in the starting but you only give html code"
                    "you give explaination only when asked and then you dont show any code and if asked at once you do show code"
                    "To maintain good visual preveiw you make sure the html file is greatly detailed"
                    "You are a good tool for email marketing and you are good for creating email templates"
                    "Remove ```html in the front"
                    "You check the email in it doesnt have generated content add it "
                    "You look into the prompt and generate content"
                    )
        ]),
        stream=True
    )
    
    response.resolve()  # Resolve the response
    
    generated_code = response.text if response is not None else "No code generated."
    
    # Display the generated code and its visual representation
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Generated Code:")
        st.code(generated_code, language='html')  # Display the generated code as HTML
    
    with col2:
        st.subheader("Visual Preview:")
        
        # Render the generated HTML code directly
        st.components.v1.html(generated_code, height=500, scrolling=True)