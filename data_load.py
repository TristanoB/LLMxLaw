import re
import json
from docx import Document
import os

# Charger le document DOCX
file_path = "C:\\Users\\trist\\Documents\\dev\\LLMxLaw\\LLMxLaw\\database"

processed_files = {}

for root, dirs, files in os.walk(file_path):
        for file in files:
            # Get full file path
            file_path = os.path.join(root, file)
            
        
            # Process based on file extension
            if file.lower().endswith('.docx'):
                # Process Word document
                doc = Document(file_path)
                content = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
                processed_files[file] = content



# Réorganiser les chunks en articles
articles = []
for name, text in processed_files.items() :

    # Diviser le texte en chunks basés sur le motif "Art. xx-x"
    pattern = r'\n\s*(Art\.\s*[\w\.-]+(?:\s\d+)?)'
    splits = re.split(pattern, text)

    
    for i in range(1, len(splits), 2):  ## Réorganiser les chunks en articles
        title = splits[i].strip()
        content = splits[i + 1].strip() if i + 1 < len(splits) else ""
        articles.append({"article": f'{name} - {title}', "content": content})

    # Exporter les articles dans un fichier JSON
    output_path = f"C:\\Users\\trist\\Documents\\dev\\LLMxLaw\\LLMxLaw\\data_test\\all_articles.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)

    print(f"Les articles ont été extraits et sauvegardés dans {output_path}.")




    
