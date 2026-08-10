---
title: "Research notes — relational time"
status: open question
---

# Relational time

Notes on relational quantum mechanics (Rovelli), the Page–Wootters mechanism, and causal-set
approaches to emergent spacetime — read as background for one question:

> Can time be treated as constituted by relations between systems rather than as an external
> parameter, in a way that is *implementable* and *testable*, not merely interpretive?

**Status: open question.** This is the least mature line in the lab and is labelled accordingly.

| Related work | What actually exists |
|---|---|
| [qmnet](https://github.com/QHDALabs/qmnet) | The one concrete result: a mid-circuit measurement outcome deterministically conditions later circuit structure (P_ret = 0.000 at T=2,4 in the m=1 branch). Simulation only. |
| [qhda-core](https://github.com/QHDALabs/qhda-core) | `emergent/clock.py` — the primitives extracted from that experiment. |
| [QHDALabs-RTANA](https://github.com/QHDALabs/QHDALabs-RTANA) | The neural-architecture version of the question. **No code exists.** Manifesto and open questions only. |

**What is missing.** There is no falsifiable test that would distinguish an internal relational
clock from a well-fitted positional encoding. Until that test is designed, this stays a question.
Writing it is the next step, and it comes before any implementation.
