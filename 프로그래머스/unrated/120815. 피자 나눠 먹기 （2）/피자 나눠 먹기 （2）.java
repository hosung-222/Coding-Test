class Solution {
    private static final int PIZZA_SLICE = 6;
    public int solution(int n) {
        int answer = 1;
        while (PIZZA_SLICE * answer % n  !=0){
            answer ++;
        }
        return answer;
    }
}