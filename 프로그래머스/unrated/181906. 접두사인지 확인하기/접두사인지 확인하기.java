class Solution {
    public int solution(String my_string, String is_prefix) {
        String[] my = my_string.split("");
        String[] pre = is_prefix.split("");
        for (int i = 0; i <is_prefix.length() ; i++) {
            if (i>= my_string.length()){
                return 0;
            }
            if (!pre[i].equals(my[i])){
                return 0;
            }
        }
        return 1;
    }
}