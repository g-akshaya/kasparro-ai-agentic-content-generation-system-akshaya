# Multi-Agent Content Generation System (LangGraph)

This project implements a **modular, agent-based content generation system** using **Python** and **LangGraph**.  
It was built as part of the **Applied AI Engineer Internship Challenge** and demonstrates system design, agent orchestration, reusable logic blocks, and machine-readable outputs.

---

## 🎯 Objective

To design an automated multi-agent pipeline that:
- Takes structured product data as input
- Processes it through isolated agents
- Generates three structured JSON pages:
  - FAQ Page
  - Product Description Page
  - Comparison Page

The system emphasizes **engineering design**, not prompt engineering.

---

## 🧠 System Architecture Overview

The system is built using a **LangGraph StateGraph**, where:

- Each node is a **single-responsibility agent**
- A shared typed state flows through the graph
- Agents incrementally enrich the state
- Final outputs are validated using **Pydantic models**

### Agent Flow:
```text
Parser Agent → QA Agent → Content Agent → JSON Outputs
