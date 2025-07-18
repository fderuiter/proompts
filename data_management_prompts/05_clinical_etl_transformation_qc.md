# Clinical ETL Transformation Code and QC

You are a senior statistical-programming mentor.

## Task

Write production-ready code that transforms a raw Lab Results dataset into ADLB (analysis-ready), with identical logic in R and SAS.

## Detailed instructions

1. R section: tidyverse pipeline with explicit factor handling and `vctrs::vec_c` type safety.
1. SAS section: PROC SQL + DATA step macro; include LOG checks for uninitialized variables and unit mismatches.
1. Create mirrored unit-test scripts using testthat (R) and `%assert_compare` macro (SAS) to confirm the two outputs are byte-for-byte identical on sample data.

## Output format

## R code

```r
...code...
```

## SAS code

```sas
...code...
```

## QC tests

...tests...

## Check list before finishing

- Match column order to ADaM IG v2.2
- Set all date variables to ISO-8601 (`YYYY-MM-DD`).
- Add inline comments for regulatory traceability.
