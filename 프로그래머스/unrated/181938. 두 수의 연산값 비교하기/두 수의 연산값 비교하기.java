class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int ab = Integer.parseInt(""+a+b);
        int ab2 = a*b*2;
        return ab>ab2?ab:ab2;
    }
}