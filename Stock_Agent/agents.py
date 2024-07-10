import os
from textwrap import dedent

from crewai import Agent


from langchain_google_genai import ChatGoogleGenerativeAI
from tools import calculate_pe_ratio, search_tool, web_search_tool

google_api_key = os.environ['GOOGLE_API_KEY']
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=google_api_key,
)


senior_analyst = Agent(
  role="Senior Financial Analyst",
  goal=dedent("""Impress all customers with your indepth financial data 
      and market trends analysis, including key metrics like P/E Ratio, 
      Earnings Growth Rate, and Return on Equity."""),
  verbose=True,
  memory=True,
  backstory=dedent("""
      The most seasoned financial analyst with 
      expertise of 15+years in stock market analysis and investment
      strategies.
      you work for a super important customer.
      And try to give your best efforts.
      """),
  tools=[search_tool, web_search_tool, calculate_pe_ratio],
  llm=llm,
  allow_delegation=True)

senior_researcher = Agent(
  role="Senior Researcher",
  goal=dedent("""
  Being the best at gather and interpret data, 
  amaze your customer with it
  """),
  verbose=True,
  memory=True,
  backstory=dedent("""
      Known as the BEST research analyst in the entire universe, 
      you're skilled in sifting through news, 
      company announcements, and market sentiments. 
      Now you're working for a super important customer.
      """),
  tools=[search_tool, web_search_tool],
  llm=llm,
  allow_delegation=True)

senior_advisor = Agent(
  role="Private Investment Advisor",
  goal=dedent("""Impress your customers with full analyses over stocks
      and complete investment recommendations"""),
  verbose=True,
  memory=True,
  backstory=dedent("""
      You're the most experienced investment advisor
      and you combine various analytical insights to formulate
      strategic investment advice. You are now working for
      a super important customer you need to impress.
      """),
  tools=[search_tool, web_search_tool],
  llm=llm,
  allow_delegation=True)
