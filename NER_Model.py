# TRAIN_DATA = [
#     {"sentence": "I love using ggplot2 for data visualization in R.", "entities": [{"start": 16,"end" : 23, "label": "R_PACKAGE"}]},
#     {
#     "sentence": "Shiny is a fantastic R package for building web applications.",
#     "entities": [
#       {"start": 0, "end": 5, "label": "PACKAGE_NAME"},
#     ]
#     },
#     {
#     "sentence": "I frequently use lubridate for handling date-time data in R.",
#     "entities": [
#       {"start": 25, "end": 33, "label": "PACKAGE_NAME"},
#     ]
#     },
#     {
#     "sentence": "tidyr is a helpful package for data tidying tasks.",
#     "entities": [
#       {"start": 0, "end": 5, "label": "PACKAGE_NAME"},
#     ]
#   },
#     {
#     "sentence": "dplyr is a popular package for data manipulation in R.",
#     "entities": [
#       {"start": 0, "end": 5, "label": "PACKAGE_NAME"},
#     ]
#   },
#   {
#     "sentence": "We utilized the 'BiocVersion' package to manage and query Bioconductor version information.",
#     "entities": [
#       {"start": 18, "end": 30, "label": "PACKAGE_NAME"},
#       {"start": 62, "end": 75, "label": "SOFTWARE_NAME"}
#     ]
#   },
#   {
#     "sentence": "Data manipulation tasks were performed efficiently with the help of the 'dplyr' package.",
#     "entities": [
#       {"start": 61, "end": 66, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "In our analysis pipeline, we relied on the 'tidyverse' package for data cleaning and visualization.",
#     "entities": [
#       {"start": 41, "end": 50, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "Genome annotation and manipulation were facilitated using the 'GenomicRanges' and 'GenomicFeatures' packages.",
#     "entities": [
#       {"start": 60, "end": 75, "label": "PACKAGE_NAME"},
#       {"start": 80, "end": 96, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The 'DESeq2' package played a crucial role in differential gene expression analysis.",
#     "entities": [
#       {"start": 4, "end": 11, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "For network analysis, we employed the 'igraph' package to study interactions among genes.",
#     "entities": [
#       {"start": 34, "end": 40, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The 'ggplot2' package allowed us to create visually appealing and informative plots.",
#     "entities": [
#       {"start": 4, "end": 11, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "Quality control of sequencing data was conducted using the 'Rqc' package.",
#     "entities": [
#       {"start": 52, "end": 56, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "Functional enrichment analysis was performed using the 'clusterProfiler' package.",
#     "entities": [
#       {"start": 44, "end": 59, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The 'limma' package was employed for linear modeling and differential expression analysis.",
#     "entities": [
#       {"start": 4, "end": 9, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "We used the 'Seurat' package for single-cell RNA sequencing data analysis.",
#     "entities": [
#       {"start": 8, "end": 14, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "To fetch and manage biological data, the 'biomaRt' package was a valuable resource.",
#     "entities": [
#       {"start": 33, "end": 41, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The 'edgeR' package was instrumental in identifying differentially expressed genes.",
#     "entities": [
#       {"start": 4, "end": 9, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "We employed the 'KEGGREST' package to access KEGG pathway information.",
#     "entities": [
#       {"start": 13, "end": 21, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The 'ggcyto' package was used for cytometry data analysis and visualization.",
#     "entities": [
#       {"start": 4, "end": 11, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "Data exploration and visualization were performed using the 'ggplot2' and 'ggpubr' packages.",
#     "entities": [
#       {"start": 54, "end": 61, "label": "PACKAGE_NAME"},
#       {"start": 66, "end": 73, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The 'Bioconductor' package ecosystem provided a comprehensive toolkit for genomics research.",
#     "entities": [
#       {"start": 4, "end": 16, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "To assess and visualize single-cell data, we used the 'scater' and 'scran' packages for a holistic analysis.",
#     "entities": [
#       {"start": 42, "end": 48, "label": "PACKAGE_NAME"},
#       {"start": 53, "end": 59, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "Functional annotation of genes was carried out using the 'AnnotationDbi' package.",
#     "entities": [
#       {"start": 42, "end": 55, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "We integrated multiple omics datasets with the 'multiMiR' package for a holistic analysis.",
#     "entities": [
#       {"start": 54, "end": 61, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "We conducted APC analysis using the 'APCanalysis' package.",
#     "entities": [
#       {"start": 34, "end": 46, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The 'APCI' method was applied to the data using the 'apcf' package.",
#     "entities": [
#       {"start": 4, "end": 8, "label": "SOFTWARE_NAME"},
#       {"start": 52, "end": 56, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "We performed clustering analysis with the 'apcluster' package.",
#     "entities": [
#       {"start": 38, "end": 47, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "A principal coordinate analysis (PCoA) was carried out using 'aPCoA'.",
#     "entities": [
#       {"start": 48, "end": 53, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "APC analysis results were visualized using 'APCtools'.",
#     "entities": [
#       {"start": 38, "end": 46, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The 'apexcharter' package was used for interactive charting.",
#     "entities": [
#       {"start": 4, "end": 14, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The 'APFr' library provided useful functions for financial analysis.",
#     "entities": [
#       {"start": 4, "end": 9, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "Aphid population dynamics were studied using 'aphid'.",
#     "entities": [
#       {"start": 39, "end": 44, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "Phylogenetic analysis was conducted with 'aphylo'.",
#     "entities": [
#       {"start": 32, "end": 38, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "API data was transformed into LM objects using 'api2lm'.",
#     "entities": [
#       {"start": 46, "end": 52, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "We used 'BayesARIMAX' for time series forecasting.",
#     "entities": [
#       {"start": 7, "end": 17, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "Bayesian analysis was performed using the 'bayesm' package.",
#     "entities": [
#       {"start": 38, "end": 45, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The 'bcp' package was employed for Bayesian change point analysis.",
#     "entities": [
#       {"start": 4, "end": 7, "label": "PACKAGE_NAME"},
#       {"start": 35, "end": 38, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "We utilized the 'beeswarm' package for data visualization.",
#     "entities": [
#       {"start": 15, "end": 23, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "Beta regression was performed using 'betareg'.",
#     "entities": [
#       {"start": 29, "end": 36, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The 'bfast' package was used for land change monitoring.",
#     "entities": [
#       {"start": 4, "end": 8, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "We employed 'BFS' for efficient breadth-first search.",
#     "entities": [
#       {"start": 12, "end": 15, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "Bayesian hierarchical modeling was done using 'bggAnalytics'.",
#     "entities": [
#       {"start": 38, "end": 50, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The 'BCA1SG' package is widely used in bioinformatics.",
#     "entities": [
#       {"start": 5, "end": 11, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "We implemented the 'bcaboot' package for bootstrap analysis.",
#     "entities": [
#       {"start": 19, "end": 27, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "Bayesian network modeling was performed using 'BayesianNetwork'.",
#     "entities": [
#       {"start": 45, "end": 61, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The 'bfast' package is commonly used for satellite image analysis.",
#     "entities": [
#       {"start": 4, "end": 8, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "We utilized 'beautier' for data preprocessing and cleaning.",
#     "entities": [
#       {"start": 11, "end": 18, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "'BET' is a versatile package for Bayesian econometric analysis.",
#     "entities": [
#       {"start": 1, "end": 4, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The 'BetaBit' package provides tools for beta regression.",
#     "entities": [
#       {"start": 4, "end": 11, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "In machine learning, 'betaclass' is often used for classification tasks.",
#     "entities": [
#       {"start": 20, "end": 28, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The BCA1SG package is a powerful tool in bioinformatics.",
#     "entities": [
#       {"start": 4, "end": 10, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The bayesAB method is used for probabilistic analysis.",
#     "entities": [
#       {"start": 4, "end": 10, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "We employed bayesammi to assess mutual information.",
#     "entities": [
#       {"start": 12, "end": 20, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "BayesARIMAX is a popular choice for time series modeling.",
#     "entities": [
#       {"start": 0, "end": 10, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The bayesassurance library provides reliability analysis tools.",
#     "entities": [
#       {"start": 4, "end": 18, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "BayesBEKK is commonly used for financial risk assessment.",
#     "entities": [
#       {"start": 0, "end": 9, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The BayesCACE package is essential for causal inference.",
#     "entities": [
#       {"start": 4, "end": 13, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "Bayesian network analysis is facilitated by BayesNetBP.",
#     "entities": [
#       {"start": 35, "end": 44, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The ARDL package is a powerful tool for autoregressive distributed lag analysis.",
#     "entities": [
#       {"start": 4, "end": 8, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The ARpLMEC library is used for modeling ecological data with mixed-effects models.",
#     "entities": [
#       {"start": 4, "end": 13, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The armada package provides tools for analyzing and visualizing marine ecosystem data.",
#     "entities": [
#       {"start": 4, "end": 10, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "BayesGPfit is a Bayesian method for Gaussian process regression.",
#     "entities": [
#       {"start": 0, "end": 10, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The BayesGWQS package is essential for genome-wide quantitative trait analysis.",
#     "entities": [
#       {"start": 4, "end": 13, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "Behaviorchange is a versatile R package for studying behavior change interventions.",
#     "entities": [
#       {"start": 0, "end": 14, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "The beeswarm library is commonly used for creating bee swarm plots.",
#     "entities": [
#       {"start": 4, "end": 12, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {
#     "sentence": "BET is a popular R package for Bayesian estimation of the treatment effect.",
#     "entities": [
#       {"start": 0, "end": 2, "label": "PACKAGE_NAME"}
#     ]
#   },
#   {"sentence": "ARCensReg is a package for fitting accelerated failure time models with censored data.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "ArchaeoChron is a package for Bayesian age-depth modeling.", "entities": [{"start": 0, "end": 11, "label": "PACKAGE_NAME"}]},
#   {"sentence": "ArchaeoPhases is a package for analyzing phases in archaeological data.", "entities": [{"start": 0, "end": 12, "label": "PACKAGE_NAME"}]},
#   {"sentence": "archdata is a package for analyzing archaeological data.", "entities": [{"start": 0, "end": 7, "label": "PACKAGE_NAME"}]},
#   {"sentence": "archeofrag is a package for measuring archaeological site fragmentation.", "entities": [{"start": 0, "end": 9, "label": "PACKAGE_NAME"}]},
#   {"sentence": "archeoViz is a package for visualizing archaeological data.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "archetypal is a package for finding archetypal analysis solutions.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "archetyper is a package for calculating and visualizing archetypal analysis solutions.", "entities": [{"start": 0, "end": 9, "label": "PACKAGE_NAME"}]},
#   {"sentence": "archetypes is a package for visualizing archetypal analysis solutions.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "archiDART is a package for assessing architectural traits of plant root systems.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "archive is a package for managing file archives.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]},
#   {"sentence": "archiveRetriever is a package for retrieving archived web pages.", "entities": [{"start": 0, "end": 15, "label": "PACKAGE_NAME"}]},
#   {"sentence": "archivist is a package for managing and sharing data analysis artifacts.", "entities": [{"start": 0, "end": 9, "label": "PACKAGE_NAME"}]},
#   {"sentence": "archivist.github is a package for integrating archivist with GitHub.", "entities": [{"start": 0, "end": 17, "label": "PACKAGE_NAME"}]},
#   {"sentence": "ArCo is a package for creating annotated connection networks.", "entities": [{"start": 0, "end": 4, "label": "PACKAGE_NAME"}]},
#   {"sentence": "ARCokrig is a package for fitting kriging models with censored data.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "arcpullr is a package for retrieving data from ArcGIS REST APIs.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "arctools is a package for managing and analyzing Arctic sea ice data.", "entities": [{"start": 0, "end": 7, "label": "PACKAGE_NAME"}]},
#   {"sentence": "ArDec is a package for performing arithmetic decoding.", "entities": [{"start": 0, "end": 4, "label": "PACKAGE_NAME"}]},
#   {"sentence": "ARDL is a package for estimating autoregressive distributed lag models.", "entities": [{"start": 0, "end": 3, "label": "PACKAGE_NAME"}]},
#   {"sentence": "ardl.nardl is a package for estimating nonlinear autoregressive distributed lag models.", "entities": [{"start": 0, "end": 9, "label": "PACKAGE_NAME"}]},
#   {"sentence": "ards is a package for analyzing and modeling acute respiratory distress syndrome (ARDS) data.", "entities": [{"start": 0, "end": 3, "label": "PACKAGE_NAME"}]},
#   {"sentence": "area is a package for computing the area under the receiver operating characteristic (ROC) curve.", "entities": [{"start": 0, "end": 4, "label": "PACKAGE_NAME"}]},
#   {"sentence": "areabiplot is a package for creating area biplots.", "entities": [{"start": 0, "end": 9, "label": "PACKAGE_NAME"}]},
#   {"sentence": "areal is a package for spatial data analysis and geostatistics.", "entities": [{"start": 0, "end": 5, "label": "PACKAGE_NAME"}]},
#   {"sentence": "arealDB is a package for managing and analyzing spatial databases.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]},
#   {"sentence": "areaplot is a package for creating area plots.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "arena2r is a package for accessing and analyzing data from the Arena database.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]},
#   {"sentence": "arenar is a package for simulating and analyzing arena-based experiments.", "entities": [{"start": 0, "end": 5, "label": "PACKAGE_NAME"}]},
#   {"sentence": "An R package for working with HTML tables and data frames is htmldf.", "entities": [{"start": 48, "end": 54, "label": "PACKAGE_NAME"}]},
#   {"sentence": "htmlTable allows you to create HTML tables from data frames in R.", "entities": [{"start": 0, "end": 9, "label": "PACKAGE_NAME"}]},
#   {"sentence": "In R, you can use htmltools for creating and rendering HTML content.", "entities": [{"start": 15, "end": 24, "label": "PACKAGE_NAME"}]},
#   {"sentence": "HTMLUtils is a package in R that handles HTML-related tasks.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "Create interactive web widgets in R using the popular package htmlwidgets.", "entities": [{"start": 41, "end": 52, "label": "PACKAGE_NAME"}]},
#   {"sentence": "For high-throughput RNA sequencing analysis, consider using HTRX in R.", "entities": [{"start": 50, "end": 54, "label": "PACKAGE_NAME"}]},
#   {"sentence": "hts is the go-to R package for hierarchical and grouped time series forecasting.", "entities": [{"start": 0, "end": 3, "label": "PACKAGE_NAME"}]},
#   {"sentence": "Cluster hierarchical time series data efficiently with HTSCluster in R.", "entities": [{"start": 41, "end": 51, "label": "PACKAGE_NAME"}]},
#   {"sentence": "Analyze high-throughput sequencing data easily with htsr in R.", "entities": [{"start": 45, "end": 49, "label": "PACKAGE_NAME"}]},
#   {"sentence": "HTSSIP is an R package designed for analyzing microbial community sequencing data.", "entities": [{"start": 0, "end": 5, "label": "PACKAGE_NAME"}]},
#   {"sentence": "High-throughput toxicity testing data analysis can be done using HTT in R.", "entities": [{"start": 53, "end": 57, "label": "PACKAGE_NAME"}]},
#   {"sentence": "Work with hypertriglyceridemia data in R using the httk package.", "entities": [{"start": 48, "end": 52, "label": "PACKAGE_NAME"}]},
#   {"sentence": "httpcache is a useful package in R for caching HTTP requests.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "Handle HTTP status codes effectively with the httpcode R package.", "entities": [{"start": 36, "end": 43, "label": "PACKAGE_NAME"}]},
#   {"sentence": "Download files using HTTP conveniently with the httpgd R package.", "entities": [{"start": 38, "end": 44, "label": "PACKAGE_NAME"}]},
#   {"sentence": "Consider using ICvectorfields for vector field analysis in R.", "entities": [{"start": 19, "end": 33, "label": "PACKAGE_NAME"}]},
#   {"sentence": "Apply exteriorMatch to perform exterior matching in your data analysis.", "entities": [{"start": 6, "end": 19, "label": "PACKAGE_NAME"}]},
#   {"sentence": "rBiasCorrection is a handy package for bias correction in statistical modeling.", "entities": [{"start": 0, "end": 15, "label": "PACKAGE_NAME"}]},
#   {"sentence": "logitr is an R package designed for logistic regression modeling.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]},
#   {"sentence": "ODEsensitivity allows you to perform sensitivity analysis on ODE models.", "entities": [{"start": 0, "end": 13, "label": "PACKAGE_NAME"}]},
#   {"sentence": "risks is an R package for risk assessment and management.", "entities": [{"start": 0, "end": 5, "label": "PACKAGE_NAME"}]},
#   {"sentence": "lsei is a package in R for solving linear least-squares problems.", "entities": [{"start": 0, "end": 3, "label": "PACKAGE_NAME"}]},
#   {"sentence": "vmdTDNN is an R package for time-delay neural network modeling.", "entities": [{"start": 0, "end": 7, "label": "PACKAGE_NAME"}]},
#   {"sentence": "glmnetcr is a package for fitting elastic net models in R.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "EpiILM is an R package for epidemiological modeling.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]},
#   {"sentence": "Google traffic data can be accessed and analyzed using the googletraffic package in R.", "entities": [{"start": 61, "end": 75, "label": "PACKAGE_NAME"}]},
#   {"sentence": "Packager is a utility package in R for managing and installing packages.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "Use metaMA for meta-analysis of microarray data in R.", "entities": [{"start": 4, "end": 10, "label": "PACKAGE_NAME"}]},
#   {"sentence": "vfinputs is an R package for validating and formatting inputs.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "Motif analysis can be performed using the motif package in R.", "entities": [{"start": 47, "end": 52, "label": "PACKAGE_NAME"}]},
#   {"sentence": "MicEconCES is a comprehensive R package for microeconomic analysis.", "entities": [{"start": 0, "end": 10, "label": "PACKAGE_NAME"}]},
#   {"sentence": "The GIFTr package simplifies gift-giving analysis in R.", "entities": [{"start": 4, "end": 9, "label": "PACKAGE_NAME"}]},
#   {"sentence": "Use the 'runonce' package to execute code blocks once in R.", "entities": [{"start": 9, "end": 17, "label": "PACKAGE_NAME"}]},
#   {"sentence": "OmegaG is a versatile package for omega-3 fatty acid analysis in R.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]},
#   {"sentence": "ImpactEffectsize helps assess the impact effect size in R.", "entities": [{"start": 0, "end": 16, "label": "PACKAGE_NAME"}]},
#   {"sentence": "With parmigene, you can perform parametric gene expression analysis in R.", "entities": [{"start": 5, "end": 14, "label": "PACKAGE_NAME"}]},
#   {"sentence": "sarp.snowprofile.alignment provides alignment tools for snow profile data in R.", "entities": [{"start": 0, "end": 24, "label": "PACKAGE_NAME"}]},
#   {"sentence": "scUtils is a package that simplifies single-cell analysis workflows in R.", "entities": [{"start": 0, "end": 7, "label": "PACKAGE_NAME"}]},
#   {"sentence": "mARP is a package for multi-objective optimization problems in R.", "entities": [{"start": 0, "end": 4, "label": "PACKAGE_NAME"}]},
#   {"sentence": "RSauceLabs is a useful R package for interacting with Sauce Labs services.", "entities": [{"start": 0, "end": 11, "label": "PACKAGE_NAME"}]},
#   {"sentence": "Use prepdat to preprocess and clean your data efficiently in R.", "entities": [{"start": 4, "end": 11, "label": "PACKAGE_NAME"}]},
#   {"sentence": "grattanInflators provides inflation rates data from Grattan Institute in R.", "entities": [{"start": 0, "end": 16, "label": "PACKAGE_NAME"}]},
#   {"sentence": "With npboottprm, perform non-parametric bootstrapping in R.", "entities": [{"start": 5, "end": 15, "label": "PACKAGE_NAME"}]},
#   {"sentence": "qqtest is a package that simplifies quantile-quantile testing in R.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]},
#   {"sentence": "PhaseType is an R package for phase-type distribution modeling.", "entities": [{"start": 0, "end": 9, "label": "PACKAGE_NAME"}]},
#   {"sentence": "lsm is a lightweight statistical modeling package for R.", "entities": [{"start": 0, "end": 2, "label": "PACKAGE_NAME"}]},
#   {"sentence": "lolliplot allows you to create lollipop plots in R easily.", "entities": [{"start": 0, "end": 9, "label": "PACKAGE_NAME"}]},
#   {"sentence": "wpp2008 is a package that provides World Population Prospects data in R.", "entities": [{"start": 0, "end": 7, "label": "PACKAGE_NAME"}]},
#   {"sentence": "pryr is a package for inspecting and testing R code efficiently.", "entities": [{"start": 0, "end": 4, "label": "PACKAGE_NAME"}]},
#   {"sentence": "filterNHP simplifies non-homogeneous Poisson process filtering in R.", "entities": [{"start": 0, "end": 10, "label": "PACKAGE_NAME"}]},
#   {"sentence": "AzureQstor is an R package for working with Azure Queue Storage.", "entities": [{"start": 0, "end": 9, "label": "PACKAGE_NAME"}]},
#   {"sentence": "readNSx is a package for reading and analyzing Neuralynx NSx files in R.", "entities": [{"start": 0, "end": 7, "label": "PACKAGE_NAME"}]},
#   {"sentence": "brio is a lightweight package for reading and writing data in R.", "entities": [{"start": 0, "end": 4, "label": "PACKAGE_NAME"}]},
#   {"sentence": "hysteresis is a package for analyzing and modeling hysteresis phenomena in R.", "entities": [{"start": 0, "end": 10, "label": "PACKAGE_NAME"}]},
#   {"sentence": "maptools is a versatile R package for working with spatial data.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "visdat is a package that simplifies visualizing data frames in R.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]},
#   {"sentence": "caretForecast extends the capabilities of the 'caret' package for forecasting.", "entities": [{"start": 0, "end": 14, "label": "PACKAGE_NAME"}]},
#   {"sentence": "mind is a package for multi-information integration and visualization in R.", "entities": [{"start": 0, "end": 4, "label": "PACKAGE_NAME"}]},
#   {"sentence": "opencpu is an R package for embedding and interfacing with OpenCPU.", "entities": [{"start": 0, "end": 7, "label": "PACKAGE_NAME"}]},
#   {"sentence": "datetoiso is a package that converts dates to ISO8601 format in R.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "Use 'here' for easy management of file paths and directories in R.", "entities": [{"start": 4, "end": 9, "label": "PACKAGE_NAME"}]},
#   {"sentence": "IMIX is a package that simplifies mixture modeling in R.", "entities": [{"start": 0, "end": 4, "label": "PACKAGE_NAME"}]},
#   {"sentence": "leaflet.extras provides additional features for creating leaflet maps in R.", "entities": [{"start": 0, "end": 14, "label": "PACKAGE_NAME"}]},
#   {"sentence": "With shinytest2, you can perform testing and automation of Shiny apps.", "entities": [{"start": 5, "end": 15, "label": "PACKAGE_NAME"}]},
#   {"sentence": "independenceWeights is an R package for weighted independence testing.", "entities": [{"start": 0, "end": 19, "label": "PACKAGE_NAME"}]},
#   {"sentence": "wally is a package for generating random wallpapers in R.", "entities": [{"start": 0, "end": 5, "label": "PACKAGE_NAME"}]},
#   {"sentence": "rbmn simplifies the computation of Bayesian network models in R.", "entities": [{"start": 0, "end": 4, "label": "PACKAGE_NAME"}]},
#   {"sentence": "sphet is an R package for spatial econometric modeling.", "entities": [{"start": 0, "end": 5, "label": "PACKAGE_NAME"}]},
#   {"sentence": "REPPlabShiny offers a Shiny app interface for REPPlab in R.", "entities": [{"start": 0, "end": 13, "label": "PACKAGE_NAME"}]},
#   {"sentence": "CPBayes is a package for Bayesian analysis of change points in R.", "entities": [{"start": 0, "end": 7, "label": "PACKAGE_NAME"}]},
#   {"sentence": "higrad provides tools for high-dimensional gradient-based optimization in R.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]},
#   {"sentence": "iotarelr is an R package for computing the Iota matrix.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "Partiallyoverlapping allows you to analyze partially overlapping datasets in R.", "entities": [{"start": 0, "end": 18, "label": "PACKAGE_NAME"}]},
#   {"sentence": "rbi.helpers is a package that provides utility functions for RBI analysis in R.", "entities": [{"start": 0, "end": 11, "label": "PACKAGE_NAME"}]},
#   {"sentence": "TwoSampleTest.HD is an R package for two-sample hypothesis testing.", "entities": [{"start": 0, "end": 15, "label": "PACKAGE_NAME"}]},
#   {"sentence": "RcmdrPlugin.RiskDemo is a plugin for the R Commander GUI with risk analysis tools.", "entities": [{"start": 0, "end": 22, "label": "PACKAGE_NAME"}]},
#   {"sentence": "BatchExperiments simplifies the management of batch processing experiments in R.", "entities": [{"start": 0, "end": 15, "label": "PACKAGE_NAME"}]},
#   {"sentence": "xmlconvert is an R package for converting XML data to other formats.", "entities": [{"start": 0, "end": 10, "label": "PACKAGE_NAME"}]},
#   {"sentence": "NMMIPW offers non-parametric marginal maximum likelihood estimation in R.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]},
#   {"sentence": "hpiR is a comprehensive package for hydrogeophysical data analysis in R.", "entities": [{"start": 0, "end": 4, "label": "PACKAGE_NAME"}]},
#   {"sentence": "rankFD provides methods for ranking features in high-dimensional data in R.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]},
#   {"sentence": "HaploCatcher is an R package for haplotype-based association analysis.", "entities": [{"start": 0, "end": 12, "label": "PACKAGE_NAME"}]},
#   {"sentence": "afthd is a package for after the fact high-dimensional data analysis in R.", "entities": [{"start": 0, "end": 5, "label": "PACKAGE_NAME"}]},
#   {"sentence": "mlfit is an R package for maximum likelihood estimation of mixed-effects models.", "entities": [{"start": 0, "end": 5, "label": "PACKAGE_NAME"}]},
#   {"sentence": "springer is a package that provides easy access to Springer's publications.", "entities": [{"start": 0, "end": 7, "label": "PACKAGE_NAME"}]},
#   {"sentence": "nlsic simplifies non-linear regression models in R.", "entities": [{"start": 0, "end": 4, "label": "PACKAGE_NAME"}]},
#   {"sentence": "powRICLPM is an R package for power analysis of random intercept cross-lagged panel models.", "entities": [{"start": 0, "end": 9, "label": "PACKAGE_NAME"}]},
#   {"sentence": "netdiffuseR provides tools for analyzing and visualizing diffusion networks in R.", "entities": [{"start": 0, "end": 11, "label": "PACKAGE_NAME"}]},
#   {"sentence": "modMax is a package for modeling and optimizing the maxima of a function in R.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]},
#   {"sentence": "CAMML is an R package for fitting conditional autoregressive models for spatial data.", "entities": [{"start": 0, "end": 5, "label": "PACKAGE_NAME"}]},
#   {"sentence": "SDLfilter is a package for smoothing and denoising in spatial data analysis in R.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "RAthena is an R package for interacting with Amazon Athena.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]},
#   {"sentence": "DataFakeR generates synthetic data for testing and experimentation in R.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "FAVAR is an R package for estimating factor-augmented VAR models.", "entities": [{"start": 0, "end": 5, "label": "PACKAGE_NAME"}]},
#   {"sentence": "befproj is an R package for Bayesian effect projection.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]},
#   {"sentence": "FSAtools provides various tools for fisheries stock assessment in R.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "UNPaC is a package for creating and analyzing Unicode character n-grams in R.", "entities": [{"start": 0, "end": 5, "label": "PACKAGE_NAME"}]},
#   {"sentence": "ringostat is an R package for working with Ringostat API.", "entities": [{"start": 0, "end": 9, "label": "PACKAGE_NAME"}]},
#   {"sentence": "visNetwork is an R package for creating interactive network visualizations.", "entities": [{"start": 0, "end": 10, "label": "PACKAGE_NAME"}]},
#   {"sentence": "R.huge is a package that simplifies working with large datasets in R.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]},
#   {"sentence": "RNetLogo provides an interface to the NetLogo modeling environment in R.", "entities": [{"start": 0, "end": 8, "label": "PACKAGE_NAME"}]},
#   {"sentence": "LPower is a package for power analysis of linear models in R.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]},
#   {"sentence": "promote is an R package for promotion of R packages.", "entities": [{"start": 0, "end": 6, "label": "PACKAGE_NAME"}]}
# ]

