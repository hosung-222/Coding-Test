class Solution {
    public String solution(String rsp) {
        String[] arr = rsp.split("");
        StringBuilder answer = new StringBuilder();
        for(String s: arr){
            if (s.equals("2")){
                answer.append("0");
            } else if (s.equals("0")) {
                answer.append("5");
            } else if (s.equals("5")) {
                answer.append("2");
            }
        }
        return answer.toString();
    }
}