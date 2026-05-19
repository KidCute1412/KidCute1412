<p align="center">
  <img src="./header.svg" width="100%" alt="Le Tuan Loc - GitHub Header" />
</p>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=15&duration=3000&pause=1500&color=00F0FF&center=true&vCenter=true&width=600&lines=LOC%40KIDCUTE1412%3A%7E%24+systemctl+status+engineer-profile;System+Status%3A+Active+%5BPORT%3A+8080%5D;Prevents+database+race+conditions+via+SELECT+FOR+UPDATE;Geospatial+indexing+with+Uber+H3+%26+PostGIS;Distributed+message+queues+via+RabbitMQ;Resilient+WebSocket+recovery+via+Socket.io" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <img src="./terminal.svg" width="100%" alt="System Architecture Diagram" />
</p>

---

## ⚡ CORE SYSTEMS CAPABILITIES

What makes me stand out as a backend developer:

*   **🔒 High Concurrency & State Integrity**: Expert in managing complex race conditions during high-volume operations (e.g. concurrent auction bidding) using **Pessimistic Database Locking (`SELECT FOR UPDATE`)** and transactional boundaries.
*   **🗺️ Spatial Indexing & Geospatial Queries**: Designing low-latency mapping and routing systems using **Uber H3 Spatial Hexagonal Indexing**, **PostGIS** geo-queries, and **GraphHopper** path calculations.
*   **⚡ Resilient Real-Time Orchestration**: Building robust bidirectional sync layers using **Socket.io** (with **Connection State Recovery** for network recovery) and **Supabase Realtime**.
*   **📩 Distributed Messaging & Reliability**: Strong understanding of building fault-tolerant architectures using **RabbitMQ** for asynchronous tasks, and applying **Idempotency** patterns to ensure duplicate-free API processing during network retries.
*   **🏗️ Modular Clean Architecture**: Designing loose-coupled backend monoliths using asynchronous messaging paradigms like **Spring ApplicationEvents** to keep core domains independent.

---

## 🛠️ TECH STACK & TOOLCHAIN

Comfortable working across these languages, frameworks, databases, and infrastructure tools:

### 💻 Languages & Core Runtimes
<p align="left">
  <a href="#"><img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBmaWxsPSJ3aGl0ZSI%2BPHBhdGggZD0iTTkuMDI0IDE4Yy0uMjA0IDAtLjMyNC0uMDcyLS4zMjQtLjIxNiAwLS4yMTYuMjI4LS4zMTIuNDQ0LS4zMTJoLjc0NGMuNDggMCAuODA0LS4yNjQuODA0LS43MDggMC0uMy0uMTU2LS41NC0uNTE2LS43NThsLS44NC0uNTI4Yy0uODA0LS41MTYtMS4xMjgtMS4xMjgtMS4xMjgtMS45MiAwLTEuNjQ0IDEuMzQ0LTIuNTggMy4yNTItMi41OCAxLjE1MiAwIDEuOTU2LjMyNCAyLjIyLjQyLS4wNDguMjQtLjA5Ni41MDQtLjE1Ni44NC0uNDY4LS4xNjgtMS4xNC0uNDItMS45NjgtLjQyLTEuMjk2IDAtMi4xMjQuNjEyLTIuMTI0IDEuNTQ4IDAgLjQ2OC4yMjguNzY4LjY0OCAxLjAzMmwuODQuNTI4Yy44NC41MjggMS4xNjQgMS4xODggMS4xNjQgMS45NTYgMCAxLjY5Mi0xLjI4NCAyLjY1Mi0zLjIxNiAyLjY1MnptNi4yNzYtLjA4NGMtLjQ2OCAwLS43NDQtLjE0NC0uNzQ0LS4zNzIgMC0uMzEyLjMzNi0uMzk2LjYxMi0uMzk2aC4zMTJjLjUwNCAwIC43OC0uMzI0Ljc4LS43NDQgMC0uMzQ4LS4xNTYtLjU3Ni0uNTY0LS44MTZsLS44MDQtLjQ5MmMtLjczMi0uNDU2LTEuMDMyLS45OTYtMS4wMzItMS43NCAwLTEuNDg4IDEuMTg4LTIuMzE2IDIuODItMi4zMTYuOTI0IDAgMS41NzIuMjQgMS44MzYuMzI0bC0uMTU2LjgyOGMtLjQwOC0uMTMyLS45NzItLjMxMi0xLjYyLS4zMTItMS4wNDQgMC0xLjcwNC40OTItMS43MDQgMS4zMDggMCAuMzk2LjIwNC42Ni41NzYuODc2bC43OTIuNDkyYy42OTYuNDMyLjk5Ni45NzIgLjk5NiAxLjcwNCAwIDEuNTI0LTEuMTI4IDIuMzc2LTIuNzM2IDIuMzc2em0uNTQtNi44NGMtLjAzNi0uMzEyLS4wNDgtLjU2NC0uMDQ4LS43OTIgMC0uMjUyLjAxMi0uNDguMDM2LS42OTZoLjg4OHYxLjQ4OHptLTMuMDg0IDEwLjkyYy01LjAxNiAwLTYuNzU2LS45OTYtNi43NTYtLjk5NmwuMzk2LS45MjRzMS42NTYuODY0IDYuMTMyLjg2NGM0LjMyIDAgNS42NC0uNzggNS42NC0xLjY1NiAwLS44MDQtLjY5Ni0xLjI2-My44NzYtMS42MDgtNC4yMjQtLjQ2OC02LjE5Mi0xLjI4NC02LjE5Mi0zLjE5MiAwLTIuNDk2LTIuODItMy42NTItNy4wMDgtMy42NTJ6bTEwLjc0LTQuODM2Yy4wMzYuMjY0LjA2LjUzLS4wNi43MThoLjg0Yy4wNDgtLjIyOC4wNi0uNDguMDYtLjcyIDAtLjI3Ni0uMDI0LS41NTItLjA2LS44MjhsLjg1Mi0uMTA4eiIvPjwvc3ZnPg%3D%3D" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/SQL-00758F?style=flat-square&logo=mysql&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white" height="25" /></a>
