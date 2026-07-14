# Research Note Schema

This repository uses a research-vault pattern inspired by SRTP_PowerElectronicsAI. Every substantive claim should carry evidence status, source links, and a red-team review.

## Fields

| Field | Folder | Domain |
| --- | --- | --- |
| `ee` | `research_notes/ee/` | Power electronics: DC-DC converters, flyback converters, traction inverters, components, control, simulation, and standards. |
| `cs` | `research_notes/cs/` | Computer science and AI: agent architectures, evaluation methods, tool use, orchestration, RAG, and benchmark design. |

## Note Types

| Type | Purpose | Typical folder | Red-team required |
| --- | --- | --- | --- |
| `source` | Immutable capture of one paper, repo, standard, or source. | `research_notes/<field>/sources/` | No |
| `claim` | One defensible, checkable finding with evidence. | Any field subfolder | Yes |
| `topic` | Synthesis across multiple claims or papers. | Any field subfolder | Required if it advances a position |
| `index` | Navigation page. | Any folder | No |

## Frontmatter

Use this YAML frontmatter for `claim`, `topic`, and `index` notes:

```yaml
---
title: Note Title
type: claim | topic | index
field: ee | cs
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: supported | contested | refuted | unverified
evidence: replicated | single-study | theoretical | disputed
tags: [tag-one, tag-two]
sources: [docs/citations.md#ref-key, research_notes/ee/source-note.md]
contradicts: []
review_by: YYYY-MM-DD
---
```

Use this frontmatter for `source` notes:

```yaml
---
title: Source Title
authors: []
year: YYYY
venue: "journal, conference, repository, standard, or proposal"
doi: ""
url: ""
captured: YYYY-MM-DD
reliability: high | medium | low | unknown
peer_reviewed: true | false
motivated: true | false
reliability_note: ""
sha256: ""
---
```

## Status Values

- `supported`: corroborated by at least two credible independent sources or reproduced by an executable benchmark.
- `contested`: credible evidence disagrees or the red-team review found an unresolved objection.
- `refuted`: evidence shows the claim is false. Keep the note and link the replacement.
- `unverified`: a plausible claim with incomplete evidence.

New claims default to `unverified`.

## Evidence Values

- `replicated`: independently reproduced or supported by multiple credible sources.
- `single-study`: one credible source, one repo, or one benchmark run.
- `theoretical`: derived, modeled, or simulated without independent validation.
- `disputed`: replication attempts or sources conflict.

## Red-Team Block

Every `claim` note must include:

```markdown
## Red Team

**Steelman against:** ...
**How it could be false:** ...
**What would change my mind:** ...
**Residual doubt:** ...
```

## Tag Taxonomy

Allowed field tags:

- `ee`
- `cs`

Allowed power electronics tags:

- `flyback`
- `dc-dc`
- `traction-inverter`
- `plecs`
- `matlab`
- `spice`
- `simulation`
- `constraints`
- `thermal`
- `emi`
- `safety`
- `efficiency`
- `waveforms`
- `component-selection`
- `standards`

Allowed AI and evaluation tags:

- `agent-evaluation`
- `multi-agent`
- `single-agent`
- `rag`
- `tool-use`
- `simulation-grounded`
- `benchmark`
- `evidence-gate`
- `reproducibility`
- `explainability`
- `robustness`
- `schema`

Add new tags to this file before using them.

## Append-First Rule

Search [catalog.md](catalog.md) and existing notes before adding a new note. If the new material extends an existing note, append to that note, update `updated`, and re-run red-team review if the status could change.

