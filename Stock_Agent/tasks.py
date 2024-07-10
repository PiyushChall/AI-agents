from textwrap import dedent

#from langchain_core.language_models.chat_models import agenerate_from_stream

from agents import senior_analyst, senior_advisor, senior_researcher
from crewai import Task
from tools import search_tool, web_search_tool, calculate_pe_ratio


research = Task(
    description = dedent(
        """
        Collect and summarize recent news articles, press
        releases, and market analyses related to the stock and
        its industry.
        Pay special attention to any significant events, market
        sentiments, and analysts' opinions. Also include upcoming 
        events like earnings and others.
        
        Make sure to use the most recent data as possible.

        Selected company by the customer: {company}
        """
    ),
    expected_output=dedent(
        """
        Your final answer MUST be a report that includes a
        comprehensive summary of the latest news, any notable
        shifts in market sentiment, and potential impacts on 
        the stock.
        """
    ),
    agent=senior_researcher,
    tools=[search_tool, web_search_tool]
)

financial_analysis = Task(
    description = dedent(
        """
        Conduct a thorough analysis of the stock's financial
        health and market performance. 
        This includes examining key financial metrics such as
        P/E ratio, EPS growth, revenue trends, and 
        debt-to-equity ratio. 
        Also, analyze the stock's performance of the {company} stock 
        in comparison to its industry peers and overall market trends.
        
        Make sure to use the most recent data possible.

        Selected company by the customer: {company}
        """
    ),
    expected_output=dedent(
        """
        Your final report MUST expand on the summary provided
        but now including a clear assessment of the stock's
        financial standing, its strengths and weaknesses, 
        and how it fares against its competitors in the current
        market.
        """
    ),
    agent=senior_analyst,
    tools=[search_tool, web_search_tool, calculate_pe_ratio]
)

filings_analysis = Task(
    description = dedent(
        """
        Analyze the latest 10-Q and 10-K filings from EDGAR for
        the stock in question. 
        Focus on key sections like Management's Discussion and
        Analysis, financial statements, insider trading activity, 
        and any disclosed risks.
        Extract relevant data and insights that could influence
        the stock's future performance.

        Make sure to use the most recent data possible.

        Selected company by the customer: {company}
        """
    ),
    expected_output=dedent(
        """
        Your final answer must be an expanded report that now
        also highlights significant findings from these filings,
        including any red flags or positive indicators for
        your customer.
        """
    ),
    agent=senior_analyst,
    tools=[search_tool, web_search_tool]
)

recommend = Task(
    description = dedent(
        """
        Review and synthesize the analyses provided by the
        Financial Analyst and the Research Analyst.
        Combine these insights to form a comprehensive
        investment recommendation based on the {company} stock. 
        
        You MUST Consider all aspects, including financial
        health, market sentiment, and qualitative data from
        EDGAR filings.

        Make sure to include a section that shows insider 
        trading activity, and upcoming events like earnings.
        """
    ),
    expected_output=dedent(
        """
        Your final answer MUST be a recommendation for your
        customer. It should be a full super detailed report, providing a 
        clear investment stance and strategy with supporting evidence.
        Make it pretty and well formatted for your customer.
        """
    ),
    agent=senior_advisor,
    tools=[search_tool, web_search_tool]
)