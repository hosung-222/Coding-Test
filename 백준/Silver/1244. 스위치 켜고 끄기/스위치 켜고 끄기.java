import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int switchCount = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Integer> switchList = new ArrayList<>();
        for (int i = 0; i < switchCount; i++) {
            switchList.add(Integer.parseInt(st.nextToken()));
        }
        int studentCount = Integer.parseInt(br.readLine());
        for (int i = 0; i < studentCount; i++) {
            st = new StringTokenizer(br.readLine());
            int sex = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());

            if (sex == 1) { // 남학생
                for (int j = num; j <= switchCount; j += num) {
                    int index = j - 1;
                    switchList.set(index, switchList.get(index) == 1 ? 0 : 1);
                }
            } else if (sex == 2) { // 여학생
                int index = num - 1;
                switchList.set(index, switchList.get(index) == 1 ? 0 : 1);
                for (int j = 1; j < switchCount; j++) {
                    int left = index - j;
                    int right = index + j;
                    if (left < 0 || right >= switchCount) break;
                    if (!switchList.get(left).equals(switchList.get(right))) break;

                    switchList.set(left, switchList.get(left) == 1 ? 0 : 1);
                    switchList.set(right, switchList.get(right) == 1 ? 0 : 1);
                }
            }
        }
        for (int i = 0; i < switchCount; i++) {
            System.out.print(switchList.get(i));
            if (i < switchCount - 1) {
                System.out.print(" ");
            }
            if ((i + 1) % 20 == 0) {
                System.out.println();
            }
        }
    }
}