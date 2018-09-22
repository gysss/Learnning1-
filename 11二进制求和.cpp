class Solution {
public:
    string addBinary(string a, string b) {
        string s;
        int lena = a.length()-1;
        int lenb = b.length()-1;
        int temp = 0;
        char c;
        while(lena>=0 && lenb>=0){
            c = (a[lena]-'0') + (b[lenb] - '0') +temp +'0';
            temp = 0;
            if ((c-'0')>=2)
            {
            	temp = 1;
            	c = c -2;
            }
            s = c+s;
            lena --;
            lenb --;
        }
        while(lena>=0){
        	c = (a[lena]-'0')+ temp +'0';
        	temp = 0;
        	if((c-'0')>=2){
        		temp = 1;
        		c = c-2;
        	}
        	s = c+s;
        	lena--;
        }
        while(lenb>=0){
        	c = (b[lenb]-'0')+ temp +'0';
        	temp = 0;
        	if((c-'0')>=2){
        		temp = 1;
        		c = c-2;
        	}
        	s = c+s;
        	lenb--;
        }
        if(temp == 1){
        	s ='1'+s;
        }
        return s;
    }
};