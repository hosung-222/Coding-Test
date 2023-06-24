import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String[] ls = a.split("");
        for(String s : ls){
            System.out.println(s);
        }
    }
}