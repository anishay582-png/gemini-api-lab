import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

prompt = input("Enter your question: ")

response = client.models.generate_content(
    model="gemini-3.8-flash" \
    "",
    contents=prompt
)

print("\nGemini Response:\n")
print(response.text)