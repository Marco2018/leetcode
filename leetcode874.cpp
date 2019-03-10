#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles){
        map<pair<int,int>,bool> obposition;
        int i;
        for (i =0;i<obstacles.size();i++){
            obposition[make_pair(obstacles[i][0],obstacles[i][1])]== true;
        }
        //state 0:north,1:east,2:south,3:west
        int state=0,x=0,y=0,maxdis=0;
        for (i=0;i<commands.size();i++){
            switch(commands[i]){
                case -1:
                    state+=1;state%=4;break;
                case -2:
                    state-=1;state%=4;break;
                default:
                    switch(state){
                        case 0:
                            while(commands[i]-- && !obposition[make_pair(x,y+1)]){y++;}break;
                        case 1:
                            while(commands[i]-- && !obposition[make_pair(x+1,y)]){ x++;}break;
                        case 2:
                            while(commands[i]-- && !obposition[make_pair(x,y-1)]){
                                y--;
                            }
                            break;
                        case 3:
                            while(commands[i]-- && !obposition[make_pair(x-1,y)]){
                                x--;
                            }
                            break;
                    }
            }
            maxdis=std::max(maxdis,x*x+y*y);
        }
        return maxdis;
    }
};
int main() {
    std::cout << "Hello, World!" << std::endl;
    Solution s;
    vector<int> commands;
    vector<vector<int>> obstacles;
    vector<int> temp;
    commands.push_back(4);
    commands.push_back(-1);
    commands.push_back(4);
    commands.push_back(-2);
    commands.push_back(4);
    temp.push_back(2);
    temp.push_back(4);
    obstacles.push_back(temp);
    cout<<s.robotSim(commands,obstacles);
    return 0;
}