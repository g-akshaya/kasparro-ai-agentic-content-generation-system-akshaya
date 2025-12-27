# Multi-Agent Content Generation System (LangGraph)

This project implements a **modular, agent-based content generation system** using **Python** and **LangGraph**.  
It was built as part of the **Applied AI Engineer Internship Challenge** and demonstrates system design, agent orchestration, reusable logic blocks, and machine-readable outputs.

---

## 🎯 Objective

To design an automated multi-agent pipeline that:
-To finalize your **Applied AI Engineer** internship submission, here is a professional `README.md` file. It is designed to be clear, instructional, and impressive to a technical recruiter.

# Multi-Agent Content Generation System

This project is a modular, agentic automation system designed to transform raw product data into structured, machine-readable JSON pages. It utilizes **LangGraph** to orchestrate a multi-agent workflow where specialized agents handle data parsing, question generation, and content assembly.

---

## 🚀 Quick Start

### 1. Prerequisites

* **Python 3.10+**
* A virtual environment (recommended)

### 2. Installation

Clone the repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com/your-username/kasparro-ai-agentic-content-generation-system-akshaya.git
cd kasparro-ai-agentic-content-generation-system-akshaya

# Install dependencies
pip install -U langgraph pydantic

```

### 3. Running the Pipeline

The system can be executed via the main entry point, which triggers the orchestration graph and saves the outputs to the `outputs/` directory:

```bash
python main.py ; echo "Content generated successfully" 
```

---

## 🏗️ System Architecture

The system is built as a **State Machine** where a shared state object is passed between nodes:

* **Parser Agent:** Normalizes raw input into a clean internal model.
* **QA Agent:** Brainstorms 15 categorized questions based on product facts.
* **Content Agent:** Assembles the final pages using **Logic Blocks** and **Pydantic Schemas** for strict data validation.

---

## 📂 Project Structure

* **`main.py`**: The orchestration brain that compiles and invokes the LangGraph.
* **`state.py`**: Defines the `TypedDict` used for state management.
* **`models.py`**: Contains Pydantic models for machine-readable JSON validation.
* **`agents/`**: Contains specialized agent logic for parsing, QA, and content writing.
* **`blocks/`**: Modular logic functions for reusable data transformations.
* **`outputs/`**: Final generated JSON files (`faq.json`, `product_page.json`, `comparison_page.json`).

---

## 🧪 Testing the System

You can verify the output by checking the generated files in the `outputs/` folder.
```python
# To see a text-based version of your graph
python -c "from main import app; print(app.get_graph().draw_ascii())"

```

---

## 📖 Documentation

Detailed engineering design decisions, assumptions, and system abstractions can be found in [docs/projectdocumentation.md](https://www.google.com/search?q=./docs/projectdocumentation.md).


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
