from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(query_features, reference_features):
    similarity_scores = cosine_similarity(query_features, reference_features)
    return similarity_scores
