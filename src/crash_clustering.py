from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

def collect_crash_data():    
    #simulated crash data from mutation analysis
    mutation_crash_data = [
        {"mutation": "Initial Input", "stack_trace_hash": 0.9, "memory_address": 0.3},
        {"mutation": "SegFlip Bit Fault", "stack_trace_hash": 0.8, "memory_address": 0.4},
        {"mutation": "Byte Swap", "stack_trace_hash": 0.5, "memory_address": 0.2},
        {"mutation": "Increase Size", "stack_trace_hash": 0.3, "memory_address": 0.6},
        {"mutation": "Buffer Overflow", "stack_trace_hash": 0.7, "memory_address": 0.8},
        {"mutation": "Null Pointer", "stack_trace_hash": 0.6, "memory_address": 0.7},
        {"mutation": "Segmentation Fault", "stack_trace_hash": 0.4, "memory_address": 0.3},
        {"mutation": "Stack Overflow", "stack_trace_hash": 0.2, "memory_address": 0.5},
        {"mutation": "Memory Corruption", "stack_trace_hash": 0.1, "memory_address": 0.9},
        {"mutation": "Integer Overflow", "stack_trace_hash": 0.8, "memory_address": 0.1}
    ]
    #convert crash data into array of features for clustering
    crash_data = np.array([[entry["stack_trace_hash"], entry["memory_address"]] for entry in mutation_crash_data])
    return crash_data

def cluster_crashes(crash_data, num_clusters=3):
    #apply k-means clustering
    kmeans = KMeans(n_clusters=num_clusters)
    clusters = kmeans.fit_predict(crash_data)

    return clusters, kmeans.cluster_centers_

def visualize_crash_clusters(crash_data, clusters, centers):
    #plot the crash clusters with centers highlighted
    plt.scatter(crash_data[:, 0], crash_data[:, 1], c=clusters, cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], marker='x', color='red', s=200, label='Cluster Centers')
    plt.title("Crash Clustering Analysis")
    plt.xlabel("Stack Trace High")
    plt.ylabel("Memory Address")
    plt.legend()
    plt.show()

def main():
    crash_data = collect_crash_data()
    clusters, centers = cluster_crashes(crash_data)
    visualize_crash_clusters(crash_data, clusters, centers)

if __name__ == "__main__":
    main()
