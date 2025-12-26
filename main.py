from langgraph.graph import StateGraph
from state import ContentState
from agents.parser_agent import parser_agent
from agents.qa_agent import qa_agent
from agents.content_agent import content_agent
import json

graph = StateGraph(ContentState)

graph.add_node("parser", parser_agent)
graph.add_node("qa", qa_agent)
graph.add_node("content", content_agent)

graph.set_entry_point("parser")
graph.add_edge("parser", "qa")
graph.add_edge("qa", "content")
graph.set_finish_point("content")

app = graph.compile()

final_state = app.invoke({"raw_input": "GlowBoost raw data"})

with open("outputs/faq.json", "w") as f:
    json.dump(final_state["faq_page"], f, indent=2)

with open("outputs/product_page.json", "w") as f:
    json.dump(final_state["product_page"], f, indent=2)

with open("outputs/comparison_page.json", "w") as f:
    json.dump(final_state["comparison_page"], f, indent=2)
