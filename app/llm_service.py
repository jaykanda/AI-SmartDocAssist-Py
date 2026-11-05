from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Create prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a company document assistant.

        Answer questions using ONLY the provided
        document content.

        Instructions:
        1. Provide clear human-readable answers.
        2. Do not invent information.
        3. If information is unavailable, say
           that the documents do not contain
           the requested information.
        4. Mention the source document.
        """
    ),
    (
        "human",
        """
        User Question:
        {question}

        Retrieved Document Content:
        {context}

        Provide the answer.
        """
    )
])

# Create LLM processing function
def generate_answer(question, context):
    chain = prompt | llm
    response = chain.invoke({
        "question": question,
        "context": context
    })
    return response.content