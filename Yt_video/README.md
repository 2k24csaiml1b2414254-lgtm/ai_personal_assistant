# Agentic Agno

A collection of AI agents built with the [Agno](https://github.com/agno-agi/agno) framework, powered by Groq and OpenAI models.

## Agents

| File | Description |
|------|-------------|
| `agent.py` | Travel agent that answers safety/travel questions using DuckDuckGo search |
| `finance.py` | Investment analyst that fetches stock prices, fundamentals, and analyst recommendations |
| `memory.py` | Conversational agent with persistent user memory backed by SQLite |
| `team.py` | Multi-language team that answers queries in English, Chinese, and Hindi simultaneously |
| `youtube_analyzer.py` | YouTube content analyst that generates timestamps and summaries from video URLs |
| `ui.py` | Streamlit web UI for the YouTube analyzer |

## Setup

1. Clone the repo and install dependencies:
   ```bash
   pip install agno streamlit python-dotenv yfinance
   ```

2. Copy `.env.example` to `.env` and fill in your API keys:
   ```bash
   cp .env.example .env
   ```

## Running

```bash
# Travel agent
python agent.py

# Finance analyst
python finance.py

# Memory agent
python memory.py

# Multi-language team
python team.py

# YouTube analyzer (CLI)
python youtube_analyzer.py

# YouTube analyzer (Web UI)
streamlit run ui.py
```
