from gpt4all import GPT4All

# Replace the filename with EXACTLY the name of your model file
model_name = "Phi-3-mini-4k-instruct.Q4_0.gguf"
model = GPT4All(model_name)

SYSTEM_PROMPT = "You are a helpful assistant. Answer clearly and do not use <|assistant|> or <|user|> tags."

with model.chat_session():
    model.generate(SYSTEM_PROMPT)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = model.generate(user_input, max_tokens=200)
        # Remove weird tags the model sometimes adds
        clean = response.replace("<|assistant|>", "").replace("<|user|>", "")
        print("Bot:", clean.strip())