- ## Characteristics
#Characteristics #Task #Modelling #Task #Analysis  #Modeling 
A task- model diagram conveys the structural properties of task models by highlighting  relationships defined among them.

- ## Collaborative
#Collaborative #Task #Models #Types  #Models #Task #Modelling #Task #Analysis  #Modeling 
define a cooperative  task model as a tuple consisting of a set of roles, a set of task specifications (one for  each role), a set of actors where each actor belongs to a certain role and a set of global  constraints

- ## Collaborative
#Collaborative #Task #Models #Types  #Models #Task #Modelling #Task #Analysis  #Modeling 
Within  a collaborative task model, however, additionally the global constraints have to be  taken into account.

- ## Notation
#Notation #ConcurTaskTrees #CTT #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
In recent years various attempts were made to extend the CTT notation. In [13; 14]  Klug and Dittmar propose additional modelling constructs, namely input/output ports  and object dependencies, respectively. Luyten [15] introduces a new node type  (decision node) which allows to augment task models with context of use  dependencies

- ## Limitations
#Limitations #ConcurTaskTrees #CTT #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
CTT’s inability to specify task failures and error cases  Bastide and Basnyat introduce the concept of error patterns [6].

- ## Cooperative
#Cooperative #ConcurTaskTrees #CCTT #ConcurTaskTrees #CTT #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
CCTT (Collaborative ConcurTaskTrees) [11]

- ## Operators
#Operators #ConcurTaskTrees #CTT #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Additional CTT Temporal Operators

- ## Operators
#Operators #ConcurTaskTrees #CTT #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
Based on this observation, we propose to replace the CTT “general purpose”  choice operator by two operators; one for a deterministic choice and another one for  non-deterministic choice

- ## Operators
#Operators #ConcurTaskTrees #CTT #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
The unary CTT Iteration operator (*) specifies that a task may be re-executed after  completion. The constraint of task completion before another iteration takes place  proves to be too rigid for certain tasks.

- ## LOTOS
#LOTOS #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
LOTOS [12].

- ## Complex
#Complex #Task #Decomposition #Characteristics  #Notations #Notations  #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
higher-level models are created through composition of  lower-level task models. This becomes possible if we define a task model as a task  tree, whose leaves are either atomic tasks or references to other task models1

- ## TCL
#TCL #Notation #Languages #Notations  #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
defined in a language called Task-Constraint Language (TCL)

- ## TCL
#TCL #Notation #Languages #Notations  #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
It consists of a left operand, a temporal operator, and a right  operand. The operands signify tasks, whereas the temporal operator expresses the type  of the constraint. Tasks are identified in two steps: First, we select the instance task  model(s) the task belongs to and second we select the task within the model(s).

- ## TCL
#TCL #Notation #Languages #Notations  #Task #Models #Task #Modelling #Task #Analysis  #Modeling 
TCL Constraints for Ubiquitous Meeting

- ## Task
#Task #Modelling #Patterns #Challenges #Task #Modelling #Task #Analysis  #Modeling 
Often designs are derived without a  thorough understanding of individual goals and tasks of involved actors [19; 20].

- ## Task
#Task #Modelling #Patterns #Challenges #Task #Modelling #Task #Analysis  #Modeling 
defining an entire specification within a single monolithic task  tree is only suitable for small applications and does not scale for sizable applications.

- ## Task
#Task #Modelling #Patterns #Challenges #Task #Modelling #Task #Analysis  #Modeling 
We envision using model-checking techniques to detect  deadlocks which are consequences of conflicting constraints.

- ## Expressiveness
#Expressiveness  #Notation #Challenges #Task #Modelling #Task #Analysis  #Modeling 
For example, CTT—one of the most popular task modelling  notations—does not have an operator defining the premature termination of a scenario  Practical Extensions for Task Models 43  (whether it is due to human or system error).

- ## Expressiveness
#Expressiveness  #Notation #Challenges #Task #Modelling #Task #Analysis  #Modeling 
Currently CTT only supports references to tasks within the same task tree. A modular  construction of the task model out of sub-models is not possible.

- ## Expressiveness
#Expressiveness  #Notation #Challenges #Task #Modelling #Task #Analysis  #Modeling 
Within such a model-based  development lifecycle, purely idealised task models, as proposed by Johnson, are  insufficient since human errors and system errors are not taken into account

- ## Cooperative
#Cooperative #Aspects #Challenges #Task #Modelling #Task #Analysis  #Modeling 
cooperative task model. Within such a cooperative  task model the execution of a task of one model may enable or disable the execution  of a task in a different task model.

- ## Cooperative
#Cooperative #Aspects #Challenges #Task #Modelling #Task #Analysis  #Modeling 
cooperative task  specification can serve as input for the derivation of probabilistic models, such as  Dynamic Bayesian Networks, which are widely used in the research field of proactive  assistance in ambient environments [20]

- ## Cooperative
#Cooperative #Aspects #Challenges #Task #Modelling #Task #Analysis  #Modeling 
starting point for more in-depth research for each of the  proposed operators and concepts. One future research avenue would be the extension of  TCL to be able to specify temporal dependencies based on the state of the actor

