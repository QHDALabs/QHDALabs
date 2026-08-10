# Evidence matrix

**Purpose:** answer one question — *what can an external evaluator independently verify in the
QHDALabs public repositories, without asking the author for anything?*

Every row points to a file, a command, or a public API response. Rows marked **NOT VERIFIABLE**
are listed deliberately: claims that cannot be checked are worth less than claims that can, and
pretending otherwise is the failure mode this document exists to prevent.

Snapshot date: **2026-08-10**. Repository facts were taken from the public GitHub API
(`https://api.github.com/users/QHDALabs/repos`) and from the file trees of each repository.

Status vocabulary used throughout:

| Term | Meaning |
|---|---|
| **VERIFIED** | An external party can confirm it from public files or a public API today |
| **REPRODUCIBLE** | Verified, and re-runnable from a clean checkout with documented commands |
| **PARTIALLY VERIFIED** | Some of the claim is checkable; a named part is not |
| **EXPERIMENTAL** | Code exists and runs; results are from simulation or a single run, not validated |
| **CONCEPTUAL** | Written design or hypothesis, no implementation |
| **NOT VERIFIABLE** | Cannot be checked from public material — treat as no evidence |

---

## 1. Lab-level facts

| Claim | Evidence | Verification method | Status |
|---|---|---|---|
| 12 public repositories | GitHub API `public_repos: 12` | `curl https://api.github.com/users/QHDALabs` | VERIFIED |
| Active since 2026-02 | Account `created_at: 2026-02-25` | same | VERIFIED |
| Single operator, no institutional affiliation | Account type `User`; all repos owned by one account; no org members | GitHub UI / API | VERIFIED |
| 1 of the 12 public repositories is a fork (`Multiverse-Theory`) whose commits are upstream work | API `fork: true` on that repo | `curl .../repos/QHDALabs/Multiverse-Theory` | VERIFIED |
| Additional private repositories exist | — | Not inspectable by definition | NOT VERIFIABLE — **no claims are made about them and nothing in the public presentation depends on them** |
| Any aggregate statistic spanning private repos (total commits, total code volume, language shares) | — | — | NOT VERIFIABLE — **such figures have been removed from the public presentation** |
| Peer-reviewed publications | None | Search | VERIFIED: **zero** |
| External replication of any result | None | — | VERIFIED: **none to date** |

---

## 2. QHDALabs-Axon — verification-first literature inference

Strongest evidence in the lab. Repo: <https://github.com/QHDALabs/QHDALabs-Axon>

