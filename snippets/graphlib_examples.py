"""
This module covers the graphlib module, which is used to create and manipulate graph-like structures.
"""
import graphlib

# Define your graph. This is a directed graph where the edge direction indicates dependencies.
# For example, "component2" depends on "component1".
dependency_graph = {
    "component1": {"component3"},  # component1 depends on component3
    "component2": {"component1"},  # component2 depends on component1
    "component3": set(),  # component3 has no dependencies
    "component4": {
        "component2",
        "component3",
    },  # component4 depends on component2 and component3
}

# Create a TopologicalSorter object
sorter = graphlib.TopologicalSorter(dependency_graph)

# Perform the topological sort to determine the order of creation
try:
    build_order = list(sorter.static_order())
    print("Build order:", build_order)
except graphlib.CycleError:
    print("A dependency cycle was detected in the graph!")

# Example output: Build order: ['component3', 'component1', 'component2', 'component4']
