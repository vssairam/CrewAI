# 📰 Technology News Newsletter Using CrewAI

## 1. Project Overview

This project demonstrates a **multi-agent AI workflow using CrewAI**, where two specialized AI agents collaborate sequentially to research technology news and generate a concise newsletter.

The Researcher Agent searches the internet for the top three technology news stories of the day using SerperDevTool.

The Writer Agent receives the Researcher's findings and converts them into a five-line technology newsletter without accessing the internet.

The project demonstrates **agent collaboration, tool restrictions, sequential task execution, and explicit context sharing**.

## 2. Problem Statement

Yesterday one agent worked alone. Today two work in a line.

Build a CrewAI crew with:
- A Researcher that searches the web using SerperDevTool.
- A Writer that cannot search the web.
- The Researcher identifying today's top three technology news stories.
- The Writer transforming those findings into a five-line newsletter.
- Tasks executing sequentially.
- The Researcher's output being explicitly passed to the Writer.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| CrewAI | Multi-agent orchestration |
| SerperDevTool | Internet search |
| OpenAI GPT-4.1-mini | Language model for both agents |
| python-dotenv | Environment variable management |
| Markdown | Saving agent outputs |
| VS Code | Development environment |

## 4. Project Structure

```text
CrewAI/
│
├── main.py
├── test_serper.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
└── output/
    ├── research_results.md
    └── tech_newsletter.md
```

**Note:** The `.env` file contains private API credentials and must never be committed to GitHub.

## 5. Agent Architecture

### Agent 1: Technology News Researcher

**Role:** Technology News Researcher

**Responsibilities:**
- Search the internet using SerperDevTool.
- Identify three important technology news stories.
- Collect headlines, summaries, publication dates, and source URLs.
- Pass the research findings to the Writer.

**Tools:** SerperDevTool

### Agent 2: Technology Newsletter Writer

**Role:** Technology Newsletter Writer

**Responsibilities:**
- Receive the Researcher's findings.
- Summarize three technology news stories.
- Generate a newsletter containing exactly five lines.
- Avoid introducing unsupported information.

**Tools:** None

The Writer has no CrewAI search tools and is instructed to use only the Researcher's findings.

## 6. Workflow Architecture

```text
              START
                |
                v
       Researcher Agent
                |
                v
         SerperDevTool
                |
                v
     Search Technology News
                |
                v
      Identify Top 3 Stories
                |
                v
       Research Task Output
                |
                +----> research_results.md
                |
                v
       Context Handoff
                |
                v
          Writer Agent
        (No Search Tools)
                |
                v
      Generate Newsletter
                |
                v
        Writing Task Output
                |
                +----> tech_newsletter.md
                |
                v
               END
```

## 7. Sequential Execution

The CrewAI workflow uses:

```python
process=Process.sequential
```

This ensures that the Researcher completes its task before the Writer begins.

The Writer explicitly receives the Researcher's output through:

```python
context=[research_task]
```

This establishes the dependency between the two tasks.

## 8. Installation and Setup

### Prerequisites

- Python installed
- VS Code
- OpenAI API key
- Serper.dev API key

### Create Virtual Environment

```powershell
python -m venv venv
```

### Activate Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```powershell
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project directory.

```env
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

Never publish actual API keys.

## 9. Running the Application

Execute:

```powershell
python main.py
```

The CrewAI application will:

1. Initialize both agents.
2. Execute the Researcher's web searches.
3. Collect technology news stories.
4. Pass the research findings to the Writer.
5. Generate the five-line newsletter.
6. Save both task outputs into separate Markdown files.

## 10. Output Files

### research_results.md

Contains the Researcher's findings, including:
- News headlines
- Short summaries
- Source URLs
- Publication dates

### tech_newsletter.md

Contains the Writer's five-line newsletter.

The newsletter follows this structure:

| Line | Content |
|---|---|
| 1 | Newsletter title and date |
| 2 | First technology news story |
| 3 | Second technology news story |
| 4 | Third technology news story |
| 5 | Overall takeaway |

## 11. Validation

### Test Serper API

```powershell
python test_serper.py
```

A successful request returns HTTP status code 200.

### Validate Newsletter Length

```powershell
(Get-Content .\output\tech_newsletter.md |
Where-Object { $_.Trim() -ne "" }).Count
```

**Expected result:**

```text
5
```

### Execution Results

The application was successfully executed on November 12, 2026.

| Validation | Result |
|---|---|
| CrewAI initialization | PASS |
| SerperDevTool execution | PASS |
| Researcher task | PASS |
| Writer task | PASS |
| Sequential execution | PASS |
| Research-to-Writer handoff | PASS |
| Research output file created | PASS |
| Newsletter output file created | PASS |
| Five-line validation | PASS |

## 12. Key Learnings

This assignment demonstrates:

- Creating multiple AI agents using CrewAI.
- Assigning different responsibilities to agents.
- Restricting tool access based on agent roles.
- Integrating external search APIs.
- Executing tasks sequentially.
- Sharing task outputs through explicit context dependencies.
- Saving individual agent outputs.
- Validating the generated newsletter.

## 13. Limitations and Future Enhancements

The current implementation uses search results and snippets to identify technology news.

Potential improvements include:

- Verifying headlines against individual news articles.
- Validating publication dates.
- Providing direct article URLs.
- Adding automated source-grounding checks.
- Exporting newsletters to PDF.
- Scheduling daily newsletter generation.

## 14. Conclusion

This project successfully demonstrates a **two-agent sequential workflow using CrewAI**.

The Researcher gathers current technology news using SerperDevTool, while the Writer transforms the findings into a concise five-line newsletter without using search tools.

The project highlights the importance of **agent specialization, controlled tool access, task dependencies, and structured output generation**.