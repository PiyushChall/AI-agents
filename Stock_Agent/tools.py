import os


from langchain.tools import tool
from crewai_tools import SerperDevTool, WebsiteSearchTool

serper_api_key = os.environ['SERPER_API_KEY']
search_tool = SerperDevTool()

web_search_tool = WebsiteSearchTool(
    config=dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini-1.5-flash",
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
            ),
        ),
    )
)

@tool("Make a calculation")
def calculate_pe_ratio(stock_price, earnings_per_share):
  """Calculates the Price-to-Earnings Ratio (P/E Ratio) for a stock.

  Args:
      stock_price (float): Current price of the stock.
      earnings_per_share (float): Earnings per share of the stock.

  Returns:
      float: The calculated P/E Ratio.
  """
  if earnings_per_share == 0:
    return None  # Handle division by zero
  return stock_price / earnings_per_share
