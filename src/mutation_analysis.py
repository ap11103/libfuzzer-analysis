import networkx as nx
import matplotlib.pyplot as plt

#simulated function that logs input mutations and crashes
def log_mutation(mutation_type, crash_type, parent_mutation=None):
    return {
        "mutation": mutation_type,
        "crash": crash_type,
        "parent": parent_mutation
    }

def visualize_mutation_graph(mutation_log):
    #relationship between mutation and crashes
    G = nx.DiGraph()
    #adding nodes and edges based on mutation logs
    for log in mutation_log:
        G.add_node(log['mutation'], crash=log['crash'])
        if log['parent']:
            G.add_edge(log['parent'], log['mutation'])

    #create a plot of the mutation tree
    pos = nx.spring_layout(G, k=0.5, seed=42)
    labels = nx.get_node_attributes(G, 'crash')

    color_map = {
        "No Crash": 'green',
        "Segmentation Fault": 'red',
        "Memory Corruption": 'orange',
        "Buffer Overflow": 'yellow'
    }
    node_colors = [color_map.get(labels[node], 'gray') for node in G.nodes]
    plt.figure(figsize=(12, 8))

    nx.draw(G, pos, with_labels=True, node_size=5000, node_color=node_colors, font_size=12, font_weight='bold', edge_color='gray', width=2)
    nx.draw_networkx_labels(G, pos, labels, font_size=10, font_color='black')

    plt.title("Fuzzer Input Mutation Analysis")
    plt.show()

def main():
    #example of mutation logs (normally, you'd capture this dynamically during fuzzing)
    mutation_log = [
        log_mutation("Initial Input", "No Crash"),
        log_mutation("Flip Bit", "Segmentation Fault", "Initial Input"),
        log_mutation("Byte Swap", "Memory Corruption", "Flip Bit"),
        log_mutation("Increase Size", "Buffer Overflow", "Byte Swap"),
    ]

    visualize_mutation_graph(mutation_log)

if __name__ == "__main__":
    main()
