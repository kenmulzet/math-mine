# Math Mine development roadmap

This document outlines proposed work for the existing Math Mine application. Estimates are planning ranges, not time already spent. Scope and priorities may change as the code is tested.

| Workstream | Planned work | Estimate |
| --- | --- | ---: |
| Reproducible setup | Audit imports, create a dependency manifest, document system prerequisites, validate clean install | 4–6 h |
| Generator testing | Add deterministic tests for representative problem generators, edge cases, and answer consistency | 6–9 h |
| API robustness | Review request schemas, improve validation and error responses, add endpoint integration tests | 5–8 h |
| Worksheet output | Improve layout, pagination, answer-key formatting, and PDF export error handling | 6–10 h |
| Problem variety | Extend existing generators with new parameter ranges and difficulty controls | 6–10 h |
| Documentation | Add developer guide, example requests, architecture notes, and contribution guidance | 3–5 h |

**Estimated total: 30–48 hours.**

## Suggested milestones

1. **Foundation:** Establish reproducible setup and a baseline test suite.
2. **Correctness:** Add generator invariants, regression tests, and API validation.
3. **Product improvements:** Expand problem generation and improve worksheet/PDF output.
4. **Maintainability:** Document architecture and examples; clean up technical debt discovered by tests.

## Definition of done

For each item, commit the implementation with appropriate tests or documented manual verification, and update user-facing instructions when behavior changes. Preserve authentic commit history.
