class Solution:
    def climbStairs(self, n: int) -> int:
      #using fibonacci sequence
        sq=(5)**(1/2) fib=((1+sq)/2)**(n+1)-((1-sq)/2)**(n+1)# sqare root calculation and fibonnaci sequence declare
        return(int(fib/sq))#printing output
