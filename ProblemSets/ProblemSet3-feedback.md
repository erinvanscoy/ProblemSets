# PSYC 5P02- Introduction to Programming for Psychology
## Fall 2025

### Problem Set #3

### Rubric:
* Accuracy & Efficiency: 50%
* Explanation and documentation: 50%

--- 
###  Feedback:

* Using a dialogue drop-down menu is cool, but it seems impractical to have to run your 3 different conditions by running the task 3 different times. why not combine them into a single experimental run? 
* Good work avoiding hard-coding: e.g., : ``half_trials = numb_Trials // 2 ``
* for this code here: ``Trial_Condition = [1]*half_trials + [0]*(numb_Trials - half_trials)`` -- a small thing but couldn't you just do ``Trial_Condition = [1]*half_trials + [0]* half_trials``?
* For this:
> ``#Next I am defining my target present, target absent variables. 
#If the target is present, it is associated with 1. If the target is absent it is associated with 0.
Targ_present = "1" 
Targ_absent = "0"``

At first I was confused as to why you need these variables, since they're already defined by the Trial_condition variable as 0 or 1. Plus, why use two variables each with a unique value? Seemed like there's a lot of unnecessary redundancy here. It turns out these are the keys that are used for target present and target absent responses. This documentation doesn't make that clear here. 

* I wonder if you should consider using a different unit (norm, degrees) for creating your locations, as pixels may not translate well to other monitors?
* Could have also found some other way (other than chatGPT) to come up with possible locations? 
* * The data file doesn't write the full data -- only the summary. This isn't great practice since you may have trials you want to exclude later (slow RTs) and there's no way to recover that data if you only save the summary statistics. 
* You're re-using a lot of code in the practice and the main experiment. If you're re-using code try to think of ways to put them into functions (defs) or objects.
* **Overall:** Generally speaking very good. Managed to accomplish most of what I asked. You're showing good improvement with regard to fundamentals of programming. A few odd choices for implementing the task (i.e., having conditions run separately; only saving summary data).  Could be made more efficient with the use of functions or classes for repeated code. 

**Accuracy & Efficiency:** 19/25
**Explanation and documentation:** 23/25
**Total:** 42/50
