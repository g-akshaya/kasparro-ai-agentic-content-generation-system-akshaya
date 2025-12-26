# Project Documentation  
## Multi-Agent Content Generation System

---

## 1. Problem Statement

Digital platforms increasingly depend on structured content such as FAQs, product descriptions, and comparison pages. Creating and maintaining this content manually is time-consuming, difficult to scale, and prone to inconsistencies across products and platforms.

The challenge addressed in this project is to design an automated system that can transform a small, structured product dataset into multiple high-quality, machine-readable content pages. The solution must demonstrate strong engineering practices including modularity, deterministic execution, and clear separation of responsibilities.

This project focuses on **system architecture and automation design**, rather than domain expertise or user interface development.

---

## 2. Solution Overview

This project implements a **multi-agent content generation system** using **Python** and **LangGraph**. The system is architected as an agent-driven pipeline in which autonomous agents collaborate through a shared state.

Each agent contributes a specific transformation:
- structuring raw product data,
- generating categorized user questions,
- assembling validated content pages using reusable logic blocks and templates.

The system autonomously produces three structured JSON outputs:
- FAQ Page  
- Product Description Page  
- Comparison Page  

All outputs are validated to ensure consistency and machine readability.

---

## 3. Scope and Assumptions

### Scope
- Operates strictly on the provided product dataset.
- Uses deterministic, rule-based logic.
- Generates structured JSON outputs.
- Introduces a fictional product solely for comparison purposes.

### Assumptions
- No external APIs or data sources are used.
- No additional facts beyond the given dataset are introduced.
- The system is designed as a backend automation pipeline.
- Execution flow is linear and non-cyclic.

Frontend rendering, real-time user interaction, and external knowledge enrichment are intentionally out of scope.

---

## 4. System Design (Core Section)

### 4.1 Architectural Philosophy

The system is designed around a **Directed Acyclic Graph (DAG)** implemented using LangGraph’s `StateGraph`. A shared, typed state object flows through the graph and is incrementally enriched by specialized agents.

This architecture ensures:
- clear separation of concerns,
- predictable execution,
- ease of extension,
- strong testability.

Each agent operates independently, without hidden dependencies or global state.

---

### 4.2 High-Level System Architecture

+----------------------+
|  Raw Product Input   |
+----------------------+
            |
            v
+----------------------+
|   Parser Agent       |
| (Data Structuring)   |
+----------------------+
            |
            v
+----------------------+
|   QA Agent           |
| (Question Generation)|
+----------------------+
            |
            v
+----------------------+
|   Content Agent      |
| - Logic Blocks       |
| - Templates          |
| - Validation         |
+----------------------+
            |
            v
+-----------------------------+
|   Structured JSON Outputs   |
| - FAQ Page                  |
| - Product Page              |
| - Comparison Page           |
+-----------------------------+
This architecture provides a clear, traceable transformation path from input to output.

4.3 Shared State Flow
A typed shared state acts as the system’s single source of truth. As it moves through the graph, the state evolves through successive stages:


Raw Input
   ↓
Structured Product Data
   ↓
Generated Questions
   ↓
Final Content Pages
Each agent appends information without mutating unrelated data, enabling loose coupling and deterministic execution.

4.4 Agent Responsibilities
Parser Agent
Converts raw input into a clean, structured internal representation.

Question Generation Agent
Produces categorized user questions independent of formatting or output structure.

Content Assembly Agent
Applies templates and reusable logic blocks to generate validated content pages.

Each agent adheres strictly to the single-responsibility principle.

4.5 Reusable Logic Blocks and Templates
Logic blocks are stateless, reusable functions that encapsulate transformation rules such as:

usage extraction,

ingredient comparison,

price comparison.

Templates define the structure and required fields for each content page, binding structured data and logic outputs into finalized JSON documents.

4.6 Output Validation
All generated pages are validated using strict schema definitions to ensure:

structural correctness,

consistent data types,

machine-readable outputs suitable for downstream systems.

5. Execution Flowchart

Start
  |
  v
Parse Product Data
  |
  v
Generate Categorized Questions
  |
  v
Apply Logic Blocks
  |
  v
Bind Templates
  |
  v
Validate JSON Output
  |
  v
End