<div align="center">

# 🚨 DIGITAL FUGITIVE 🚨
**[ SYSTEM CLASSIFICATION: ACTIVE PURSUIT ]**

<br>

> *"In the grid, there is nowhere to hide. Only paths yet to be calculated."*

<br>

[![Python](https://img.shields.io/badge/Engine-Python_3.x-00599C?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pygame](https://img.shields.io/badge/Render-PyGame-F6D220?style=for-the-badge&logo=python&logoColor=black)](https://pygame.org)
[![AI](https://img.shields.io/badge/Logic-Stochastic_Agents-FF0055?style=for-the-badge&logo=smartthings&logoColor=white)]()

<br>
</div>

<hr>

### 🎨 00. SYSTEM ANIMATION SOURCE CODE

<details>
<summary><b>[ ACCESS CUSTOM SVG ANIMATION CODE ]</b></summary>
<i>GitHub blocks inline SVGs for security, but you can save the code below as <code>chase_animation.svg</code> locally and open it in any web browser to view the dynamic pursuit simulation.</i>

```xml
<svg width="800" height="300" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)">
  <style>
    .background { fill: #0d1117; }
    .grid { stroke: #30363d; stroke-width: 1; }
    .radar-spin { transform-origin: 400px 150px; animation: spin 3s linear infinite; }
    .police { fill: #00ffff; animation: blink 1s infinite, police-search 6s infinite alternate ease-in-out; }
    .thief { fill: #ff0055; animation: evade 6s infinite alternate ease-in-out; }
    .heat-ring { fill: none; stroke: #ff0055; stroke-width: 1; animation: pulse 2s infinite ease-out; }
    @keyframes spin { 100% { transform: rotate(360deg); } }
    @keyframes blink { 50% { opacity: 0.5; } }
    @keyframes pulse { 0% { r: 5; opacity: 1; } 100% { r: 40; opacity: 0; } }
    @keyframes evade { 0% { cx: 600; cy: 100; } 50% { cx: 650; cy: 220; } 100% { cx: 500; cy: 80; } }
    @keyframes police-search { 0% { cx: 400; cy: 150; } 50% { cx: 480; cy: 180; } 100% { cx: 520; cy: 100; } }
  </style>
  <rect width="100%" height="100%" class="background" rx="10"/>
  <pattern id="gridPattern" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M 40 0 L 0 0 0 40" fill="none" class="grid"/>
  </pattern>
  <rect width="100%" height="100%" fill="url(#gridPattern)"/>
  <circle cx="400" cy="150" r="140" stroke="#00ff00" stroke-width="2" fill="none" opacity="0.2"/>
  <circle cx="400" cy="150" r="90" stroke="#00ff00" stroke-width="2" fill="none" opacity="0.2"/>
  <circle cx="400" cy="150" r="40" stroke="#00ff00" stroke-width="2" fill="none" opacity="0.2"/>
  <path class="radar-spin" d="M400,150 L400,10 A140,140 0 0,1 540,150 Z" fill="rgba(0, 255, 0, 0.15)"/>
  <circle r="8" class="police"/>
  <circle r="6" class="police" style="animation-delay: 1s;"/>
  <circle r="8" class="thief"/>
  <circle class="heat-ring" style="animation: evade 6s infinite alternate ease-in-out, pulse 2s infinite ease-out;"/>
  <text x="20" y="30" fill="#c9d1d9" font-family="monospace" font-size="14" font-weight="bold">SYSTEM LOGS</text>
  <text x="20" y="55" fill="#00ffff" font-family="monospace" font-size="12">> STOCHASTIC AGENTS: DEPLOYED</text>
  <text x="20" y="75" fill="#00ff00" font-family="monospace" font-size="12">> HOT/COLD RADAR: ACTIVE</text>
  <text x="20" y="95" fill="#ff0055" font-family="monospace" font-size="12">> TARGET HEAT SIGNATURE DETECTED</text>
</svg>** 📡 01. MISSION BRIEFING**

**Digital Fugitive** is a high-octane AI simulation engineered to visualize search paradigms and autonomous agent logic. Operating within a constrained digital grid, stochastic "Police" agents must 
dynamically calculate paths, interpret heat signatures, and corner an evasive "Fugitive" entity.

It is an exploration of probabilistic reasoning, real-time pathfinding, and algorithmic efficiency.

**🧠 02. SYSTEM ARCHITECTURE (AI LOGIC)**

_The pursuit operates on a continuous feedback loop between the hunters and the hunted._

Code snippet

graph TD;

A\[Fugitive Agent\] -->|Calculates Evasion| B(Terrain Grid)

B -->|Generates Heat Signature| C{Hot/Cold Radar}

C -->|Proximity Data| D\[Police Agents\]

D -->|Stochastic Sweep| E\[Adjust Pursuit Path\]

E --> B

style A fill:#ff0055,stroke:#333,stroke-width:2px,color:#fff

style D fill:#00ffff,stroke:#333,stroke-width:2px,color:#000

style C fill:#00ff00,stroke:#333,stroke-width:2px,color:#000

**⚙️ 03. TACTICAL CAPABILITIES**

**🔵 The Hunters (Police)**

- **Stochastic Pathfinding:** Agents do not rely on hardcoded routes; they use probabilistic algorithms to dynamically adapt to the fugitive's movements.
- **Hot/Cold Radar System _(Final Review Implementation)_:** A proximity-based tracking mechanic. The grid dynamically registers "heat", allowing agents to triangulate the fugitive's general vector even without direct line-of-sight.

**🔴 The Hunted (Fugitive)**

- **Dynamic Evasion:** Actively scans the grid to chart escape routes, maximizing distance from the nearest pursuit agent while avoiding dead ends.

**🏔️ The Environment**

- **Variable Terrain _(Final Review Implementation)_:** The grid is not flat. Complex terrain introduces varied movement penalties and obstacles, heavily taxing the pathfinding capabilities of both AI entities.

**💻 04. DEPLOYMENT PROTOCOL**

**ENVIRONMENT SETUP:**

Bash

\# 1. Clone the repository to your local mainframe

git clone \[<https://github.com/sooriya-moorthy-0107/Digital-Fugitive.git\>](<https://github.com/sooriya-moorthy-0107/Digital-Fugitive.git>)

\# 2. Access the directory

cd Digital-Fugitive

\# 3. Initialize virtual environment (Recommended)

python -m venv venv

\# Windows: venv\\Scripts\\activate | Mac/Linux: source venv/bin/activate

\# 4. Install dependencies

pip install pygame

\# 5. Execute simulation

python main.py

**🗄️ 05. AUTHORIZATION & CREDENTIALS**

**Lead Architect:** Sooriya Moorthy

**Affiliation:** Integrated M.Tech Software Engineering, VIT Vellore

**GitHub Terminal:** [@sooriya-moorthy-0107](https://www.google.com/search?q=https://github.com/sooriya-moorthy-0107)

**END OF FILE** | _If this simulation assisted your research, acknowledge by starring (⭐) the repository._# 🚨 Digital Fugitive 

<div align="center">
  <!-- You can replace this URL with any specific high-res GIF of your actual gameplay later -->
  <img src="https://media.giphy.com/media/3o7aD2saalEvTe8O3u/giphy.gif" alt="Cyberpunk AI Chase Animation" width="600" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.5);"/>
  <br/>
  <p><i>A Python-based simulation visualizing AI search paradigms and stochastic agents.</i></p>
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pygame-Simulation-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Pygame">
  <img src="https://img.shields.io/badge/AI-Search_Paradigms-ff69b4?style=for-the-badge&logo=probot&logoColor=white" alt="AI">
</div>

## 📖 Overview

**Digital Fugitive** is an interactive simulation built to explore and visualize AI search paradigms. Developed using Python and Pygame, the project creates a dynamic environment where intelligent "Police" agents hunt down an evasive "Thief" (the fugitive). The simulation emphasizes real-time pathfinding, probabilistic reasoning, and algorithmic efficiency in a constrained digital space.

## ✨ Key Features

* **🤖 Stochastic Search Agents**: The pursuit agents are powered by stochastic algorithms, utilizing probabilistic decision-making to sweep the map and outmaneuver the fugitive.
* **🏃 Dynamic Evasion Logic**: The fugitive agent actively analyzes the environment to chart escape routes and avoid immediate capture.
* **📡 Hot and Cold Radar System (Final Review)**: Designed specifically for the final review build, this proximity-based tracking mechanic allows search agents to detect the fugitive's general direction based on "heat" signatures.
* **🏔️ Terrain Systems (Final Review)**: A complex grid environment implemented for the final review, introducing obstacles and varying movement costs that challenge the pathfinding capabilities of both the police and the thief.

## 🛠️ Tech Stack

* **Programming Language**: Python
* **Rendering Engine**: Pygame
* **Core Logic**: Stochastic Algorithms, Autonomous Agents, Pathfinding Math

## 🚀 Installation & Setup

Follow these steps to run the simulation on your local machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sooriya-moorthy-0107/Digital-Fugitive.git](https://github.com/sooriya-moorthy-0107/Digital-Fugitive.git)
   cd Digital-Fugitive
