class Solution {
public:
    int numWays(int steps, int arrLen) {
        int sz = min(steps / 2 + 1, arrLen);
        vector<long> ivec(sz,0);
        int step, pos;
        ivec[0] = 1;
        for (step=1;step<=steps;step++){
            vector<long> new_vec(sz,0);
            new_vec[0] = (ivec[0]+ivec[1])%1000000007;
            new_vec[sz-1] = (ivec[sz-1]+ivec[sz-2])%1000000007;
            for(pos = 1;pos<sz-1;pos++){
                new_vec[pos] = (ivec[pos-1]+ivec[pos]+ivec[pos+1])%1000000007;
            }
            ivec = new_vec;
        }
        return ivec[0];
    }
};