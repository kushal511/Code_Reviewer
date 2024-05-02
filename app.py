import streamlit as st
from openai import OpenAI

st.title("🧑‍💻 BugMaster: AI-Powered Code Reviewer")

code= st.text_area("Enter your code")

if st.button("Generate") == True:
    f=open("keys/project_openai_api_key.txt")
    key = f.read()
    client= OpenAI(api_key=key)
    response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "system", "content": """You are a helpful AI Assistant. You job is to find the bugs, 
                                             explain the bugs and correct the errors in the code.After correcting the code write the
                                             correct code and write the changes that made"""},
            {"role": "user", "content":code}

          ]
    )

    st.write(response.choices[0].message.content)
