class Solution {
public:
    bool check(vector<vector<int>>& ivec, int a){
        int i;
        for(i=0;i<3;i++){
            if(ivec[i][0] == a && ivec[i][1] == a && ivec[i][2] == a) return true;
            if(ivec[0][i] == a && ivec[1][i] == a && ivec[2][i] == a) return true;
        }
        if(ivec[0][0] == a && ivec[1][1] == a && ivec[2][2] == a) return true;
        if(ivec[0][2] == a && ivec[1][1] == a && ivec[2][0] == a) return true;
        return false;
    }
    string tictactoe(vector<vector<int>>& moves) {
        vector<vector <int> > ivec(3, vector<int>(3, 0));
        int i, n = moves.size();
        for(i=0;i<n;i++){
            if(i%2==0) ivec[moves[i][0]][moves[i][1]] = 1;
            else ivec[moves[i][0]][moves[i][1]] = 2;
        }
        if(check(ivec, 1)) return "A";
        else{
            if(check(ivec, 2)) return "B";
        }
        if(n == 9) return "Draw";
        return "Pending";
    }
};