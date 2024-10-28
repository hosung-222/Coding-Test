import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // 1, 2~7 8~19, 20~37 -> 1, 6, 12, 18, 24
        int range = 2;
        int count = 1;
        if (n==1)
            System.out.println(count);
        else{
            while (range <= n){
                range += count * 6;
                count ++;
            }
            System.out.println(count);
        }
    }
}
