#include <bits/stdc++.h>
class Graph {
    // number of vertices
    int V; 
    // adjacency list to vertices
    std::list<int>* adj;

    void DFSUtil(int v, bool visited[]);

    public:
    Graph(int V);
    // add edge, this is vertex and its new vertex
    void addEdge(int v, int w);
    void DFS(int v);

};

Graph::Graph(int V) {
    this->V = V;
    adj = new std::list<int>[V];
}

void Graph::DFSUtil(int v, bool visited[]) {
    // visit
    visited[v] = true;
    std::cout << v << std::endl;

    // recur for adjacent vertices
    for (i = adj[v].begin(); i != adj[v].end(); ++i) {
        
    }
}