🚦 Intelligent Traffic Route Finder

📌 Project Overview

This project is an AI-based system that finds the shortest and most optimal route between two locations using the A (A-Star) search algorithm*. It simulates a traffic network using graph data structures and heuristic-based pathfinding.

🎯 Problem Statement

Traffic congestion is a common real-world problem that causes delays, fuel wastage, and inefficiency. Choosing the best route manually is difficult when multiple paths exist. This project aims to solve this problem using Artificial Intelligence techniques.


🧠 Solution Approach

The system models the traffic network as a graph:

Nodes → Locations

Edges → Roads

Weights → Distance

The A* algorithm is used to find the optimal path by combining:

g(n) → Actual distance from start

h(n) → Estimated distance to goal (heuristic)

f(n) = g(n) + h(n)


⚙️ Features

Finds shortest path between two locations

Uses A* search algorithm (AI concept)

Graph-based traffic simulation

Simple command-line interface

Efficient and optimized routing


🛠️ Technologies Used

Python

Data Structures (Graph)

A* Search Algorithm


📂 Project Structure


traffic-route-ai/

│── main.py

│── a_star.py

│── graph.py

│── utils.py

│── requirements.txt


▶️ How to Run the Project

Install Python (3.x)

Download or clone this repository

Open terminal in project folder

Run the program:

python main.py

Enter start and destination locations when prompted


📊 Example Output

Enter start location: A

Enter destination: E

✅ Shortest Path Found:

A -> C -> E

Total Distance: 5


🧠 Concepts Covered

Artificial Intelligence (AI)

A* Search Algorithm

Graph Representation

Heuristic Functions


📚 Learning Outcomes

Learned how to implement A* algorithm

Understood graph-based problem solving

Applied AI concepts to real-world scenario


🚀 Future Scope

Real-time traffic data integration

GUI (Graphical Interface)

Map visualization (like Google Maps)


👩‍🎓 Author

Name: Archita Singh Registration No: 25BAI11553 Course: Fundamentals in AIML


