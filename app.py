import os

import streamlit as st

from DevGPT import PythonDevAssistant

# Streamlit UI
st.title("Python Dev Assistant")

# Input box at the top
user_input = st.text_input("Please enter your coding query:")
env_vars_input = st.text_input(
    "Please enter your environment variables (if any):")

# Button saying 'start dev-gpt'
if st.button('Start Dev-GPT'):
  assistant = PythonDevAssistant()

  try:
    if env_vars_input:
      # Environment variables must be set
      for env_var in env_vars_input.split(','):
        key, value = env_var.split('=')
        os.environ[key.strip()] = value.strip()
      assistant.add_msg(
          f"you have set the following environment variables: {env_vars_input}"
      )

    # Generate code
    output = assistant.generate_code(user_input)

    # Code section
    st.subheader("Generated code:")
    st.code(output, language='python')

    # Console log box
    st.subheader("Console Log:")
    with st.spinner("Running code..."):
      console_log = assistant.run_script('temp.py').stdout
      st.text(console_log)

  except Exception as e:
    st.error(f"Error: {str(e)}")
