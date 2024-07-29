import os
import sys

# Add the scripts directory to the sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

from extract_text import extract_text_from_pdf
from preprocess import preprocess_text
from feature_extraction import extract_features
from similarity_calculation import calculate_cosine_similarity

def main(input_invoice_path, database_folder):
    input_text = preprocess_text(extract_text_from_pdf(input_invoice_path))
    input_features = extract_features(input_text)

    database_texts = []
    database_files = []
    for file in os.listdir(database_folder):
        if file.endswith('.pdf'):
            db_text = preprocess_text(extract_text_from_pdf(os.path.join(database_folder, file)))
            database_texts.append(db_text)
            database_files.append(file)
    
    max_similarity = 0
    most_similar_invoice = None

    for i, db_text in enumerate(database_texts):
        db_features = extract_features(db_text)
        similarity = calculate_cosine_similarity(input_features, db_features)
        
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_invoice = database_files[i]

    return most_similar_invoice, max_similarity

if __name__ == "__main__":
    input_invoice_path = 'invoices/invoice_77098.pdf'
    database_folder = 'invoices/database'
    most_similar_invoice, similarity_score = main(input_invoice_path, database_folder)
    print(f"Most Similar Invoice: {most_similar_invoice}")
    print(f"Similarity Score: {similarity_score}")