</p>

### 🚀 Frameworks & Core Libraries
<p align="left">
  <a href="#"><img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=spring&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/React_19-20232A?style=flat-square&logo=react&logoColor=61DAFB" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Socket.io-010101?style=flat-square&logo=socketdotio&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/TailwindCSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/SFML-8CC43C?style=flat-square&logo=sfml&logoColor=white" height="25" /></a>
</p>

### 💾 Databases, Caching & Cloud Infrastructure
<p align="left">
  <a href="#"><img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/PostGIS-339933?style=flat-square&logo=googlemaps&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/RabbitMQ-FF6600?style=flat-square&logo=rabbitmq&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Cloudinary-3448C5?style=flat-square&logo=cloudinary&logoColor=white" height="25" /></a>
</p>

### 🛠️ DevOps, Infrastructure & Tools
<p align="left">
  <a href="#"><img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=FF9900" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Linux_Shell-FCC624?style=flat-square&logo=gnubash&logoColor=black" height="25" /></a>
</p>

---

## 🤝 CONNECTIVITY BOARD

Let's discuss system design, backend architectures, or high-performance APIs!

<p align="left">
  <a href="mailto:letuanloc1412@gmail.com">
    <img src="https://img.shields.io/badge/Email-letuanloc1412%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" height="35" />
  </a>
  <a href="https://www.linkedin.com/in/l%E1%BB%99c-l%C3%AA-tu%E1%BA%A5n-341208390/">
    <img src="https://img.shields.io/badge/LinkedIn-L%E1%BB%99c_L%C3%AA_Tu%E1%BA%A5n-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="35" />
  </a>
  <a href="https://www.facebook.com/le.tuan.loc.39104/?locale=vi_VN">
    <img src="https://img.shields.io/badge/Facebook-L%C3%AA_Tu%E1%BA%A5n_L%E1%BB%99c-1877F2?style=for-the-badge&logo=facebook&logoColor=white" height="35" />
  </a>
  <img src="https://img.shields.io/badge/Location-Ho_Chi_Minh_City-34A853?style=for-the-badge&logo=googlemaps&logoColor=white" height="35" />
</p>

---
<p align="center" style="font-size: 11px; color: #4b5563;">
  System Status: Active | Built with ❤️ and high-performance backend pipelines
</p>
