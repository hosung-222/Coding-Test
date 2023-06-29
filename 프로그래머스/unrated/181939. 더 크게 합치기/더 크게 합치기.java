class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String ab = Integer.toString(a) + Integer.toString(b);
        String ba = Integer.toString(b) + Integer.toString(a);
        int x = Integer.parseInt(ab);
        int y = Integer.parseInt(ba);
        return x>y?x:y;
    }
}