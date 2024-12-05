- ## Requirements
#Requirements #Monitoring 
Instrumenting a Java program can have an observer  effect—that is, the act of observing can affect the phe- nomenon being observed. For example, the program’s  execution time might increase

- ## Adaptive
#Adaptive #Monitoring #Challenges #Requirements #Monitoring 
implementation bias can restrict the kinds  of properties developers model and monitor. Many BAM  systems rely on relational databases for event storage;  consequently, their property languages are based on  SQL

- ## Objective
#Objective #Requirements #Monitoring 
Requirements monitoring can help determine if the  software meets its users’ needs; it establishes whether  the developer built the correct system. Like verification,  validation is no longer idealized as an activity that occurs  once. Instead, incremental development implies incre- mental validation. Now, analyzers should continuously  validate systems against users’ needs.

- ## Objective
#Objective #Requirements #Monitoring 
Requirements monitoring addresses two fundamental  software engineering problems: verification and valida- tion. Verification, including requirements analyses and

- ## Definitions
#Definitions #Requirements #Monitoring 
Requirements monitoring differs from other types of  monitoring in its analysis of abstract, requirements-level  properties and automation of runtime requirements evalu- ation. This evaluation interprets low-level software events  as contributors to eventual requirements satisfaction or  violation

- ## Definitions
#Definitions #Requirements #Monitoring 
requirements monitoring  addresses five problems: •  Distributed debugging. Determines  what’s wrong with software. •  Runtime verification. Determines  whether the software works as  specified. •  Runtime validation. Determines  whether the software satisfies the  user goals, especially in the face of  an evolving software system. •  Business activity monitoring. De- termines whether an enterprise  system satisfies the business goals. •  Evolution and codesign. Informs  users and developers as they jointly  evolve the system to meet their  needs.

- ## Definitions
#Definitions #Requirements #Monitoring 
Independent  testing agencies (Underwriters Laboratories, Consumers  Union, and so on) use a similar monitoring model to benefit  manufacturers and consumers alike

- ## Concepts
#Concepts #Requirements #Monitoring 
monitor is a software system that observes and  analyzes another (target) system’s behavior for quali- ties of interest, such as satisfying the target system

- ## Concepts
#Concepts #Requirements #Monitoring 
requirements monitor determines the  requirements status from a stream of significant input  events (INmon).2  Therefore, a monitor is a function that  processes its input event stream to derive the require- ments status: MON(INmon) → Sat(REQ).

- ## Models
#Models #Concepts #Requirements #Monitoring 
Functional models describe the states and transitions a  system allows

- ## Models
#Models #Concepts #Requirements #Monitoring 
Goal models typically augment a functional model to describe  user behaviors developers can translate into operational  specifications for system behaviors

- ## Models
#Models #Concepts #Requirements #Monitoring 
User models describe user goals and capabilities, including  cognitive impairments or software skills

- ## Models
#Models #Concepts #Requirements #Monitoring 
Antimodels describe undesirable behaviors, such as attack- ers, to support analysis of anticipated problems.4

- ## Models
#Models #Concepts #Requirements #Monitoring 
Quality-of-service (QoS) models describe qualitative mea- sures of systems, which a goal model can also include.5

- ## Models
#Models #Concepts #Requirements #Monitoring 
Diagnostic models infer causes of property violations.6

- ## Models
#Models #Concepts #Requirements #Monitoring 
Architectural and related models describe software architec- ture, design, and code models, often supporting QoS  analysis.7

- ## Models
#Models #Concepts #Requirements #Monitoring 
Evolution models describe potential changes to the system,  typically focusing on software changes; however, user  changes, such as skill learning, are possible. Evolution models  can be associated with QoS or cost models.8

- ## Models
#Models #Concepts #Requirements #Monitoring 
Discovery models, such as data mining or learning, enable  dynamic discovery of behaviors, such as hacking attacks, as  well as predictions of eventual property violations and  successes.9

- ## Models
#Models #Concepts #Requirements #Monitoring 
Decision models, such as utilities, use the other models to  select an appropriate evolution path.10

- ## Languages
#Languages #Requirements #Monitoring 
temporal  variant of UML’s Object Constraint Language (OCL)

