# Homework 1 - Agentic RAG

## Overview

This project follows the same approach and implementation style as the classwork completed during the module lessons. It builds a RAG (Retrieval-Augmented Generation) system over the course lesson materials and uses it to answer the homework questions.

## Dependencies

The project uses the following Python packages:

```bash
uv add requests minsearch openai jupyter python-dotenv gitsource
```

## Environment Setup

The project requires an `.env` file containing your OpenAI API key.

Example:

```env
OPENAI_API_KEY=your_api_key_here
```

**Note:** The `.env` file is intentionally excluded from the repository and is not committed to Git.

## Project Files

### `load_doc.py`

Uses `gitsource` to download the lesson Markdown files from the course repository, process them, and build a search index using `minsearch`.

### `rag_helper.py`

A modified version of the RAG helper developed during the module lessons.

Original implementation:
https://github.com/DataTalksClub/llm-zoomcamp/blob/main/01-agentic-rag/code/rag_helper.py

### Notebook

The Jupyter notebook executes the complete workflow required to complete the homework:

* Download and index course materials
* Run retrieval queries
* Generate answers using the RAG pipeline
* Execute the homework tasks

## Running the Project

1. Initialize the project:

```bash
uv init
```

2. Install the required dependencies:

```bash
uv add requests minsearch openai jupyter python-dotenv gitsource
```

3. Start Jupyter Notebook:

```bash
uv run jupyter notebook
```

4. Open the homework notebook and execute the cells in order to reproduce the results and obtain the homework answers.
