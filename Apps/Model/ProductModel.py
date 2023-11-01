import torch
from transformers import BertTokenizer, BertModel
from Util.Database import get_connection
from sklearn.metrics.pairwise import cosine_similarity

class ProductModel:
    def __init__(self):
        # Initialize BERT model and tokenizer
        self.model = BertModel.from_pretrained('bert-base-uncased')
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    def embed_text(self, texts):
        inputs = self.tokenizer(texts, return_tensors="pt", max_length=512, truncation=True, padding="max_length")
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.pooler_output.numpy()

    def search_products(self, query):
        # Embed the query
        query_embedding = self.embed_text([query])

        # Fetch precomputed embeddings and product IDs from the database
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, embedding FROM product_embeddings")  # Assuming you've stored pre-computed embeddings
        products = cursor.fetchall()
        cursor.close()
        conn.close()

        product_scores = []
        for product in products:
            product_embedding = product['embedding']
            similarity = cosine_similarity(query_embedding, product_embedding)
            product_scores.append((product['id'], similarity[0][0]))

        # Sort products by similarity
        sorted_products = sorted(product_scores, key=lambda x: x[1], reverse=True)

        # Return product IDs in order of relevance
        return [product_id for product_id, _ in sorted_products]