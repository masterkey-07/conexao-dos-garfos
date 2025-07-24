import pandas as pd
import json

def trades_to_balance_graph(csv_path, graph_name, balance_type):
    # Read CSV with pandas
    df = pd.read_csv(csv_path)

    # Group by Reporter country, Partner country, and Flow, summing OBS_VALUE
    grouped = df.groupby(['Reporter country', 'Partner country', 'Flow'])['OBS_VALUE'].sum().reset_index()

    # Pivot to get Imports and Exports side by side
    pivot = grouped.pivot_table(index=['Reporter country', 'Partner country'],
                                columns='Flow',
                                values='OBS_VALUE',
                                fill_value=0).reset_index()

    nodes = set()
    edges = set()

    for _, row in pivot.iterrows():
        reporter = str(row['Reporter country']).strip()
        partner = str(row['Partner country']).strip()

        imports = row['Imports'] if 'Imports' in pivot.columns else 0
        exports = row['Exports'] if 'Exports' in pivot.columns else 0
        balance = exports - imports

        # Surplus: exports > imports, Deficit: imports > exports
        if balance_type == 'surplus' and balance > 0:
            nodes.add(reporter)
            nodes.add(partner)
            edges.add((reporter, partner))
        elif balance_type == 'deficit' and balance < 0:
            nodes.add(reporter)
            nodes.add(partner)
            edges.add((reporter, partner))

    graph = {
        "nodes": [{"id": node} for node in nodes],
        "edges": [{"first_node": edge[0], "second_node": edge[1]} for edge in edges],
        "name": graph_name
    }

    return graph

if __name__ == "__main__":
    csv_file = "Trades.csv"

    surplus_graph = trades_to_balance_graph(csv_file, "TradeGraph_Surplus", "surplus")
    deficit_graph = trades_to_balance_graph(csv_file, "TradeGraph_Deficit", "deficit")

    with open("trade_graph_surplus.json", "w", encoding="utf-8") as f:
        json.dump(surplus_graph, f, ensure_ascii=False, indent=2)

    with open("trade_graph_deficit.json", "w", encoding="utf-8") as f:
        json.dump(deficit_graph, f, ensure_ascii=False, indent=2)