<p align="center">
  <img src="./header.svg?v=2" width="100%" alt="Le Tuan Loc - GitHub Header" />
</p>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=15&duration=3000&pause=1500&color=00F0FF&center=true&vCenter=true&width=600&lines=LOC%40KIDCUTE1412%3A%7E%24+systemctl+status+backend-engine;Engine+Status%3A+Active+%5BTLS+1.3+%7C+HTTP%2F2%5D;Pessimistic+locking+to+prevent+race+conditions;Distributed+locks+%26+cache+orchestration+via+Redis;High-throughput+async+messaging+via+RabbitMQ;Scaling+real-time+WebSockets+via+Redis+Pub%2FSub;Geospatial+indexing+via+PostGIS+%26+Uber+H3+hexagons" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=KidCute1412&color=00F0FF&style=for-the-badge&label=PROFILE+VIEWS" alt="Profile Views" />
</p>

## ABOUT ME

Computer Science student at **VNUHCM University of Science** with a focus on backend and full-stack engineering.

I build transaction-safe APIs, event-driven workflows, real-time systems, and data-intensive applications with TypeScript, Node.js, PostgreSQL, Redis, and Kafka. I am particularly interested in concurrency control, system reliability, asynchronous processing, and practical system design.

---

## FEATURED PROJECTS

### Backend & Distributed Systems

