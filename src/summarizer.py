import ollama
# Use the generate function for a one-off prompt
#result = ollama.generate(model="mistral", prompt="Summarize the following text: 'The quick brown fox jumps over the lazy dog.'")
#print(result["response"])

def summary(text):
    result = ollama.generate(model="mistral", prompt=f"Summarize the following text: '{text}'")
    return result["response"]

text = input("Enter meeting text: ")
print(summary(text))