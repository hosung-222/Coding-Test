import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        List<String> channels = new ArrayList<>();
        for (int i = 0; i <n ; i++) {
            channels.add(sc.nextLine());
        }

        StringBuilder moves = new StringBuilder();
        int cursor = 0;
        int kbs1Index = channels.indexOf("KBS1");
        for (int i = 0; i <kbs1Index ; i++) {
            moves.append("1");
            cursor++;
        }

        for (int i = 0; i <kbs1Index ; i++) {
            moves.append("4");
            String temp = channels.get(cursor);
            channels.set(cursor, channels.get(cursor-1));
            channels.set(cursor-1, temp);
            cursor -- ;
        }

        int kbs2Index = channels.indexOf("KBS2");
        for (int i = 0; i < kbs2Index; i++)
            moves.append("1");

        for (int i = 0; i < kbs2Index-1; i++)
            moves.append("4");

        System.out.println(moves.toString());
        sc.close();
    }
}