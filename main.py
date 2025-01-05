!pip install openai
import openai
openai.api_key= "s-proj-Crm6FrndRpm3-ydUTdIFElWWVb_PG47j-fVB_eLWw-oA4st-MNi_NUjGYwaOWsPjNe9uo-lkcaT3BlbkFJitg-8R-r3UtqqwtiffBPbYtSm1ORPAj-6361wKCMavICfC6Y92NAPFigl3gDo_mrVjyoFoEcEA"

def chat_with_gpt(prompt):
  response = openai.chat.completions.create(
      model = "gpt-4o-mini",
      messages = [{"role": "user", "content": prompt}]
      
      # messages = [
      #     {"role": "system", "content": "You are a helpful assistant."},
      #     {"role": "user", "content": prompt}
      # ]
  )
  return response.choices[0].message.content.strip()

# if __name__ == "_main_":
#   while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#       break
#     response = chat_with_gpt(user_input)
#     print("ChatGPT: ", response)

if __name__ == "__main__":
  while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
      break

    response = chat_with_gpt(user_input)
    print("ChatGPT:", response)
