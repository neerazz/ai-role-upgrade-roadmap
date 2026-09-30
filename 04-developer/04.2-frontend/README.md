# Part 4.2: Frontend developer — AI interfaces people can trust

> Hands-on track under [The Application Developer's AI Learning Roadmap](../README.md).
> This is the frontend slice: you are turning probabilistic backend behavior into
> an interface a person can understand, control, and recover.

## What changes when the backend is probabilistic

A normal UI renders known application state. An AI interface also has to represent
work in progress, partial output, uncertain output, tool activity, approval, and
failure after some work has already happened. A chat box alone does not solve any
of those problems.

## Learning path

### This week: make generation visible

1. Stream a response and support cancel, retry, and regenerate.
2. Separate user input, model output, tool activity, and system status in the UI.
3. Preserve enough client state to recover after a refresh or dropped connection.

**Proof:** throttle the network, interrupt generation halfway through, reload the
page, and verify that the user can tell what happened and what to do next.

### This month: design for trust

1. Attach citations to the claims they support instead of placing a source list at
   the bottom.
2. Show uncertainty and missing evidence without turning every response into a
   warning banner.
3. Add preview-and-approve flows before the system sends, deletes, purchases, or
   changes durable state.
4. Capture explicit feedback and the implicit signal of what users accept, edit,
   retry, or abandon.
5. Test keyboard navigation, screen-reader output, focus movement, and live-region
   behavior while tokens stream.

**Proof:** a user can identify the source of an answer, reject a proposed action,
recover from one failed tool call, and complete the task without guessing whether
the system is still working.

### This quarter: ship one end-to-end feature

Build one narrow workflow that joins the frontend to the
[backend track](../04.1-backend/README.md). Include:

- a real user task and success criterion;
- streaming or progressive status;
- citations or evidence where the task needs them;
- an approval gate before consequential action;
- typed failure states for timeout, model error, tool error, and invalid output;
- a small evaluation set plus product telemetry;
- an end-to-end trace that connects the user interaction to model and tool calls.

## What to learn, not what to collect

Learn the browser and product mechanics first: streaming transports, state
machines, optimistic versus confirmed state, accessibility, and failure recovery.
Then choose the framework that fits your stack. A UI SDK can remove plumbing; it
cannot decide what the user should trust or what requires approval.

## What to skip

- **A chat box as the entire product.** Start from the user's job, not the model's
  preferred interface.
- **Fake certainty.** Smooth prose is not proof. Show evidence and make limits
  legible.
- **Token animation without recovery.** Streaming that cannot be cancelled,
  retried, or resumed is theater.
- **Approval after the action.** Confirmation must happen before the side effect.
- **Framework-first learning.** Learn the interaction and failure model before the
  component library.

## Completion test

You are ready to move on when a second person can use the feature, encounter a
forced failure, understand what happened, and finish the task without your help.
