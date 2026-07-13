# Evaluation Report

## Dataset Summary
- Total questions: 200
- Departments covered: HR, IT, Security, Finance, Legal, and General Policies
- Difficulty mix: Easy, Medium, and Hard questions included
- Ground truth coverage: Complete for every question
- Out-of-scope coverage: 13 real refusal test cases included

## Department Distribution
- HR: 33
- IT: 32
- Security: 32
- Finance: 32
- Legal: 32
- General Policies: 39

## Difficulty Distribution
- Easy: 64
- Medium: 94
- Hard: 42

## Evaluation Metrics
- Accuracy: TBD after the first backend run
- Groundedness: TBD after the first backend run
- Retrieval Precision: TBD after the first backend run
- Latency: TBD after the first backend run
- Out-of-Scope Detection: TBD after the first backend run
- Multi-Hop Success: TBD after the first backend run

## Accuracy
Placeholder for automated accuracy results after the first evaluation pass.

## Groundedness
Placeholder for groundedness scores based on answer support and source alignment.

## Retrieval Precision
Placeholder for retrieval precision results using the retrieved document and section metadata.

## Latency
Placeholder for end-to-end latency statistics collected during evaluation runs.

## Error Analysis
Placeholder for recurring failure modes once the backend responses are available.

## Strengths
- Realistic employee-style prompts spanning policy lookup and multi-hop reasoning.
- Explicit out-of-scope refusals to test hallucination control.
- Balanced coverage across functions and difficulty levels.

## Weaknesses
- Heuristic scoring is used as a baseline until stronger semantic grading is introduced.
- The final numbers depend on the backend endpoint behavior and returned evidence.

## Future Improvements
- Add embedding-based answer similarity scoring.
- Add citation-aware groundedness checks.
- Expand the set with more adversarial and ambiguous policy questions.
