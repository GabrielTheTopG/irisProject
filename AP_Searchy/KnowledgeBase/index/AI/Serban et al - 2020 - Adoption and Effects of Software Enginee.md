- ## AutoML
#AutoML #ResearchStreams #AI #Engineering 
We may also add more questions, for example to better measure the effects of practices related to AutoML, a relatively new direction that is receiving sharply increasing attention in academia and industry

- ## Testing
#Testing #Machine #Learning #ResearchStreams #AI #Engineering 
Similarly, Ishikawa and Yoshioka [30] as well as Wan et al. [56] have studied how software engineers perceive the challenges re- lated to ML and how ML changes the traditional software develop- ment life-cycle. Both studies ran user surveys with a majority of respondents from Asia. We could not find a similar study without this regional bias. Nonetheless, both publications concluded that testing and ensuring the quality of ML components is particularly difficult, because a test oracle is missing, the components often behave nondeterministically, and test coverage is hard to define. In order to better classify the challenges raised by ML components, Lwakatare et al. introduced a comprehensive taxonomy [36].

- ## Software
#Software #Quality  #ML #components #Software #Engineering #ResearchStreams #AI #Engineering 
One of the initial publications on this topic is the work of Sculley et al. [45], which used the framework of technical debt to explore risk factors for ML components. In particular, they argued that ML components have a stronger propensity to incur technical debt, because they have all maintenance problems specific to traditional software as well as a set of additional issues specific to ML. They also presented a set of anti-patterns and practices aimed at avoiding technical debt in systems using ML components

- ## Software
#Software #Quality  #ML #components #Software #Engineering #ResearchStreams #AI #Engineering 
Breck et al. [12] introduced 28 tests and monitoring practices that target different stages of the development process for ML. They also proposed a list of benefits resulting from implementing the tests and developed a model to score test practice adoption, aimed at measuring technical debt. Again, the practices dedicated to SE from [12] have been included in our catalogue. On the same topic, Zhang et al. introduced a survey on testing techniques for ML components [59], which – in contrast to the broader approach taken in [12] – only targets testing ML models.

- ## Software
#Software #Quality  #ML #components #Software #Engineering #ResearchStreams #AI #Engineering 
Washizaki et al. [57] studied and classified software architecture design patterns and anti-patterns for ML, extracted from white and grey literature. Many of these patterns are application and context specific, i.e., they depend on the architectural style or on the type of data used. The patterns are of a general character and the ones similar to recommendations we found in literature were included in our catalogue of practices.

- ## Interplay
#Interplay #SEAI #Engineering #Process #Software #Engineering #ResearchStreams #AI #Engineering 
Amershi et al. conducted a study internally at Microsoft, aimed at collecting challenges and best practices for SE used by various teams in the organisation [3]. They reported on a broad range of challenges and practices used at different stages of the software development life cycle. Using the experience of the respondents and the set of challenges, they built a maturity model to assess each team. However, the set of challenges and reported practices are broad and often not actionable. Moreover, they represent the opinions of team members from Microsoft, where typically more resources are dedicated to ensuring adoption of best practices thanAdoption and Effects of Software Engineering Best Practices in Machine Learning ESEM ’20, October 8–9, 2020, Bari, Italy Table 1: Successful search queries. The table shows the base queries, for which any variant (described in text) led to a valid source and at least one practice. Query Documents software engineering for machine learning [3] data labeling best practices [2, 16, 39, 40] machine learning engineering practices [13, 44, 60] software development machine learning [31] machine learning production [42, 48] machine learning production practices [1, 5, 34, 38] machine learning deployment [18] machine learning deployment practices [43] machine learning pipelines practices [28] machine learning operations [52] machine learning versioning [54] machine learning versioning practices [26] within smaller companies. In our work, we aim to bridge this gap by running a survey with practitioners with various backgrounds and by presenting a set of actionable, fine-grained best practices.

- ## Interplay
#Interplay #SEAI #Engineering #Process #Software #Engineering #ResearchStreams #AI #Engineering 
As ML components are developed and deployed, several engineering challenges specific to the ML software development life-cycle emerge [4, 30, 32, 36, 56]. Arpteg et al. [4] identified a set of 12 challenges that target development, deployment and organisational issues. In particular, managing and versioning data during development, monitoring and logging data for deployed models and estimating the effort needed to develop ML components present striking differences with the development of traditional software components.

