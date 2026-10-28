from google import genai

KEY = input("Paste key: ").strip()
client = genai.Client(api_key=KEY)
try:
    r = client.models.generate_content(model="gemini-flash-latest", contents="Say hello")
    print("WORKS:", r.text)
except Exception as e:
    print("ERROR:", e)