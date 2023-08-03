class Solution {
    public String solution(String my_string, String letter) {
        String answer = "";
        String[] arr = my_string.split("");

        for (String s : arr){
            if (!s.equals(letter)){
                answer += s;
            }
        }
        return answer;
    }
}