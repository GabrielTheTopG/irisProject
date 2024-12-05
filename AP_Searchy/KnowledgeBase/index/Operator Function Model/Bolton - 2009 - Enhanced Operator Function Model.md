- ## Characteristics
#Characteristics #ConcurTaskTrees #CTT #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
CTTs support all of these but also support the optional  execution of acts (where zero or more acts could be executed),  and the synchronous execution of acts (where the acts must be  performed at the same time, like pressing two keyboard keys at  once) [9]

- ## Requirements
#Requirements #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Language models should be capable of representing ob- servable atomic human actions

- ## Requirements
#Requirements #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Language models should be capable of representing in- ternal human behaviors

- ## Requirements
#Requirements #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Language models should support hierarchical decompo- sition of goals into activities, multiple levels of activities, and  activities into actions:

- ## Requirements
#Requirements #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Language models should support specification of sub- activity and action execution cardinality:

- ## Requirements
#Requirements #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Language models should support human behavior tem- poral orderings:

- ## Requirements
#Requirements #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
The language should be capable of describing con- straints/conditions on task execution

- ## Requirements
#Requirements #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
The language should be platform and analysis- environment independent.

- ## Requirements
#Requirements #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
The language should support interpretation or parsing  capabilities that will facilitate the incorporation of its  models into different analysis infrastructures.

- ## Characteristics
#Characteristics #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Types and constants each serve to help connect EOFMs to  the external system and to express model concepts using intui- tive descriptors.

- ## Characteristics
#Characteristics #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Constants (represented by constant nodes) are variables  meant to store fixed values.

- ## Characteristics
#Characteristics #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
The operator nodes are used to represent the different hu- man operators of the systems (one operator node for each hu- man operator being modeled). The task behavior of the opera- tor node is defined by and within its sub-nodes

- ## Decomposition
#Decomposition #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
decomposition attribute specifies a decomposition op- erator which controls the temporal execution order of a given  eofm’s sub-activity and action nodes

- ## Decomposition
#Decomposition #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
or_seq – One or more of the sub-acts must execute for  the parent eofm or activity to finish and each sub-act  must be executed one at a time.

- ## Decomposition
#Decomposition #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
or_par - One or more of the sub-acts must execute  and each sub-act can be executed concurrently.

- ## Decomposition
#Decomposition #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
and_seq – All of the sub-acts must execute and each  sub-act must be executed one at a time.

- ## Decomposition
#Decomposition #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
and_par - All of the sub-acts must execute and each  sub-act can be executed concurrently.

- ## Decomposition
#Decomposition #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
xor – Exactly one sub-act must execute.

- ## Decomposition
#Decomposition #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
seq – All of the sub-acts must execute, each sub-act  must execute one at a time, and each must execute in  the order it appears in the markup.

- ## Decomposition
#Decomposition #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
optor_seq – Zero or more of the sub-acts must execute  and each sub-act must be executed one at a time.

- ## Decomposition
#Decomposition #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
optor_par – One or more of the sub-acts must execute  and each sub-act can be executed concurrently.

- ## Decomposition
#Decomposition #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
sync – All sub-acts must be executed synchronously  (at the same time). This is different from the _seq suf- fixed decompositions as all decomposed actions must  be executed at the same time rather than arbitrarily in- terleaved with each other.

- ## Conditionals
#Conditionals #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
optional conditions provides the means of con- straining task model execution.

- ## Conditionals
#Conditionals #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
startcondition – when true, execution must start

- ## Conditionals
#Conditionals #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
endcondition – when true, execution must terminate

- ## Conditionals
#Conditionals #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
precondition – must be true for execution to start

- ## Conditionals
#Conditionals #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
postcondition – will be true when execution has  stopped

- ## Conditionals
#Conditionals #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
invariantcondition – must be true during execution

- ## Conditionals
#Conditionals #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
whilecondition – when true, execution can repeat

- ## CPMGOMS
#CPMGOMS #GOMS #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
CPM-GOMS supports the parallel execution of ac- tivities in which multiple activities (and their sub-acts) can be  executed in parallel in order to encompass human multitasking  behavior [4].

- ## OFM
#OFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Work by Lee and Sanquist has attempted to extend the  OFM by adding cognitive operations [16]. Future work should  more explicitly attempt to incorporate these capabilities into the  EOFM language.

- ## Conditions
#Conditions #OFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Initiators specify under what condition an activity  should start executing;

- ## Conditions
#Conditions #OFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Conditions to initiate specify what must be true for an  activity to start executing;

- ## Conditions
#Conditions #OFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Terminators specify under what conditions an activity  must stop executing; and

- ## Conditions
#Conditions #OFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Conditions to complete specify what will be true after  an activity has completed.

- ## Characteristics
#Characteristics #OFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
OFM supports  a number of different cardinality and ordering options (a super- set of those supported by PRL) for the sequential execution of  activities or actions in each hierarchical decomposition [1][11]:

- ## Characteristics
#Characteristics #OFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
one or more acts (an activity or action) can be executed in any  order, exactly one act can be executed, all acts must be exe- cuted in any order, and all acts must be executed in a specific  order

- ## Characteristics
#Characteristics #OFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
OFMs also represent their task models hierarchi- cally, where atomic actions are presented as rectangles and  activities as rounded rectangles.

- ## Applications
#Applications #Task #Modelling #Task #Analysis  #Modeling 
purposes includ- ing intent inferencing [1], usability evaluation [2], intelligent  tutoring [3], timing analysis of human tasks [4], hazard moni- toring [5], formal verification of human-interactive systems  [6][7], and controlling agents in simulations [8].

- ## Task
#Task #Analysis #Task #Analysis  #Modeling 
Task analytic  models are hierarchical as they decompose high level activities,  tasks, or goals into lower level ones. The lowest level in the  hierarchy includes atomic level actions such as physical actions  (e.g., pressing keys, moving a computer mouse, pressing but- tons) and perceptual and cognitive operations

