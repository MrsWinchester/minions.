# watch_next.py — recommend the most similar movie
# Requires: python -m pip install spacy
# Then:     python -m spacy download en_core_web_md

import spacy
from pathlib import Path

# load the medium English model (with word vectors)
nlp = spacy.load("en_core_web_md")

def load_movies(path: str = "movies.txt"):
    """Read movies.txt lines of the form 'Title: description'."""
    entries = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if ":" in line:
            title, desc = line.split(":", 1)
            entries.append((title.strip(), desc.strip()))
    return entries

def watch_next(current_description: str, movies_file: str = "movies.txt"):
    """Return (best_title, similarity_score) for the closest movie."""
    doc_current = nlp(current_description)
    best_title, best_score = None, -1.0
    for title, desc in load_movies(movies_file):
        score = doc_current.similarity(nlp(desc))
        if score > best_score:
            best_title, best_score = title, score
    return best_title, best_score

if __name__ == "__main__":
    # Use the Planet Hulk description from the brief
    planet_hulk = (
        "Will he save their world or destroy it? When the Hulk becomes too dangerous "
        "for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space "
        "to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the "
        "planet Sakaar where he is sold into slavery and trained as a gladiator."
    )
    title, score = watch_next(planet_hulk)
    print(f"Next to watch: {title} (similarity {score:.3f})")
