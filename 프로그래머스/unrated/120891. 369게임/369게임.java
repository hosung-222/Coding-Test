import java.util.Arrays;

class Solution {
    public int solution(int order) {
        String[] gameNumber = new String[] {"3","6","9"};
        int answer = 0;
        for (String s : Integer.toString(order).split("")){
            if(Arrays.asList(gameNumber).contains(s)){
                answer += 1;
            }
        }
        return answer;
    }
}