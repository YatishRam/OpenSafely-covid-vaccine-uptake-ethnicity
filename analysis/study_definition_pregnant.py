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
    population = patients.satisfying("(NOT died) AND (registered) AND (pregnant) AND age >= 16",        
        died = patients.died_from_any_cause(
		    on_or_before=index_date,
		    returning="binary_flag"
	    ),
        registered = patients.registered_as_of(index_date),
        pregnant = patients.with_these_clinical_events(pregnant_code,
                                                between = ["index_date", "index_date + 1 month"],
                                                returning="binary_flag",
                                                return_expectations= { "incidence": 0.6 },),
    ),

    age=patients.age_as_of(index_date,
        return_expectations={
        "rate" : "universal",
        "int" : {"distribution" : "population_ages"}
        }),



    clinical_riskgroup = patients.with_these_clinical_events(clinical_riskgroup_codes,
                                                    between = ["index_date", "index_date + 1 month"],
                                                    returning="binary_flag",
                                                    #return_expectations= { "incidence": 0.6 },),
                                                            return_expectations={
             "category": {"ratios": {"0": 0.5, "1": 0.5}},
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
    )

measures = [
    Measure(id="first_dose_stp",
        numerator="first_dose",
        denominator="population",
        group_by = ["stp", "clinical_riskgroup"]),

    Measure(id="second_dose_stp",
        numerator="second_dose",
        denominator="population",
        group_by = ["stp", "clinical_riskgroup"]),
    ]
