# 🚨 URGENT: Abduction in Progress!

Professor Charlie Eppes needs your help! A few minutes ago, robbers have stolen the last computer science book from a bookstore in College Station. Apparently, a cashier witnessed the crime and the desperate robbers abducted her! Time is of the essence!

Professor Eppes used Google Maps to monitor the traffic conditions at the time of the crime (see next page). He annotated 22 potential waypoints shown as:

1, 2, ..., 22

The robbers were last seen at (1).

Professor Amita Ramanujan is giving a talk at a conference and cannot be reached. So here is what Professor Eppes wants you to do.

Form a graph with vertices from 1 to 22. There is an edge between two nodes if and only if there is a road directly connecting them. For example, include the edges (1,11) and (1,2). There is no edge (1,3) as another waypoint is in between the nodes 1 and 3. If there is no direct road segment connecting waypoints, then there is no edge. For instance, 4 is incident with 3 and 5, but not with 7, 8, or 22.

If the road segment between two nodes is entirely green, then the edge has weight 1. If any part of the road is orange (in either direction) and the rest green, then the edge gets weight 2. For example, the edge (1,11) has weight 1. The edges (11,12) and (5,6) have weight 2.

Professor Eppes wants you to create the graph and run Dijkstra’s algorithm with 1 as the source node. He suspects that the robbers leave town. The local police knows that the robbers likely will pass through the destinations:

6, 8, 9, 15, 16, or 22

The FBI and the police do not have enough personnel to put up roadblocks at all of them. Determine the distances of each of the six locations from node 1. The lower weight paths are more likely to be taken by the robbers.

Unfortunately, Charlie Eppes cannot be reached for questions. So use common sense, solve it, and write up your solution in detail and include it in your homework submission. This needs to include the entire graph with weighted edges. You do not need to draw it, but you need to specify the edges and their weights. You need to explain how your implementation of Dijkstra’s algorithm finds the shortest path to the most likely of the six destinations. Give all the details here.

Include the source code of your implementation of Dijkstra’s algorithm. [Of course, this example is short, so you could have implemented it by hand. However, this would not be possible when more waypoints would be used.]

---

## Problem 4 (40 points)

Help Professor Charlie Eppes find the most likely escape routes of thieves that robbed a bookstore on Texas Avenue in College Station. The map will be published on Thursday evening. In preparation, you might want to implement Dijkstra’s single-source shortest path algorithm, so that you can join the manhunt on Thursday evening. Include your implementation of Dijkstra’s algorithm and explain all details of your choice of the min-priority queue.

**[Edge weight 1 means very desirable street, weight 2 means less desirable street.]**
