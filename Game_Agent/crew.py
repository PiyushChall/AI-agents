import os

import agentops
from agents import chief_developer, qa_engineer, senior_developer
from crewai import Crew, Process
from tasks import brainstorm, evaluation, programming, reviewing
from tools import llm

agentop_api_key = os.environ['AGENTOP_API_KEY']
agentops.init(agentop_api_key)

game = input(
    "What is the name of the game you want to create? (e.g. Pong, 2048, Tetris, etc): ")
#mechanism = input("What Specific mechanism would you like to add: ")

crew = Crew(agents=[senior_developer, qa_engineer, chief_developer],
            tasks=[brainstorm, programming, reviewing, evaluation],
            process=Process.hierarchical,
            manager_llm=llm)

result = crew.kickoff(inputs={"game": game})
print(result)
