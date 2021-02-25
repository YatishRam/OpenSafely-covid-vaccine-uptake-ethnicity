from cohortextractor import (
    codelist,
    codelist_from_csv
)

# Vaccination doses
first_dose_code = codelist("COVADM1_COD", system="snomed")
second_dose_code = codelist("COVADM2_COD", system="snomed")

# Risk groups
all_riskgroup_codes = codelist_from_csv("codelists-local/all-riskgroup-disease.csv",
                                    system="snomed",
                                    column="code",)

clinical_riskgroup_codes = codelist_from_csv("codelists-local/clinical-riskgroup-disease.csv",
                                    system="snomed",
                                    column="code",)

# Ethnicity
ethnicity_white_british_code = codelist("ETH2001_WHIBRIT_COD", system="snomed")
ethnicity_white_irish_code = codelist("ETH2001_WHIIRISH_COD", system="snomed")
ethnicity_white_other_code = codelist("ETH2001_WHIOTHER_COD", system="snomed")
ethnicity_mixed_white_caribbean_code = codelist("ETH2001_MXDWHIBLKCAR_COD", system="snomed")
ethnicity_mixed_white_african_code = codelist("ETH2001_MXDWHIBLKAFR_COD", system="snomed")
ethnicity_mixed_white_asian_code = codelist("ETH2001_MXDWHIASN_COD", system="snomed")
ethnicity_mixed_other_code = codelist("ETH2001_MXDOTHER_COD", system="snomed")
ethnicity_asian_indian_code = codelist("ETH2001_ASNINDIAN_COD", system="snomed")
ethnicity_asian_pak_code = codelist("ETH2001_ASNPAK_COD", system="snomed")
ethnicity_mixed_asian_bang_code = codelist("ETH2001_ASNBANG_COD", system="snomed")
ethnicity_asian_other_code = codelist("ETH2001_ASNOTHER_COD", system="snomed")
ethnicity_black_caribbean_code = codelist("ETH2001_BLKCARIB_COD", system="snomed")
ethnicity_black_african_code = codelist("ETH2001_BLKAFRIC_COD", system="snomed")
ethnicity_black_other_code = codelist("ETH2001_BLKOTH_COD", system="snomed")
ethnicity_chinese_code = codelist("ETH2001_CHINESE_COD", system="snomed")
ethnicity_other_code = codelist("ETH2001_OTHER_COD", system="snomed")
ethnicity_non_other_code = codelist("NON_ETH2001_COD", system="snomed")
ethnicity_not_stated_code = codelist("ETH_NOTSTATED_COD", system="snomed")
ethnicity_not_recorded_code = codelist("ETH_NORECORD_COD", system="snomed")
ethnicity_not_given_refused_code = codelist("ETH_NOTGIPTREF_COD", system="snomed")

# Pregnancy
pregnant_code = codelist("PREG_COD", system="snomed")