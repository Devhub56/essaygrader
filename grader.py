# alternative import
# from spacy_download import load_spacy
# Will download the model if it isn't installed yet
# nlp = load_spacy("en_core_web_sm", exclude=["parser", "tagger"])  

import spacy

# Load the language model
nlp = spacy.load('en_core_web_sm')

# Define the rubric
rubric = {
    'content': 50,
    'structure': 20,
    'grammar': 10,
    'coherence': 20
}

def calculate_score(rubric, doc):
    scores = {}
    scores['content'] = doc.similarity(nlp("This essay addresses the prompt and includes relevant examples."))
    scores['structure'] = doc.similarity(nlp("The essay has a clear structure and is easy to follow."))
    scores['grammar'] = doc.similarity(nlp("The essay has correct grammar, spelling, and punctuation."))
    scores['coherence'] = doc.similarity(nlp("The essay flows well and is easy to understand."))
    
    total_score = sum(scores[aspect] * weight for aspect, weight in rubric.items())
    return total_score, scores

def assign_grade(total_score):
    if total_score >= 90:
        grade = 'A'
    elif total_score >= 80:
        grade = 'B'
    elif total_score >= 70:
        grade = 'C'
    else:
        grade = 'F'
    return grade

# Take student response
response = input("Enter your essay: ")

# Analyze the essay using spaCy
doc = nlp(response)

# Calculate score and assign grade
total_score, scores = calculate_score(rubric, doc)
grade = assign_grade(total_score)

# Generate the report
print(f"Total score: {total_score}")
print(f"Grade: {grade}")
print("Individual scores:")
for aspect, score in scores.items():
    print(f"{aspect.capitalize()}: {score * rubric[aspect]}")
