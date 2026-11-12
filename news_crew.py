import os
from datetime import datetime

from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool


# ----------------------------------------
# STEP 1: Load Environment Variables
# ----------------------------------------

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing in .env")

if not os.getenv("SERPER_API_KEY"):
    raise ValueError("SERPER_API_KEY is missing in .env")


# ----------------------------------------
# STEP 2: Configure LLM
# ----------------------------------------

llm = LLM(
    model="openai/gpt-4.1-mini",
    temperature=0.3
)


# ----------------------------------------
# STEP 3: Initialize Search Tool
# ----------------------------------------

search_tool = SerperDevTool()


# ----------------------------------------
# STEP 4: Create Researcher Agent
# ----------------------------------------

researcher = Agent(
    role="Technology News Researcher",

    goal=(
        "Find today's top 3 important technology "
        "news stories using web search."
    ),

    backstory=(
        "You are an experienced technology journalist "
        "who researches current technology developments "
        "and verifies news using reliable sources."
    ),

    tools=[search_tool],

    llm=llm,

    verbose=True,

    allow_delegation=False
)


# ----------------------------------------
# STEP 5: Create Writer Agent
# ----------------------------------------

writer = Agent(
    role="Technology Newsletter Writer",

    goal=(
        "Convert researched technology news "
        "into a clear and engaging 5-line newsletter."
    ),

    backstory=(
        "You are a professional newsletter writer "
        "who creates short, informative technology "
        "news summaries for readers."
    ),

    tools=[],  # Writer has NO web search access

    llm=llm,

    verbose=True,

    allow_delegation=False
)


# ----------------------------------------
# STEP 6: Create Research Task
# ----------------------------------------

today = datetime.now().strftime("%B %d, %Y")

research_task = Task(
    description=(
        f"Search the web for the top 3 technology "
        f"news stories published today ({today}). "
        "Use SerperDevTool to find reliable sources. "
        "For each story, provide:\n"
        "1. News headline\n"
        "2. Short summary\n"
        "3. Source URL\n"
        "4. Publication date\n"
        "Do not invent news. If fewer than 3 "
        "verified stories are available, say so."
    ),

    expected_output=(
        "A list of up to 3 verified technology "
        "news stories with headlines, summaries, "
        "source URLs and publication dates."
    ),

    agent=researcher,

    output_file="output/research_results.md"
)


# ----------------------------------------
# STEP 7: Create Writing Task
# ----------------------------------------

writing_task = Task(
    description=(
        "Using ONLY the Researcher's findings, "
        "create a technology newsletter containing "
        "exactly 5 lines.\n"
        "Line 1: Newsletter title and date.\n"
        "Lines 2-4: One concise news story per line.\n"
        "Line 5: A brief overall takeaway.\n"
        "Do not search the web. "
        "Do not introduce unsupported information. "
        "If fewer than 3 verified stories are provided, "
        "do not invent missing stories."
    ),

    expected_output=(
        "An engaging technology newsletter "
        "containing exactly 5 lines."
    ),

    agent=writer,

    context=[research_task],  # Explicit output handoff

    output_file="output/tech_newsletter.md"
)


# ----------------------------------------
# STEP 8: Create Crew
# ----------------------------------------

tech_news_crew = Crew(
    agents=[
        researcher,
        writer
    ],

    tasks=[
        research_task,
        writing_task
    ],

    process=Process.sequential,

    verbose=True
)


# ----------------------------------------
# STEP 9: Execute Crew
# ----------------------------------------

if __name__ == "__main__":

    print("\nStarting Technology News Crew...\n")

    result = tech_news_crew.kickoff()

    print("\n" + "=" * 60)
    print("FINAL TECHNOLOGY NEWSLETTER")
    print("=" * 60)

    print(result.raw)

    print("=" * 60)