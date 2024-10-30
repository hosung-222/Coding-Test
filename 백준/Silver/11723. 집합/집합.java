import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입출력을 위해 BufferedReader 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder(); // 출력 결과를 저장할 StringBuilder
        int n = Integer.parseInt(br.readLine());
        int s = 0; // 비트마스크를 사용하여 집합을 표현

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            int x = 0;
            if (command.equals("add") || command.equals("remove") || command.equals("check") || command.equals("toggle")) {
                x = Integer.parseInt(st.nextToken());
            }

            switch (command) {
                case "add":
                    s |= (1 << (x - 1));
                    break;
                case "remove":
                    s &= ~(1 << (x - 1));
                    break;
                case "check":
                    if ((s & (1 << (x - 1))) != 0) {
                        sb.append("1\n");
                    } else {
                        sb.append("0\n");
                    }
                    break;
                case "toggle":
                    s ^= (1 << (x - 1));
                    break;
                case "all":
                    s = (1 << 20) - 1;
                    break;
                case "empty":
                    s = 0;
                    break;
            }
        }

        // 결과를 한 번에 출력
        System.out.print(sb.toString());
        br.close();
    }
}
