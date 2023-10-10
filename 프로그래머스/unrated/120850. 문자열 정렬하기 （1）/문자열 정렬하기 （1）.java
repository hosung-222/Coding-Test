import java.util.ArrayList;
import java.util.Comparator;
class Solution {
     public ArrayList<Integer> solution(String my_string) {
        ArrayList<Integer> arr = new ArrayList<>();
        String[] str = my_string.split("");
        for (String s:
             str) {
            try{
                arr.add(Integer.parseInt(s));
            }catch (NumberFormatException ex){
                continue;
            }
        }
        arr.sort(Comparator.naturalOrder());
        return arr;
    }
}