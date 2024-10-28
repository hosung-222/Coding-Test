import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String n = sc.nextLine();
        String[] alphabet = n.split("");
        Map<String, Integer> dict = new HashMap<>();

        for(String a : alphabet){
            a = a.toUpperCase();
            dict.put(a, dict.getOrDefault(a,0) + 1);
        }

        String maxChar = "";
        int maxCount = 0;
        for (Map.Entry<String, Integer> entry : dict.entrySet()){
            if (maxCount < entry.getValue()){
                maxCount = entry.getValue();
                maxChar = entry.getKey();
            }
            else if (maxCount == entry.getValue()){
                maxChar = "?";
            }
        }
        System.out.println(maxChar);
        sc.close();
    }
}
