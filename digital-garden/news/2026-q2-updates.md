---
title: "Q2 2026 status"
date: 2026-06-30
categories: ["News"]
---

# Q2 2026 status

What actually happened in Q2 2026, per repository:

- **[Axon](https://github.com/QHDALabs/QHDALabs-Axon)** opened (June). Pipeline, two verifiers,
  test suite and CI. The proximity verifier returned a **null result** after FDR correction, and
  the pre-registered held-out bridge test **failed to recover**. Both are recorded in
  `VERIFICATION_LOG.md`.
- **[XSIG](https://github.com/QHDALabs/QHDALabs-XSIG)** opened (June). Positive control on
  synthetic injection passed; the real-data search returned a **confirmed null** across five
  channels.
- **[qhda-core](https://github.com/QHDALabs/qhda-core)** extracted (June) as the shared kernel and
  wired in as a dependency of Axon.
- **[qmnet](https://github.com/QHDALabs/qmnet)** — RQTE v3 and the bridge experiments stabilised
  (May), both technical notes committed.
- **[wildfire-risk-pl](https://github.com/QHDALabs/QHDALabs-wildfire-risk-pl)** — v4 and v5
  development, including the coverage gate and EFFIS validator.
- **[RTANA](https://github.com/QHDALabs/QHDALabs-RTANA)** opened (May) as written notes. Still no
  code.

Three of the quarter's headline outcomes were negative results. That is the intended behaviour of
the process, not a bad quarter — see [docs/PROJECT_STATUS.md](../../docs/PROJECT_STATUS.md).
