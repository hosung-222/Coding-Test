class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        StringBuilder a = new StringBuilder();
        StringBuilder b = new StringBuilder();
        for (int i:
             num_list) {
            if (i%2 ==0){
                a.append(String.valueOf(i));
            }
            else {
                b.append(String.valueOf(i));
            }
        }
        System.out.println(a);
        answer += Integer.parseInt(String.valueOf(a));
        answer +=  Integer.parseInt(String.valueOf(b));
        
        return answer;
    }
}