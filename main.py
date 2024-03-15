from preprocess import preprocess_text
from feature_extraction import tfidf_features
from similarity_calculation import calculate_similarity

def detect_plagiarism(query_text, reference_texts, feature_extraction='tfidf', threshold=0.8):
    preprocessed_query = preprocess_text(query_text)
    preprocessed_references = [preprocess_text(text) for text in reference_texts]

    if feature_extraction == 'bow':
        # Implement if needed
        pass
    else:
        query_features, _ = tfidf_features([query_text])  # Pass query_text as a list
        reference_features, _ = tfidf_features(reference_texts)  # Pass reference_texts directly

    similarity_scores = calculate_similarity(query_features, reference_features)

    plagiarism_results = []
    for i, score in enumerate(similarity_scores[0]):
        if score >= threshold:
            plagiarism_results.append({
                'reference_text': reference_texts[i],
                'similarity_score': score
            })

    return plagiarism_results

if __name__ == "__main__":
    # Read the content of the example document
    with open("example_document.txt", "r") as file:
        query_text = file.read()

    # Define the reference texts
    reference_texts = []
    for i in range(1, 3):  # Assuming you have 2 reference texts: reference1.txt, reference2.txt
        with open(f"reference{i}.txt", "r") as file:
            reference_texts.append(file.read())

    # Test plagiarism detection
    results = detect_plagiarism(query_text, reference_texts)

    # Print results
    if results:
        print("Plagiarized content detected:")
        for result in results:
            print("Reference:", result['reference_text'])
            print("Similarity Score:", result['similarity_score'])
            print()
    else:
        print("No plagiarism detected.")
