import java.util.ArrayList;


class Solution {
    public ArrayList<Integer> solution(int start, int end_num) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = start; i >= end_num ; i--) {
            answer.add(i);
        }
        return answer;
    }
}