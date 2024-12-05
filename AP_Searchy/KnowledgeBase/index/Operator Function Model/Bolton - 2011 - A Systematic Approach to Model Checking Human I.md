- ## Programmable
#Programmable #User #Models #Demarcation #to #other #Modelling #Approaches #Task #Modelling #Task #Analysis  #Modeling 
programmable user models (PUMs) [44] that capture the knowledge and cognitively plausible behavior that an operator might use when interacting with an automated system and implementing them as part of a formal system model [45]– [47]. PUMs encompass the goals that the operator wishes to achieve with the system, his beliefs and knowledge about the operation of the system, the information available to him from the human–device interface, and the actions that he can execute to interact with the system

- ## Limitations
#Limitations #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Task Priority and Interruption: One feature that is sup- ported by the UAN and CTT is the ability for activities to be interrupted when a higher priority activity becomes relevant due to a change in the human–device interface or environmental conditions

- ## Limitations
#Limitations #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Root Activity Execution: The current EOFM implemen- tation assumes that all root activities are temporally related with the equivalent of an optor_seq decomposition operator

- ## Limitations
#Limitations #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
The EOFM currently only supports a simple model of cognitive and perceptual operations using local variables and thus does not utilize more realistic models of human memory, perception, or cognitive processing

- ## Characteristics
#Characteristics #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
The enhanced operator function model (EOFM) [23] was designed to be a generic task analytic modeling language that specifically addresses these issues. EOFM extends the OFM [10] which supports a visual and object-oriented means of representing task models.

- ## Actions
#Actions #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Atomic actions are either an assignment to an output variable (indicating an action has been performed) or a local variable (representing a perceptual or cognitive action). All variables are defined in terms of constants, user-defined types, and basic types, described hereinafter

- ## Activities
#Activities #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Each human operator model is a set of EOFM task models that describe goal-level activities. Activities decompose into lower level activities and, eventually, atomic actions. Decompo- sitions are controlled by decomposition operators that specify the cardinality of and temporal relationship between the sub- activities or actions

- ## Activities
#Activities #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Activities can have preconditions, repeat conditions, and completion conditions (Boolean expressions written in terms of input, output, and local variables as well as constants) which specify what must be true before an activity can execute, when it can execute again, and what is true when it has completed the execution, respectively.

- ## Decomposition
#Decomposition #Components #EOFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
DECOMPOSITION OPERATORS

- ## Characteristics
#Characteristics #GOMS #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
The GOMS family of models [21] supports the timing anal- ysis of human task behavior based on cognitive modeling. Rukšenas ˙ et al. [51] have shown how these types of anal- yses can be coupled with formal verification analyses with formal PUMs.

- ## OFM
#OFM #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Lee and Sanquist’s Operator Function Model with Cogni- tive Operations [43] extended the OFM to support cognitive operations related to the following: perceptual sensitivity, per- ceptual discrimination, selective attention, distributed attention, working memory, long-term memory, and response precision. They have shown how this can be used to identify design and training requirements to prevent erroneous human behavior and facilitate efficient human work.

- ## Human
#Human #Error #Detection #Applications #Task #Modelling #Task #Analysis  #Modeling 
human factors engineers use task analytic methods to describe the normative human behaviors required to control the system automation [8]. The resulting task analytic models represent the mental and physical activ- ities that operators use to achieve the goals that the system was designed to support.

- ## Model
#Model #Checking #Validation  #Model #Quality #Challenges #Task #Modelling #Task #Analysis  #Modeling 
e present the for- mal syntax and semantics of the EOFM and an automated process for translating an instantiated EOFM into the model checking language Symbolic Analysis Laboratory. We present an evaluation of the scalability of the translation algorithm

- ## Formal
#Formal #Verification #Challenges #Task #Modelling #Task #Analysis  #Modeling 
The power of these formal verification analyses is limited by the ability of the task analytic modeling notations to express normative human behavior. For example, CTT [9] and Fields’ task modeling notation [20] do not support all of the temporal and cardinal relationships between activities and actions (re- ferred to as subacts hereinafter) of other task analytic modeling notations.

- ## Formal
#Formal #Verification #Challenges #Task #Modelling #Task #Analysis  #Modeling 
Of the task modeling notations used in formal verification (and task analytic modeling techniques in general), only the UAN supports all of these relationships

