## 1. Problem Statement

The objective is to design a modular agentic system capable of transforming raw, unstructured product data into structured, machine-readable content pages. Traditional single-prompt LLM wrappers are insufficient for production environments because they lack modularity, are difficult to debug, and fail to provide the granular control needed for complex content generation. This project implements a sophisticated **Multi-Agent Orchestration System** to automate the creation of FAQs, Product Pages, and Comparison Pages with high reliability.

## 2. Solution Overview

The solution utilizes an **Agentic State Machine** architecture built on **LangGraph**. Instead of a monolithic script, the system is decomposed into specialized agents with distinct responsibilities:

* 
**Structured Parsing:** An agent dedicated to creating a clean "Internal Model" from raw text.


* 
**Synthetic Brainstorming:** An agent focused on generating 15 categorized user questions (Informational, Safety, etc.).


* 
**Template Assembly:** A final agent that uses "Logic Blocks" to fill JSON templates for three unique pages.



## 3. Scopes & Assumptions

* 
**Data Constraint:** The system strictly adheres to the provided dataset for the primary product (GlowBoost). No external research or hallucinations are permitted.


* 
**Fictional Data Generation:** For comparison purposes, the system is scoped to autonomously generate a fictional "Product B" with a similar structure to Product A.


* 
**Technical Stack:** The architecture assumes a graph-based orchestration (DAG or State Machine) to handle message passing and state updates.


* 
**Output Requirement:** Every page generated is strictly valid, machine-readable JSON.



## 4. System Design (Mandatory)

### A. Architectural Design: Directed Acyclic Graph (DAG)

The system follows a sequential pipeline where data flows through nodes. Each node represents an AI Agent or a Logic Block.

### B. Agent Definitions & Boundaries

Each agent in the system follows the principle of **Single Responsibility**:

1. **Parser Agent:** (Input: Raw String  Output: JSON Schema). Normalizes the "GlowBoost" data into a Python dictionary.


2. **QA Generator Agent:** (Input: Schema  Output: List). Analyzes the internal model to brainstorm 15 questions across five categories.


3. **Assembly Agent:** (Input: List + Schema  Output: Final Pages). This agent acts as the orchestrator for the **Template Engine**.



### C. Reusable Logic Blocks

The system avoids hard-coded content. Instead, it uses **Logic Blocks**—reusable functions that apply specific rules to data:

* 
`generate-benefits-block`: Transforms the "Benefits" field into descriptive marketing copy.


* 
`extract-usage-block`: Parses "How to Use" text into a step-by-step list.


* 
`compare-ingredients-block`: Compares GlowBoost ingredients against Product B to identify key differences.



### D. Template Engine

The Template Engine defines the "blueprint" for each page. It specifies:

* 
**Fields:** Which data points are required.


* 
**Rules:** Formatting requirements (e.g., minimum 5 Q&As).


* 
**Dependencies:** Which Logic Blocks are required to populate specific fields.



### E. Data Flow Sequence

1. **Start:** Raw data is fed into the `State`.
2. **Node 1 (Parser):** State is updated with `product_model`.
3. **Node 2 (QA Gen):** State is updated with `categorized_questions`.
4. **Node 3 (Assembly):** The `Content Writer` pulls from Logic Blocks to generate `faq.json`, `product_page.json`, and `comparison_page.json`.
5. **End:** The system returns a final, validated State object.

---
