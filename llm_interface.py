import os
from dotenv import load_dotenv
from langchain.llms import OpenAI

load_dotenv()

class LLMInterface:
    def __init__(self, model_name="text-davinci-003", temperature=0.0):
        # For a real project, you'd handle different LLM providers
        # and potentially more sophisticated model loading.
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        self.llm = OpenAI(model_name=model_name, temperature=temperature, openai_api_key=openai_api_key)

    def extract_entities(self, text: str) -> list[str]:
        # This is a placeholder. Real implementation would use careful prompting.
        prompt = f"Extract all named entities (people, organizations, locations, events) from the following text:\n\nText: {text}\nEntities:"
        response = self.llm.invoke(prompt)
        return [e.strip() for e in response.split(',') if e.strip()]

    def extract_relations(self, text: str, entities: list[str]) -> list[tuple[str, str, str]]:
        # This is a placeholder. Real implementation would use careful prompting.
        # Format: (subject, predicate, object)
        prompt = f"Given the text and entities, extract factual relationships as (subject, predicate, object) triples.\n\nText: {text}\nEntities: {', '.join(entities)}\nRelationships:"
        response = self.llm.invoke(prompt)
        # Dummy parsing for demonstration
        triples = []
        for line in response.split('\n'):
            parts = line.strip('() ').split(', ')
            if len(parts) == 3:
                triples.append(tuple(p.strip() for p in parts))
        return triples
