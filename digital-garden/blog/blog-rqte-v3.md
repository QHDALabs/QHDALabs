---
title: "When Measurement Creates Time: RQTE v3.0"
date: 2026-05-21
tags: ["quantum", "cryptography", "research", "qiskit", "rovelli"]
categories: ["Research"]
author: "Krzysztof Banasiewicz"
draft: false
---

# When Measurement Creates Time: RQTE v3.0

What if the act of measuring a qubit didn't just read information —
but *created* a moment in time?

That's the question behind **RQTE** (Relational Quantum Temporal
Encryption), a research prototype we've been building at QHDALabs.

---

## The idea

Carlo Rovelli argues that time is not a river flowing in the background.
It emerges from relations between physical systems. A clock doesn't
*measure* time — it *is* time, relative to whatever interacts with it.

We took that seriously and asked: can we build a cryptographic system
where the encryption key emerges from a sequence of quantum measurements,
each one constituting a "relational fact" in Rovelli's sense?

The answer, at least in simulation, is: yes.

---

## How it works

The system runs 16 steps. In each step:

1. A 5-qubit quantum state is scrambled through a brickwork circuit
2. A perturbation is applied to the hub qubit
3. A **measurement** is taken on a rule qubit → outcome m ∈ {0, 1}
4. If m = 1: a conditional CZ gate fires between two designated qubits
   (the "bridge")
5. The scrambler is inverted
6. A clock tick derived from a star Ising Hamiltonian distinguishes
   this step from all others

The sequence of 16 measurement outcomes — something like `0001001011000011`
— is the **emergent timeline**. This sequence is public. The encryption
key is derived from the final quantum state plus this timeline using
SHA-512.

The secret is the circuit itself: which qubits, which bridge, which
Hamiltonian coupling, which scrambler depth.

---

## What the experiments actually show

We tested three variants:

| Mode | Timeline entropy | Bridges fired | Decrypts correctly |
|---|---|---|---|
| UNITARY | 1.000 bit | 8 / 16 | ✓ |
| BUTTERFLY | 0.811 bit | 4 / 16 | ✓ |
| EMERGENT | 0.989 bit | 9 / 16 | ✓ |

A few honest observations:

**Every mode decrypts correctly.** The trajectory reconstruction is
deterministic: given the same circuit parameters and the public outcome
sequence, the final quantum state — and therefore the key — is
reproduced exactly.

**Every parameter choice gives a different ciphertext.** Same plaintext,
different bridge pair → completely different ciphertext. The bridge pair
is part of the secret.

**The BUTTERFLY mode was the least random, not the most.** Each time
the bridge fires, it perturbs the Hamiltonian slightly. The system
develops a memory, and that memory reduces timeline entropy (0.811 vs
~1.0 for the others). Whether this is a weakness or a feature is an
open question we haven't answered yet.

We didn't claim otherwise. The data is what it is.

---

## What this is not

This is not post-quantum cryptography. We have not proven security
against any class of attacker. We have not run on physical quantum
hardware. We have not tested the keystream against NIST randomness
standards.

This is a research prototype exploring whether a physically motivated
construction — time emerging from measurement — can produce a
functional cryptographic primitive.

---

## What comes next

- Run NIST SP 800-22 randomness tests on the keystream
- Understand why BUTTERFLY produces fewer bridges
- Test the 4-step version on IBM Quantum hardware
- Figure out whether bridge topology (we know pair (1,3) is least
  disruptive in echo experiments) has measurable cryptographic impact

The code is open: **[github.com/QHDALabs/qmnet](https://github.com/QHDALabs/qmnet)**

If you find something wrong, say so. If you find something interesting,
let's talk.

---

*Krzysztof Banasiewicz — independent researcher*  
*contact@qhdalabs.com*