| Project | Technologies | Highlights |
| :--- | :--- | :--- |
| [**Miracle Auction Platform**](https://github.com/KidCute1412/miracle-auction-platform) | `TypeScript` `PostgreSQL` `Redis` `Kafka` `Socket.IO` | Real-time auction platform with concurrency-safe bidding, ordered event projection, transactional outbox delivery, reconnect recovery, and operational diagnostics. |
| [**Mutux**](https://github.com/KidCute1412/startup-k23-hcmus) | `TypeScript` `NestJS` `PostgreSQL` `Next.js` | Five-person gaming-gear rental project. Served as Backend Head and contributed to authentication, KYC, credit workflows, transactional finance, catalog search, testing, and deployment. |
| [**UniHub**](https://github.com/Luke23127006/UniHub) | `JavaScript` `System Design` | University platform designed around high-concurrency registration, dispute handling, traffic spikes, asynchronous AI processing, and offline QR check-in. |

### AI & Applied Systems

| Project | Technologies | Highlights |
| :--- | :--- | :--- |
| [**HypeRoom**](https://github.com/KidCute1412/VietnameseHackAIthon2026-SocialMedia) | `Python` `FastAPI` `Redis/RQ` `React` `WebSocket` | AI-assisted newsroom workflow for evidence retrieval, claim analysis, risk reporting, and editorial support. Qualified for Round 2 of the Vietnamese Student HackAIthon 2026. |
| [**AidBridge**](https://github.com/phatnguyen975/AidBridge/tree/feature/backend) | `Java` `Spring Boot` `PostGIS` `Uber H3` | Disaster-relief coordination system using geospatial indexing, route-aware volunteer dispatch, real-time tracking, and retryable mission workflows. |

### Software Engineering & Game Development

| Project | Technologies | Highlights |
| :--- | :--- | :--- |
| [**Mario-Reflourished**](https://github.com/Luke23127006/Mario-Reflourished) | `C++` `SFML` `OOP` | Game project focused on refactoring gameplay code, improving object-oriented structure, and organizing rendering and game-state logic. |


---

## SYSTEM ARCHITECTURE DIAGRAM AND TELEMETRY

<p align="center">
  <img src="./terminal.svg" width="100%" alt="System Architecture Diagram" />
</p>

---

## CORE STRENGTHS

Key capabilities demonstrated across my projects:

- **Backend & Data:** Transaction-safe APIs, PostgreSQL, Redis, search, and concurrency control.
- **Event-Driven Systems:** Redis Streams, Kafka, transactional outbox, workers, retries, and idempotency.
- **Real-Time Applications:** WebSocket/Socket.IO synchronization and reconnect recovery.
- **Security & Quality:** Authentication, CSRF, RBAC, rate limiting, integration testing, Docker, and CI/CD.
- **Applied Systems:** PostGIS, Uber H3, route-aware dispatch, and real-time tracking.

### ✦ In-Memory Atomic Authority & Concurrency Control
* **Atomic Lua Mutations:** Used **Redis Lua Scripts (`EVALSHA`)** to atomically validate bidding windows, anti-sniping extensions, proxy bid increments, and balance checks.
* **Synchronous Replica Acknowledgment:** Used `WAIT 1` replica acknowledgments in the benchmarked bid path to improve write durability before responding.
* **Pessimistic & Distributed Locking:** Applied database-level `SELECT FOR UPDATE` and **Redis distributed locks (Redlock/Redisson)** for cross-instance coordination and transactional state isolation.

### ✦ Event Streaming & Ordered Durable Projection
* **Append-Only Stream Ingestion:** Logged mutation events into **Redis Streams** as an ordered durable commit log, decoupling high-throughput ingest from disk I/O.
* **Idempotent Single Projector:** Designed background workers (`auction-worker`) consuming streams with sequence fencing and per-entity sequence counters to project authoritative state into **PostgreSQL** without duplication or reordering.

### ✦ Dual-Write Elimination & Messaging (Transactional Outbox)
* **Transactional Outbox Pattern:** Eliminated dual-write hazards by storing outbound domain events directly inside PostgreSQL transactional boundaries.
* **Asynchronous Outbox Relay:** Built dedicated polling/leasing relays to stream committed events to **Apache Kafka** with aggregate partition keys for guaranteed partition ordering.
* **Fault Tolerance & DLQ:** Configured **Dead Letter Queues (DLQ)** with exponential backoff retries and consumer idempotency fences.

### ✦ Post-Commit Real-Time Synchronization
* **Post-Commit WebSocket Broadcast:** Broadcasted live state updates via **Socket.IO (Redis Pub/Sub Adapter)** after PostgreSQL projection commits.
* **Connection State Recovery:** Implemented heartbeat telemetry, room partitioning, and event buffering for seamless reconnection and state reconciliation.

### ✦ Modular Monolith & Process Isolation
* **Multi-Process Architecture:** Structured backends with decoupled composition roots (`API Process`, `Projector Worker`, `Outbox Relay`, `Async Worker`) sharing core domain contracts while isolating HTTP ingress latency from background tasks.
* **Thread & CPU Offloading:** Isolated heavy computations and background workers from the main event loop using **Node.js Worker Threads** and **Spring ThreadPoolTaskExecutor**.

### ✦ API Defense, Security & Caching
* **Defense-in-Depth Protection:** Structured sliding-window rate limiters via Redis, strict CORS, CSRF token validation, Helmet headers, and RBAC permissions.
* **End-to-End Traceability:** Injected `X-Request-ID` correlation tokens across the HTTP gateway, database transactions, Kafka events, and structured logs.
* **Cache-Aside & Strategic Invalidation:** Optimized reads using Redis cache layers with strategic TTLs to minimize database load.

### ✦ Deterministic Testing & Performance Benchmarking
* **Containerized Integration Testing:** Configured **Testcontainers** (Docker-in-Test) to orchestrate ephemeral PostgreSQL, Redis primary/replica, and Kafka clusters for deterministic CI/CD pipelines.
* **Concurrency & Load Profiling:** Measured throughput and latency under concurrent traffic using **k6 load test suites**.

### ✦ Low-Latency Geospatial Indexing
* **Spatial Computing:** Used **Uber H3 Spatial Hexagons** and **PostGIS** for geospatial indexing and proximity queries.

---

## TECH STACK

Primary technologies used across my projects:

### Languages & Core Runtimes
<p align="left">
  <a href="#"><img src="./java.svg" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/SQL-00758F?style=flat-square&logo=mysql&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black" height="25" /></a>
</p>

### Frameworks & Core Libraries
<p align="left">
  <a href="#"><img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=spring&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/NestJS-E0234E?style=flat-square&logo=nestjs&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/React_19-20232A?style=flat-square&logo=react&logoColor=61DAFB" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Socket.io-010101?style=flat-square&logo=socketdotio&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/TailwindCSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/SFML-8CC43C?style=flat-square&logo=sfml&logoColor=white" height="25" /></a>
</p>

### Databases, Caching & Cloud Infrastructure
<p align="left">
  <a href="#"><img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Oracle-F80000?style=flat-square&logo=oracle&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/PostGIS-339933?style=flat-square&logo=googlemaps&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/RabbitMQ-FF6600?style=flat-square&logo=rabbitmq&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Apache_Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Cloudinary-3448C5?style=flat-square&logo=cloudinary&logoColor=white" height="25" /></a>
</p>

### DevOps, Infrastructure & Tools
<p align="left">
  <a href="#"><img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=FF9900" height="25" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Linux_Shell-FCC624?style=flat-square&logo=gnubash&logoColor=black" height="25" /></a>
</p>

---

## GITHUB TELEMETRY & SYSTEM ANALYTICS

<p align="center">
  <a href="https://github.com/KidCute1412">
    <img src="https://github-readme-stats.shion.dev/api?username=KidCute1412&show_icons=true&theme=tokyonight&bg_color=06080c&title_color=00F0FF&icon_color=00F0FF&text_color=ffffff&border_color=ff007b&count_private=true" height="195" alt="GitHub Stats" />
  </a>
  <a href="https://github.com/KidCute1412">
    <img src="./profile-summary-card-output/tokyonight/2-most-commit-language.svg" height="195" alt="Top Languages by Commit" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/KidCute1412">
    <img src="./github-streak-stats.svg" height="195" alt="GitHub Streak Stats" />
  </a>
  <a href="https://github.com/KidCute1412">
    <img src="./profile-summary-card-output/tokyonight/4-productive-time.svg" height="195" alt="Productive Time Telemetry" />
  </a>
</p>

---

## CONNECTIVITY BOARD

Let's discuss system design, backend architectures, or high-performance APIs!

<p align="center">
  <img src="./connectivity_hub.svg" width="100%" alt="Connectivity Hub Ports" />
</p>

<p align="center">
  <a href="mailto:letuanloc1412@gmail.com">
    <img src="https://img.shields.io/badge/Email-00F0FF?style=for-the-badge&logo=gmail&logoColor=black" alt="Email" />
  </a>
  <a href="https://www.linkedin.com/in/loc-le-tuan/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://www.facebook.com/le.tuan.loc.39104/">
    <img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook" />
  </a>
</p>

---

## 🐍 CONTRIBUTION MATRIX ANIMATION

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/KidCute1412/KidCute1412/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/KidCute1412/KidCute1412/output/github-contribution-grid-snake-light.svg">
    <img alt="Snake Contribution Animation" src="https://raw.githubusercontent.com/KidCute1412/KidCute1412/output/github-contribution-grid-snake-dark.svg">
  </picture>
</p>

---

## ⚡ DEV QUOTE & MOTTO

<p align="center">
  <img src="https://readme-daily-quotes.vercel.app/api?theme=tokyonight&authorColor=00F0FF&quoteColor=ffffff" alt="Daily Dev Quote" />
</p>

---

<!-- System Operational Status Banner -->
<p align="center">
  <img src="https://img.shields.io/badge/System_Status-Active-00ffaa?style=flat-square&logo=statuspage&logoColor=black" alt="System Status" />
  <img src="https://img.shields.io/badge/Uptime-99.99%25-00f0ff?style=flat-square&logo=uptime&logoColor=black" alt="System Uptime" />
</p>

<p align="center" style="font-size: 11px; color: #4b5563; font-family: monospace;">
  ⚡ System Status: Active | Built with passion and high-performance backend pipelines
</p>
