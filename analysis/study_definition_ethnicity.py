# Import functions
from cohortextractor import (
    StudyDefinition, 
    Measure,
    patients, 
)

from codelists import *

index_date = "2020-01-01"

# Specifiy study defeinition
study = StudyDefinition(
    # Configure the expectations framework
    default_expectations={
        "date": {"earliest": "2020-01-01", "latest": "today"},
        "rate": "universal",
    },
    
    # define the study index date
    index_date = index_date,


    # This line defines the study population
    population = patients.satisfying("(NOT died) AND (registered)",        
        died = patients.died_from_any_cause(
		    on_or_before=index_date,
		    returning="binary_flag"
	    ),
        registered = patients.registered_as_of(index_date),
    ),

    age=patients.age_as_of(index_date,
        return_expectations={
        "rate" : "universal",
        "int" : {"distribution" : "population_ages"}
        }),

    age_group = patients.categorised_as({
            "0": "DEFAULT",
            "16 - under 40": """ age >= 16 AND age < 40""",
            "40 - under 50": """ age >= 40 AND age < 50""",
            "50 - under 65": """ age >= 50 AND age < 65""",
            "65 plus": """ age >=  65""", 
        },
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "16 - under 40": 0.25,
                    "40 - under 50": 0.25,
                    "50 - under 65": 0.25,
                    "65 plus": 0.25,
                }
            },
        },),

    stp = patients.registered_practice_as_of("index_date",
        returning="stp_code",
        return_expectations={
             "category": {"ratios": {"STP1": 0.5, "STP2": 0.5}},
        },),

    first_dose=patients.with_these_clinical_events(first_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),
    
    second_dose=patients.with_these_clinical_events(second_dose_code,
        returning="binary_flag",
        between = ["index_date", "index_date + 1 month"],
        return_expectations = { "incidence": 0.4 }
        ),

    ethnicity_white_british=patients.with_these_clinical_events(ethnicity_white_british_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_white_irish=patients.with_these_clinical_events(ethnicity_white_irish_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_white_other=patients.with_these_clinical_events(ethnicity_white_other_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_mixed_white_caribbean=patients.with_these_clinical_events(ethnicity_mixed_white_caribbean_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_mixed_white_african=patients.with_these_clinical_events(ethnicity_mixed_white_african_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_mixed_white_asian=patients.with_these_clinical_events(ethnicity_mixed_white_asian_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_mixed_other=patients.with_these_clinical_events(ethnicity_mixed_other_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_asian_indian=patients.with_these_clinical_events(ethnicity_asian_indian_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_asian_pak=patients.with_these_clinical_events(ethnicity_asian_pak_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_mixed_asian_bang=patients.with_these_clinical_events(ethnicity_mixed_asian_bang_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_asian_other=patients.with_these_clinical_events(ethnicity_asian_other_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_black_caribbean=patients.with_these_clinical_events(ethnicity_black_caribbean_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_black_african=patients.with_these_clinical_events(ethnicity_black_african_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_black_other=patients.with_these_clinical_events(ethnicity_black_other_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_chinese=patients.with_these_clinical_events(ethnicity_chinese_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_other=patients.with_these_clinical_events(ethnicity_other_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_non_other=patients.with_these_clinical_events(ethnicity_non_other_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_not_stated=patients.with_these_clinical_events(ethnicity_not_stated_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_not_recorded=patients.with_these_clinical_events(ethnicity_not_recorded_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity_not_given_refused=patients.with_these_clinical_events(ethnicity_not_given_refused_code,
            returning="binary_flag",
            between = ["index_date", "index_date + 1 month"],
            return_expectations = { "incidence": 0.4 }
            ),

    ethnicity = patients.categorised_as({
            "0": "DEFAULT",
            "white_british": """ (ethnicity_white_british) """,
            "white_irish": """ (ethnicity_white_irish) """,
            "white_other": """ (ethnicity_white_other) """,
            "mixed_white_caribbean": """ (ethnicity_mixed_white_caribbean) """,
            "mixed_white_african": """ (ethnicity_mixed_white_african) """, 
            "mixed_white_asian": """ (ethnicity_mixed_white_asian) """,
            "mixed_other": """ (ethnicity_mixed_other) """,
            "asian_indian": """ (ethnicity_asian_indian) """,
            "asian_pak": """ (ethnicity_asian_pak) """,
            "mixed_asian_bang": """ (ethnicity_mixed_asian_bang) """, 
            "asian_other": """ (ethnicity_asian_other) """,
            "black_caribbean": """ (ethnicity_black_caribbean) """,
            "black_african": """ (ethnicity_black_african) """,
            "black_other": """ (ethnicity_black_other) """,
            "chinese": """ (ethnicity_chinese) """, 
            "other": """ (ethnicity_other) """,
            "non_other": """ (ethnicity_non_other) """,
            "not_stated": """ (ethnicity_not_stated) """,
            "not_recorded": """ (ethnicity_not_recorded) """,
            "not_given_refused": """ (ethnicity_not_given_refused) """, 
        },
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "white_british": 0.05,
                    "white_irish": 0.05,
                    "white_other": 0.05,
                    "mixed_white_caribbean": 0.05,
                    "mixed_white_african": 0.05,
                    "mixed_white_asian": 0.05,
                    "mixed_other": 0.05,
                    "asian_indian": 0.05,
                    "asian_pak": 0.05,
                    "mixed_asian_bang": 0.05,
                    "asian_other": 0.05,
                    "black_caribbean": 0.05,
                    "black_african": 0.05,
                    "black_other": 0.05,
                    "chinese": 0.05,
                    "other": 0.05,
                    "non_other": 0.05,
                    "not_stated": 0.05,
                    "not_recorded": 0.05,
                    "not_given_refused": 0.05,
                }
            },
        },),
    )

measures = [
    Measure(id="first_dose_stp",
        numerator="first_dose",
        denominator="population",
        group_by = ["stp", "age_group", "ethnicity"]),

    Measure(id="second_dose_stp",
        numerator="second_dose",
        denominator="population",
        group_by = ["stp", "age_group", "ethnicity"]),
    ]