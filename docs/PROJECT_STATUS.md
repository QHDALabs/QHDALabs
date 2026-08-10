# Project status

Per-component technical status for the QHDALabs public repositories.
Snapshot: **2026-08-10**. Companion document: [EVIDENCE.md](./EVIDENCE.md).

This document exists so that no reader has to infer maturity from tone. Each component is placed
in exactly one of four tiers, and the boundary conditions are stated.

---

## Status model

| Tier | Definition | Bar for entry |
|---|---|---|
| **Implemented** | Working code, automated tests, runnable by a third party from a clean checkout | Test suite present and passing |
| **Experimental** | Working code producing results; no test suite, or results limited to simulation / single runs | Code runs and produces the reported numbers |
| **Research hypothesis** | A question with a written argument and an intended method. No implementation. | Written analysis exists |
| **Planned** | Intent only. Not started. | — |

Deliberately **not** used: TRL numbers. No component here has been assessed against a TRL scale by
anyone, and self-assigned TRL is noise. If a formal assessment is required, the components in
*Implemented* are the only defensible candidates for anything above laboratory-concept level.

---

## Implemented

### QHDALabs-Axon — verification-first inference over scientific literature

Four-stage pipeline (perception → relational representation → verification → hypothesis) with two
registered relation verifiers.

- **Working:** `PROXIMITY` (TF-IDF, empirical random-pair null, Benjamini–Hochberg FDR) and
  `ABC_BRIDGE` (Swanson closed discovery, two explicit nulls). 24 test modules, CI workflow,
  packaged install, fetch scripts that rebuild the corpora from public sources.
- **Validated:** in-sample recovery of the Swanson Raynaud / fish-oil bridge
  (direct_sim 0.046, mediated 5.10, p_random 0.0345).
- **Failed, and documented:** the pre-registered held-out case (migraine / magnesium) did not
  recover (p_random 0.1214), and a sibling literature would be falsely accepted at q = 0.0135.
- **Halted by protocol:** the V2-A Tier-0 confirmatory run (frozen pre-registration, R = 200,
  11 cells) failed contract cell `thin_half_n4` at degradation 0.53 against a required 0.80.
  Tier 1 was not attempted.
- **Boundary:** the bridge gate is valid for **closed discovery in-sample only**. It is not
  validated for general or open discovery, and is not claimed to be.
- **Not started:** a replacement selectivity mechanism for the failed cell.

### QHDALabs-wildfire-risk-pl — wildfire risk pipeline for Poland

Five successive versions; v5 is the current six-module pipeline over a 33-node Lower Silesia
forest-district graph.

- **Working:** topology construction, Sentinel-2 NDWI vegetation stress, ignition pressure from
  NASA FIRMS + OSM + BDOT10k + CLC 2018, fusion scoring, optional EFFIS comparison, SHAP
  explainability reports, generated interactive maps. pytest suite. `--stub` mode runs with no
  credentials.
- **Integrity:** FIRMS downloads validated atomically with SHA-256 across 73 five-day windows
  for 2025. Fusion is **blocked** below 70% layer coverage or fewer than three sources; missing
  data returns `null` rather than an imputed score.
- **Gaps:** ARiMR LPIS and IBL KSIPL layers have no automated source (manual import required), so
  a full end-to-end run is not reproducible from a clean checkout. EFFIS has no automated
  hotspot feed.
- **Not done:** predictive skill validation against a held-out fire season. No ROC/AUC, no
  Brier score, no operational deployment. Coverage is one voivodeship, not national.

### qhda-core — shared kernel

Small packaged library (~21 KB): relational state, quantum circuit helpers, emergent-clock
primitives. Integration test present. Consumed as a real dependency by Axon and exercised against
the wildfire domain via `examples/wildfire_relational.py`. Not an orphan abstraction.

---

## Experimental

### qmnet — measurement-fuelled bridges and RQTE

Three Qiskit experiments, all on a **noise-free Aer simulator**.

