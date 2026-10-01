import importlib.util
import sys
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "scripts" / "paperaudit_lint.py"
spec = importlib.util.spec_from_file_location("paperaudit_lint", SCRIPT)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
assert spec.loader is not None
spec.loader.exec_module(mod)


def test_flags_generic_pivot():
    findings = mod.analyse("This highlights the broader implications of the change.")
    assert any(f.rule == "pivot.generic" for f in findings)


def test_protects_normal_study_opening():
    findings = mod.analyse("This study examines institutional responsibility across pathways.")
    assert findings == []


def test_flags_not_but_as_low_in_isolation():
    findings = mod.analyse("The issue is not access but continuity.")
    matches = [f for f in findings if f.rule == "contrast.not_but"]
    assert matches
    assert all(f.severity == "low" for f in matches)


def test_risk_not_authorship():
    findings = mod.analyse("This highlights a wider transformation. More broadly, this underscores the critical importance of reform.")
    assert mod.risk_level(findings) in {"Moderate", "High"}


def test_detects_local_contrast_cluster():
    text = "\n".join([
        "The issue is not access but continuity.",
        "The distinction is not merely formal but institutional.",
        "The contribution is not to add a category but to trace retained arrangements.",
    ])
    findings, metrics = mod.analyse_with_metrics(text)
    assert any(f.rule == "repetition.contrast_cluster" for f in findings)
    assert metrics["contrast_clusters"] >= 1


def test_long_text_not_high_from_sparse_flags():
    filler = "The analysis records a specific institutional arrangement."
    text = " ".join([filler] * 120 + [
        "The issue is not access but continuity.",
        "The distinction is not merely formal but institutional.",
        "The contribution is not to add a category but to trace retained arrangements.",
        "This highlights a specific analytical distinction.",
    ])
    findings, metrics = mod.analyse_with_metrics(text)
    assert mod.risk_level(findings, metrics) != "High"


def test_sparse_isolated_contrasts_stay_low_in_long_manuscript():
    filler = "The analysis records a specific institutional arrangement."
    text = " ".join([filler] * 400 + [
        "The issue is not access but continuity.",
        "The distinction is not merely formal but institutional.",
    ])
    findings, metrics = mod.analyse_with_metrics(text)
    assert metrics["contrast_clusters"] == 0
    assert mod.risk_level(findings, metrics) == "Low"

def test_evidence_summary_pivot_is_low_candidate():
    findings = mod.analyse("This finding demonstrates the limits of a system-level classification.")
    matches = [f for f in findings if f.rule == "pivot.evidence_summary"]
    assert matches
    assert all(f.severity == "low" for f in matches)

def test_soft_wrapped_paragraph_is_joined_before_sentence_analysis():
    text = "\n".join([
        "The issue is not access but",
        "continuity. The analysis then records a specific arrangement.",
    ])
    findings, metrics = mod.analyse_with_metrics(text)
    assert any(f.rule == "contrast.not_but" for f in findings)
    assert metrics["total_sentences"] == 2


def test_isolated_metadiscursive_pivot_is_tracked_but_not_flagged():
    findings, metrics = mod.analyse_with_metrics(
        "The contribution is to distinguish developmental from inferential sufficiency."
    )
    assert metrics["metadiscursive_pivots"] == 1
    assert not any(f.rule == "repetition.metadiscursive_pivot_cluster" for f in findings)


def test_detects_metadiscursive_pivot_cluster_in_conceptual_prose():
    text = " ".join([
        "The important point is that the two problems can diverge.",
        "The analysis records two separate conditions.",
        "The issue is not simply whether AI was used.",
        "The evidence requirement depends on the capability claim.",
        "A further question therefore remains: must both protections arise together?",
    ])
    findings, metrics = mod.analyse_with_metrics(text)
    assert metrics["metadiscursive_pivot_clusters"] >= 1
    assert any(f.rule == "repetition.metadiscursive_pivot_cluster" for f in findings)


