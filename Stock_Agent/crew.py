import os
from textwrap import dedent

import agentops
from agents import senior_researcher, senior_analyst, senior_advisor
from crewai import Crew, Process
from tasks import research, financial_analysis, filings_analysis, recommend

agentop_api_key = os.environ['AGENTOP_API_KEY']
agentops.init(agentop_api_key)

def run():
  print("## Welcome to Financial Analysis Crew")
  print('-------------------------------')
  company = input(
      dedent("""
        What is the company you want to analyze?
      """))

  crew = Crew(agents=[senior_researcher, senior_analyst, senior_advisor],
              tasks=[research, financial_analysis, filings_analysis, recommend],
              process=Process.sequential
             )

  result = crew.kickoff(inputs={"company": company})
  print(result)

if __name__ == "__main__":
  run()