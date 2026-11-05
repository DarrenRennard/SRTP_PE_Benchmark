# Research Notes

Short summaries of four papers we have read, followed by ideas to implement in PE-GPT 2.0. Paper summaries describe the uploaded versions; implementation points are proposed adaptations for this SRTP project.

## ReAct

**Paper:** [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629v3), Yao et al., ICLR 2023. Relevant sections: 2 and 3; pp. 3-6.

### Summary

- ReAct interleaves reasoning, actions, and observations. Tool feedback can help an agent revise its plan instead of relying entirely on its initial response.
- The paper evaluates question answering, fact verification, and interactive decision-making tasks. Performance depends on the task and retrieval quality; tool access does not guarantee correctness.

### What we can implement for PE-GPT 2.0

- Extend the existing tool and trace system to record concise decision summaries, actual tool calls, returned observations, and the next chosen action.
- In Requirements, call a deterministic unit-normalization or specification-checking helper, inspect the result, and ask for clarification when critical information remains unresolved.
- In Reporter, connect numerical claims to actual calculation or simulation records. A generated explanation alone should not count as engineering evidence.

**First step:** Test one unit-conversion request and one missing-field request, checking whether the next action uses the tool result correctly.

## EngDesign

**Paper:** [Toward Engineering AGI: Benchmarking the Engineering Design Capabilities of LLMs](https://arxiv.org/abs/2509.16204v2), Guo et al., 2025. Relevant sections: 2.1-2.3 and 3.2-3.3; pp. 5-10.

### Summary

- EngDesign evaluates open-ended engineering designs through task-specific executable checks and scientific tools, including simulation. Multiple different designs may satisfy the same requirements.
- Tasks include a description, grading rubric, evaluation pipeline, and validated reference design. Evaluation returns pass/fail, a partial-credit score, and diagnostic logs; feedback can support iterative improvement.

### What we can implement for PE-GPT 2.0

- Define flyback tasks with explicit input ranges, output targets, load conditions, ripple limits, and required evidence.
- Evaluate design artifacts with independent equations and, where available, PLECS measurements instead of grading only the final explanation.
- Keep an overall compliance verdict separate from a partial-credit score. Passing some checks must not conceal a failed critical requirement.
- Feed failed checks and measured values into a bounded correction attempt, then compare the resulting design with the previous attempt.

**First step:** Create one reviewed flyback reference case with an evaluator that reports per-check results and diagnostic messages.

## xbench

**Paper:** [xbench: Tracking Agents Productivity Scaling with Profession-Aligned Real-World Evaluations](https://arxiv.org/abs/2506.13651v1), Chen et al., 2025. Relevant sections: 2 and 3.1; pp. 3-5.

### Summary

- xbench argues for evaluating agents on real professional demands and useful work outcomes. Its uploaded version studies Recruitment and Marketing.
- Domain experts help define tasks and rubrics. The framework distinguishes static and changing tasks and considers the value and time associated with professional work.

### What we can implement for PE-GPT 2.0

- Ask a supervisor or experienced power electronics researcher to review whether flyback tasks resemble useful engineering work.
- Include realistic requests such as incomplete specifications, a changed load requirement, component-rating checks, and explaining a failed simulation.
- Measure successful task completion and engineering validity alongside runtime, model cost where available, and the number of manual corrections needed.
- Start with a fixed evaluation set for fair comparisons; add versioned new tasks later as requirements or component information change.

**First step:** Review a small set of realistic design requests and define what a useful, correct outcome looks like for each.

**Scope:** Applying this method to power electronics is our proposal, not a result demonstrated by the uploaded xbench paper.

## PaperBench

**Paper:** [PaperBench: Evaluating AI's Ability to Replicate AI Research](https://arxiv.org/abs/2504.01848v3), Starace et al., 2025. Relevant sections: 2.2-2.6 and 4; pp. 3-4 and 6-7.

### Summary

- PaperBench evaluates whether agents can implement and execute research replications. Complex goals are decomposed into a hierarchy of weighted, individually gradable requirements.
- It distinguishes code development, successful execution, and matching the target results. A separate reproduction run checks execution evidence, and JudgeEval tests automated judges against human labels.

### What we can implement for PE-GPT 2.0

- Break each workflow task into checkable milestones: extract specifications, calculate parameters, select supported components, run simulation, validate constraints, and report evidence.
- Award partial credit for completed milestones while separately reporting whether the full design meets its requirements.
- Distinguish a generated model or script, a successfully executed simulation, and measurements that satisfy the specification. A saved file alone proves neither execution nor compliance.
- Start with deterministic checks for units, numbers, and status consistency. If an LLM judges report quality, validate its decisions against manually reviewed examples.

**First step:** Build a small Requirements and Reporter rubric with explicit criteria and independently reviewed expected outcomes.

**Scope:** Our project improves existing PE-GPT 2.0 code; it does not adopt PaperBench's from-scratch research-replication task or all of its resource restrictions.

## Initial implementation priorities

1. **Requirements:** Combine structured extraction with deterministic checks and targeted clarification, drawing on ReAct and EngDesign.
2. **Reporter:** Link claims to evidence and check report accuracy against a rubric, drawing on ReAct and PaperBench.
3. **Benchmark:** Use reviewed engineering tasks, partial-progress scores, and independent functional checks, drawing on EngDesign, xbench, and PaperBench.

Return to the [project overview](../README.md).
