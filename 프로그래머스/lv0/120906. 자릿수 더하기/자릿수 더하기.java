class Solution {
    public int solution(int n) {
        int answer = 0;
        String sn = Integer.toString(n);
        String[] arr = sn.split("");

        for(String s : arr){
            answer += Integer.parseInt(s);
        }


        return answer;
    }
}