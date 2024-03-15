# main.py

from preprocess import preprocess_text
from feature_extraction import tfidf_features
from similarity_calculation import calculate_similarity


def detect_plagiarism(query_text, reference_texts, threshold=0.8):
    preprocessed_query = preprocess_text(query_text)
    preprocessed_references = [preprocess_text(text) for text in reference_texts]

    # Extract TF-IDF features
    query_features, _ = tfidf_features([' '.join(preprocessed_query)])
    reference_features, _ = tfidf_features([' '.join(text) for text in preprocessed_references])

    # Ensure the number of features is consistent
    if query_features.shape[1] != reference_features.shape[1]:
        raise ValueError("Incompatible dimensions for query and reference features")

    # Calculate similarity
    similarity_scores = calculate_similarity(query_features, reference_features)

    print("Query features shape:", query_features.shape)
    print("Reference features shape:", reference_features.shape)
    print("Similarity scores:", similarity_scores)

    # Identify plagiarized content
    plagiarism_results = []
    for i, score in enumerate(similarity_scores[0]):
        if score >= threshold:
            plagiarism_results.append({
                'reference_text': reference_texts[i],
                'similarity_score': score
            })

    return plagiarism_results


if __name__ == "__main__":
    # Define the example document
    example_document = """
    This is an example document for testing plagiarism detection.
    It contains some text that may or may not be plagiarized from other sources.
    The goal is to identify any similarities between this document and the reference texts.
    """

    # Define the reference texts
    reference_texts = [
        "This is the first reference text. It contains some unique content that may or may not be similar to the example document.",
        "This is the second reference text. It also contains some unique content for testing plagiarism detection."
    ]

    try:
        # Test plagiarism detection
        results = detect_plagiarism(example_document, reference_texts)

        # Print results
        if results:
            print("Plagiarized content detected:")
            for result in results:
                print("Reference:", result['reference_text'])
                print("Similarity Score:", result['similarity_score'])
                print()
        else:
            print("No plagiarism detected.")
