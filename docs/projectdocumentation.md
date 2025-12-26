# Project Documentation  
## Multi-Agent Content Generation System

---

## 1. Problem Statement

Modern digital platforms require large volumes of structured, consistent, and machine-readable content such as FAQs, product descriptions, and comparison pages. Manually creating and maintaining this content is time-consuming, error-prone, and difficult to scale.

The challenge is to design an automated system that can take a small, structured product dataset and autonomously generate multiple high-quality content pages while maintaining:
- clear separation of responsibilities,
- deterministic and reusable logic,
- and machine-readable outputs suitable for downstream systems.

This project focuses on **system design and automation**, not domain expertise or UI development.

---

## 2. Solution Overview

The proposed solution is a **multi-agent content generation system** built using **Python** and **LangGraph**. The system is architected as an **agentic pipeline**, where each agent has a single responsibility and operates over a shared typed state.

The system:
- Parses raw product data into a clean internal representation
- Automatically generates categorized user questions
- Applies reusable logic blocks and templates
- Produces three structured JSON pages:
  - FAQ Page
  - Product Page
  - Comparison Page

All outputs are validated using **Pydantic models** to ensure consistency and machine readability.

---

## 3. Scope and Assumptions

### Scope
- The system operates on a predefined product dataset.
- Content generation is deterministic and rule-based.
- Outputs are generated as structured JSON files.
- A fictional product is introduced only for comparison purposes.

### Assumptions
- No external data sources or APIs are used.
- No additional facts beyond the provided dataset are introduced.
- The system is intended for backend automation, not UI rendering.
- The orchestration flow is linear and non-cyclic.

Out-of-scope items include frontend development, real-time user interaction, and external knowledge enrichment.

---

## 4. System Design (Core Section)

### 4.1 Architectural Approach

The system is designed as a **Directed Acyclic Graph (DAG)** using LangGraph’s `StateGraph`. A shared typed state object flows through the graph, progressively enriched by independent agents.

Each agent:
- Reads only the required fields from the state
- Writes its output back to the state
- Does not maintain hidden or global state

This design ensures modularity, extensibility, and testability.

---

### 4.2 Shared State Model

A typed state acts as a shared memory structure across agents.  
It incrementally accumulates:
- parsed product data,
- generated questions,
- finalized content pages.

This approach enables loose coupling between agents while maintaining deterministic execution.

---

### 4.3 Agent Responsibilities

The system consists of three core agents:

**Parser Agent**
- Converts raw input into a structured internal data model
- Ensures data cleanliness and consistency

**QA Agent**
- Generates categorized user questions
- Operates independently of content formatting or logic

**Content Agent**
- Applies templates and reusable logic blocks
- Assembles final content pages
- Validates outputs using Pydantic schemas

Each agent has a single responsibility and a clearly defined input/output contract.

---

### 4.4 Logic Blocks

Logic blocks are reusable, stateless functions that encapsulate transformation rules.  
Examples include:
- Usage extraction logic
- Ingredient comparison logic
- Price comparison logic

These blocks are independent of agents and can be reused across different pipelines or templates, promoting composability and maintainability.

---

### 4.5 Template-Driven Content Generation

Templates define the structure of each content page, including:
- required fields,
- formatting rules,
- dependencies on logic blocks.

The Content Agent binds structured data and logic block outputs into these templates to produce final JSON pages.

---

### 4.6 Output Validation

All final outputs are validated using **Pydantic models**, ensuring:
- schema correctness,
- consistent field types,
- machine-readable JSON output.

This guarantees reliability for downstream consumption by APIs, databases, or frontend systems.

---

## 5. Optional Diagrams (Conceptual)

### High-Level Flow
```text
Raw Input
   ↓
Parser Agent
   ↓
QA Agent
   ↓
Content Agent
   ↓
Validated JSON Outputs
