from decimal import Context
from textwrap import dedent

from agents import factFinder, wordWeaver
from crewai import Task
from tools import search_tool, web_search_tool

topic = input("What would you like to research: ")
size = input("What would be the size of the documentation: ")


        
research = Task(description=dedent("""
        Develop a compelling narrative that captures the essence of the {topic}
        considering its potential to disrupt or reshape the {topic} ecosystem.
        Your final report should clearly articulate the key points,
        its market opportunities and potential risks.
        This will be used for documentation purposes. 
        """),
                expected_output=dedent("""
        A comprehensive report/documentaion on the {topic}.
        It would be used as a documentation.
        """),
                tools=[search_tool, web_search_tool],
                agent=factFinder)

#proof_read = Task()

write = Task(description=dedent("""
        Draft a complete research report on {topic}.
        Use creative writing and clear language, formatted as markdown.
        Based on the Senior Researcher's findings, consider its origins,
        key developments, and the human element that drives its evolution.
        Conclude with a compelling analysis of its potential 
        to disrupt or reshape the {topic} ecosystem, 
        highlighting market opportunities and potential risks.
        Then proof read your work properly.
        """),
             expected_output=dedent("""
        Your final output must be the detailed report on the {topic}
        of size {size} and nothing else.
        It should contain a Proper introduction related to the {topic}, 
        a Problem-statement, the objective of the research, 
        Research-Purpose, the research-methodology, the research-results, 
        a null hypothesis, an hypothesis to nullyfy the problem, 
        the research-conclusion, and a reference detail 
        that includes all the links for the website used for the research.
        """),
             tools=[search_tool, web_search_tool],
             agent=wordWeaver,
             Context=research,
             async_execution=False,
             output_file=topic + ".txt")
