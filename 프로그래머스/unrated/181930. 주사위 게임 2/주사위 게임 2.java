class Solution {
    public int solution(int a, int b, int c) {
        if(a == b && b ==c ){
            
            return (a+b+c)*
                (int)(Math.pow(a,2)*3)*
                (int)(Math.pow(a,3)*3);
        }
        else if(a == b || b == c || a==c){
            return (a+b+c)*
                (int)(Math.pow(a,2)+Math.pow(b,2)+Math.pow(c,2));
        }
        else{
            return a+b+c;
        }
    }
}