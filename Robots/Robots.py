import telnetlib

HOST = "practice.n0l3ptr.com"
PORT = 9998
t = telnetlib.Telnet(HOST,PORT)
t.open(HOST,PORT)

#Objective: Reverse this
#def encode(codestr, xor, shift): return
#    [basestr[((basestr.index(s)^xor)+shift)%64] for s in codestr]


while (1):
    print t.read_until(": ")
    basestr = t.read_until("\n")

    print "Base string: " + basestr
    basestr = basestr[:-1]

    t.read_until("!\n")
    codestr = t.read_until("\n")

    print "Code string: " + codestr
    codestr = codestr[:-1]
    answer = ""

    # A robot
    charA = basestr.index("A")
    char_ = basestr.index(" ")
    charr = basestr.index("r")
    charo = basestr.index("o")
    charb = basestr.index("b")
    chart = basestr.index("t")
    XOR = 0
    SHIFT = 0
    
    for x in range(0,64):       # I realize this is super bad form but I've not yet been able to wrap my head
        for y in range(0,64):   # around python's condensed syntax and for now this works
            if ((((charA^x)+y)%64 == basestr.index(codestr[0])) and (((char_^x)+y)%64 == basestr.index(codestr[1])) 
            and (((charr^x)+y)%64 == basestr.index(codestr[2])) and (((charo^x)+y)%64 == basestr.index(codestr[3])) 
            and (((charb^x)+y)%64 == basestr.index(codestr[4])) and (((chart^x)+y)%64 == basestr.index(codestr[6]))):
                print "Success! " + str(x) + " : " + str(y)
                XOR = x
                SHIFT = y

    # this is also really bad style, sorry.
    for x in codestr:
        num = basestr.index(x)
        if (num - SHIFT < 0):
            num += 64
        num -= SHIFT
        num = num^XOR
        answer += basestr[num]
        
    # I wrote an alternative here, but the server is down so I'm unable to test it at the moment:
    #def decode(codestr, xor, shift):
        #return [basestr[((basest.index(x)^xor)-shift+64)%64] for x in codestr]

    print "Answer: " + answer

    print t.write("answer\n")
