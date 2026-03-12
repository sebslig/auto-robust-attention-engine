import sys
from llm_interface import LLMInterface
from kg_builder import KnowledgeGraphBuilder

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"<your text here>\"")
        sys.exit(1)

    text_to_process = sys.argv[1]

    print("Initializing LLM Interface...")
    try:
        llm_interface = LLMInterface()
    except ValueError as e:
        print(f"Error initializing LLM: {e}. Make sure OPENAI_API_KEY is set.")
        sys.exit(1)

    kg_builder = KnowledgeGraphBuilder(llm_interface)

    print(f"\nProcessing text: '{text_to_process}'")
    kg_builder.process_text(text_to_process)

    print("\n--- Final Knowledge Graph Triples ---")
    triples = kg_builder.get_knowledge_graph_triples()
    if triples:
        for s, p, o in triples:
            print(f"({s}, {p}, {o})")
    else:
        print("No triples extracted.")

if __name__ == "__main__":
    main()
