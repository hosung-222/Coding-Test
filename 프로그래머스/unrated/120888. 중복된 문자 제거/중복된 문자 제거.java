class Solution {
    public String solution(String my_string) {
        StringBuilder answer = new StringBuilder();
        String[] arr = my_string.split("");
        for (String s:
             arr) {
            if (!answer.toString().contains(s)){
                answer.append(s);
            }
        }
        return answer.toString();
    }
}