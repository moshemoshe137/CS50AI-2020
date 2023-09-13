# Knowledge

---
## Week 1 - CS50AI
###### Moshe Rubin
###### 4/28/2021
https://cs50.harvard.edu/ai/2020/weeks/1/

---
## Knowledge
A lot of intelligence is based on Knowledge. This is how a lot of human intelligence works. 

**Knowledge-based agents**: agents that reason by operating on internal representations of knowledge. 

How could knowledge work? Take the following facts, for example:
- If it didn't rain, Harry visited Hagrid today.
- Harry visited Hagrid or Dumbledore today, but not both.
- Harry visited Dumbledore today. 

We can pretty reasonably draw the conclusion, Harry didn't visit Hagrid today. 
- **Harry did not visit Hagrid today.**

But we can go further:
- **It rained today.**

How can we make our AI do this too? Formal logic:

**Sentence**: an assertion about the world in a knowledge representation language.

## Propositional Logic

Symbols like
- **¬**: Not
- **∧**: And
- **∨**: Or
- **⇒**: Implication
- **⇔**: Biconditional

Buncha truth tables for all these... the only interesting one:

| _P_   | _Q_   | _P ⇒ Q_
| ---   | ---   | ---   
| True  | True  | True
| True  | False | False
| False | True  | True
| False | False | True

and

| _P_   | _Q_   | _P ⇔ Q_
| ---   | ---   | ---   
| True  | True  | True
| True  | False | False
| False | True  | False
| False | False | True

More terms:

What is actually true in the world?

**Model**: Assignment of a truth value to every possible model

For example, if I have the events _P_: It is raining, and _Q_: It is a Tuesday, then a model might look like:
```
{P=True, Q=False}
```

