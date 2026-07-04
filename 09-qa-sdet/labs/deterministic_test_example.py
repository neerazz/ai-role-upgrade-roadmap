"""The classic deterministic test that breaks on LLM output.
From Part 9 of the AI Role Upgrade Roadmap series.
"""
def test_summary_generation():
    result = generate_summary(article_text)
    assertEqual(result, expected_summary)
