import csv
import json

def trades_to_graph(csv_path, graph_name, flow_type):
    nodes = set()
    edges = set()

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row.get('Flow') and row['Flow'].strip() == flow_type:
                source_id = row['Reporter country'].strip()
                dest_id = row['Partner country'].strip()
                if source_id and dest_id:
                    nodes.add(source_id)
                    nodes.add(dest_id)
                    edges.add((source_id, dest_id))

    graph = {
        "nodes": [{"id": node} for node in nodes],
        "edges": [{"first_node": edge[0], "second_node": edge[1]} for edge in edges],
        "name": graph_name
    }

    return graph

if __name__ == "__main__":
    csv_file = "Trades.csv"

    imports_graph = trades_to_graph(csv_file, "TradeGraph_Imports", "Imports")
    exports_graph = trades_to_graph(csv_file, "TradeGraph_Exports", "Exports")

    with open("trade_graph_imports.json", "w", encoding="utf-8") as f:
        json.dump(imports_graph, f, ensure_ascii=False, indent=2)

    with open("trade_graph_exports.json", "w", encoding="utf-8") as f:
        json.dump(exports_graph, f, ensure_ascii=False, indent=2)
