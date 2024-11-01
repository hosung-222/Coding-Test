import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[][] peoples = new int[n][2];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            peoples[i][0] = Integer.parseInt(st.nextToken());
            peoples[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n; i++) {
            int score = 1;
            for (int j = 0; j < n; j++) {
                if(i == j) continue;
                if (peoples[i][0] < peoples[j][0] && peoples[i][1] < peoples[j][1]){
                    score ++;
                }
            }
            bw.write(score + " ");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}