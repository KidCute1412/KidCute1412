<p align="center">
  <img src="./header.svg" width="100%" alt="Le Tuan Loc - GitHub Header" />
</p>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=15&duration=3000&pause=1500&color=00F0FF&center=true&vCenter=true&width=600&lines=LOC%40KIDCUTE1412%3A%7E%24+systemctl+status+backend-engine;Engine+Status%3A+Active+%5BTLS+1.3+%7C+HTTP%2F2%5D;Pessimistic+locking+to+prevent+race+conditions;Distributed+locks+%26+cache+orchestration+via+Redis;High-throughput+async+messaging+via+RabbitMQ;Scaling+real-time+WebSockets+via+Redis+Pub%2FSub;Geospatial+indexing+via+PostGIS+%26+Uber+H3+hexagons" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <img src="./terminal.svg" width="100%" alt="System Architecture Diagram" />
</p>

<p align="center">
  <img src="./skills_telemetry.svg" width="100%" alt="System Core Skills Telemetry" />
</p>

---

## TECHNICAL ARCHITECTURE & SYSTEMS ENGINEERING

A checklist of core backend paradigms and architectural patterns I implement to build resilient, distributed, and high-performance systems:

### Concurrency & Distributed Locking
* ✦ **Race Condition Prevention:** Implemented database-level pessimistic locking (`SELECT FOR UPDATE`) to guarantee transactional isolation during state changes.
* ✦ **Distributed Locks:** Utilized **Redis (Redlock/Redisson)** to orchestrate distributed locking across horizontally-scaled API instances.

### High-Availability WebSockets & Sync
* ✦ **Horizontal Scaling:** Scaled WebSocket nodes using **Redis Pub/Sub Adapter** to synchronize connections and broadcast events across multiple instances.
* ✦ **Resilient Reconnection:** Built connection state recovery to automatically buffer and replay missed events upon reconnection.

### Event-Driven Architecture & Messaging
* ✦ **At-Least-Once Delivery:** Engineered event streams using **RabbitMQ / Kafka** with manual acknowledgements and publisher confirms.
* ✦ **Fault Tolerance:** Implemented **Dead Letter Queues (DLQ)** with exponential backoff retries, and **Idempotency checks** (via Redis tokens) to prevent duplicate processing.

### Multi-Processing & Thread Offloading
* ✦ **CPU-Intensive Task Delegation:** Isolated heavy computations from the main event loop using **Node.js Worker Threads / Child Processes** and **Spring ThreadPoolTaskExecutor**.

### Caching Strategies & Rate Limiting
* ✦ **Cache Patterns:** Applied Cache-Aside pattern using **Redis** with strategic TTLs to minimize database load.
* ✦ **DDoS & API Protection:** Structured sliding-window rate limiters at the gateway and application level utilizing Redis.

### Asynchronous AI Orchestration
* ✦ **Non-Blocking LLM Integration:** Offloaded heavy AI generation/inference requests to background workers using message queues.
* ✦ **Real-time Streaming:** Implemented **Server-Sent Events (SSE)** to stream LLM responses to clients with minimal latency.

### Integration Testing & Reliability
* ✦ **Isolated E2E Testing:** Configured **Testcontainers** (Docker-in-Test) to spin up ephemeral Postgres, Redis, and RabbitMQ instances for deterministic integration testing.
* ✦ **CI/CD Quality Gates:** Maintained high test coverage with automated unit & integration test suites.

### Low-Latency Geospatial Indexing
* ✦ **Spatial Computing:** Indexed coordinates using **Uber H3 Spatial Hexagons** and **PostGIS** for sub-millisecond proximity queries.


---

## TECH STACK & TOOLCHAIN

Comfortable working across these languages, frameworks, databases, and infrastructure tools:

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

## CONNECTIVITY BOARD

Let's discuss system design, backend architectures, or high-performance APIs!

<p align="center">
  <img src="./connectivity_hub.svg" width="100%" alt="Connectivity Hub Ports" />
</p>

---
<p align="center" style="font-size: 11px; color: #4b5563;">
  System Status: Active | Built with ❤️ and high-performance backend pipelines
</p>
