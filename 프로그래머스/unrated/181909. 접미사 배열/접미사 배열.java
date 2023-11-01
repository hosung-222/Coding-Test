import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public ArrayList<String> solution(String my_string) {
        ArrayList<String> arr = new ArrayList<>();
        String[] my_arr = my_string.split("");
        for (int i = 0; i <my_string.length() ; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = i; j < my_arr.length ; j++) {
                sb.append(my_arr[j]);
            }
            arr.add(sb.toString());
        }
        Collections.sort(arr);
        return arr;
    }
}