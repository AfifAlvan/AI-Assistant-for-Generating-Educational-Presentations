from transformers import pipeline

def generate_materi(topic: str) -> str:
    generator = pipeline(
        "text-generation",
        model="EleutherAI/gpt-neo-2.7B",
        tokenizer="EleutherAI/gpt-neo-2.7B",
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
        num_return_sequences=1,
        max_new_tokens=300  # Bisa kamu ubah jadi 200–500 sesuai kebutuhan
    )

    prompt = (
        "You are an assistant that helps create PowerPoint presentation material. "
        "Provide a detailed, informative, and structured explanation in English about the following topic. "
        "Include definitions, key characteristics, causes or history if relevant, and real-world examples if applicable.\n\n"
        "Make the explanation easy to understand, clear, and suitable for an educational slide. Use paragraph format.\n\n"
        f"Topic: {topic}"
    )

    result = generator(prompt)
    teks = result[0]['generated_text'].replace(prompt, '').strip()
    return teks
