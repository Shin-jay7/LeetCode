from __future__ import annotations


# Generate a from 1 to 7 and b from 1 to 7, then we have 7x7 = 49 options. 
# Let us create number c = (a-1)*7 + b-1, then we can show that c is number 
# between 0 and 48: substitute all possible values for a and b and you will see.
# Now, let us divide these number into groups: [0,9]; [10;19]; [20;29]; [30;39]; [40;48]. 
# If we get into one of the first four group we are happy: there is ten number 
# in each group, so we just return c%10 + 1. If we are in the fifth group, 
# we are not happy, there are only 9 numbers in this group and we need 10, 
# use 9 is not fair. So in these case, we say, that our experiment was not working,
# and we just start it all over again! That is all.
class Solution:
    def rand10(self):
        # we can't multiply rand7() * rand7(). It won't produce the numbers
        # that are uniformly distributed. '1' can be produced only once (1 * 1) 
        # whereas we can get 12 in 4 ways. (2 * 6, 3 * 4, 4 * 3, 6 * 2). 
        # So the end result will be with less number of 1's and more 12's
        calc = (rand7() - 1) * 7 + rand7() - 1
        return self.rand10() if calc >= 40 else (calc % 10) + 1
