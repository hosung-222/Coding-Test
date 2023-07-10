class Solution {
    public int solution(int[] num_list) {
        int pow = 1;
        int plu = 0;
        for(int i : num_list){
            pow *= i;
            plu += i;
        }
        return pow < (int)Math.pow(plu,2) ? 1 : 0;
        
        
    }
}