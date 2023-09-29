class Solution {
    public String solution(String myString) {
        StringBuilder answer = new StringBuilder();
        String[] arr =myString.split("");
        for (char s : myString.toCharArray()){
            if ((byte) s <= 108){
                answer.append("l");
            }
            else {
                answer.append(s);
            }
        }
        return answer.toString();
    }
}