from pathlib import Path

# find the folder containing this python file
BASE_DIR = Path(__file__).resolve().parent
# print(f"base dir ===> ${BASE_DIR}")

# location of the text documents
DOCUMENT_DIR = BASE_DIR / "documents"
print(f"doc dir ===> ${DOCUMENT_DIR}")

def search_documents(query: str) -> list[dict]:
    """Find sample documents containing relevant query."""
    terms = set()
    for word in query.split():
        cleaned_word = word.lower().strip(".,?!:")
        if len(cleaned_word) > 1:
            terms.add(cleaned_word)
            print(f"terms ===> {terms}")        

    results = []

    for path in DOCUMENT_DIR.glob("*.txt"):
        content = path.read_text(encoding="utf-8")
        matched_terms = sum(
            1
            for term in terms
                if term in content.lower()
        )

        if matched_terms:
            results.append({
                "source": path.name,
                "content": content,
                "matched_terms": matched_terms,
            })
    results.sort(
        key=lambda item: item["matched_terms"],
        reverse=True,
    )
    return results[:3]