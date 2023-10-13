class Solution {
    public String solution(int age) {
        StringBuilder answer = new StringBuilder();
        String sage = Integer.toString(age);
        String[] arr = sage.split("");
        for (String c : arr){
            int temp = Integer.parseInt(c);
            temp += 97;
            answer.append((char) temp);
        }
        return answer.toString();
    }
}