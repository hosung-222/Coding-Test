import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int max = 0;
        int maxi = 0;
        int maxj = 0;
        for (int i = 0; i <9 ; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            for (int j = 0; j <9 ; j++) {
                int x = Integer.parseInt(st.nextToken());
                if (x>max){
                    max = x;
                    maxi = i ;
                    maxj = j;
                }
            }
        }
        maxi += 1;
        maxj += 1;
        System.out.println(max);
        System.out.println(maxi+" "+maxj);
    }
}
