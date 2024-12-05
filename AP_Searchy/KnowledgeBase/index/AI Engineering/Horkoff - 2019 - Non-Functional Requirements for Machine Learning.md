- <span style="color:white">**Context**</span> in a context where the solution involves ML, much of our knowledge about NFRs no longer applies 

- <span style="color:steelblue">**Objective**</span> agenda for the exploration of NFRs for ML-based solutions 

- <span style="color:seagreen">**Method**</span> we consider whether traditional knowledge about NFRs and quality from a requirements perspective can apply to ML-based systems can view this knowledge from two dimensions: 1) knowledge of NFRs 2) method s f or NFRs, i.e., catalogues of NFRs modeling methods methods to reason over NFRs to use NFRs to monitor software 

- <span style="color:Tomato">**Results**</span> we outline challenges related to treatment of NFRs for ML. The first four challenges relate to knowledge of NFRs (1), while the last three focus on methods (2) 

- <span style="color:MediumPurple">**Conclusion**</span> C1. Our understanding of NFRs for ML is fragmented and incomplete, including how to define and refine NFRs in ML- specific contexts. C5. ML researchers and users currently lack an ML-specific way to express and specify quality requirements for ML, including targets and trade-offs, and the influence of domain context. C6. We need to understand how evolution, both in terms of available training data, and in terms of quality requirements and thresholds, may affect our ML solutions C7. We need to understand how ML-based solutions inte- grate with typical software from a quality perspective. 

---
> 
Horkoff \cite{horkoff_non-functional_2019} examines requirements engineering (RE) practices for eliciting quality requirements towards ML-based systems. The author recognized that researchers and users of ML-based systems lack an effective methodology to express and specify quality requirements for ML-based systems, including targets and trade-offs, e.g., based on domain-specific best practices.

---
#AI #NFR #Challenges 

#Requirements #Engineering #AI 

#Quality #Attributes #AI 

The concept of quality has had better luck in terms of a precise definition, being covered by several prominent ontologies, e.g., DOLCE [18]. More recent work in RE uses ideas from DOLCE to treat NFRs as qualities over an entity [19], usually a functional requirement, the system, or a system component, e.g., “send mail (entity) quickly (quality)” or “the system (entity) should be secure (quality)”.

Accuracy & Performance. Most ML work reports on algorithm accuracy (often precision and recall), i.e., how “correct” the output is compared to reality.

Fairness. Recent work has focused on technical solutions to make ML algorithms more fair, finding that the removal of sensitive features (e.g., race, gender) is not sufficient to ensure fair results, and considering the trade-off between fairness and other NFRs [2]. Work in this area has attempted to find mathematical or formal definitions of fairness, e.g. statistical parity, individual fairness, and has found that the accurate implementation of fairness depends more on how fairness is defined and measured than how it is implemented [26].

Transparency.

Security & Privacy.

Work in [4] introduces protocols for preserving privacy in various ML approaches, and explicitly acknowledges the trade-off in terms of algorithm speed when revising techniques for privacy. Similarly, Bonawitz et al. introduce a method to preserve privacy in ML, focusing on keeping the overhead in terms of runtime and communication low [5]. Papernot et al. recognize the increase in ML-related security and privacy threats and create a threat model for ML [29].

Testability.

majority of work focuses on the other direction, applying ML to improve software testing strategies (e.g., [30]).

Reliability.

sustainability or maintainabil- ity, have not seen significant attention.

aware, there is no unified collection or consideration of many NFRs for ML, including a consideration of ML-specific quality trade-off data

#Requirements #Engineering #AI #Challenges 

C2. Our knowledge of how various ML algorithms, along with their optimizations and assumptions, affect relevant ML qualities, including trade-offs among qualities, is incomplete and fragmented.

C3. Given our new understanding of the meaning and refinements of NFRs, we must also understand how NFRs can be measured in practice for ML-based solutions.

C4. We need to understand the effects of ML algorithms on desired qualities not only during ML solution design, but at runtime – during the lifetime of the ML solution.

