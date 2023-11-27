import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> solution(String myString) {
        List<Integer> answer = new ArrayList<>();
        String[] arr = myString.split("");
        int count = 0;
        for (String s : arr){
            if (s.equals("x")){
                answer.add(count);
                count = 0;
            }else{
            count += 1;
            }
        }
        answer.add(count);
        return answer;
    }
    }