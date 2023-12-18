import streamlit as st
import google.generativeai as genai
import api

# Configure the API key
genai.configure(api_key=api.api_key)

# Set default parameters
defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.5,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
}

st.write('# ClassiFire \N{fire}')

classes = st.number_input("Class count", min_value=0)

inputs = [st.text_input(f'Class {i + 1}', i+1, key=f"text_input_{i}")for i in range(classes)]

classification = ', '.join(inputs)

if classes > 0:
  prompt = st.text_input("Enter Text :")
  if st.button('Generate'):
    try:
        response = genai.generate_text(**defaults,
                                   prompt=(('base on this text: ' + prompt + ' , give me the answer of ' + classification + ' as an output.')))
        st.write(response.result)
    except:
        st.write("Try again, I, A.I. cannot think as a woman. Kono Giorno Giovanna ga yume ga aru")

    