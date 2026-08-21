from pipeline import translate_to_hindi, retrieve

test_queries = [
    ("ಕಾರ್ಪೊರೇಷನ್ ಎಂದರೇನು?", "kannada"),
    ("Does medical marijuana help?", "english"),
    ("How does pollution cause human population to grow", "english"),
]

for q, lang in test_queries:
    translated = translate_to_hindi(q, source_language=lang)
    docs, metas, distances = retrieve(translated)
    print(f"\nOriginal: {q}")
    print(f"Translated: {translated}")
    print(f"Distances: {distances}")
    print(f"Top doc: {docs[0][:100]}")
