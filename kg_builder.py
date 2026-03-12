from llm_interface import LLMInterface

class KnowledgeGraphBuilder:
    def __init__(self, llm_interface: LLMInterface):
        self.llm = llm_interface
        self.triples = set() # Store as unique (subject, predicate, object) tuples

    def process_text(self, text: str):
        print("\n--- Extracting Entities ---")
        entities = self.llm.extract_entities(text)
        print("Found Entities:", entities)

        if not entities:
            print("No entities found. Skipping relation extraction.")
            return

        print("\n--- Extracting Relations ---")
        relations = self.llm.extract_relations(text, entities)
        for r in relations:
            if len(r) == 3: # Ensure it's a valid triple
                self.triples.add(r)
        print("Found Relations (triples):")
        for triple in self.triples:
            print(triple)

    def get_knowledge_graph_triples(self) -> list[tuple[str, str, str]]:
        return list(self.triples)
