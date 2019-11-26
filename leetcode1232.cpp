class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int n = coordinates.size();
        int i;
        if(n<=2) return true;
        if(coordinates[0][0]==coordinates[1][0]){
            int last_x = coordinates[0][0];
            for(i=2;i<n;i++){
                if(coordinates[i][0]!=last_x) return false;
            }
        }
        else{
            double k = 1.0*(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0]);
            for(i=2;i<n;i++){
                if(k!=1.0*(coordinates[i][1]-coordinates[i-1][1])/(coordinates[i][0]-coordinates[i-1][0]))
                    return false;
            }
        }
        return true;
    }
};