class Solution {
    public int solution(int num, int k) {
        int answer = -1;
        String [] arr = Integer.toString(num).split("");
        for (int i = 0; i < arr.length ; i++) {
            if(k == Integer.parseInt(arr[i])){
                return i + 1;
            }
        }
        return answer;
    }
}