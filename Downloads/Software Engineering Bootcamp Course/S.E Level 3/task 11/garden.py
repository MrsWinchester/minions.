"""
garden.py — spaCy basics with tokenisation + Named Entity Recognition (NER)

What this script does:
- Loads spaCy's English model with basic error handling
- Tokenises each sentence
- Performs NER and prints (entity text, entity label)
- Prints explanations for all entity labels seen (via spacy.explain)
- Includes a short reflection comment at the bottom (as required)
"""

from pathlib import Path

try:
    import spacy
    from spacy.cli import download as spacy_download
except ImportError as e:
    raise SystemExit(
        "spaCy is not installed. Install it first:\n\n  python -m pip install spacy\n"
    ) from e


def load_model(name: str = "en_core_web_sm"):
    """Load a spaCy model, downloading it if needed."""
    try:
        return spacy.load(name)
    except OSError:
        print(f"[info] Model '{name}' not found — downloading...")
        spacy_download(name)
        return spacy.load(name)


def analyze(sentences: list[str]) -> None:
    """Tokenise + run NER for each sentence and explain labels."""
    if not sentences:
        print("[warn] No sentences provided.")
        return

    nlp = load_model()
    seen_labels: set[str] = set()

    for i, raw in enumerate(sentences, start=1):
        s = (raw or "").strip()
        if not s:
            print(f"\n[{i}] <empty> — skipped.")
            continue

        doc = nlp(s)
        print(f"\n[{i}] {s}")
        print("Tokens:", [t.text for t in doc])

        if doc.ents:
            ents = [(ent.text, ent.label_) for ent in doc.ents]
            print("Entities:", ents)
            seen_labels.update(lbl for _, lbl in ents)
        else:
            print("Entities: (none)")

    if seen_labels:
        print("\nEntity label explanations:")
        for lbl in sorted(seen_labels):
            explanation = spacy.explain(lbl) or "No explanation available"
            print(f"  {lbl}: {explanation}")


if __name__ == "__main__":
    # Add at least 2 garden-path sentences + the required three:
    gardenpathSentences = [
        "Mary gave the child a Band-Aid.",
        "That Jill is never here hurts.",
        "The cotton clothing is made of grows in Mississippi.",
        "The old man the boats.",
        "The complex houses married and single soldiers and their families.",
    ]
    analyze(gardenpathSentences)

"""
Reflection on two looked-up entities (required):

1) GPE — 'Countries, cities, states' (spacy.explain('GPE')).
   In my output, 'Mississippi' is tagged GPE. This makes sense because Mississippi is a U.S. state.

2) PERSON — 'People, including fictional' (spacy.explain('PERSON')).
   'Mary' and 'Jill' are tagged PERSON. That matches their use as human names.

Note: Depending on the model, 'Band-Aid' may appear as PRODUCT or ORG; either is reasonable.
"""
