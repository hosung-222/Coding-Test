import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int newScore = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        List<Integer> rank = new ArrayList<>();
        if (n >0){
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                rank.add(Integer.parseInt(st.nextToken()));
            }
            if (n==p && rank.get(n-1) >= newScore)
                System.out.println(-1);
            else {
                int ranking = n + 1;
                for (int i = 0; i < n; i++) {
                    if (rank.get(i)<=newScore){
                        ranking = i + 1;
                        break;
                    }
                }
                System.out.println(ranking);
            }
        }else {
            System.out.println(1);
        }

    }
}