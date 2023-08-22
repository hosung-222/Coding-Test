class Solution {
    public int solution(String my_string) {
       int answer = 0;
        String[] arr = my_string.split("");
        for (String s : arr){
            if (s.chars().allMatch(Character::isDigit)){
                answer += Integer.parseInt(s);
            }
        }
        return answer;
    }
}