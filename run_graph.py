from elements.edges import Project_Graph

graph = Project_Graph()
config = {"configurable": {"thread_id": "1"}}

with open("graph_output.png", "wb") as f:
    f.write(graph.get_graph().draw_mermaid_png())

if __name__ == "__main__":
    while True:
        try:
            graph.invoke({"start_input": ""}, config=config)
        except Exception as e:
            print(f"Error {e}")
            break
