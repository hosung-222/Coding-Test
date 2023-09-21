class Solution {
    public String solution(String[] str_list, String ex) {
        StringBuilder s = new StringBuilder();
        for (String value : str_list) {
            if (! value.contains(ex))
                s.append(value);
        }
        return s.toString();
    }
}