import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n =Integer.parseInt(bf.readLine());
        for (int i = 0; i < n; i++) {
            String[] str = bf.readLine().split(" ");
            
            int r = Integer.parseInt(str[0]);
            String s = str[1];
            for (int j = 0; j <s.length() ; j++) {
                for (int k = 0; k <r ; k++) {
                    System.out.print(s.charAt(j));
                }
            }
            System.out.println();
        }
    }
}