| Capability | Repository evidence | Verification method | Status |
|---|---|---|---|
| Four-stage pipeline (perception → relational representation → verification → hypothesis) exists as code | `src/axon/{perception,relational_representation,verification,hypothesis}/` | Read the tree; `pytest` | VERIFIED |
| Automated test suite | 24 `test_*.py` modules under `tests/` (14 of them in `tests/verification/`), plus 2 XML fixtures | `pytest` | REPRODUCIBLE |
| Continuous integration | `.github/workflows/ci.yml` | Actions tab / run history | VERIFIED |
| Packaged and installable | `pyproject.toml`, `requirements-dev.txt` | `pip install .` | REPRODUCIBLE |
| Depends on `qhda-core` (the dependency edge claimed in the architecture diagram is real) | Install instruction in README: `pip install "git+https://github.com/QHDALabs/qhda-core.git"` | Read README; install | VERIFIED |
| `PROXIMITY` verifier uses an *empirical corpus null*, not an invalid permutation null | `src/axon/verification/null_models.py`; change recorded in `VERIFICATION_LOG.md` (2026-06-21) | Read both | VERIFIED |
| Multiple-testing correction (Benjamini–Hochberg FDR) is applied | `src/axon/verification/multiple_testing.py` + tests | `pytest tests/verification/test_multiple_testing.py` | REPRODUCIBLE |
| **Null result:** 780 pairs / 40 arXiv abstracts → 0 accepted, 311 null, 469 rejected; **0 survive BH-FDR at α=0.05** | `VERIFICATION_LOG.md`; `examples/mvp_proximity_null.py`; `data/corpus_mvp.json` | `python examples/mvp_proximity_null.py` | REPRODUCIBLE |
| **Positive control:** Swanson Raynaud / fish-oil bridge recovered in-sample (717 pre-1986 MeSH records; direct_sim 0.046, mediated 5.10, p_random 0.0345) | `examples/abc_bridge_recovery.py`; `data/bridge_corpus.json` + its README | `python examples/abc_bridge_recovery.py` | REPRODUCIBLE |
| **Pre-registered held-out test FAILED:** migraine / magnesium not recovered, p_random 0.1214 | `docs/ABC_BRIDGE_V2A_TIER0_PRE_REGISTRATION.md`; `examples/migraine_magnesium_heldout.py`; `data/heldout_corpus.json`; `tests/test_heldout_recovery.py` | `python examples/migraine_magnesium_heldout.py` | REPRODUCIBLE — **documented negative result** |
| **Known defect, self-reported:** sibling literature (cluster headache, direct_sim 0.283) would be falsely accepted at q=0.0135 — the gate cannot separate siblings from true bridges | `VERIFICATION_LOG.md` (2026-06-26); `src/axon/verification/sibling_safety.py`; `tests/verification/test_sibling_safety.py` | Read log; run tests | VERIFIED — **defect disclosed by the author** |
| **Confirmatory tier failed and development was stopped per protocol:** V2-A Tier-0, frozen pre-registration, R=200, 11 cells → failed contract cell `thin_half_n4` (degradation 0.53 < 0.80 required); latent-parent control passed (risk_rate ≥ 0.90); Tier 1 never attempted | `docs/ABC_BRIDGE_V2A_TIER0_PRE_REGISTRATION.md`, `docs/ABC_BRIDGE_V2A_TIER0_DRAFT.md`, `scripts/confirmatory_v2a_tier0.py`, `v2a_confirmatory.json`, `tests/verification/test_confirmatory_v2a.py` | Read pre-registration, then `python scripts/confirmatory_v2a_tier0.py` and compare to `v2a_confirmatory.json` | REPRODUCIBLE — **strongest single credibility signal in the lab** |
| Method transparency | `docs/method_cards/ABC_BRIDGE.md`, `docs/method_cards/PROXIMITY_MVP.md`, `RELATION_STATUS.md` (generated by `scripts/gen_relation_status.py`) | Read | VERIFIED |
| V2-A pair-selectivity audit is production-ready | — | Author states "IN DEVELOPMENT — not validated" | CONCEPTUAL — **explicitly not claimed** |
| Corpora are fetched from public sources rather than hand-curated | `scripts/fetch_corpus.py`, `fetch_bridge_corpus.py`, `fetch_heldout_corpus.py` + per-corpus README files | Re-run the fetch scripts and diff against the committed JSON | REPRODUCIBLE |

---

## 3. QHDALabs-wildfire-risk-pl — applied risk pipeline

Repo: <https://github.com/QHDALabs/QHDALabs-wildfire-risk-pl>

