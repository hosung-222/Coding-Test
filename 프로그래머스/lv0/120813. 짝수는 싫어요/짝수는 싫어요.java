import java.util.ArrayList;
class Solution {
    public ArrayList<Integer> solution(int n) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for (int i=1; i<=n ;i++){
            if (i % 2 != 0){
                arr.add(i);
            }
        }
        return arr;
    }
}