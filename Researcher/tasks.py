from textwrap import dedent

from agents import factFinder, wordWeaver
from crewai import Task
from tools import search_tool, web_search_tool

research = Task(
    description=dedent(
        """
        Develop a compelling narrative that captures the essence of the {topic}
        considering its potential to disrupt or reshape the {topic} ecosystem.
        Your final report should clearly articulate the key points,
        its market opportunities and potential risks.
        This will be used for documentation purposes. 
        """
    ),
    expected_output=dedent(
        """
        A comprehensive report/documentaion on the {topic}.
        It would be used as a documentation.
        """
    ),
    tools=[search_tool, web_search_tool],
    agent=factFinder
)

#proof_read = Task()

write = Task(
    description=dedent(
        """
        Draft a complete research reprt on {topic}.
        Use creative writing and clear language, formatted as markdown.
        Based on the Senior Researcher's findings, consider its origins,
        key developments, and the human element that drives its evolution.
        Conclude with a compelling analysis of its potential 
        to disrupt or reshape the {topic} ecosystem, 
        highlighting market opportunities and potential risks.
        Then proof read your work properly.
        """
    ),
    expected_output=dedent(
        """
        Your final output must be the detailed report on the {topic}
        of size {size} and nothing else.
        """
    ),
    tools=[search_tool, web_search_tool],
    agent=wordWeaver,
    async_execution=False,
    output_file="Research.txt"
)
