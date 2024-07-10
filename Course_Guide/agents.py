from textwrap import dedent

from crewai import Agent
from tools import llm, search_tool, web_search_tool

Researcher = Agent(
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