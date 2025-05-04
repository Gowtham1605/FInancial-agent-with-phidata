FInancial-agent-with-phidata

What This Project Does?
The agent is designed to:
1) Retrieve real-time stock prices, analyst recommendations, company news, and stock fundamentals.
2) Use DuckDuckGo for web-based information retrieval.
3) Present results in a clean, markdown-formatted interface using Phidata’s Playground.

The project includes two agents:

1) A Web Search Agent for general internet queries.
2) A Finance AI Agent focused specifically on financial data analysis.
These are combined in a single interface using the Playground UI for an interactive experience.

Requirements:
1) To run the project, ensure you have the following installed:
2) Python 3.x

Git:
pip (Python package manager)
Required Python libraries (listed in requirements.txt)

A .env file with your API key:

PHI_API_KEY for Phidata

GROQ_API_KEY for the Groq model (used in agents)

🚀 How to Run the Project:

Ensure all dependencies are installed using:
pip install -r requirements.txt

Create a .env file in the root directory with your API keys:

Add PHI_API_KEY=your_key_here

Add GROQ_API_KEY=your_key_here

Run the main script. This will:

Load your environment variables

Initialize both agents (financial and web)

Launch the Playground app on your local server

Open your browser and interact with the agents directly through the user interface.

Project Structure:
main.py – Contains agent definitions and the Playground launch script
.env – Stores environment variables (not committed to Git)
requirements.txt – Lists all dependencies needed to run the project

Why I Built This?
This project helps me understand how to architect multi-agent systems using real-world data sources and integrate them into a usable interface. I’m especially interested in how autonomous tools like this could evolve in finance and enterprise AI solutions.