- ## Application
#Application #Layer #Layers #Conceptual #Architectures #Requirements #Monitoring 
The application layer uses the model layer to provide  application-specific services, including model presenta- tions, to present, control, and modify the target system

- ## Application
#Application #Layer #Layers #Conceptual #Architectures #Requirements #Monitoring 
A monitoring system  can ensure it acquires, stores, and analyzes the necessary  event sources, thereby providing an active auditing func- tion rather than a periodic retrospective function.

- ## Presentation
#Presentation #Layer #Layers #Conceptual #Architectures #Requirements #Monitoring 
The model-presentation layer provides services for pre- senting analysis to developers. Minimally, the presentation  layer presents a property-satisfaction log.

- ## Presentation
#Presentation #Layer #Layers #Conceptual #Architectures #Requirements #Monitoring 
four states: initially  unknown; then partial satisfaction, when a portion of the  tree is true; and satisfied or violated,

- ## Model
#Model #Layer #Layers #Conceptual #Architectures #Requirements #Monitoring 
Monitoring a user goal-model of e-mailing behavior  illustrates a more complex model.5 First, a developer  specifies user e-mailing properties, such as prr: “never  reply to a request with a request.” Next, a compiler  translates property specifications, in OCL for example,  into operational monitors on the model’s event objects.  A translator then converts sourced e-mail events into  model events—for example, the translator translates an  XML e-mail event from the event layer as a UML message  in the model repository.

- ## Model
#Model #Layer #Layers #Conceptual #Architectures #Requirements #Monitoring 
During the system’s execution, the developer receives  the user goal-model monitoring results. Recurring failures  should lead to changes in the system—more specifically,  those that either assist the user or adapt the software.

- ## Model
#Model #Layer #Layers #Conceptual #Architectures #Requirements #Monitoring 
The model layer, requirements monitoring’s center- piece, provides services for interpreting source events  according to one or more models. It provides the follow- ing capabilities:

- ## Model
#Model #Layer #Layers #Conceptual #Architectures #Requirements #Monitoring 
Interpreting software behavior. Knowing the soft- ware’s state and its potential responses. •  Interpreting user behavior. Knowing a user’s state and  likely responses. This is particularly difficult with  even the most skilled and rational users; individuals  can use software in unanticipated ways to achieve  their goals. •  Informing users. Diagnosing inadequacies in software  use and providing user guidance.  •  Informing developers. Diagnosing inadequacies in the  software and providing developer guidance for the  software’s evolution

- ## Event
#Event #Layer #Layers #Conceptual #Architectures #Requirements #Monitoring 
scription of a significant action in time, typically modeled  as instantaneous state change—for example, the comple- tion of a method-call in an object-oriented program

- ## Event
#Event #Layer #Layers #Conceptual #Architectures #Requirements #Monitoring 
The event layer provides services  for event acquisition, transportation,  filtering, and storage.

- ## Event
#Event #Layer #Layers #Conceptual #Architectures #Requirements #Monitoring 
Distributed events, in particular, raise  important, well-known technical issues: How does a  system establish temporal event order with independent  clocks? How does a developer associate an event with a  context, such as a transaction?

- ## Benefits
#Benefits #GoalDriven #Eliciting #Requirements #Requirements #Engineering 
Analyzers can automatically evaluate goals at runtime  as patients use the e-mailing system. The e-mailing system  is instrumented to output relevant events. During system  use, a monitor listens to the events and incrementally up- dates goal satisfaction, which can be partial and eventually  either satisfied or violated.

- ## Continuous
#Continuous #Validation  #Requirements #Challenges #Requirements #Engineering 
On a smaller  scale, researchers are working on continuous validation,  which monitors the satisfaction of user goals during  software use.

- ## Continuous
#Continuous #Validation  #Requirements #Challenges #Requirements #Engineering 
To date, no single  project describes or implements a comprehensive monitor- ing solution that comprises event acquisition, multimodel  event interpretation, and guidance for system evolution.

- ## Data
#Data #Privacy #Governance #Interest #Classification #ValueBased #Software #Engineering #Software #Engineering 
privacy

- ## Safety
#Safety #Quality #Interest #Classification #ValueBased #Software #Engineering #Software #Engineering 
safety

- ## CrossDomain
#CrossDomain #Convergence #Organization #Interest #Classification #ValueBased #Software #Engineering #Software #Engineering 
network connection

