import java.util.ArrayList;

class Solution {
    public ArrayList<String> solution(String my_string) {
        String[] arr = my_string.split(" ");
        ArrayList<String> answer = new ArrayList<>();
        for (String s: arr){
            if (!s.equals("")){
                answer.add(s);
            }
        }
        return answer;
    }
}