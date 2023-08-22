class Solution {
    public String solution(String my_string, int n) {
        String[] arr = my_string.split("");
        StringBuilder answer = new StringBuilder();
        for (String s : arr){
            for (int i =0; i<n; i++){
                answer.append(s);
            }
        }
        return answer.toString();
    }
}