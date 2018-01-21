# Robots

Robots are taking over the world! Find out why! We have figured out that they have encoded 
messages by indexing into a string of characters and performing an xor then shift on that 
index. Here is a code snippet:

    def encode(codestr, xor, shift): return [basestr[((basestr.index(s)^xor)+shift)%64] for s in codestr]

practice.n0l3ptr.com 9998


###Part 1:
CTF questions are often difficult to understand at a first glance of reading them. Reread 
the sentence "We have figured out that they have encoded messages by indexing into a string 
of characters and performing an xor then shift on that index.". Until you can unpack what 
exactly it means, then describe it in detail - feel free to use pictures or diagrams for 
some/all of this.

###Part 2:
CTF questions often include code or code snippets that are difficult to understand. Several 
concepts from the lecture slides have been included in this code snippet. Describe in detail 
what happens in this code snippet. How similar is this to your answer in part 1?

###Part 3:
Find the flag!
