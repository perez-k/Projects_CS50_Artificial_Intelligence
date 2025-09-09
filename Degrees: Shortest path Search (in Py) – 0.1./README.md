
# Degrees – CS50 AI (Search)
- Actor Connection Degrees: Shortest Path Search 

---

## Description  
A Python program that determines the shortest path between two actors by linking them through the movies they have appeared in together.  \
Uses data from the IMDb database (provided in CSV format) and models the problem as a graph, where actors are connected via shared movies. \
It is a search problem where the **states** are people, the **actions** are movies, which take us from one actor to another. Our initial state and goal state are defined by the two people we’re trying to connect. By using **breadth-first search**, we can find the shortest path from one actor to another. \
The output is the smallest number of connections, "degrees of separation" between the two chosen actors.


---

### **Key CS/AI Concepts**
- **Graph representation**: actors as nodes, shared movies as edges.  
- **Breadth-First Search (BFS)** for shortest path in an unweighted graph.  
**Queue-based frontier** for systematic exploration of neighbors.  
- **Optimization of search algorithms** to guarantee the minimal connection path.
- **Data parsing** and preprocessing from CSV into Python dictionaries.  


---

### **Example Output**

<video src="images/Video_Demo/cs50ai_p0a_degrees.mp4" controls width="600"></video>

```
[![Watch the video](/images/Certificat_CS50AI.png)](/images/Video_Demo/cs50ai_p0a_degrees.mp4)





<video src="https://github.com/AI-Health-Master/Projects_CS50_Artificial_Intelligence/blob/main/images/Video_Demo/cs50ai_p0a_degrees.mp4" controls width="600"></video>

![Watch the video](https://github.com/AI-Health-Master/Projects_CS50_Artificial_Intelligence/raw/refs/heads/main/images/Video_Demo/cs50ai_p0a_degrees.mp4)

[![Watch the video](https://raw.githubusercontent.com/AI-Health-Master/Projects_CS50_Artificial_Intelligence/images/Certificat_CS50AI.png)](https://github.com/AI-Health-Master/Projects_CS50_Artificial_Intelligence/raw/refs/heads/main/images/Video_Demo/cs50ai_p0a_degrees.mp4)

[![Watch the video](https://github.com/AI-Health-Master/Projects_CS50_Artificial_Intelligence/tree/main/images/Certificat_CS50AI.png)](https://github.com/AI-Health-Master/Projects_CS50_Artificial_Intelligence/raw/refs/heads/main/images/Video_Demo/cs50ai_p0a_degrees.mp4)

<p align="center">
  <img src="assets/logo.png" width="200" alt="Logo">
</p>

<details>
  <summary>Click to expand</summary>
  <p>This text is hidden until clicked.</p>
</details>

<video src="assets/demo.mp4" controls width="600"></video>

---


