# semantic.py — spaCy similarity (words + all-vs-all + sentences)

import spacy

def run(model="en_core_web_md"):
    nlp = spacy.load(model)

    # word similarity
    w1, w2, w3 = nlp("cat"), nlp("monkey"), nlp("banana")
    print("cat ~ monkey:", w1.similarity(w2))
    print("banana ~ monkey:", w3.similarity(w2))
    print("banana ~ cat:", w3.similarity(w1))

    # all-vs-all word matrix
    tokens = nlp("cat apple monkey banana")
    for t1 in tokens:
        for t2 in tokens:
            print(f"{t1.text:>6} vs {t2.text:<6} -> {t1.similarity(t2):.3f}")

    # sentence similarity
    sentence_to_compare = "Why is my cat on the car"
    sentences = [
        "where did my dog go",
        "Hello, there is my car",
        "I've lost my car in my car",
        "I'd like my boat back",
        "I will name my dog Diana",
    ]
    base = nlp(sentence_to_compare)
    for s in sentences:
        print(s, "->", nlp(s).similarity(base))

if __name__ == "__main__":
    # try md; download if missing
    try:
        run("en_core_web_md")
    except OSError:
        import spacy.cli as cli
        cli.download("en_core_web_md")
        run("en_core_web_md")

    # also try sm to compare (brief asks for a note on differences)
    try:
        print("\n--- Now with en_core_web_sm ---")
        run("en_core_web_sm")
    except OSError:
        pass

"""
NOTES (fill in after running):
- monkey~banana > monkey~apple (monkeys eat bananas) — interesting relation.
- md vs sm: 'md' has vectors → more meaningful similarity scores; 'sm' is flatter/less accurate.
"""