TRAIN_DATA = [
    ("I love using ggplot2 for data visualization in R.", {"entities": [(16, 23, "R_PACKAGE")]}),
    ("ARCensReg is a package for fitting accelerated failure time models with censored data.", {"entities": [(0, 8, "R_PACKAGE")]}),
    ("ArchaeoChron is a package for Bayesian age-depth modeling.", {"entities": [(0, 11, "R_PACKAGE")]}),
    ("ArchaeoPhases is a package for analyzing phases in archaeological data.", {"entities": [(0, 12, "R_PACKAGE")]}),
    ("archdata is a package for analyzing archaeological data.", {"entities": [(0, 7, "R_PACKAGE")]}),
    ("archeofrag is a package for measuring archaeological site fragmentation.", {"entities": [(0, 9, "R_PACKAGE")]}),
    ("archeoViz is a package for visualizing archaeological data.", {"entities": [(0, 8, "R_PACKAGE")]}),
    ("archetypal is a package for finding archetypal analysis solutions.", {"entities": [(0, 8, "R_PACKAGE")]}),
    ("archetyper is a package for calculating and visualizing archetypal analysis solutions.", {"entities": [(0, 9, "R_PACKAGE")]}),
    ("archetypes is a package for visualizing archetypal analysis solutions.", {"entities": [(0, 8, "R_PACKAGE")]}),
    ("archiDART is a package for assessing architectural traits of plant root systems.", {"entities": [(0, 8, "R_PACKAGE")]}),
    ("archive is a package for managing file archives.", {"entities": [(0, 6, "R_PACKAGE")]}),
    ("archiveRetriever is a package for retrieving archived web pages.", {"entities": [(0, 15, "R_PACKAGE")]}),
    ("archivist is a package for managing and sharing data analysis artifacts.", {"entities": [(0, 9, "R_PACKAGE")]}),
    ("archivist.github is a package for integrating archivist with GitHub.", {"entities": [(0, 17, "R_PACKAGE")]}),
    ("ArCo is a package for creating annotated connection networks.", {"entities": [(0, 4, "R_PACKAGE")]}),
    ("ARCokrig is a package for fitting kriging models with censored data.", {"entities": [(0, 8, "R_PACKAGE")]}),
    ("arcpullr is a package for retrieving data from ArcGIS REST APIs.", {"entities": [(0, 8, "R_PACKAGE")]}),
    ("arctools is a package for managing and analyzing Arctic sea ice data.", {"entities": [(0, 7, "R_PACKAGE")]}),
    ("ArDec is a package for performing arithmetic decoding.", {"entities": [(0, 4, "R_PACKAGE")]}),
    ("ARDL is a package for estimating autoregressive distributed lag models.", {"entities": [(0, 3, "R_PACKAGE")]}),
    ("ardl.nardl is a package for estimating nonlinear autoregressive distributed lag models.", {"entities": [(0, 9, "R_PACKAGE")]}),
    ("ards is a package for analyzing and modeling acute respiratory distress syndrome (ARDS) data.", {"entities": [(0, 3, "R_PACKAGE")]}),
    ("area is a package for computing the area under the receiver operating characteristic (ROC) curve.", {"entities": [(0, 4, "R_PACKAGE")]}),
    ("areabiplot is a package for creating area biplots.", {"entities": [(0, 9, "R_PACKAGE")]}),
    ("areal is a package for spatial data analysis and geostatistics.", {"entities": [(0, 5, "R_PACKAGE")]}),
    ("arealDB is a package for managing and analyzing spatial databases.", {"entities": [(0, 6, "R_PACKAGE")]}),
    ("areaplot is a package for creating area plots.", {"entities": [(0, 8, "R_PACKAGE")]}),
    ("arena2r is a package for accessing and analyzing data from the Arena database.", {"entities": [(0, 6, "R_PACKAGE")]}),
    ("arenar is a package for simulating and analyzing arena-based experiments.", {"entities": [(0, 5, "R_PACKAGE")]}),
    ("An R package for working with HTML tables and data frames is htmldf.", {"entities": [(48, 54, "R_PACKAGE")]}),
    ("htmlTable allows you to create HTML tables from data frames in R.", {"entities": [(0, 9, "R_PACKAGE")]}),
    ("In R, you can use htmltools for creating and rendering HTML content.", {"entities": [(15, 24, "R_PACKAGE")]}),
    ("HTMLUtils is a package in R that handles HTML-related tasks.", {"entities": [(0, 8, "R_PACKAGE")]}),
    ("Create interactive web widgets in R using the popular package htmlwidgets.", {"entities": [(41, 52, "R_PACKAGE")]}),
    ("For high-throughput RNA sequencing analysis, consider using HTRX in R.", {"entities": [(50, 54, "R_PACKAGE")]}),
    ("hts is the go-to R package for hierarchical and grouped time series forecasting.", {"entities": [(0, 3, "R_PACKAGE")]}),
    ("Cluster hierarchical time series data efficiently with HTSCluster in R.", {"entities": [(41, 51, "R_PACKAGE")]}),
    ("Analyze high-throughput sequencing data easily with htsr in R.", {"entities": [(45, 49, "R_PACKAGE")]}),
    ("HTSSIP is an R package designed for analyzing microbial community sequencing data.", {"entities": [(0, 5, "R_PACKAGE")]}),
    ("High-throughput toxicity testing data analysis can be done using HTT in R.", {"entities": [(53, 57, "R_PACKAGE")]}),
    ("Work with hypertriglyceridemia data in R using the httk package.", {"entities": [(48, 52, "R_PACKAGE")]}),
    ("httpcache is a useful package in R for caching HTTP requests.", {"entities": [(0, 8, "R_PACKAGE")]}),
    ("Handle HTTP status codes effectively with the httpcode R package.", {"entities": [(36, 43, "R_PACKAGE")]}),
    ("Download files using HTTP conveniently with the httpgd R package.", {"entities": [(38, 44, "R_PACKAGE")]}),
    ("Consider using ICvectorfields for vector field analysis in R.", {"entities": [(19, 33, "R_PACKAGE")]}),
    ("Apply exteriorMatch to perform exterior matching in your data analysis.", {"entities": [(6, 19, "R_PACKAGE")]}),
    ("rBiasCorrection is a handy package for bias correction in statistical modeling.", {"entities": [(0, 15, "R_PACKAGE")]}),
    ("logitr is an R package designed for logistic regression modeling.", {"entities": [(0, 6, "R_PACKAGE")]}),
    ("ODEsensitivity allows you to perform sensitivity analysis on ODE models.", {"entities": [(0, 13, "R_PACKAGE")]}),
    ("risks is an R package for risk assessment and management.", {"entities": [(0, 5, "R_PACKAGE")]}),
    ("lsei is a package in R for solving linear least-squares problems.", {"entities": [(0, 3, "R_PACKAGE")]}),
    ("vmdTDNN is an R package for time-delay neural network modeling.", {"entities": [(0, 7, "R_PACKAGE")]}),
    ("glmnetcr is a package for fitting elastic net models in R.", {"entities": [(0, 8, "R_PACKAGE")]}),
    ("EpiILM is an R package for epidemiological modeling.", {"entities": [(0, 6, "R_PACKAGE")]}),
    ("Google traffic data can be accessed and analyzed using the googletraffic package in R.", {"entities": [(61, 75, "R_PACKAGE")]}),
    ("Packager is a utility package in R for managing and installing packages.", {"entities": [(0, 8, "R_PACKAGE")]}),
    ("Use metaMA for meta-analysis of microarray data in R.", {"entities": [(4, 10, "R_PACKAGE")]}),
    ("vfinputs is an R package for validating and formatting inputs.", {"entities": [(0, 8, "R_PACKAGE")]}),
    ("Motif analysis can be performed using the motif package in R.", {"entities": [(47, 52, "R_PACKAGE")]}),
    ("MicEconCES is a comprehensive R package for microeconomic analysis.", {"entities": [(0, 10, "R_PACKAGE")]}),
    ("The GIFTr package simplifies gift-giving analysis in R.", {"entities": [(4, 9, "R_PACKAGE")]}),
    ("Use the 'runonce' package to execute code blocks once in R.", {"entities": [(9, 17, "R_PACKAGE")]}),
    ("OmegaG is a versatile package for omega-3 fatty acid analysis in R.", {"entities": [(0, 6, "R_PACKAGE")]}),
    ("ImpactEffectsize helps assess the impact effect size in R.", {"entities": [(0, 16, "R_PACKAGE")]}),
    ("With parmigene, you can perform parametric gene expression analysis in R.", {"entities": [(5, 14, "R_PACKAGE")]}),
    ("sarp.snowprofile.alignment provides alignment tools for snow profile data in R.", {"entities": [(0, 24, "R_PACKAGE")]}),
    ("scUtils is a package that simplifies single-cell analysis workflows in R.", {"entities": [(0, 7, "R_PACKAGE")]}),
    ("mARP is a package for multi-objective optimization problems in R.", {"entities": [(0, 4, "R_PACKAGE")]}),
    ("RSauceLabs is a useful R package for interacting with Sauce Labs services.", {"entities": [(0, 11, "R_PACKAGE")]}),
    ("Use prepdat to preprocess and clean your data efficiently in R.", {"entities": [(4, 11, "R_PACKAGE")]}),
    ("grattanInflators provides inflation rates data from Grattan Institute in R.", {"entities": [(0, 16, "R_PACKAGE")]}),
    ("With npboottprm, perform non-parametric bootstrapping in R.", {"entities": [(5, 15, "R_PACKAGE")]}),
    ("qqtest is a package that simplifies quantile-quantile testing in R.", {"entities": [(0, 6, "R_PACKAGE")]}),
    ("PhaseType is an R package for phase-type distribution modeling.", {"entities": [(0, 9, "R_PACKAGE")]}),
    ("lsm is a package in R for estimating population size from capture-recapture data.", {"entities": [(0, 3, "R_PACKAGE")]}),
    ("useitR is a package for facilitating the use of research data in R.", {"entities": [(0, 6, "R_PACKAGE")]}),
    ("Create interactive web applications in R with the 'shiny' package.", {"entities": [(53, 58, "R_PACKAGE")]})
]

