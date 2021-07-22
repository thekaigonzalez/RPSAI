# RPSAI
RPSAI is a "different" approach to the infamous "Python Rock Paper scissors AI".
## Normal Python RPS VS RPSAI
Normal Python RPS Code usually contains basic logic.

```
if USERINPUT is THIS:
    if CPU is THAT:
        print(THIS > THAT)
    ELSE THEN
        PRINT THAT > THIS
```

Obviously, not real code, just pseudo.

basically, RPSAI instead asks you to calculate how primitive you would like
your round to be, where it has an algorithm which takes a limit and sorts the default
array into a new array, with more options, not going past the limit.

Here's the basic Function overview W/ Documentation.

```
def calculate_decision(limits: int)

Calculates the decision between the array defaults. 
LIMITS Decides how many times it is able to iterate 
through the defaults table for a more precise and 
genuine decision.

Params:

limits 

Returns:

RANDOM CHOICE
```
So you are able to choose between a more *random* approach,
or, a simpler approach.