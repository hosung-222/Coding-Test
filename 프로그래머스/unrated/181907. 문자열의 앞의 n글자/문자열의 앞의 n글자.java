import java.util.Arrays;
class Solution {
    public String solution(String my_string, int n) {
        StringBuilder answer = new StringBuilder();

        String[] myArr = my_string.split("");
        String[] arr = new String[n];
        System.arraycopy(myArr,0,arr,0,n);
        for (String s : arr){
            answer.append(s);
        }
        return answer.toString();
    }
}