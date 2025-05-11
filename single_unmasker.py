# filename: interactive_unmasker.py

from transformers import pipeline

def main():
    # Load the fill-mask pipeline
    print("Loading model... (this may take a few seconds the first time)")
    unmasker = pipeline("fill-mask", model="bert-base-uncased")

    print("\nEnter a sentence with [MASK] to predict (type 'exit' to quit):")
    while True:
        user_input = input("Your sentence: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if "[MASK]" not in user_input:
            print("Please include a [MASK] token in your sentence.")
            continue

        try:
            result = unmasker(user_input)
            print("\nPredictions:")
            for r in result:
                print(f"{r['sequence']} (score: {r['score']:.4f})")
            print()  # Add space between predictions
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
