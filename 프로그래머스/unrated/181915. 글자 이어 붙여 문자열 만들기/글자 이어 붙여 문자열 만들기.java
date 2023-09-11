class Solution {
    public String solution(String my_string, int[] index_list) {
        StringBuilder answer = new StringBuilder();
        String[] arr = my_string.split("");
        for (int i:
             index_list) {
            answer.append(arr[i]);
        }
        return answer.toString();
    }
}