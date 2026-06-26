# Module 2 - Vector Search

## Overview

Module 2 explores one of the most important components of modern Retrieval-Augmented Generation (RAG) systems: **Vector Search**.

Rather than treating embeddings and vector databases as black boxes, this module walks through how semantic search works internally by generating embeddings, calculating vector similarity, and implementing search algorithms from scratch.

## What I Learned

During this module I learned how to:

* Generate text embeddings using a lightweight ONNX model.
* Build vector search from scratch using NumPy.
* Understand the difference between keyword search and semantic search.
* Implement hybrid search using Reciprocal Rank Fusion (RRF).
* Improve retrieval using document chunking.
* Understand how embeddings enable similarity-based retrieval.

## Beyond the Course

Before starting this module, I realized I was missing some of the fundamentals behind vectors and embeddings.

To strengthen my understanding, I also completed an additional course dedicated to:

* Vector Databases
* Embeddings
* Tokenization
* Similarity Search
* ChromaDB
* Google Gemini Embeddings

That extra learning made many of the concepts in this module much easier to understand when implementing them myself.

## Challenges

This module was definitely more challenging than Module 1.

Some concepts that took me extra time to understand were:

* How the ONNX embedding model actually converts text into vectors.
* How SQLite fits into the retrieval pipeline before introducing semantic search.
* Connecting all the pieces—from embeddings, to indexing, to similarity search—into one complete workflow.

Working through these challenges helped me understand what happens "behind the scenes" instead of simply calling a library.

## Homework

The implementation for this homework can be found in this directory.

## Key Takeaway

My biggest takeaway from this module is that **vector search isn't magic**.

At its core, it is a combination of embeddings, mathematical similarity, indexing, and efficient retrieval that enables LLM applications to search based on meaning instead of exact keywords.

Understanding these fundamentals makes modern RAG systems much less of a black box.

---

*This repository is part of my LLM Zoomcamp 2026 learning journey, where I'm documenting each module while learning in public.*