- **Reproducible:** conditional bridge fires deterministically on the mid-circuit outcome
  (P_ret = 0.000 at T = 2,4 in the m=1 branch; ⟨Z⟩ = ±1.000 by branch); five-pair bridge topology
  sweep; RQTE 16-step construction encrypts and decrypts correctly in all three irreversibility
  classes.
- **Unexpected result, published:** BUTTERFLY timeline entropy 0.811 bit against ≈1.0 for the
  other modes — the opposite of the design expectation. Cause unresolved.
- **Hard boundaries:** no noise model, no physical QPU run, no scaling beyond 5 qubits, no
  security proof, no attacker model, no NIST SP 800-22 testing. **RQTE is not a cryptosystem and
  is not claimed to be one** — it is a construction that demonstrates a mechanism.
- **No test suite.** This is the main engineering gap in the repository.

### QHDALabs-XSIG — cross-cycle structural information geometry

Search for non-random cross-channel structure in ΛCDM residuals across five observational
channels, with real committed Planck 2018 data.

- **Methodology order is correct:** positive control on injected synthetic signal (d ≈ 2.5,
  p < 0.0001) was run before the real data.
- **Result: null.** 500 bootstrap permutations; best real-data test z = +1.29, p = 0.108; no test
  reached p < 0.05. Consistent with standard cosmology.
- **Self-caught artifact:** replacing the smooth Webb+2011 α dipole model with King+2012 raw
  absorber data removed the apparent signal, identifying the earlier hint as a model artifact.
- **Limits:** 16 observational windows (acknowledged insufficient), parametric BAO rather than raw
  data, shared instrumental systematics across channels cannot be excluded.
- **No test suite.**

### QHDALabs-Genesis-Protocol — ethical-constraint voting prototype

React frontend with LLM scenario generation and World ID proof-of-personhood, collecting
preferences over two safety parameters (`MAX_ENERGY_SPIKE_RATE`, `MIN_BIOSPHERE_VIABILITY`).

- **Runs locally** via `npm run dev`. **There is no public deployment and no production instance.**
- **Conceptual only:** the Quantum Hardware Security Module (Q-HSM) has firmware source but no
  silicon; the distributed vote ledger and paradox-detection algorithms are unbuilt.
- Treat this as a UI prototype for a governance idea, not as a platform.

---

## Research hypothesis

### QHDALabs-RTANA — relational temporal awareness in neural architectures

**Contains no code.** `MANIFESTO.md`, `QUESTIONS.md` and `RESEARCH_LOG.md` articulate the
question: whether a neural system can carry an internal relational clock — time constituted by
relations between its own states — rather than an external timestamp.

- **Grounding:** motivated by the `qmnet` finding that a mid-circuit measurement creates a
  relational fact with a deterministic downstream effect.
- **Explicitly not about:** machine consciousness, subjective experience, or adding timestamps.
- **Unstarted:** architecture proposal, proof of concept, evaluation protocol. All three.
- **What would make it real:** a falsifiable behavioural test that distinguishes an internal
  relational clock from a well-fitted positional encoding. That test does not yet exist, and until
  it does this remains a question, not a project.

### QHDALabs-Universe — precision cosmology umbrella

README only, marked "init alpha". Names five intended sub-projects (cosmoaudit, photon-engine,
h0lab, reltime, cosmohub) and a technology stack. No implementations, datasets or results.
Currently an intent statement. XSIG is the one line from this umbrella that produced actual work,
and it lives in its own repository.

### Multiverse-Theory — research origin (earliest indexed 2025)

The theoretical work the lab grew out of. Its earliest **currently indexed** artifacts date to
**April 2025** — ten months before the QHDALabs account existed — and the repository was brought
under the organisation in April 2026. A self-fork of the operator's personal account; all commits
are his own across both accounts.

> **Chronology is provisional.** 2025-04 is a lower bound, not an established origin. Earlier
> personal research artifacts exist that may belong to the same lineage; a provenance
> reconstruction across the older archives is planned to fix the earliest defensible date for each
> line from files, dates and technical continuity. Neither shortening the history to 2025 nor
> claiming older unrelated work is acceptable, so this stays provisional until that is done.

