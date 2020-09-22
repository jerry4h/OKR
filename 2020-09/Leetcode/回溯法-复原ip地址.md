[LC93](https://leetcode-cn.com/problems/restore-ip-addresses/)

```cpp
class Solution {
private:
    vector<string> result;
    void backtrack(const string& s, int start, vector<string>& tmp){
        if(start>=s.size() && tmp.size()<4){
            return;
        }
        if(tmp.size() == 4){
            if(start==s.size()){
                string tmpstr = "";
                // string 类型的concate
                tmpstr += tmp[0];
                for(int i=1; i<tmp.size(); i++){
                    tmpstr += ".";
                    tmpstr += tmp[i];
                }
                result.emplace_back(tmpstr);
            }
            return;
        }
        if(s[start]=='0'){
            tmp.emplace_back(s.substr(start,1));
            backtrack(s, start+1, tmp);
            tmp.pop_back();
            return;
        }
        int d = 0;
        int address = 0;
        while(start+d<s.size() && d<=2){
            // 字符串到数字的转换
            address = address*10 + (s[start+d] - '0');
            if(address > 255){
                break;
            }
            // substr 第二个参数一定记清，是长度。
            tmp.emplace_back(s.substr(start, d+1));
            backtrack(s, start+d+1, tmp);
            tmp.pop_back();
            d++;
        }
    }
public:
    vector<string> restoreIpAddresses(string s) {
        if(s.empty()){
            return result;
        }
        vector<string> tmp;
        backtrack(s, 0, tmp);
        return result;
    }
};
```