# AI Smart Document Assistant

A local web application for asking questions about the sample company policy documents. The React frontend sends questions to a FastAPI backend. The backend searches the text files in `app/documents` and uses OpenAI's `gpt-4o-mini` model to answer from the matching document content.

## Features

- Search the sample leave, expense, and IT security policies.
- Get a natural-language answer grounded in matched policy documents.
- Return the source filenames with the API response.
- Run the frontend and backend locally during development.

## Requirements

- Python 3.9 or later
- Node.js 20.19+ or 22.12+, with npm
- An OpenAI API key

## Setup

### 1. Configure the OpenAI API key

Create a `.env` file in the project root (next to this README) and add your key:

```dotenv
OPENAI_API_KEY=your_openai_api_key
```

Do not commit this file or share your API key. `.env` is ignored by Git.

### 2. Install backend dependencies

From the project root, create and activate a virtual environment in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell prevents script activation, use the Python executable in the virtual environment directly:

```powershell
.\.venv\Scripts\python.exe -m pip install fastapi uvicorn langchain-openai langchain-core python-dotenv
```

Otherwise, install the packages into the activated environment:

```powershell
python -m pip install fastapi uvicorn langchain-openai langchain-core python-dotenv
```

> `requirements.txt` is currently empty, so it does not install the backend packages.

### 3. Install frontend dependencies

Open a second PowerShell terminal:

```powershell
Set-Location frontend
npm install
```

## Run the application

Start the backend from the `app` directory:

```powershell
Set-Location app
python -m uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`. Interactive API documentation is available at `http://localhost:8000/docs`.

In the second terminal, start the frontend:

```powershell
Set-Location frontend
npm run dev
```

Open the local URL printed by Vite (by default, `http://localhost:5173`). Keep both development servers running while using the app.

## Using the assistant

Enter a question about a policy in the chat page, then select **Ask AI**. Example questions:

- “How many days of annual leave do full-time employees receive?”
- “What receipts are required for expense reimbursement?”
- “What should I do if I suspect a phishing email?”

The backend checks the policy text files for query terms and sends the matching document content, together with the question, to the language model. If no documents match, it returns a message saying no relevant information was found.

## API

### `POST /userprompt`

Request:

```json
{
  "question": "How many days of annual leave do employees receive?"
}
```

When documents match, the response includes the question, generated answer, and source filenames:

```json
{
  "question": "How many days of annual leave do employees receive?",
  "answer": "The leave entitlement is described in the leave policy.",
  "sources": ["leave_policy.txt"]
}
```

The backend returns an `answer` and an empty `sources` array when no documents match. The frontend calls this endpoint at `http://localhost:8000/userprompt`.

## Project structure

```text
app/
  main.py                 FastAPI endpoint and request handling
  document_search.py      Keyword search over policy text files
  llm_service.py          OpenAI chat model and answer prompt
  tool_calling.py         Optional command-line policy search tool
  documents/              Searchable company policy documents
frontend/
  src/
    components/
      ChatWindow.jsx      Question and answer interface
    services/
      api.js              Backend API client
    main.jsx              React entry point
```

## Notes and limitations

- Search is a simple case-insensitive keyword match, not semantic or vector search. It returns up to three matching files, ordered by the number of matched terms.
- Answers depend on the contents of the supplied policy files and the configured OpenAI model. Verify important policy decisions against the official company policy.
- The frontend is configured for the local backend at `http://localhost:8000`; the backend CORS configuration allows the Vite development origin `http://localhost:5173`.
- The optional `app/tool_calling.py` script runs policy search without calling the language model:

  ```powershell
  Set-Location app
  python tool_calling.py
  ```
