class Solution {
    public int[] solution(int[] arr, int n) {
        int cnt = arr.length;
        if (cnt % 2== 0){
            for (int i = 1; i < cnt ; i +=2) {
                arr[i] += n;
            }
        }else {
            for (int i = 0; i <cnt ; i+=2) {
                arr[i] += n;
            }
        }

        return arr;
    }
}