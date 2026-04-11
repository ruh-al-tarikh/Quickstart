# ⚡ QuickStart — A Minimal Python Dev Scaffold

**Fast to start. Clean by design. Built to scale.**

QuickStart is a lightweight, no-friction Python foundation for developers who want to move from idea → execution without getting buried in setup. It provides just enough structure to stay organized while remaining flexible enough for experimentation, automation, and production-ready systems.

Whether you're building workflows, CLI utilities, or reusable libraries, QuickStart keeps your codebase sharp, modular, and maintainable.

---

## 🚀 What You Can Build

* Orchestrated workflows with Prefect
* Command-line tools with clear structure
* Reusable Python packages
* Automation pipelines and internal tooling

---

## 🧠 Design Philosophy

QuickStart follows three core principles:

* **Clarity over clutter** → Every file has a reason to exist
* **Modularity first** → Components are reusable and composable
* **Separation of concerns** → Logic, interfaces, and execution are cleanly divided

This makes it ideal for both learning modern Python architecture and shipping real-world systems efficiently.

---

## ⚙️ Setup

```bash
# 1. Clone the repository
git clone <your-repo-url>

# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# 3. Install dependencies (editable mode)
pip install -e .

# 4. Run the starter example
python 01_getting_started.py
```

---

## 📁 Project Layout

```
.
├── 01_getting_started.py   # Intro Prefect flow
├── 02_logging.py           # Logging + stdout capture
├── pyproject.toml          # Dependencies & metadata
└── README.md               # Documentation
```

---

## ▶️ Usage

Run examples directly:

```bash
python 01_getting_started.py
python 02_logging.py
```

---

## 🧪 Development Workflow

Maintain code quality with:

```bash
black .
ruff check .
mypy .
```

---

## 🔄 Example: Prefect Flow

```python
from prefect import flow, task

@task
def step():
    return "processed"

@flow
def pipeline():
    return step()
```

Run it:

```bash
python 01_getting_started.py
```

---

## 📦 Packaging

Install locally for development:

```bash
pip install -e .
```

---

## ✅ Included Best Practices

* Testing-ready structure
* Linting (ruff)
* Formatting (black)
* Type checking (mypy)
* Build-friendly configuration

---

## 🔀 Contribution Flow

```
fork → branch → commit → pull request → merge
```

---

## 📄 License

MIT License

---

## 🧩 Final Note

QuickStart is more than a template—it’s a disciplined baseline for building clean, scalable Python systems without unnecessary overhead. Start simple, stay organized, and grow without friction.
