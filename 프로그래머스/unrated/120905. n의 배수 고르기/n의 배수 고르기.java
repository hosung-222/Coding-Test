import java.util.List;
import java.util.stream.Collectors;
import java.util.Arrays;
class Solution {
    public List<Integer> solution(int n, int[] numlist) {
        return Arrays.stream(numlist).filter(i-> i%n == 0).boxed().collect(Collectors.toList());
    }
    
}