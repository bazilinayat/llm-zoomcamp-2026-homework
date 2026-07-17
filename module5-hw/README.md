# Module 5 - Monitoring

## Overview

Module 5 focuses on **monitoring LLM applications in production**.

Up until this point, the course covered the individual building blocks of a modern RAG application—retrieval, vector search, orchestration, and evaluation. This module brings those pieces together into a complete application and introduces the tools needed to observe, monitor, and improve it once users start interacting with it.

Throughout this module, I explored:

* Building an end-to-end RAG application
* Creating a user interface with Streamlit
* Storing conversations and feedback
* Instrumenting LLM calls with traces
* Monitoring application metrics
* Visualizing data using Grafana dashboards

---

## Homework Overview

This directory contains my implementation for **Module 5 - Monitoring**.

The homework extends the RAG application built in previous modules by adding monitoring and observability capabilities, allowing visibility into:

* LLM requests and responses
* Token usage
* Response latency
* Traces and spans
* User interactions
* Application metrics

The notebook and accompanying code demonstrate how these metrics can be collected and inspected to better understand the behavior of an LLM application.

---

## What I Learned

During this module I learned how to:

* Build a simple chat interface using **Streamlit**.
* Instrument an LLM application to collect traces and metrics.
* Monitor requests using **OpenTelemetry** concepts such as traces and spans.
* Visualize application metrics with **Grafana**.
* Understand how monitoring helps identify performance bottlenecks and improve user experience.
* Bring together concepts learned across previous modules into one working application.

---

## Challenges

Although the implementation itself wasn't overly difficult, this module introduced several tools that were completely new to me.

Some of the things I spent time understanding were:

* How Streamlit makes it possible to build interactive applications with very little code.
* How traces and spans represent the execution flow of an LLM application.
* How Grafana dashboards visualize telemetry collected from the application.
* How all the components communicate with one another to provide end-to-end observability.

Seeing everything work together gave me a much better understanding of what a production-ready AI application looks like.

---

## Key Takeaway

This module was one of my favorites because it finally connected many of the concepts introduced throughout the course.

Instead of working with isolated notebooks, I built and monitored a complete application—from the user interface, to the LLM, to the monitoring dashboard.

Two tools that particularly stood out were:

* **Streamlit** – an incredibly simple way to build interactive web applications in Python.
* **Grafana** – a powerful visualization platform that makes monitoring and understanding application behavior much easier.

Monitoring isn't just about collecting metrics—it's about understanding how users interact with your application and having the visibility needed to improve it over time.

---

*This repository is part of my **LLM Zoomcamp 2026** learning journey, where I'm documenting each module while learning in public.*
