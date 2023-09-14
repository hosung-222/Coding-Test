import java.util.ArrayList;
import java.util.List;
class Solution {
    public List<Integer> solution(int n, int k) {
        List<Integer> answer = new ArrayList<>(); 
        for (int i = k; i <=n ; i += k) {
            answer.add(i);
        }
        return answer;
    }
}