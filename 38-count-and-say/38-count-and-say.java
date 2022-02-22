/*
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221 
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
 10.   13211311123113112211
 

546546 

151416
*/

/*
1
1

2
countString(1) = 11

3
countString(11) = 21

4
countString(21) = 1211

4
*/
class Solution {
    public String countAndSay(int n) {
        String result = "1";
        
        for(int i = 2; i <= n; i++) {
            result = countString(result);
        }
        
        return result;
    }
    
    public String countString(String s) {
        
        String parsedStr = "";
        char[] cArr = s.toCharArray();
        
        int count = 0;
        int i = 0;
        int j = 0;
        
        while(i < cArr.length + 1) {
            
            if(i == cArr.length) {
                parsedStr += Integer.toString(count) + cArr[j]; //check this
                break;
            }
            
            if(cArr[i] == cArr[j]) {
                count++;
                i++; 
            } else {
                parsedStr += Integer.toString(count) + cArr[j];
                j = i;
                count = 0;
            }
        }
        
        return parsedStr;
        
    }
}