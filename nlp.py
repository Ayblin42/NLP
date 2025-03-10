import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import string


candidates = [
    {"id": 1, "name": "Alice Martin", "skills": ["python", "sql", "machine learning", "data visualization", "statistics"], "experience": 5, "bio": "Data scientist passionnée par l'IA et l'analyse de données pour résoudre des problèmes business"},
    {"id": 2, "name": "Thomas Dubois", "skills": ["java", "spring", "postgresql", "microservices", "docker"], "experience": 8, "bio": "Développeur backend senior spécialisé en applications d'entreprise et architecture distribuée"},
    {"id": 3, "name": "Emma Bernard", "skills": ["python", "react", "docker", "javascript", "typescript"], "experience": 3, "bio": "Développeuse fullstack avec expérience en containerisation et interfaces modernes"},
    {"id": 4, "name": "Lucas Petit", "skills": ["c++", "python", "aws", "algorithms", "cuda"], "experience": 6, "bio": "Ingénieur logiciel intéressé par le calcul haute performance et l'optimisation"},
    {"id": 5, "name": "Chloé Dupont", "skills": ["javascript", "node.js", "mongodb", "react", "graphql"], "experience": 4, "bio": "Développeuse web créative orientée applications en temps réel et interfaces utilisateur"},
    {"id": 6, "name": "Hugo Leroy", "skills": ["python", "django", "sql", "rest api", "git"], "experience": 2, "bio": "Développeur backend junior avec intérêt pour le web et les bases de données"},
    {"id": 7, "name": "Léa Moreau", "skills": ["java", "kotlin", "sql", "android", "firebase"], "experience": 7, "bio": "Développeuse mobile expérimentée spécialisée en Android et applications connectées"},
    {"id": 8, "name": "Nathan Fournier", "skills": ["javascript", "react", "aws", "serverless", "redux"], "experience": 5, "bio": "Architecte frontend intéressé par le cloud computing et les architectures décentralisées"},
    {"id": 9, "name": "Camille Girard", "skills": ["python", "tensorflow", "sql", "nlp", "bert"], "experience": 4, "bio": "Data scientist spécialisée en deep learning pour NLP et analyse de texte"},
    {"id": 10, "name": "Maxime Roux", "skills": ["c#", ".net", "azure", "sql server", "xamarin"], "experience": 6, "bio": "Développeur Microsoft avec expertise en services cloud et applications multi-plateformes"},
    {"id": 11, "name": "Julie Lambert", "skills": ["product management", "agile", "user research", "data analysis", "python"], "experience": 5, "bio": "Product manager technique avec background en développement et forte orientation données"},
    {"id": 12, "name": "Romain Bonnet", "skills": ["devops", "kubernetes", "terraform", "aws", "ci/cd"], "experience": 7, "bio": "Ingénieur DevOps passionné par l'automatisation et les infrastructures évolutives"},
    {"id": 13, "name": "Sophie Mercier", "skills": ["ux design", "figma", "user research", "html", "css"], "experience": 4, "bio": "Designer UX/UI centrée sur l'expérience utilisateur et l'accessibilité"},
    {"id": 14, "name": "Antoine Perrin", "skills": ["php", "symfony", "mysql", "elasticsearch", "redis"], "experience": 6, "bio": "Développeur backend PHP avec expertise en performance et systèmes distribués"},
    {"id": 15, "name": "Élodie Blanc", "skills": ["data engineering", "spark", "kafka", "python", "scala"], "experience": 5, "bio": "Data engineer spécialisée dans les architectures big data et le traitement en temps réel"}
]

jobs = [
    {"id": 1, "title": "Data Scientist", "required_skills": ["python", "machine learning", "statistics", "sql", "data visualization"], "min_experience": 3, "description": "Analyser des données et créer des modèles prédictifs pour notre plateforme de recommandation. Travailler sur l'optimisation de nos algorithmes de matching."},
    {"id": 2, "title": "Développeur Backend Java", "required_skills": ["java", "spring", "sql", "microservices", "docker"], "min_experience": 5, "description": "Concevoir et développer des microservices performants pour notre architecture d'entreprise. Optimiser les requêtes de base de données et les API REST."},
    {"id": 3, "title": "Développeur Fullstack", "required_skills": ["javascript", "react", "node.js", "mongodb", "typescript"], "min_experience": 2, "description": "Travailler sur notre application web moderne avec stack JavaScript. Implémenter de nouvelles fonctionnalités et améliorer l'expérience utilisateur."},
    {"id": 4, "title": "Ingénieur DevOps", "required_skills": ["docker", "kubernetes", "aws", "terraform", "ci/cd"], "min_experience": 4, "description": "Optimiser notre pipeline CI/CD et gérer l'infrastructure cloud. Automatiser le déploiement et améliorer la fiabilité de nos services."},
    {"id": 5, "title": "Data Engineer", "required_skills": ["python", "sql", "spark", "kafka", "data pipelines"], "min_experience": 3, "description": "Construire des pipelines de données efficaces pour alimenter nos systèmes d'analyse. Gérer l'intégration de différentes sources de données et assurer leur qualité."},
    {"id": 6, "title": "Développeur Mobile", "required_skills": ["kotlin", "android", "java", "firebase", "rest api"], "min_experience": 3, "description": "Développer et maintenir notre application mobile Android. Implémenter de nouvelles fonctionnalités et assurer la compatibilité avec différents appareils."},
    {"id": 7, "title": "NLP Engineer", "required_skills": ["python", "nlp", "tensorflow", "bert", "machine learning"], "min_experience": 2, "description": "Travailler sur des modèles de traitement du langage naturel pour extraire automatiquement des informations pertinentes à partir de CVs et descriptions de postes."},
    {"id": 8, "title": "Frontend Developer", "required_skills": ["javascript", "react", "html", "css", "redux"], "min_experience": 2, "description": "Développer des interfaces utilisateur réactives et intuitives pour notre plateforme. Collaborer avec les designers UX pour implémenter de nouvelles fonctionnalités."}
]


#Nettoie et normalise un texte via tokenisation, stopwords et lemmatisation.
def preprocess_text(text):
    stemmer=nltk.stem.SnowballStemmer('french') 

    tokens = word_tokenize(text.lower())                                    # Tokenisation
    tokens = [word for word in tokens if word.isalnum()]                    # Suppression des ponctuations

    french_stopwords = set(stopwords.words('french'))
    tokens = [word for word in tokens if word not in french_stopwords]      # Suppression des mots inutiles

    tokens = [stemmer.stem(word) for word in tokens]                        # Lemmatisation
    return tokens


for candidate in candidates:
    candidate["bio_processed"] = preprocess_text(candidate["bio"])
    print(f"Bio de {candidate['name']} après traitement:", candidate["bio_processed"])

for job in jobs:
    job["description_processed"] = preprocess_text(job["description"])
    print(f"Description du poste '{job['title']}' après traitement:", job["description_processed"])