| Capability | Repository evidence | Verification method | Status |
|---|---|---|---|
| Five successive implementations (v1 → v5), not a single sketch | `qhdalabs-wildfire_risk_v1..v3.py`, `v4/`, `v5/` | Read tree | VERIFIED |
| v5 is a six-module pipeline (topology, Sentinel NDWI, QTE signal, ignition, fusion, EFFIS validation) | `v5/qhdalabs_wildfire_{topology,sentinel,qte,ignition,fusion}_v1.py`, `v5/effis_validator.py`, `v5/run_all.py` | Read source | VERIFIED |
| Automated tests | `v5/tests/{conftest,test_cli,test_coverage_and_fusion,test_ignition_data}.py`, `v5/pytest.ini` | `pytest` in `v5/` | REPRODUCIBLE |
| Runs without credentials for inspection | `--stub` synthetic mode | `python qhdalabs_wildfire_ignition_v1.py --stub` | REPRODUCIBLE |
| Real public data sources: NASA FIRMS, OSM/Geofabrik, BDOT10k, CLC 2018 | `v5/config.py`, `v5/ignition_data.py`, `v5/sentinel_diag.py`; documented in `v5/README.md` | Read config; run with `FIRMS_MAP_KEY` | PARTIALLY VERIFIED — needs a free NASA key |
| Downloads are integrity-checked | SHA-256 atomic validation across 73 five-day FIRMS windows for 2025, per `v5/README.md` | Read fetch code | VERIFIED |
| **Refuses to output a score on thin data:** minimum 70% layer coverage and ≥3 sources, else `null` | `v5/README.md`; `v5/tests/test_coverage_and_fusion.py` | `pytest v5/tests/test_coverage_and_fusion.py` | REPRODUCIBLE — **honest-failure behaviour, tested** |
| Concrete outputs exist, not just code | `v5/topology/{nodes,graph,risk_scores,ignition_scores,qte_results,alerts,ndwi_sentinel}.json`, `final_map.html`, `network_map*.html`, `shap_report*.html`, `example_map.png`, `v5/Screenshot_map20260601.png` | Open the artifacts | VERIFIED |
| Explainability | SHAP reports committed as HTML | Open `shap_report_v4.html` | VERIFIED |
| Technical notes | `banasiewicz_rqm_scpf_verification_2026.pdf` (+ PL version) | Read | VERIFIED (self-published, not peer-reviewed) |
| Full end-to-end run from a clean checkout | — | ARiMR LPIS and IBL KSIPL layers have **no automated source** and must be supplied manually; EFFIS has no automated hotspot feed | PARTIALLY VERIFIED — **reproducibility gap, disclosed** |
| Predictive skill against a held-out fire season | Not present | — | **NOT CLAIMED** — no skill score, ROC/AUC or held-out validation exists |
| Geographic coverage | 33-node Lower Silesia forest-district graph | `v5/topology/nodes.json` | VERIFIED — **one voivodeship, not national** |

---

## 4. qmnet — relational quantum experiments

Repo: <https://github.com/QHDALabs/qmnet> (MIT)

| Capability | Repository evidence | Verification method | Status |
|---|---|---|---|
| Three distinct experiments implemented in Qiskit ≥1.0 | `routed_measurement_full_experiment.py`, `qmnet_v3.py`, `qmnet_v4.py`, `rqte_v3.py` | Read; run | REPRODUCIBLE (~11 min total, CPU only) |
| Conditional bridge fires deterministically on measurement outcome: P_ret = 0.000 at T=2,4 in the m=1 branch; ⟨Z⟩ = +1.000 (m=0) / −1.000 (m=1) | `qmnet_v3.py` output; technical note *Measurement-Fueled Conditional Bridges in Graph-State Echo Experiments.pdf* | `python qmnet_v3.py` | REPRODUCIBLE — **ideal simulator only** |
| Bridge-topology sweep across five qubit pairs | `qmnet_v4.py` | `python qmnet_v4.py` | REPRODUCIBLE |
| RQTE: 16-step construction, key = f(final state, public measurement timeline, SHA-512); encrypt/decrypt correct in all three irreversibility classes | `rqte_v3.py`; technical note *Relational Quantum Temporal Encryption (RQTE).pdf*; write-up in [`digital-garden/blog/blog-rqte-v3.md`](../digital-garden/blog/blog-rqte-v3.md) | `python rqte_v3.py` | REPRODUCIBLE |
| **Result that contradicted the expectation:** BUTTERFLY mode timeline entropy 0.811 bit vs ≈1.0 for UNITARY/EMERGENT — reported as an unresolved open question | Blog write-up + `rqte_v3.py` | Run and compare | VERIFIED — **negative/unexpected result published** |
| RQTE is post-quantum cryptography | — | Author explicitly denies it | **NOT CLAIMED** |
| Security against any attacker class | No proof, no attacker model | — | **NOT CLAIMED** |
| NIST SP 800-22 randomness testing of the keystream | Not performed | — | **PLANNED, not done** |
| Behaviour under a noise model, or on physical hardware | Not performed; no QPU credentials in the codebase | — | **NOT CLAIMED** — all results are noise-free simulation |
| Scaling beyond 5 qubits | Not tested | — | **NOT CLAIMED** |

