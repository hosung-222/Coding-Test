import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int arr[][] = new int[n+1][4];
        int rank = 1;

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            int index = Integer.parseInt(st.nextToken());
            int gold = Integer.parseInt(st.nextToken());
            int silver = Integer.parseInt(st.nextToken());
            int bronze = Integer.parseInt(st.nextToken());
            arr[index][0] = gold;
            arr[index][1] = silver;
            arr[index][2] = bronze;
        }

        for (int i = 1; i <= n; i++) {
            if (arr[i][0] > arr[c][0]){
                rank ++;
            } else if (arr[i][0] == arr[c][0] && arr[i][1] > arr[c][1]) {
                rank ++;
            } else if (arr[i][0] == arr[c][0] && arr[i][1] == arr[c][1] && arr[i][2] > arr[i][2]) {
                rank ++;
            }
        }
        System.out.println(rank);
        br.close();
    }
}