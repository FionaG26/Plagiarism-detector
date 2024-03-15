from main import detect_plagiarism

if __name__ == "__main__":
    # Define the query text
    query_text = "The quick brown fox jumps over the lazy dog."

    # Define the reference texts
    reference_texts = [
        "The brown fox jumps over the lazy dog.",
        "A quick fox jumps over a lazy dog.",
        "The swift brown fox leaps over the lazy hound."
    ]

    # Test plagiarism
    results = detect_plagiarism(query_text, reference_texts)

    # Print results
    if results:
        print("Plagiarized content detected:")
        for result in results:
            print("Reference:", result['reference_text'])
            print("Similarity Score:", result['similarity_score'])
            print("Similarity Percentage:", result['similarity_percentage'])
            print()
    else:
        print("No plagiarism detected.")
