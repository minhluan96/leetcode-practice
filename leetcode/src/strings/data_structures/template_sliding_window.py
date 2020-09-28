def find_substr(self, s: str) -> int:
    hmap = {}

    counter # check whether the substring is valid
    begin, end = 0, 0 # two pointers, one point to tail and one head
    d # the length of substring

    for: #  initialize the hash map here

    while s < len(s):
        if s in hmap:
            if hmap[s[end]] > 0:
                # modify the counter here
        
        hmap[s[end]] -= 1
        
        while: # counter condition:
            # update d here if finding minimum
            # increase begin to make it invalid/valid again

            if s[begin] in hmap:
                if hmap[s[begin]] > 0:
                    hmap[s[begin]] += 1

                # modify counter here

            begin += 1

        # update d here if finding maximum
    return d
