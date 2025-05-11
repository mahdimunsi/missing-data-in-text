from transformers import pipeline

print("Loading BERT model...")
unmasker = pipeline("fill-mask", model="bert-base-uncased")
print("Model loaded successfully.")

def fill_blanks(text, top_k=1):
    while "[MASK]" in text:
        results = unmasker(text, top_k=top_k)
        
        if isinstance(results, list) and isinstance(results[0], list):
            result = results[0][0]
        else:
            result = results[0]

        predicted_word = result['token_str'].strip()
        text = text.replace("[MASK]", predicted_word, 1)
    return text

def main():
    print("\nWelcome to the BERT Interactive Fill-Mask Script!")
    print("Enter a sentence with one or more [MASK] tokens to begin.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter your sentence: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if "[MASK]" not in user_input:
            print("Please include at least one [MASK] token in your sentence.")
            continue
        
        print("\nFilling blanks...")
        completed_text = fill_blanks(user_input)
        print(f"\nFinal Result: {completed_text}\n")

if __name__ == "__main__":
    main()
