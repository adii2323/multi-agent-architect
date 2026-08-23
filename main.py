from crewai import Agent, Task, Crew
import os
from dotenv import load_dotenv

load_dotenv() # Loads your API keys from the .env file

# 1. Researcher Agent: Reads documentation
researcher = Agent(
    role='Repository Researcher',
    goal='Understand the codebase architecture and API specs',
    backstory='You are a senior analyst who quickly grasps complex repositories.',
    verbose=True,
    allow_delegation=False
)

# 2. Explorer Agent: Navigates file structure
explorer = Agent(
    role='File Structure Explorer',
    goal='Locate the exact files that need modification based on feature requests',
    backstory='You are an expert at navigating large codebases and finding dependencies.',
    verbose=True,
    allow_delegation=False
)

# 3. Coder Agent: Writes the code
coder = Agent(
    role='Senior Software Engineer',
    goal='Synthesize context to write clean, working code for the feature request',
    backstory='You are a 10x developer who writes bug-free, efficient code.',
    verbose=True
)