topic = input("Feed me the topic: ")
size = input("What would be the size of the documentation: ")

from agents import factFinder, wordWeaver
from crewai import Crew, Process
from tasks import research, write
from tools import llm


def crew_execution(topic, size):
    crew = Crew(
        agents=[factFinder, wordWeaver],
        tasks=[research, write],
        process=Process.hierarchical,
        manager_llm=llm
    )
    result = crew.kickoff(inputs={"topic": topic, "size":size})
    print(result)

if __name__ == "__main__":
    crew_execution(topic, size)