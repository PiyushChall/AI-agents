from textwrap import dedent

from crewai import Agent
from tools import llm, search_tool, web_search_tool

topic = input("What topic you would want to learn today? : ")
Researcher = Agent(
  name = "Markus"
  role = "Researcher",
  goal = dedent(
    """
    
    """
  ),
  memory = True,
  verbose = True,
  backstory = dedent(
    """
    
    """
  ),
  tools = [search_tool, web_search_tool],
  llm = llm
)

Investigator = Agent(
  name = "Conor"
  role = "Investigator",
  goal = dedent(
    """
    
    """
  ),
  memory = True,
  verbose = True,
  backstory = dedent(
    """
    
    """
  ),
  tools = [search_tool, web_search_tool],
  llm = llm
)