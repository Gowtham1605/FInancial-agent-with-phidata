from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
from os import getenv
from dotenv import load_dotenv


load_dotenv()

## web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tools_calls=True,
    markdown=True,

)

## Financial agent - agentic ai
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,

)

multi_ai_agent = Agent(
    name='A Stock Market Agent',
    role='A comprehensive assistant specializing in stock market analysis by combining financial insights with real-time web searches to deliver accurate, up-to-date information',
    model=Groq(api_key=getenv('GROQ_API_KEY')),
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)


multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for Nvidia.",stream=True)
