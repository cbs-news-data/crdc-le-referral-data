"""contains shared constants"""

# race values in the data and corresponding human-readable values
RACE_VALUES = {
    "am": "American Indian/Alaska Native",
    "as": "Asian",
    "bl": "Black",
    "wh": "White",
    "hi": "Hispanic",
    "hp": "Native Hawaiian/Pacific Islander",
    "tr": "Two or More Races",
}

# arrest-related columns
ARR_COLS = [
    "SCH_DISCWDIS_ARR_IDEA_AM_F",
    "SCH_DISCWDIS_ARR_IDEA_AM_M",
    "SCH_DISCWDIS_ARR_IDEA_AS_F",
    "SCH_DISCWDIS_ARR_IDEA_AS_M",
    "SCH_DISCWDIS_ARR_IDEA_BL_F",
    "SCH_DISCWDIS_ARR_IDEA_BL_M",
    "SCH_DISCWDIS_ARR_IDEA_HI_F",
    "SCH_DISCWDIS_ARR_IDEA_HI_M",
    "SCH_DISCWDIS_ARR_IDEA_HP_F",
    "SCH_DISCWDIS_ARR_IDEA_HP_M",
    "SCH_DISCWDIS_ARR_IDEA_TR_F",
    "SCH_DISCWDIS_ARR_IDEA_TR_M",
    "SCH_DISCWDIS_ARR_IDEA_WH_F",
    "SCH_DISCWDIS_ARR_IDEA_WH_M",
    "SCH_DISCWODIS_ARR_AM_F",
    "SCH_DISCWODIS_ARR_AM_M",
    "SCH_DISCWODIS_ARR_AS_F",
    "SCH_DISCWODIS_ARR_AS_M",
    "SCH_DISCWODIS_ARR_BL_F",
    "SCH_DISCWODIS_ARR_BL_M",
    "SCH_DISCWODIS_ARR_HI_F",
    "SCH_DISCWODIS_ARR_HI_M",
    "SCH_DISCWODIS_ARR_HP_F",
    "SCH_DISCWODIS_ARR_HP_M",
    "SCH_DISCWODIS_ARR_TR_F",
    "SCH_DISCWODIS_ARR_TR_M",
    "SCH_DISCWODIS_ARR_WH_F",
    "SCH_DISCWODIS_ARR_WH_M",
    "TOT_DISCWDIS_ARR_IDEA_F",
    "TOT_DISCWDIS_ARR_IDEA_M",
    "TOT_DISCWODIS_ARR_F",
    "TOT_DISCWODIS_ARR_M",
]

# referral-related columns
REF_COLS = [
    "SCH_DISCWDIS_REF_IDEA_AM_F",
    "SCH_DISCWDIS_REF_IDEA_AM_M",
    "SCH_DISCWDIS_REF_IDEA_AS_F",
    "SCH_DISCWDIS_REF_IDEA_AS_M",
    "SCH_DISCWDIS_REF_IDEA_BL_F",
    "SCH_DISCWDIS_REF_IDEA_BL_M",
    "SCH_DISCWDIS_REF_IDEA_HI_F",
    "SCH_DISCWDIS_REF_IDEA_HI_M",
    "SCH_DISCWDIS_REF_IDEA_HP_F",
    "SCH_DISCWDIS_REF_IDEA_HP_M",
    "SCH_DISCWDIS_REF_IDEA_TR_F",
    "SCH_DISCWDIS_REF_IDEA_TR_M",
    "SCH_DISCWDIS_REF_IDEA_WH_F",
    "SCH_DISCWDIS_REF_IDEA_WH_M",
    "SCH_DISCWODIS_REF_AM_F",
    "SCH_DISCWODIS_REF_AM_M",
    "SCH_DISCWODIS_REF_AS_F",
    "SCH_DISCWODIS_REF_AS_M",
    "SCH_DISCWODIS_REF_BL_F",
    "SCH_DISCWODIS_REF_BL_M",
    "SCH_DISCWODIS_REF_HI_F",
    "SCH_DISCWODIS_REF_HI_M",
    "SCH_DISCWODIS_REF_HP_F",
    "SCH_DISCWODIS_REF_HP_M",
    "SCH_DISCWODIS_REF_TR_F",
    "SCH_DISCWODIS_REF_TR_M",
    "SCH_DISCWODIS_REF_WH_F",
    "SCH_DISCWODIS_REF_WH_M",
    "TOT_DISCWDIS_REF_IDEA_F",
    "TOT_DISCWDIS_REF_IDEA_M",
    "TOT_DISCWODIS_REF_F",
    "TOT_DISCWODIS_REF_M",
]

# enrollment-related columns
ENR_COLS = [
    "SCH_ENR_AM_F",
    "SCH_ENR_AM_M",
    "SCH_ENR_AS_F",
    "SCH_ENR_AS_M",
    "SCH_ENR_BL_F",
    "SCH_ENR_BL_M",
    "SCH_ENR_HI_F",
    "SCH_ENR_HI_M",
    "SCH_ENR_HP_F",
    "SCH_ENR_HP_M",
    "SCH_ENR_TR_F",
    "SCH_ENR_TR_M",
    "SCH_ENR_WH_F",
    "SCH_ENR_WH_M",
    "SCH_IDEAENR_AM_F",
    "SCH_IDEAENR_AM_M",
    "SCH_IDEAENR_AS_F",
    "SCH_IDEAENR_AS_M",
    "SCH_IDEAENR_BL_F",
    "SCH_IDEAENR_BL_M",
    "SCH_IDEAENR_HI_F",
    "SCH_IDEAENR_HI_M",
    "SCH_IDEAENR_HP_F",
    "SCH_IDEAENR_HP_M",
    "SCH_IDEAENR_TR_F",
    "SCH_IDEAENR_TR_M",
    "SCH_IDEAENR_WH_F",
    "SCH_IDEAENR_WH_M",
    "TOT_ENR_F",
    "TOT_ENR_M",
    "TOT_IDEAENR_F",
    "TOT_IDEAENR_M",
]

# school characteristics-related columns
CHAR_COLS = ["SCH_STATUS_ALT"]

# columns containing grade data
GRADE_COLS = [
    "SCH_GRADE_G01",
    "SCH_GRADE_G02",
    "SCH_GRADE_G03",
    "SCH_GRADE_G04",
    "SCH_GRADE_G05",
    "SCH_GRADE_G06",
    "SCH_GRADE_G07",
    "SCH_GRADE_G08",
    "SCH_GRADE_G09",
    "SCH_GRADE_G10",
    "SCH_GRADE_G11",
    "SCH_GRADE_G12",
]

# text columns contained in all segmented files
INDEX_COLS = [
    "COMBOKEY",
    "LEA_STATE",
    "LEAID",
    "LEA_NAME",
    "SCHID",
    "SCH_NAME",
    "JJ",
]

# columns that contain text data used in this analysis
TEXT_COLS = INDEX_COLS + CHAR_COLS + GRADE_COLS

# all numeric columns to select from input files
NUMERIC_COLS = ENR_COLS + ARR_COLS + REF_COLS

# all columns to select from input files
USE_COLS = TEXT_COLS + NUMERIC_COLS
