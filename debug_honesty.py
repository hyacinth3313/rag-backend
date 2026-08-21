from pipeline import translate_to_hindi, retrieve, generate_answer

q = "What is the definition of honesty?"
translated = translate_to_hindi(q, source_language="english")
docs, metas, distances = retrieve(translated)
answer = generate_answer(q, docs, answer_language="english")

print(f"Translated: {translated}")
print(f"Distances: {distances}")
print(f"Top doc: {docs[0][:150]}")
print(f"RAW answer: {repr(answer)}")