Proposes that time emerges from information asymmetry, space from quantum correlations, and
causality from stable relational structure, with reality modelled as a dynamic quantum graph.

- **Contains:** ~40 theoretical documents under `docs/` (models, concepts, predictions,
  assumptions), six Qiskit/NumPy simulation scripts under `simulations/`, three preprint sources
  under `preprints/`, a `paper/` build, LaTeX CI, and citation/archival metadata
  (`CITATION.cff`, `.zenodo.json`).
- **Lineage, traceable to files:** `docs/models/emergent_time.md` → `qhda-core`'s
  `emergent/clock.py`; `docs/concepts/virtual_qubit.md` + `simulations/time_shifted_clock.py` →
  the star-topology clock tick in `qmnet`'s RQTE; `notebooks/preprint_qmnet.tex` → `qmnet` itself;
  `docs/models/time_theory.md` → RTANA's question.
- **Status: theory, unvalidated.** Not peer-reviewed. No experimental confirmation of any
  proposed mechanism. Several documents are explicitly speculative. The simulations run but have
  no test suite and no published result set.
- **The one adjacent empirical test returned a null:** XSIG searched for cross-cycle structure in
  ΛCDM residuals and found none (best p = 0.108).
- **Correct reading:** this establishes *provenance and continuity* for the algorithms, and shows
  the applied work is not a standing start. It does **not** add validated results, and is not
  offered as such.
- **Cheapest available improvement:** if the Zenodo deposit metadata has not been used to mint a
  DOI, doing so converts a folder of PDFs into citable artifacts for a few hours' work.

### qhda-coherence-bridge — coherence-layer abstraction

Earliest repository in the lab (2026-03), ~9 KB design note on abstracting between relational
quantum models and executable substrates. Superseded in practice by `qhda-core`, which implements
the parts that turned out to be needed. Retained as a record of where the work started.

---

## Planned

Nothing below exists. Listed for direction, in rough priority order.

1. **Axon:** replace or repair the pair-selectivity mechanism that failed Tier-0 — including the
   possibility that the ABC-bridge approach is abandoned. That is an acceptable outcome.
2. **Wildfire:** skill scoring against a held-out fire season; automated substitutes for the LPIS
   and IBL layers; extension beyond Lower Silesia.
3. **qmnet:** NIST SP 800-22 on the RQTE keystream; realistic noise model; first physical QPU run
   of the reduced 4-step variant (IBM Heron target); investigate the BUTTERFLY entropy anomaly.
4. **qmnet / XSIG:** add test suites. Both currently have none.
5. **XSIG:** extend beyond 16 observational windows; replace parametric BAO with raw data.
6. **RTANA:** turn the manifesto into an architecture proposal plus a falsifiable evaluation
   protocol before writing any code.
7. **Research provenance reconstruction:** establish the earliest defensible origin of each
   lineage from the older personal archives (RPi4 archive and other historical research/code
   artifacts), driven by files, dates and technical continuity — then replace the provisional
   2025-04 chronology in the README and in `EVIDENCE.md` §7a with the reconstructed one.
8. **Cross-cutting:** external replication of at least one result by someone other than the author.

---

## Cross-cutting gaps

Honest summary of what is missing across the whole lab:

| Gap | Affected | Severity |
|---|---|---|
| No peer review or external publication of any result | All | High for academic credibility |
| No external replication by a third party | All | High |
| No physical quantum hardware run | qmnet, qhda-core | High for any quantum claim |
| No test suites | qmnet, XSIG, Genesis-Protocol | Medium |
| CI exists in two repositories only (Axon: pytest; Multiverse-Theory: LaTeX builds) | All others | Medium |
| Theoretical corpus is unvalidated and undeposited (no DOI visible despite prepared metadata) | Multiverse-Theory | Medium — cheap to fix |
| Two data layers require manual import | wildfire v5 | Medium (blocks clean-checkout reproduction) |
| No held-out predictive validation | wildfire | Medium |
| Single operator; no institutional affiliation or funding | All | Structural |

None of these are hidden elsewhere in the presentation. They are the honest current state, and
closing any of them is worth more than adding another repository.
