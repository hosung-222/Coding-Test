import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true){
            String password = br.readLine();

            if (password.equals("end")) break;

            if (isAcceptable(password)){
                System.out.println("<" + password+"> is acceptable.");
            }else {
                System.out.println("<" + password+"> is not acceptable.");
            }
        }
        br.close();
    }

    public static boolean isAcceptable(String password){
        boolean hasVowel = false;
        int vowelCount = 0;
        int consonantCount = 0;

        for (int i = 0; i < password.length(); i++) {
            char current = password.charAt(i);
            if (isVowel(current)){
                hasVowel = true;
                vowelCount ++;
                consonantCount = 0;
            }else {
                consonantCount ++;
                vowelCount = 0;
            }

            if (vowelCount >= 3 || consonantCount >=3)return false;

            if (i>0 && current == password.charAt(i-1) && current != 'e' && current !='o')
                return false;
        }
        return hasVowel;
    }

    public static boolean isVowel(char c) {
        String[] vowels = {"a", "e", "i", "o", "u"};
        for (String vowel : vowels) {
            if (vowel.charAt(0) == c) return true;
        }
        return false;
    }
}