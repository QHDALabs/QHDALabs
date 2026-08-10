---
title: "Research notes — quantum"
status: working notes
---

# Quantum

Working notes on Qiskit circuit construction, simulator behaviour and Bloch-sphere intuition,
kept alongside the experiments they came from.

**These are notes, not results.** The results they refer to live in the repositories below, with
the code that produced them:

| Where the actual work is | What it contains |
|---|---|
| [qmnet](https://github.com/QHDALabs/qmnet) | Decoherence routing via ancilla coupling angle; measurement-fuelled conditional bridges in graph-state echo; RQTE. Four runnable scripts, two technical notes (PDF). |
| [qhda-core](https://github.com/QHDALabs/qhda-core) | `quantum/circuits.py` — the circuit helpers extracted from the above. |

**Scope limit that applies to everything here:** all results are from a noise-free Qiskit Aer
simulator. No noise model has been applied and no physical QPU run has been performed. Nothing in
these notes should be read as a hardware claim.

Readable write-up of the RQTE experiments, including the result that went the wrong way:
[When measurement creates time — RQTE v3.0](../../blog/blog-rqte-v3.md).
