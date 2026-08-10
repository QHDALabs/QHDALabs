---
title: "Building the QHDALabs digital garden on GitHub Pages"
date: 2026-05-21
tags: ["infrastructure", "github-pages", "digital-garden", "web-design"]
categories: ["Blog"]
author: "Krzysztof Banasiewicz"
draft: false
---

# Building the QHDALabs digital garden on GitHub Pages

An infrastructure note, not a research post. We moved the public site off a WordPress + managed
hosting stack onto a static site published from a Git repository via GitHub Pages.

## Why

A CMS was the wrong tool for what this actually is: a set of markdown notes next to a set of code
repositories. Removing the database and the PHP runtime removes the attack surface that comes with
them and the maintenance that comes with keeping them patched — the remaining surface is GitHub's,
not ours. Static hosting on Pages also costs nothing at our traffic, and the domain still routes
mail through its existing provider independently of where the site is served.

To be clear about the limits: "no database" removes one class of vulnerability, not all of them.
The page still loads third-party scripts from CDNs, which is its own trust dependency.

## How the portal is built

The entry page (`digital-garden/index.html`) is a single Tailwind page with three pieces worth
naming:

**A canvas particle field.** Nodes spawn and link by proximity. It is a *visual metaphor* for
causal-set style relational structure — it is decoration, and it does not compute anything.

**An SVG mandala with interactive sliders.** Also decorative. The sliders change the rendering;
they are not bound to any model or data.

**A demo terminal.** Fixed scripted output with buttons. It is a UI demo and is labelled as such
on the page. It is not connected to any repository, service or live system, and no telemetry of
any kind is collected or displayed.

The index of posts is generated at deploy time by a small Python step in
[the deploy workflow](../../.github/workflows/deploy.yml), which parses front matter from
`blog/`, `research/`, `notes/` and `news/` into `posts.json`. That is the entire build.

## What this is

A publishing surface for working notes. The actual research and code live in the individual
repositories, and the claims about them are catalogued in
[docs/EVIDENCE.md](../../docs/EVIDENCE.md) with pointers to files anyone can check.
