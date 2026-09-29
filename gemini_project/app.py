from google import genai

client = genai.Client()

topic = input("Enter a topic: ")

response = client.models.generate_content(
    model="gemini-3.7-flash",
    contents=f"Create 5 study flashcards about {topic}. "
             "For each flashcard, give a question and a short answer."
)

print("\nGenerated Flashcards:\n")
print(response.text)