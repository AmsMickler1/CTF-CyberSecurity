# Robots

Robots are taking over the world! Find out why! We have figured out that they have encoded 
messages by indexing into a string of characters and performing an xor then shift on that 
index. Here is a code snippet:

    def encode(codestr, xor, shift): return [basestr[((basestr.index(s)^xor)+shift)%64] for s in codestr]

practice.n0l3ptr.com 9998


### Part 1:
CTF questions are often difficult to understand at a first glance of reading them. Reread 
the sentence "We have figured out that they have encoded messages by indexing into a string 
of characters and performing an xor then shift on that index.". Until you can unpack what 
exactly it means, then describe it in detail - feel free to use pictures or diagrams for 
some/all of this.

This sentence is difficult to understand without also having the code snippet alongside it.
Just reading this, I can tell you what an xor and shifting an index do, but "indexing into a
string" was hard to really tell what it meant until I looked at the code.


### Part 2:
CTF questions often include code or code snippets that are difficult to understand. Several 
concepts from the lecture slides have been included in this code snippet. Describe in detail 
what happens in this code snippet. How similar is this to your answer in part 1?

Coming from a C++ background, having everything all on one line is a lot of condensed
information and makes it harder to figure out exactly what is going on in the above code
snippet. So I rearanged things a bit:
    
    for s in codestr:
        return basestr[((basestr.index(s)^xor)+shift)%64]

From here you can see that this function takes each character `s` in the code string and uses 
the base string to encode it. But what exactly is going on here? Let's start with

    basestr.index(s)

This looks for our character `s` in the base string and returns its index as an integer.

    ( ( [some integer] ^ xor ) + shift )
    
This integer is then exclusive ored with some unknown value, and then incremented by another
unknown value.

    [result integer] % 64
    
The resulting integer is then modded by 64 so that our final number remains in the bounds of
our base string, which is 64 characters long.

    return basestr[ final number ]
   
Finally, we take this number and use it as a way to pick a character from our base string to
replace our original character. This character is now encoded and the loop will run until it
has encoded all characters of the code string.


### Part 3:
Find the flag!

To get the flag I had to decipher three messages:

    1. A robot may not injure a human being or, through inaction, allow a human being to come to harm. 
    2. A robot must obey orders given it by human beings except where such orders would conflict with the First Law. 
    3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.
    
To start, I copied a single base and code string to my workspace so that I could work on how to
decypher the text without it changing on me every attempt. I took the encoded string and counted
the instances of each character. I hypothesized that the most occuring character was actually 
either the space character (`" "`) or `e`, since `e` is the most common letter in the english language. 
Based on the locations and frequency of the most occuring character, I decided that it made most 
sense for it to be the space character. Knowing this, I broke the code string up into words and 
started making other guesses. One letter words could either be `a` or `I`, but since the same 
character appeared in the middle of other words, I could safely assume those words were `a`, since 
there are no words with capital `I`s in the middle of them. Once I had two decently likely guesses, 
I wrote a piece of code that would print out possible values of `XOR` and `SHIFT` that would satisfy both.
I started testing values between 0 and 100, but I quickly realized none of the outputs greater than
64 would work so I changed it to only look for numbers between 0 and 64. This gave me a list of about
10 or so values that I tried one by one. None of them turned out exactly right, but they were close
enough that I was able to logic out what the string was supposed to say. 

Using this technique, I realized that all of the strings generated started with the same pattern that 
decodes to `A robot`. From there I was able to write a program that uses those 6 guaranteed characters
to determine that runthrough's `XOR` and `SHIFT` values, and then use those to decode the string. My program
was having trouble writing the strings (The server would spit back incorrect even though it had 
deciphered the string correctly, it was likely some small formatting error on my part) so after I 
discovered that there are only three unique strings I just typed them into the server myself to obtain
the flag.

    flag{4s1m0v_w0uld_b3_pr0ud}

