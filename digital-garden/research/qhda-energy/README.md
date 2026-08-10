---
title: "Research notes — energy and infrastructure"
status: speculative notes / one implemented system
---

# Energy and infrastructure

Two very different things live under this heading, and it is worth separating them clearly.

## Implemented

[**QHDALabs-wildfire-risk-pl**](https://github.com/QHDALabs/QHDALabs-wildfire-risk-pl) — an
operational-style risk pipeline over Polish infrastructure and land-cover data. Five versions;
v5 fuses ignition pressure (NASA FIRMS, OSM, BDOT10k, CLC 2018), Sentinel-2 NDWI vegetation
stress and graph topology across 33 Lower Silesia forest districts. Has a test suite, SHAP
explainability reports, and a coverage gate that returns `null` rather than a score when fewer
than three data sources or under 70% layer coverage are available.

Not yet validated against a held-out fire season. Covers one voivodeship.

## Speculative

Notes on long-horizon energy concepts, including orbital microwave power transmission. These are
**reading notes and thought experiments** — no modelling, no numbers, no design work has been
done, and none is planned in the near term. They are kept here because the reading informs the
infrastructure-resilience side of the applied work, not because they constitute a project.

If a section of this file ever moves from *speculative* to *implemented*, it will move under the
heading above, with a repository link and a way to reproduce it.
