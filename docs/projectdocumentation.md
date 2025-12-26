## 1. Problem Statement

The objective of this project is to design a **modular, agentic system** capable of transforming raw or semi-structured product data into structured, machine-readable content pages.

Traditional single-prompt or monolithic LLM wrappers are insufficient for production environments because they:
- lack modularity,
- are difficult to debug and extend,
- provide limited control over intermediate reasoning and transformations.

To address these limitations, this project implements a **Multi-Agent Orchestration System** that automates the generation of:
- FAQ Pages,
- Product Description Pages,
- Comparison Pages,

while maintaining high reliability, deterministic behavior, and clean separation of concerns.

---

## 2. Solution Overview

The solution is built using an **Agentic State Machine architecture** powered by **LangGraph**.  
Instead of a single script, the system is decomposed into multiple specialized agents, each responsible for a clearly defined task.

The system is organized around the following agent roles:

- **Structured Parsing**  
  A dedicated agent converts raw input into a clean, normalized internal data model.

- **Synthetic Brainstorming**  
  A question-generation agent analyzes the internal model to produce **15 categorized user questions** (e.g., Informational, Safety, Usage).

- **Template Assembly**  
  A final assembly agent applies reusable **Logic Blocks** and fills predefined JSON templates to generate three distinct content pages.

This approach ensures modularity, extensibility, and production-readiness.

---

## 3. Scope & Assumptions

- **Data Constraint**  
  The system strictly adheres to the provided dataset for the primary product (GlowBoost). No external research, enrichment, or hallucinated facts are permitted.

- **Fictional Data Generation**  
  For comparison purposes, the system is scoped to autonomously generate a fictional **Product B**, structured similarly to the primary product.

- **Technical Stack Assumption**  
  The architecture assumes a graph-based orchestration model (Directed Acyclic Graph or State Machine) for message passing and state updates.

- **Output Requirement**  
  All generated pages must be strictly valid, machine-readable JSON suitable for downstream systems.

---

## 4. System Design (Mandatory)

### A. Architectural Design: Directed Acyclic Graph (DAG)

The system follows a **sequential DAG-based pipeline** in which data flows through a series of nodes.  
Each node represents either:
- an AI Agent, or
- a reusable Logic Block.

The flow is linear, deterministic, and non-cyclic, ensuring predictable execution.

---

### B. Agent Definitions & Boundaries

Each agent adheres to the **Single Responsibility Principle**, with clearly defined inputs and outputs.

1. **Parser Agent**  
   - **Input:** Raw product string  
   - **Output:** Normalized JSON schema  
   - **Responsibility:** Converts raw GlowBoost data into a structured Python dictionary.

2. **QA Generator Agent**  
   - **Input:** Structured product schema  
   - **Output:** Categorized question list  
   - **Responsibility:** Generates 15 user questions across predefined categories.

3. **Assembly Agent**  
   - **Input:** Product schema + question list  
   - **Output:** Final content pages  
   - **Responsibility:** Acts as the orchestrator for the Template Engine and content assembly.

---

### C. Reusable Logic Blocks

To avoid hard-coded content, the system relies on **Logic Blocks**—stateless, reusable functions that apply deterministic rules to data.

Key logic blocks include:

- `generate-benefits-block`  
  Transforms the raw “Benefits” field into descriptive, structured copy.

- `extract-usage-block`  
  Parses “How to Use” text into step-by-step usage instructions.

- `compare-ingredients-block`  
  Compares GlowBoost ingredients with Product B to highlight key differences.

These blocks are independent of agents and can be reused across pipelines.

---

### D. Template Engine

The Template Engine defines the structural blueprint for each generated page.  
Each template specifies:

- **Fields:** Required data points for the page  
- **Rules:** Constraints such as minimum FAQ count  
- **Dependencies:** Logic Blocks required to populate specific sections  

This separation ensures consistency and flexibility across content types.

---

### E. Data Flow Sequence

1. **Start:** Raw product data is injected into the shared `State`.
2. **Node 1 – Parser Agent:** State is updated with `product_model`.
3. **Node 2 – QA Generator Agent:** State is enriched with `categorized_questions`.
4. **Node 3 – Assembly Agent:** Logic Blocks and templates are applied to generate:
   - `faq.json`
   - `product_page.json`
   - `comparison_page.json`
5. **End:** The system returns a final, fully validated State object containing all outputs.

---

