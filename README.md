# genpark-chaitin-briggs-graph-coloring-allocator-skill

[![CI](https://github.com/alphaparkinc/genpark-chaitin-briggs-graph-coloring-allocator-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/alphaparkinc/genpark-chaitin-briggs-graph-coloring-allocator-skill/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> Chaitin-Briggs graph coloring register allocator constructing interference matrices, Kempe node simplifications, and register assignments.

## Architecture

```mermaid
flowchart TD
    Client[AI Agent / Language Frontend] -->|Source Tokens / IR| Engine[genpark-chaitin-briggs-graph-coloring-allocator-skill]
    Engine --> CompilerPass[AST / Type Inference / SSA / VM Engine]
    CompilerPass --> TargetOutput[(Executable Bytecode / Machine Plan)]
```

## Features
- Pure standard library Python implementation with strictly zero pip dependencies.
- Production-grade compiler engineering principles (Pratt parsing, Algorithm W, ADCE, K-coloring).
- Native Model Context Protocol (MCP) server support for AI agent orchestration.

## Installation

```bash
git clone https://github.com/alphaparkinc/genpark-chaitin-briggs-graph-coloring-allocator-skill.git
cd genpark-chaitin-briggs-graph-coloring-allocator-skill
```

## Quickstart

```bash
python example_usage.py
```
