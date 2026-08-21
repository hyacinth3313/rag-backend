from pipeline import translate_to_hindi, retrieve, generate_answer

test_queries = [
    ("ಕಾರ್ಪೊರೇಷನ್ ಎಂದರೇನು?", "kannada"),
    ("Does medical marijuana help?", "english"),
    ("How does pollution cause human population to grow", "english"),
]

for q, lang in test_queries:
    translated = translate_to_hindi(q, source_language=lang)
    docs, metas, distances = retrieve(translated)
    answer = generate_answer(q, docs, answer_language=lang)
    print(f"\nOriginal: {q}")
    print(f"Distances: {distances}")
    print(f"RAW model answer: {repr(answer)}")
