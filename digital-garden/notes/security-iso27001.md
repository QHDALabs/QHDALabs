---
title: "ISO 27001 / ISMS — practice notes"
date: 2026-05-21
categories: ["Notes"]
status: stub
---

# ISO 27001 / ISMS — practice notes

**Status: stub.** Notes from implementing an information security management system and running
risk assessment under ISO 27001. Not yet written up.

No certification is claimed. This is practitioner experience, not an audited compliance position
for QHDALabs or any of its repositories.

Where the practice actually shows up in the code today: dependency and data-source hygiene in the
[wildfire pipeline](https://github.com/QHDALabs/QHDALabs-wildfire-risk-pl) — downloads are
integrity-checked with SHA-256 before use, and the fusion stage refuses to emit a score on
insufficient source coverage rather than silently imputing one.
