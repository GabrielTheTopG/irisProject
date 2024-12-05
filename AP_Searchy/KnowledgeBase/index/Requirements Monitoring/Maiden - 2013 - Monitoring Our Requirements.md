- ## Adaptive
#Adaptive #Monitoring #Challenges #Requirements #Monitoring 
System requirements tend to be  more coarse grain than event filters,  and monitoring a single require- ment will necessitate more than  one set of event data. Therefore, re- quirements of different types need  to be decomposed to map onto dif- ferent types of event filters.

- ## Adaptive
#Adaptive #Monitoring #Challenges #Requirements #Monitoring 
Existing languages don’t express  requirements in forms that make  reference to data in event-data re- positories. Therefore, requirements  need to be expressed in a way that  they can be mapped to data from  monitored events.

- ## Adaptive
#Adaptive #Monitoring #Challenges #Requirements #Monitoring 
We need modified methods and lan- guages to let us express requirements  in forms that enable them to be moni- tored automatically against software  system events.

- ## Definitions
#Definitions #Requirements #Monitoring 
requirements monitoring  differs from other types of monitoring  in its analysis of abstract, system-level  properties and its automation of run- time requirements evaluation

- ## Definitions
#Definitions #Requirements #Monitoring 
need filters to select  the event types needed for different mon- itors. Data in these event types is stored  in repositories over periods of time so  that we can test requirements that spec- ify desired behaviors and qualities.

- ## Definitions
#Definitions #Requirements #Monitoring 
Service-based systems are increas- ingly making use of such software  monitors to adapt automatically to  context changes

- ## Definitions
#Definitions #Requirements #Monitoring 
little  work has been reported that links soft- ware monitors explicitly to established  requirements compliance techniques.

- ## Assessing
#Assessing #Requirements #Satisfaction #Challenges #Requirements #Engineering 
a satisfaction argu- ment reads, “Given properties of do- main D, combined with the specification  of the behavior of new system S, re- quirements R on new system will hold.”

- ## Assessing
#Assessing #Requirements #Satisfaction #Challenges #Requirements #Engineering 
require- ment can be satisfied if we assume  something about the domain

- ## Assessing
#Assessing #Requirements #Satisfaction #Challenges #Requirements #Engineering 
One means of doing that is  a crosswalk, specified S. However, the  specified crosswalk only satisfies the  requirement to cross the road safely if  drivers stop their vehicles at the cross- ing. This domain property holds in  some but not all cultures, which means  that the requirement is satisfied only in  some cultures.

- ## Assessing
#Assessing #Requirements #Satisfaction #Challenges #Requirements #Engineering 
software- based systems that adapt to their envi- ronments. Such systems often invoke  remote third-party services—a design  choice that blurs the systems’ boundar- ies. Consequently, domain properties  become difficult to describe and, per- haps more importantly, likely to change  more frequently. Suddenly, writing sat- isfaction arguments for such systems  becomes a whole lot more difficult.

- ## Assessing
#Assessing #Requirements #Satisfaction #Challenges #Requirements #Engineering 
user requirement  associated with performance is “R: a  passenger can receive personal flight in- formation within an acceptable time af- ter the request for the information.” So far, so good. Now let’s specify a  possible required performance charac- teristic of the service itself: “S: the pas- senger information feature will deliver  the departure time for a requested flight  within two seconds of the request.”

- ## Assessing
#Assessing #Requirements #Satisfaction #Challenges #Requirements #Engineering 
Consequently, the  satisfaction argument needs to describe  how the specified service will enable the  user requirement to be satisfied under  different conditions. This is where soft- ware requirements monitors come in.

