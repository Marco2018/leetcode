class Solution {
public:
    string minRemoveToMakeValid(string s) {
        int i = 0, count = 0;
        // left;
        count = 0;
        while(i<s.size()){
            if (s[i] =='(') count++;
            else{
                if(s[i] == ')'){
                    if(count <= 0){
                        s.erase(i, 1);
                        i--;
                    }
                    else{
                        count--;
                    }
                }
            }
            i++;
        }
        //right
        count = 0; i = s.size() - 1;
        while(i>=0){
            if (s[i] == ')') count++;
            else{
                if(s[i] == '('){
                    if(count<=0){
                        s.erase(i, 1);
                    }
                    else{
                        count--;
                    }
                }
            }
            i--;
        }
        return s;
    }
};