# modules/site_management/inclusion_exclusion.py

from typing import Dict, List, Tuple

# Example inclusion/exclusion criteria for Phase II trial
INCLUSION_CRITERIA = {
    "min_age": 18,
    "max_age": 75,
    "min_weight": 40.0,  # kg
    "max_weight": 150.0, # kg
    "required_sex": None,  # can be "Male", "Female", or None (no restriction)
}

EXCLUSION_CRITERIA = {
    "exclude_conditions": [
        "HIV",
        "Hepatitis B",
        "Hepatitis C",
        "Pregnancy",
    ],
    "lab_limits": {
        "ALT": 3.0,  # > 3x ULN = exclude
        "AST": 3.0,
        "Creatinine": 2.0,
    },
}


def check_inclusion(patient: Dict) -> List[str]:
    """Check inclusion criteria. Returns a list of failed criteria."""
    failures = []

    age = patient.get("Age")
    if age is not None:
        if age < INCLUSION_CRITERIA["min_age"] or age > INCLUSION_CRITERIA["max_age"]:
            failures.append(f"Age {age} outside {INCLUSION_CRITERIA['min_age']}-{INCLUSION_CRITERIA['max_age']}")

    weight = patient.get("Weight")
    if weight is not None:
        if weight < INCLUSION_CRITERIA["min_weight"] or weight > INCLUSION_CRITERIA["max_weight"]:
            failures.append(f"Weight {weight} kg outside {INCLUSION_CRITERIA['min_weight']}-{INCLUSION_CRITERIA['max_weight']} kg")

    required_sex = INCLUSION_CRITERIA["required_sex"]
    if required_sex and patient.get("Sex") != required_sex:
        failures.append(f"Sex must be {required_sex}")

    return failures


def check_exclusion(patient: Dict) -> List[str]:
    """Check exclusion criteria. Returns a list of exclusion reasons."""
    failures = []

    # Medical conditions
    conditions = patient.get("Conditions", [])
    for cond in conditions:
        if cond in EXCLUSION_CRITERIA["exclude_conditions"]:
            failures.append(f"Excluded condition: {cond}")

    # Lab values
    labs = patient.get("Labs", {})
    for lab, limit in EXCLUSION_CRITERIA["lab_limits"].items():
        value = labs.get(lab)
        if value is not None and value > limit:
            failures.append(f"{lab} = {value} exceeds {limit}")

    return failures


def assess_eligibility(patient: Dict) -> Tuple[bool, List[str]]:
    """
    Assess patient eligibility based on inclusion/exclusion criteria.
    Returns: (eligible: bool, reasons: List[str])
    """
    reasons = []
    reasons.extend(check_inclusion(patient))
    reasons.extend(check_exclusion(patient))

    eligible = len(reasons) == 0
    return eligible, reasons


if __name__ == "__main__":
    # Example test patient
    patient_example = {
        "Patient ID": "P001",
        "Age": 65,
        "Sex": "Male",
        "Weight": 82.0,
        "Conditions": ["Hypertension"],
        "Labs": {"ALT": 1.2, "AST": 2.1, "Creatinine": 1.5},
    }

    eligible, reasons = assess_eligibility(patient_example)
    print("Eligible:", eligible)
    if not eligible:
        print("Reasons for exclusion:", reasons)
