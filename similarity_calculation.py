from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(query_features, reference_features):
    # Check dimensions and transpose if necessary
    if query_features.shape[1] != reference_features.shape[1]:
        reference_features = reference_features.T
    
    similarity_scores = cosine_similarity(query_features, reference_features)
    return similarity_scores
