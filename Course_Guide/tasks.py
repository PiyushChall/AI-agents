from textwrap import dedent

from crewai import Task
from agents import Researcher, Investigator
from tools import search_tool, web_search_tool

research = Task(
  description = dedent(
    """
    
    """
  ),
  expected_output = dedent(
    """
    
    """
  ),
  tools = [search_tool, web_search_tool],
  agent = Researcher
)

investigate = Task(
  description = dedent(
    """
    
    """
  ),
  expected_output = dedent(
    """

    """
  ),
  tools = [search_tool, web_search_tool],
  agent = Investigator
)