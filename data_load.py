import re
import json
from docx import Document
import os

# Charger le document DOCX
file_path = "C:\\Users\\trist\\Documents\\dev\\LLMxLaw\\LLMxLaw\\data_test\\test.docx"
file_name = os.path.basename(file_path)
document = Document(file_path)


# Extraire le texte de tout le document
text = "\n".join([paragraph.text for paragraph in document.paragraphs])

# Diviser le texte en chunks basés sur le motif "Art. xx-x"
pattern = r'\n\s*Art\.\s*([\w\.-]+(?:\s\d+)?)'
splits = re.split(pattern, text)

# Réorganiser les chunks en articles
articles = []
for i in range(1, len(splits), 2):  # Parcours des titres et du texte suivant
    title = splits[i].strip()
    content = splits[i + 1].strip() if i + 1 < len(splits) else ""
    articles.append({"article": title, "content": content})

# Exporter les articles dans un fichier JSON
output_path = f"C:\\Users\\trist\\Documents\\dev\\LLMxLaw\\LLMxLaw\\data_test\\articles_{file_name}.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(articles, f, ensure_ascii=False, indent=4)

print(f"Les articles ont été extraits et sauvegardés dans {output_path}.")




   
