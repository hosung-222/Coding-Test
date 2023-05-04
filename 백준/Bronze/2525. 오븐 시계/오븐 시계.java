import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int time = Integer.parseInt(bf.readLine());

        int min = a*60 + b;
        min += time;

        if (min>=1440){
            min -= 1440;
            a = min / 60;
            b = min % 60;
        }
        else {
            a = min/60;
            b = min%60;
        }
        System.out.println(a+" "+b);
    }
}
