- ## Eventual
#Eventual #Consistency #Terminology 
Strong consistency. After the update  completes, any subsequent access (by A,  B, or C) will return the updated value.  ˲ Weak consistency. The system does  not guarantee that subsequent ac- cesses will return the updated value. A  number of conditions need to be met  before the value will be returned. The  period between the update and the mo- ment when it is guaranteed that any ob- server will always see the updated value  is dubbed the inconsistency window.

- ## Eventual
#Eventual #Consistency #Terminology 
Eventual consistency. This is a spe- cific form of weak consistency; the  storage system guarantees that if no  new updates are made to the object,  eventually all accesses will return the  last updated value. If no failures occur,  the maximum size of the inconsistency  window can be determined based on  factors such as communication delays,  the load on the system, and the num- ber of replicas involved in the replica- tion scheme. The most popular system  that implements eventual consistency  is the domain name system (DNS).  Updates to a name are distributed ac- cording to a configured pattern and  in combination with time-controlled  caches; eventually, all clients will see  the update.

