class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        map<string, int> map1, map2;
        int n1 = list1.size(), n2 = list2.size(), i;
        for(i=0;i<n1;i++){
            map1[list1[i]] = i;  
        }
        vector<string> res;
        int min_sum = INT_MAX;
        map<string, int>::iterator it;
        for(i=0;i<n2;i++){
            string str = list2[i];
            it = map1.find(str);
            if(it!=map1.end())
		        if (min_sum>map1[str] +i){
                    min_sum = map1[str]+i;
                    res = {list2[i]};
                }
                else{
                    if(min_sum == map1[str]+i){
                        res.push_back({list2[i]});
                    }
                }
        }
        return res;
    }
};