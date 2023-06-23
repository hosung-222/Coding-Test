import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String answer = "";
        String a = sc.next();
        for(Character s : a.toCharArray()){
            if (Character.isUpperCase(s))
                answer += Character.toLowerCase(s);
            else
                answer += Character.toUpperCase(s);
        }
        System.out.print(answer);
    }
}
