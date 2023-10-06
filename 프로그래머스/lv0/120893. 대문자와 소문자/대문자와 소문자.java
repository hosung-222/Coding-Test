class Solution {
    public String solution(String my_string) {
        StringBuilder answer = new StringBuilder();
        String[] arr = my_string.split("");
        for (String s:
            arr ) {
            if (s.equals(s.toUpperCase())){
                answer.append(s.toLowerCase());
            }else {
                answer.append(s.toUpperCase());
            }
        }
        return answer.toString();
    }
}