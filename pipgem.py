!pip install -q -U google-generativeai
!pip install gradio google-generativeai
import os
import google.generativeai as genai
%env GOOGLE_API_KEY=<*******************> 
!python gemini_bot.py
import google.generativeai as genai
%env GENERATIVE_AI_ENDPOINT=https://generativelanguage.googleapis.com

genai.configure(api_key='**************************')
   
for m in genai.list_models():
      if 'generateContent' in m.supported_generation_methods:
           print(m.name)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
prompt = prompt = input("wellcome to Abhinandan's AI chat\n Ask me anything: ")
response = chat.send_message(prompt, stream=True)
for chunk in response:
  if chunk.text:
    print(chunk.text)
