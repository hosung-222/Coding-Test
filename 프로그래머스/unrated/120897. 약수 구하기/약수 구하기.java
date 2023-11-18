import java.util.ArrayList;
import java.util.List;
class Solution {
    public List<Integer> solution(int n) {
        List<Integer> arr = new ArrayList<>();
        for (int i = 1; i <= n ; i++) {
            if (n % i == 0){
                arr.add(i);
            }
        }
        return arr;
    }
}