def test_detects_repeated_negative_redefinition_pairs():
    text = " ".join([
        "The matrix is not a taxonomy of activities.",
        "It is an analytical device for comparing two forms of sufficiency.",
        "The analysis then considers a worked example.",
        "The contribution is not another AI-use scale.",
        "It is an account of why two warrants can diverge.",
    ])
    findings, metrics = mod.analyse_with_metrics(text)
    assert metrics["negative_redefinition_pairs"] >= 2
    assert metrics["negative_redefinition_clusters"] >= 1
    assert any(f.rule == "repetition.negative_redefinition_pair" for f in findings)



def test_isolated_generic_pivot_is_low():
    findings = mod.analyse("What matters is whether the responsibility transfer is completed.")
    matches = [f for f in findings if f.rule == "pivot.generic"]
    assert matches
    assert all(f.severity == "low" for f in matches)


def test_detects_local_generic_pivot_cluster():
    text = " ".join([
        "What matters is whether the first transfer is completed.",
        "The analysis records the next arrangement.",
        "The key point is that responsibility remains identifiable.",
        "The pathway then reaches another organisational boundary.",
        "More broadly, the same design problem recurs.",
    ])
    findings, metrics = mod.analyse_with_metrics(text)
    assert metrics["generic_pivot_clusters"] >= 1
    assert any(f.rule == "repetition.generic_pivot_cluster" for f in findings)


def test_diagnostic_question_is_not_short_standalone_pivot():
    findings = mod.analyse("What must happen next?")
    assert not any(f.rule == "pivot.short_standalone" for f in findings)


def test_bare_modal_definition_is_not_short_standalone_pivot():
    findings = mod.analyse("For transition, the next arrangement must actually take up the learner.")
    assert not any(f.rule == "pivot.short_standalone" for f in findings)


def test_detects_repeated_short_antithesis_pairs_only_at_density():
    text = " ".join([
        "The services exist.", "But the pathway is incomplete.",
        "Responsibility may move.", "It should not disappear.",
        "The final destination is similar.", "The institutional pathway is not.",
        "The policy problem is not movement.", "It is premature termination.",
        "Distribution is not the problem.", "The issue is connection.",
    ])
    findings, metrics = mod.analyse_with_metrics(text)
    assert metrics["short_antithesis_pairs"] >= 5
    assert metrics["short_antithesis_clusters"] == 1
    assert any(f.rule == "repetition.short_antithesis_pairs" for f in findings)


def test_reports_exact_sentence_repetition_as_low():
    text = " ".join([
        "Responsibility may move, but it should not disappear between functions.",
        "The analysis then considers another case.",
        "Responsibility may move, but it should not disappear between functions.",
    ])
    findings, metrics = mod.analyse_with_metrics(text)
    matches = [f for f in findings if f.rule == "repetition.exact_sentence"]
    assert matches
    assert all(f.severity == "low" for f in matches)
    assert metrics["exact_repeated_sentences"] >= 1


def test_cluster_findings_include_examples():
    text = " ".join([
        "The matrix is not a taxonomy.",
        "It is a diagnostic device.",
        "The analysis adds one example.",
        "The contribution is not another scale.",
        "It is an account of responsibility.",
    ])
    findings, _ = mod.analyse_with_metrics(text)
    matches = [f for f in findings if f.rule == "repetition.negative_redefinition_pair"]
    assert matches
    assert matches[0].excerpt


def test_ignores_reference_list_after_heading():
    text = "\n".join([
        "The analysis records one institutional arrangement.",
        "References",
        "Ministry of Education. Ministry of Education.",
        "Ministry of Education. Ministry of Education.",
    ])
    findings, metrics = mod.analyse_with_metrics(text)
    assert metrics["total_sentences"] == 1
    assert not any(f.rule == "repetition.exact_sentence" for f in findings)


def test_overlapping_negative_redefinition_chain_does_not_form_cluster():
    text = " ".join([
        "Policy does not provide a complete sequence for review.",
        "The problem is not that professional judgement remains necessary.",
        "It is how that judgement can remain defensible.",
    ])
    findings, metrics = mod.analyse_with_metrics(text)
    assert metrics["negative_redefinition_pairs"] == 1
    assert metrics["negative_redefinition_clusters"] == 0
    assert not any(f.rule == "repetition.negative_redefinition_pair" for f in findings)


def test_version_is_1_0_0():
    assert mod.VERSION == "1.0.0"