---

## 5. QHDALabs-XSIG — cosmological structure search

Repo: <https://github.com/QHDALabs/QHDALabs-XSIG>

| Capability | Repository evidence | Verification method | Status |
|---|---|---|---|
| Real observational data, committed | `data/planck/COM_PowerSpect_CMB-TT-binned_R3.01.txt` (Planck 2018, 83 bins) | Diff against the ESA Planck Legacy Archive release | VERIFIED |
| Five channels: CMB TT, D/H (Cooke+2018), He-4 (Aver+2015), α (Webb+2011 dipole model and King+2012 raw, 293 absorbers), eBOSS BAO | `xsig_data_adapter.py`, `xsig_bbn_catalog.py`, `xsig_king_catalog.py`, `xsig_full_catalog.py` | Read source; check citations against the published papers | VERIFIED |
| **Positive control run before real data:** injected synthetic signal detected at d ≈ 2.5, p < 0.0001 | `xsig_fullrun_v5.py` | Run | REPRODUCIBLE — **correct methodology order** |
| **Null result on real data**, 500 bootstrap permutations: proxy z=+0.73 p=0.20; 5-channel with α model z=+1.29 p=0.108; with α raw data z=−0.66 p=0.724; **no test reached p<0.05** | `xsig_real_run.py`, result plots `xsig_v3.png`, `xsig_v301.png`, `xsig_v4.png` | `python xsig_real_run.py` | REPRODUCIBLE — **published null** |
| **Self-caught artifact:** the apparent signal weakened when the smooth Webb+2011 α dipole *model* was replaced with King+2012 *raw* absorbers — i.e. the earlier hint was a model artifact, and this is stated rather than retained | README + `xsig_king_catalog.py` | Compare the two runs | VERIFIED — **strong methodological signal** |
| Automated tests | None | — | **ABSENT** — no test suite in this repository |
| Statistical power | 16 observational windows, acknowledged insufficient | README | VERIFIED (limitation disclosed) |
| Exclusion of shared instrumental systematics across channels | Not possible with this design | README | **ACKNOWLEDGED LIMITATION** |

---

## 6. qhda-core — shared kernel

Repo: <https://github.com/QHDALabs/qhda-core>

| Capability | Repository evidence | Verification method | Status |
|---|---|---|---|
| Packaged library with three submodules (`relational/state.py`, `quantum/circuits.py`, `emergent/clock.py`) | `src/qhda_core/`, `pyproject.toml` | `pip install .` | VERIFIED |
| Integration test | `tests/test_integration.py` | `pytest` | REPRODUCIBLE |
| Actually consumed downstream (not an orphan abstraction) | Axon installs it as a dependency; `examples/wildfire_relational.py` applies it to the wildfire domain | Read Axon's README install steps | VERIFIED |
| Size | ~21 KB — a small kernel, not a framework | API `size` | VERIFIED |

---

## 7. Repositories with no implementation

Listed here so they are not mistaken for capability.

