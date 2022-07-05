class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        N= len(A)
        OnesCount = 0
        for i in range(N):
            if A[i] == '1':
                OnesCount+=1
        if OnesCount == N:
            return N
        ans = 0
        preVal = A[0]
        for i in range(1,N-1):
            #print(A[i-1],A[i],A[i+1])
            if A[i] == '0':
                #print('A[i],i',A[i],i)
                l=0
                r=0
                for j in range(i-1,-1,-1):
                    #print(A[j])
                    if A[j]=='1':
                        l+=1
                    else:
                        break
                for j in range(i+1,N):
                    if A[j]=='1':
                        r+=1
                    else:
                        break
                #print(OnesCount,l,r,l+r+1)
                if OnesCount>l+r:
                    #print(ans,l+r+1)
                    ans = max(ans,l+r+1)
                else:
                    ans = max(ans,l+r)
        return ans                               