def trainModel(TRAIN_DATA):
    import spacy
    from spacy.training.example import Example
    import random

    # Create a blank spaCy NER model
    nlp = spacy.blank("en")

    # Define the labels (entity types) you want to recognize
    labels = ["R_PACKAGE"]

    # Add the NER component to the pipeline
    ner = nlp.add_pipe("ner", last=True)

    # Add the labels to the NER component
    for label in labels:
        ner.add_label(label)

    # Training data in the format [("text", {"entities": [(start, end, "label")]})]

    # Initialize the training process
    optimizer = nlp.begin_training()

    # Training loop
    for epoch in range(50):  # You can adjust the number of epochs as needed
        random.shuffle(TRAIN_DATA)  # Shuffle the training data for each epoch
        losses = {}  # Initialize losses

        # Iterate through the training data in batches
        for text, annotations in TRAIN_DATA:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update([example], drop=0.5, losses=losses)  # Update the model with examples

        print("Epoch:", epoch + 1, "Losses:", losses)

    # Save the trained NER model to a file
    nlp.to_disk("ner_model")

def testModel():
    import spacy
    # Load the trained NER model
    loaded_nlp = spacy.load("ner_model")

    # Test the loaded model
    test_text = "I love using ggplot2 and tidyr for data visualization in R."
    doc = loaded_nlp(test_text)
    for ent in doc.ents:
        print("Hello")
        print(f"Entity: {ent.text}, Label: {ent.label_}")

#trainModel(TRAIN_DATA)
testModel()
