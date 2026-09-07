---
name: domain-modeling
description: Build and sharpen a project's domain model. Use when discussing codebase terminology, resolving ambiguous domain concepts, or changing the project's domain glossary or decision model.
---

# Domain Modeling

Actively build and sharpen the project's domain model as you design. This is the active discipline: challenging terms, inventing edge-case scenarios, and recording resolved terminology and decisions when the project has an owner for them.(Merely reading the project's glossary for vocabulary is not this skill. This skill is for when you're changing the model, not just consuming it.)

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with the existing project language, call it out immediately.

For example:

> Your glossary defines “cancellation” as X, but you seem to mean Y. Which is it?

Read the project's existing glossary owner when one exists.

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term.

For example:

> You're saying “account”: do you mean the Customer or the User? Those are different things.

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios.

Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Cross-reference with code

When the user states how something currently works, check whether the relevant authoritative source agrees.

If you find a contradiction, surface it.

Distinguish current behavior from intended design when the user is deliberately proposing a change rather than describing the current system.

### Update the project glossary inline

When a term is resolved, update the project's existing glossary owner there and then rather than batching changes.

Only include terms specific to the project's context. General programming concepts do not belong unless the project gives them a project-specific meaning.

### Record durable decisions sparingly

When domain modeling produces a durable decision, use the project's existing decision-record contract.

If the project has no such contract, keep the conclusion in the conversation unless the user asks to establish one.

<!-- Adapted from mattpocock/skills at 3cca18b368ae95cdbdebbff572ccafa662551015; see LICENSE. -->