| Repository | What is actually in it | Status |
|---|---|---|
| **QHDALabs-RTANA** | `README.md`, `MANIFESTO.md`, `QUESTIONS.md`, `RESEARCH_LOG.md`. **No source files.** Architecture proposal, proof-of-concept and evaluation protocol are all explicitly unstarted. Motivated by the `qmnet` bridge results. | CONCEPTUAL |
| **QHDALabs-Universe** | README only, marked "init alpha". Names five intended sub-projects (cosmoaudit, photon-engine, h0lab, reltime, cosmohub) and a technology stack. **No implementations, datasets or results.** | CONCEPTUAL |
| **qhda-coherence-bridge** | ~9 KB design note, earliest repository in the lab (2026-03). Superseded in practice by `qhda-core`. | CONCEPTUAL |
| **QHDALabs-Genesis-Protocol** | React frontend + LLM integration + World ID that runs locally via `npm run dev`. **No public deployment.** The Q-HSM hardware module has no silicon; the distributed vote ledger is unbuilt. | EXPERIMENTAL (local prototype) — hardware and ledger CONCEPTUAL |
| **Multiverse-Theory** | Fork of an upstream TeX project. Commit count and content are **not QHDALabs output**. | NOT LAB OUTPUT |

---

## 8. Claims deliberately withdrawn

These appeared in earlier versions of the public presentation and are removed because they could
not be verified, were misleading, or were theatrical rather than technical.

| Withdrawn claim | Why |
|---|---|
| "21 nodes · 349 commits" | Aggregates private repositories; an evaluator cannot check any of it. Replaced by "12 public repositories", which is checkable via one API call. |
| "9 ENCRYPTED NODES [CLASSIFIED]" ASCII panel | Presented inaccessible material as evidence. Inaccessible evidence is not evidence. Replaced by a one-line statement that private work exists and is *not* offered as evidence. |
| Language distribution "1.96 MB across all 21 repositories" | Spans private repositories; unverifiable. Removed. |
| "the lab goes dark" / "surfaces when it survives verification" | Theatre. Communicated nothing technical and implied hidden capability. |
| RTANA badged as "Python · Qiskit, 29 KB" | **The repository contains no Python and no Qiskit code.** Corrected to "research notes — no code". |
| Multiverse-Theory listed with "48 commits" alongside original work | It is a fork; those commits are upstream authors' work. Now labelled as a fork and excluded from lab output. |
| Genesis-Protocol as an "open platform for crowdsourcing ethical consensus" | There is no public deployment. Corrected to "local prototype". |
| Per-repository code sizes (e.g. "Axon — 229 KB") | Did not match the public API and served no evaluative purpose. Replaced by an evidence column. |
| GitHub streak/activity badge images | The streak service (`herokuapp.com`) is defunct; the badges rendered broken. Removed. |
| Simulated "Connected to Mainframe" / "IPFS cluster nodes" terminal output on the portal | Fabricated infrastructure telemetry. Relabelled as an explicitly decorative simulation. |

---

## 9. What an evaluator should check first

If you have ten minutes and want to test whether this lab is real:

1. Read [`QHDALabs-Axon/VERIFICATION_LOG.md`](https://github.com/QHDALabs/QHDALabs-Axon/blob/main/VERIFICATION_LOG.md).
   It contains four dated entries, two of which are the author's own methods failing.
2. Read [`docs/ABC_BRIDGE_V2A_TIER0_PRE_REGISTRATION.md`](https://github.com/QHDALabs/QHDALabs-Axon/blob/main/docs/ABC_BRIDGE_V2A_TIER0_PRE_REGISTRATION.md),
   then `v2a_confirmatory.json`. The pre-registration was written first and the result violates it.
   Development stopped there.
3. Run `python examples/migraine_magnesium_heldout.py` in Axon and confirm you get a NULL verdict.
4. Open `v5/topology/risk_scores.json` in the wildfire repo — real outputs over real districts.
5. Run `python rqte_v3.py` in `qmnet` and confirm BUTTERFLY entropy ≈ 0.811, which is the result
   the author did **not** want.

If any of the above does not hold, that is a defect worth reporting as an issue.
