from sentence_transformers import SentenceTransformer, util

# Load a pre-trained SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')  # You can use other models like 'all-MPNet-V2'

def calculate_similarity(sentence1, sentence2):
    # Generate embeddings for the sentences
    embedding1 = model.encode(sentence1, convert_to_tensor=True)
    embedding2 = model.encode(sentence2, convert_to_tensor=True)

    # Compute cosine similarity
    similarity = util.pytorch_cos_sim(embedding1, embedding2)

    return similarity.item()  # Convert the tensor to a scalar

# Example sentences
sentence1 = "The quick brown fox jumps over the lazy dog."
sentence2 = "A fast dark-colored fox leaps over a sleeping dog."

# Calculate and display similarity
similarity_score = calculate_similarity(sentence1, sentence2)
print(f"Similarity score: {similarity_score:.4f}")