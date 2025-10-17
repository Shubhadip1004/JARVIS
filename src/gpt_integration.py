from openai import OpenAI

# Function to ask the model
def ask_model(prompt,gpt_api_key):
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=gpt_api_key,
    )
    
    completion = client.chat.completions.create(
        extra_body={},
        model="tngtech/deepseek-r1t2-chimera:free",  # free-tier model on OpenRouter
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return str(completion.choices[0].message.content).split('#')[0]



# ---------- TEST / DEMO ----------
# if __name__ == "__main__":
#     print("JARVIS is ready!")
#     while True:
#         user_input = input("\nYou: ")
#         if user_input.lower() in ["exit", "quit", "bye"]:
#             print("JARVIS: Goodbye! 👋")
#             break

#         reply = ask_model(user_input)
#         print("JARVIS:", reply)
