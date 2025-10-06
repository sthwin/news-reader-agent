# News Reader Agent

AI-powered news reader agent using CrewAI for automated news collection, summarization, and curation.

## Features

- **News Collection**: Automated gathering of recent news articles from diverse sources
- **Multi-level Summarization**: Three-tier summary system (headline, executive, comprehensive)
- **Editorial Curation**: Professional news briefing generation

## Getting Started

### Prerequisites

- Python 3.13+
- uv package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/sthwin/news-reader-agent.git
cd news-reader-agent

# Install dependencies
uv sync
```

### Usage

```bash
uv run main.py
```

## Project Structure

```
news-reader-agent/
├── config/
│   ├── agents.yaml      # Agent configurations
│   └── tasks.yaml       # Task definitions
├── main.py              # Main execution file
├── tools.py             # Utility tools
└── pyproject.toml       # Project dependencies
```

## License

MIT License
