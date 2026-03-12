# LLM Knowledge Graph Builder

This project provides a basic framework for building a knowledge graph by extracting entities and relations from unstructured text using Large Language Models (LLMs).

## Features

- Entity extraction using a placeholder LLM function.
- Relation extraction using a placeholder LLM function.
- Basic knowledge graph representation (triples).

## Setup

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your LLM API key (e.g., in an environment variable `OPENAI_API_KEY`).

## Usage

```bash
python main.py "Your unstructured text goes here to be processed by the LLM."
```

## Project Structure

- `main.py`: Main script to run the extraction process.
- `kg_builder.py`: Contains the core logic for entity and relation extraction.
- `llm_interface.py`: Abstraction layer for interacting with LLMs.
- `requirements.txt`: Project dependencies.

## Future Enhancements

- Integrate with actual LLM APIs (OpenAI, Hugging Face).
- Implement advanced prompting techniques.
- Add a proper knowledge graph storage (e.g., Neo4j, RDF).
- Develop a UI for visualization.