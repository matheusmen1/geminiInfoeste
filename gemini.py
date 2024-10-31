import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyAsLmKs8T_R0K8A4fXDneVg6nzRDKng6nk"

genai.configure(api_key = GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
prompt = "Conte a historia do windows em 2 paragrafos."
response = model.generate_content(prompt)
print (response.text)
