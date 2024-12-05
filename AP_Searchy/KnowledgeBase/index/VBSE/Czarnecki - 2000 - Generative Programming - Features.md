- ## Definitions
#Definitions #Software #Features #Software #Engineering 
“Feature: A prominent and user-visible aspect, quality, or characteristic of a software system or systems.” [KCH+90, p. 3]

- ## Definitions
#Definitions #Software #Features #Software #Engineering 
In general there are two definitions of features found in Domain Engineering literature: 1. a end-user-visible characteristic of a system, i.e. the FODA definition, or 2. a distinguishable characteristic of a concept (e.g. system, component, etc.) that is relevant to some stakeholder of the concept. The latter definition is used in the context of ODM (see Section 3.7.2) and Capture (see Section 3.7.4) and is fully compatible with the understanding of features in Conceptual Modeling.

- ## Definitions
#Definitions #Software #Features #Software #Engineering 
requires rules: Requires rules capture implications between features, e.g. “air conditioning requires horsepower greater than 100” (see Figure 13). 2. mutually-exclusive-with rules: These rules model constraints on feature combinations. An example of such a rule is “manual mutually exclusive with automatic”. However, this rule is not needed in our example since manual and automatic are alternative features. In general, mutually-exclusive-with rules allow us to exclude combinations of features where each feature may be seated in quite different locations in the feature hierarchy.

- ## Definitions
#Definitions #Software #Features #Software #Engineering 
We can also annotate features with rationales. A rationale documents the reasons or trade-offs for choosing or not choosing a particular feature. For example, manual transmission is more fuel efficient than automatic one. Rationales are necessary since, in practice, not all issues pertaining to the feature model can be represented formally as composition rules (due to the complexity involved or limited representation means)

- ## Definitions
#Definitions #Software #Features #Software #Engineering 
etween functional, operational, and presentation features. Binding time, binding location, and binding siteDomain Engineering 51 1. features diagram, i.e. a representation of a hierarchical decomposition of features including the indication whether or not each feature is mandatory, alternative, or optional; 2. feature definitions for all features including the indication of whether each feature is bound at compile time, activation time, or at runtime (or other times); 3. composition rules for features; 4. rationale for features indicating the trade-offs.

