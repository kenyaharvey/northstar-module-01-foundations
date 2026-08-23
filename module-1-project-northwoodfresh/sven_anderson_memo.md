# Memo: NorthwoodFresh Southeast Revenue — Prototype Analysis
**To:** Sven Anderson
**Re:** Southeast revenue diagnosis (synthetic data prototype)

## Executive Summary
Southeast's revenue drop is real, not random noise. Monthly revenue fell $98,887.74 (21.43%) after the mid-year change, with a 95% confidence interval of $74,410.93 to $123,364.55 that excludes zero. I recommend prioritizing the real NorthwoodFresh data pipeline so this analysis can be validated and a root-cause investigation into the Southeast change can begin.

## Findings
- **Effect size:** Southeast monthly revenue declined $98,887.74 (21.43%) following the mid-year change.
- **95% Confidence Interval:** $74,410.93 to $123,364.55. The interval does not contain zero, indicating the observed decline is unlikely to be attributable to random variation.
- **Statistical Significance:** p = 0.000013 (two-sample t-test), well below the 0.05 threshold.
- In practical terms, a CFO can be confident the Southeast decline is a genuine business change rather than a data artifact — the confidence interval rules out "no difference" as a plausible explanation, and the extremely low p-value rules out random chance as the cause.
- **Data Limitation:** This analysis was conducted on a synthetic dataset built to match the expected shape and pattern of NorthwoodFresh's actual sales data, since the real warehouse data was not yet available. Because the underlying numbers are simulated, the exact dollar figures should be treated as directional rather than final — the pattern of a real, sustained decline is well-established, but the precise magnitude may shift once actual figures are available. This approach lets the methodology be built and validated now, so the same code can be pointed at real data with minimal delay once the pipeline is complete.

## Recommendation
I recommend prioritizing completion of the NorthwoodFresh data pipeline so this analysis can be re-run and validated on actual figures. This brief is due to you by Friday of next week; once the real data is available, the same methodology used here can be applied immediately, minimizing turnaround time. Once confirmed, a separate root-cause investigation should follow to identify what drove the Southeast decline — this analysis establishes that the drop is statistically real, not why it happened. These findings are based on a synthetic dataset built to mirror the expected data pattern, and should be treated as a methodology prototype rather than a final conclusion.

## AI Use Note
I used AI tools (Claude) as learning aids throughout this project, for explaining Python, NumPy, and pandas concepts; debugging code and interpreting error messages; and reviewing code for correctness. I also received an AI-generated code suggestion from VS Code's Copilot for locating the CSV file (using `Path.rglob()`); I reviewed it, judged it more complex than the project needed, and replaced it with a simpler direct file path instead. All code was verified by running it myself and checking the output against the expected values in the project spec (row counts, regional means, confidence interval bounds, and p-value) before including it in the final project.
