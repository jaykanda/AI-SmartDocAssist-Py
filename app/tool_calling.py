from langchain_core.tools import tool
from document_search import search_documents

@tool
def search_company_policies(query: str) -> list[dict]:
    """Search the sample company policy documents"""
    tool_results =  search_documents(query)

    if not tool_results:
        print(f"Check the query once again!")

    formatted_results = []

    for result in tool_results:
        formatted_results.append(
            f"Source: {result['source']}\n"
            f"Matched terms: {result['matched_terms']}\n"
            f"Content:\n{result['content']}"
        )

    return "\n\n---\n\n".join(formatted_results)

if __name__ == "__main__":
    question = input("Ask a question about company policies: ")

    answer = search_company_policies.invoke(
        {"query": question}
    )
    print(__name__)
    print("\nSearch results:\n")
    print(answer)
    
