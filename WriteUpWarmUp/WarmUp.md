# Write-Up-Warm-Up

Read a write-up from the list below and answer the following questions.

For my write-up I chose [this one](https://github.com/RandomsCTF/write-ups/tree/master/Hack.lu%20CTF%202015/GuessTheNumber%20%5Bppc%5D%20(150)) on a LCG guess the number game.

#### 1. How well did you understand the problem statement?

I understood most of the problem statement. I understand that he's trying to find the correct sequence of
numbers to win a 100 number "guess what number I'm thinking of"-style game, but without further explanation
I'm not familiar with the underlying algorithms or what LCG means. He does explain this later on in the
write-up though and that does help.

#### 2. Before reading the write-up (and after reading the question), do you think you could have solved the question?

I'm going to give this one a solid maybe. I'm unfamiliar with the underlying algorithms and have no experience
with how a linear congruental generator works, but given sufficient time to research it I feel like I could
definitely get somewhere on this problem. The concept of a guess the number game doesn't seem too hard.

#### 3. How was the author's grammar?

Grammar was good.

#### 4. How was the author's style?

The writeup was written like a paper you would turn in to a professor; very formal, good grammar and spelling,
and shows overall techinical understanding of the problem and steps taken to solve it.

#### 5. How much of the thought process did the author describe? (Bare minimum, stream of conscience, or somewhere in-between?)

The author described most of the thought process behind solving the problem. He had a chunk of time spent on
lots of trial and error that he briefly summarized but did not spend too much time on (likely because wrong
solutions aren't relevant to the write-up), but the rest was very detailed and straightfoward much like a 
how-to guide would be.

#### 6. After reading the write-up, do you think you could have solved the question?

I think so. I understand linear congruental generators a little better now, though I would still need to 
dedicate some time to actually getting to know them and how they work in order to reach a solution.

#### 7. What libraries (if any) did they use?

He used a socket library to connect to the server hosting the problem, and a time library to help strip
the time from the server to obtain the seed for the "random" number generator.
