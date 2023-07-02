class Solution {
    public int solution(int n) {
        int answer = 0;
        if(n%2 == 0){
            for(int i = 1; i*2 <= n; i++ ){
                answer += Math.pow(i*2, 2);
            }
        }else{
            answer += 1;
            for(int i =2; i<=n; i++){
                if (i%2 != 0){
                    answer+= i;
                }
            }
        }
        return answer;
    }
}