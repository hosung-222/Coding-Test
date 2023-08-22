class Solution {
    public String solution(String my_string) {
        String arr = "aeiou";
        String[] str = my_string.split("");
        StringBuilder answer = new StringBuilder();
        for (String s : str){
            if(!arr.contains(s)){
                answer.append(s);
            }
        }
        return answer.toString();
    }
}