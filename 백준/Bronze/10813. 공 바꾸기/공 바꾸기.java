import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] box = new int[n];
        for(int i = 0; i<n; i++){
            box[i] = i+1;
        }
        for(int i = 0; i<m; i++){
            int tmp;
            st = new StringTokenizer(bf.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            tmp = box[x-1];
            box[x-1] = box[y-1];
            box[y-1] = tmp;
        }
        bf.close();
        for (int x : box){
            System.out.print(x + " ");
        }
    }
}
