# Module 3 - AI Orchestration with Kestra

## Overview

Module 3 introduces **AI Orchestration** using **Kestra**, an open-source workflow orchestration platform that enables developers to build reliable, repeatable, and observable AI workflows.

As LLM applications become more sophisticated, a single prompt is often not enough. Real-world systems require multiple steps such as data ingestion, retrieval, prompt construction, LLM calls, validation, retries, logging, and scheduling. Kestra provides a way to orchestrate these tasks into well-defined workflows.

Throughout this module, I explored:

* AI workflows and orchestration fundamentals
* Building workflows using Kestra
* Context Engineering
* Retrieval-Augmented Generation (RAG) inside workflows
* Prompt engineering and token usage
* When to use AI agents versus traditional task-based workflows

## Homework Answers

### Question 1 - Context Engineering

**Question**

After trying the same prompt in ChatGPT vs Kestra AI Copilot, what is the primary reason AI Copilot generates better Kestra flows?

**Answer**

> ✅ AI Copilot has access to current Kestra plugin documentation

**Explanation**

Kestra AI Copilot augments the language model with the latest Kestra plugin documentation, enabling it to generate workflows using the correct tasks, syntax, and configuration instead of relying solely on the model's pre-trained knowledge.

---

### Question 2 - RAG vs No RAG

**Question**

The non-RAG response about Kestra 1.1 features is best described as:

**Answer**

> ✅ Vague, generic, or fabricated — the model guesses from training data

**Explanation**

Without Retrieval-Augmented Generation (RAG), the model does not have access to the latest product documentation. Instead, it relies only on what it learned during training, which can result in generic or inaccurate responses.

---

### Question 3 - Token Usage (Short Summary)

**Expected Answer**

> ✅ 60–100 tokens

**Actual Output**

> **71 tokens**

---

### Question 4 - Token Usage (Long Summary)

**Expected Answer**

> ✅ 2–5× more tokens

**Actual Output**

> **182 tokens**

---

### Question 5 - Prompt Length

**Expected Answer**

> ✅ 2–4× more

**Actual Output**

* One sentence: **34 tokens**
* Three sentences: **88 tokens**

This demonstrates how additional instructions significantly increase the prompt size, which directly affects token usage and inference cost.

---

### Question 6 - Agents vs Traditional Workflows

**Question**

When should traditional task-based workflows be preferred?

**Answer**

> ✅ Use traditional task-based workflows for predictability and auditability.

**Explanation**

Traditional workflows are deterministic and follow predefined execution paths, making them easier to debug, monitor, test, and audit. AI agents are more flexible and adaptive but introduce non-deterministic behavior, making them better suited for open-ended reasoning tasks rather than highly regulated or repeatable business processes.

---

## Key Takeaways

This module shifted my perspective from simply calling an LLM to thinking about how complete AI systems are built.

Some of my biggest learnings were:

* AI applications require orchestration, not just prompts.
* Context engineering is just as important as prompt engineering.
* RAG enables models to answer questions using up-to-date information instead of relying only on training data.
* Token usage has a direct impact on latency and cost.
* AI agents are powerful, but deterministic workflows remain the better choice when reliability and traceability are essential.

