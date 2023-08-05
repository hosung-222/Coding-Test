class Solution {
    public int solution(int slice, int n) {
        int answer = 0;
        while(slice > 0){
            if (slice >= n){
                answer += 1;
                break;
}
            answer += 1;
            n -= slice;
            }
        return answer;
    }
}