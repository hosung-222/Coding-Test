class Solution {
    public int solution(String myString, String pat) {
        String change;
        change = myString.replace("A","C").replace("B","A").replace("C","B");
        int answer = 0;
        if (change.contains(pat)){
            answer = 1;
        }
        return answer;
    }
}