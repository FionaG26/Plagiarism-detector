from preprocess import preprocess_text
from feature_extraction import bow_features, tfidf_features
from similarity_calculation import calculate_similarity


def detect_plagiarism(query_text, reference_texts, feature_extraction='tfidf', threshold=0.8):
    preprocessed_query = preprocess_text(query_text)
    preprocessed_references = [preprocess_text(text) for text in reference_texts]

    if feature_extraction == 'bow':
        query_features, _ = bow_features([' '.join(preprocessed_query)])
        reference_features, _ = bow_features([' '.join(text) for text in preprocessed_references])
    else:
        query_features, _ = tfidf_features([' '.join(preprocessed_query)])
        reference_features, _ = tfidf_features([' '.join(text) for text in preprocessed_references])

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
    query_text = "Your query text goes here."
    reference_texts = ["Reference document 1.", "Reference document 2.", "Reference document 3."]

    results = detect_plagiarism(query_text, reference_texts)

    if results:
        print("Plagiarized content detected:")
        for result in results:
            print("Reference:", result['reference_text'])
            print("Similarity Score:", result['similarity_score'])
            print()
    else:
        print("No plagiarism detected.")

