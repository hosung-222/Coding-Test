import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        String game = st.nextToken();

        Set<String> player = new HashSet<>();
        for (int i = 0; i < n; i++) {
            player.add(br.readLine());
        }
        int playerCount = player.size();
        switch (game){
            case "Y":
                System.out.println(playerCount);
                break;
            case "F":
                System.out.println(playerCount/2);
                break;
            case "O":
                System.out.println(playerCount/3);
                break;
        }
    }
}