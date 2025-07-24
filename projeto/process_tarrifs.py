import json
# Ensure both Reporter and Partner are considered as nodes
HIGH_TARIFF_THRESHOLD = 20

low_nodes = set()
high_nodes = set()
low_edges = set()
high_edges = set()

data = json.load(open("./wits_tarrifs.json", "r"))

for entry in data:
    print(entry)

    if entry["AverageAppliedTariff"] == 0.0:
        continue

    if entry["AverageAppliedTariff"] < HIGH_TARIFF_THRESHOLD:
        low_nodes.add(entry['Reporter'])
        low_nodes.add(entry['Partner'])
        low_edges.add((entry['Reporter'], entry['Partner']))
    else:
        high_nodes.add(entry['Reporter'])
        high_nodes.add(entry['Partner'])
        high_edges.add((entry['Reporter'], entry['Partner']))

open('high_tarrifs.json', '+w').write(json.dumps({
    "name": "HighTarrifs",
    "nodes": [{"id": c} for c in high_nodes],
    "edges": [{"first_node": c[0], "second_node": c[1]} for c in high_edges],
}))

open('low_tarrifs.json', '+w').write(json.dumps({
    "name": "LowTarrifs",
    "nodes": [{"id": c} for c in low_nodes],
    "edges": [{"first_node": c[0], "second_node": c[1]} for c in low_edges],
}))