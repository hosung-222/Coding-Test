class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i = 4; i <= n; i++) {
            if (!isPrimeNumber(i)){
                answer += 1;
            }
        }
        return answer;
    }
    public boolean isPrimeNumber(int number){
        for (int i = 2; i <= Math.sqrt(number) ; i++) {
            if (number % i == 0){
                return false;
            }
        }
        return true;
    }
}