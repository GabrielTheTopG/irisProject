- ## DevOps
#DevOps #Terminology 
According to Jabbari et al., DevOps is “a development methodology aimed at bridging the gap between Development and Operations, emphasizing communication and collabora- tion, continuous integration, quality assurance and delivery with automated deployment utilizing a set of development practices” [1].

- ## Keptn
#Keptn #DSLs #DevOps 
For evaluation purposes, we adopt Keptn [8], an open- source tool for DevOps automation, configured via a family of languages based on JSON schema [9]. Keptn automatically pushes the configuration files to Git. We implemented a PoC [10] for consistency checking between two languages of the Keptn family used for Quality Assurance (QA): ServiceLevel Objectives (SLO) and Service Level Indicators (SLI). As a result of the PoC, we can transform the configurations of SLI and SLO to models, check their consistency with model queries, and apply basic model repairs by inconsistency resolution actions. The corrected models are transformed back to artefacts valid for Keptn.

- ## Keptn
#Keptn #DSLs #DevOps 
The SLI defines quantitative measures of some aspects of the service level. These measures are defined by the key and value attributes of the Indicators Pattern Properties metaclass. The key identifies the indicator, and the value holds the tool- specific query to compute the indicator. The SLO specifies a target value or a range of values for a service level that the SLImeasures. Therefore, the sli field of the Objective metaclass in the SLO metamodel must refer to an Indicators Pattern Properties with the same key. If such a key is missing, then a validation error occurs. Listing 1 illustrates the corresponding validation rule in the Viatra Query Language. 1 @Constraint( 2 message = "Objective’s SLI field must refer to an indicator with the same key.", 3 severity = "error" 4 ) 5 pattern objRefersToWrongProperty(obj: Objective, name: java String, property: IndicatorsPatternProperties){ 6 Sli2SloLink.sli(link, sliRoot); 7 Sli2SloLink.slo(link, sloRoot); 8 9 ServiceLevelObjectives.objectives(sloRoot, obj); 10 Objective.sli(obj, name); 11 12 ServiceLevelIndicators.indicators(sliRoot, indicator); 13 Indicators.patternProperties(indicator, property); 14 neg Indicators.patternProperties.key(indicator, name); 15 } Listing 1. Validation rule for Objective referring to wrong indicator pattern property key.

- ## Keptn
#Keptn #DSLs #DevOps 
Keptn [8] requires SLO [19] and SLI [20] JSON-based specifications to specify and measure the quality of cloud services, respectively. These specifications are illustrated as synthesized metamodels in Fig. 3 together with examples in JSON

