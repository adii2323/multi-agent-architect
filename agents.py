from crewai import Agent, LLM
from tools import list_directory, read_file

# Initialize the local Ollama model
# Ensure the model name matches exactly what you pulled in the terminal
local_llm = LLM(
    model="ollama/llama3.1",
    base_url="http://localhost:11434"
)

# 1. The Researcher
researcher = Agent(
    role='Codebase Researcher',
    goal='Understand the architecture and API specs of the repository.',
    backstory='You are a senior software architect who excels at understanding complex codebases.',
    llm=local_llm,
    tools=[list_directory, read_file]
)

# 2. The Explorer
explorer = Agent(
    role='File System Explorer',
    goal='Find exactly which files need to be modified for a new feature request.',
    backstory='You are a structural engineer for code, expert at navigating directories to locate where logic lives.',
    llm=local_llm,
    tools=[list_directory, read_file]
)

# 3. The Coder
coder = Agent(
    role='Senior Developer',
    goal='Write production-ready code based on research and exact file context.',
    backstory='You are a 10x developer who writes flawless code matching existing conventions.',
    llm=local_llm,
    tools=[] 
)