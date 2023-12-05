class Solution {
    public String solution(String my_string) {
        String answer = my_string.toLowerCase();
        return answer.chars()
                .sorted()
                .collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append)
                .toString();
    }
}