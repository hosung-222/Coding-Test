class Solution {
    public int[] solution(int[] num_list) {
        int n = num_list.length;
        int[] answer = new int[n];
        
        for(int i=n-1, j=0; i>=0; i--, j++){
            answer[j] = num_list[i];
        }
        
        return answer;
    }
}