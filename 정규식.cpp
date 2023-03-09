#include<bits/stdc++.h>
using namespace std;
/*
std::regex_match �� �̿��ؼ� ���� ǥ�������� ��ü ���ڿ� ���� ��Ī�ϱ�.

std::regex_search �� �̿��ؼ� ���� ǥ�������� ���ڿ� �˻��ϱ�

std::regex_replace �� �̿��ؼ� ���� ǥ�������� ���ڿ� ġȯ�ϱ�
*/


/*
[]�� 1����, [a-z0-9] a�� z ������ �� ���� Ȥ�� 0�� 9 ���� �� ���� 
*�� 0ȸ �̻�, +�� 1ȸ �̻�, ?�� 0ȸ Ȥ�� 1ȸ �� ����� �տ� ����.
\�� �ڿ� �ִ� ���ڸ� ���� �״�� ���� �Ѵ�.
^8�� ���ڿ� �տ� 8�� �ֳ� 8$ ���ڿ� �ڿ� 8�� �ֳ� 
[]�ӿ� ^�� not�� �ǹ̴�. [^1-2] 1-2�� ������ ���� 
  [0-9]+-52[0-5]-8585�� �� ��: 072-521-8585  
*/

/*
{}�� �տ� �ִ� ������ ������ �����Ѵ�.
.{5}�̸� ��� ���ڵ� 5�� �ִ�. 
[1f]{1,4} 1 �Ǵ� f�� 1�� �̻� 4�� ����
{3,} 3�̻�   {,5} 5 ����
r.*? ������ �ڿ� ?�� ���� �����ڰ� ��Ÿ���� ���� ���� ������ ������Ŵ r �ϳ��� ��

\w == [A-z0-9_]
\W != [A-z0-9_]
\d == [0-9]    \D == [^0-9]
\ba...cat\b   axxxcat
\A.. ���� �տ� ���� 3��  ...\Z ���� �ڿ� ���� 3��  -> ��ü �ٿ��� 1���� ����
^ &�� �� �ٸ��� ����� 
[a|e] a �Ǵ� e �� ����

\w+(?=X) X�� �˻��� �� �⿩�ص� ���õ��� �ʴ´�. AAX--aax���  AA�� ���õ� 
*/


/*
�������� ���ϵ�ī��(�۷κ�)�� ȥ���� �� �ֱ� ������ �ٽ� �����Ѵ�.
�̰��� ������ Ŀ��Ʈ ���ο��� ����Ѵ�.  mv cp ls rm 
�׷��� grep�� ���Խ��� ����. 


* ��� �����̸� ������ ����
? ��� �����̸� 1���� ���� 

[] ��ȣ ���� ���¿� �ش��ϴ�  1���� ���� 

[!]  ������

[:alnum:] ���ĺ��� ����
[:alpha:], [:digit:] ���ĺ�, ���� 
[:lower:], [:upper:] �ҹ���, �빮�� 




*/



int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	regex ppap("a.*b"); // a�� b ���̿� ��� ���ڵ��� ��� ����(.) *�� 0ȸ, �ټ��� ��Ÿ��. 
	if(regex_match("ereraerebrab", ppap)) cout << "matching"<<endl; //���Խİ� �´��� �Ǻ�
	
	cout << regex_search("ereraerebrab", ppap)<<endl;	
	cout << regex_search("eeeeeeeeee", ppap)<<endl; // ���ڿ� �ӿ� �ִ��� ������ �Ǻ�
	string p= "123-4564565-032";
	regex pp("-.");
	auto start = std::sregex_iterator(p.begin(), p.end(), pp);
	for(auto it = start;it != std::sregex_iterator();it++){
		cout << (*it).str()<<endl;
	}
	
	
	
	 
	std::vector<std::string> phone_numbers = {"010-1234-5678", "010-123-4567",
                                            "011-1234-5567", "010-12345-6789",
                                            "123-4567-8901", "010-1234-567"};
    std::regex re("[01]{3}-(\\d{3,4})-\\d{4}");
  	std::smatch match;  // ��Ī�� ����� string ���� ����
  	for (const auto &number : phone_numbers) {
    	if (std::regex_match(number, match, re)) {
      	for (size_t i = 0; i < match.size(); i++) {
        	std::cout << "Match : " << match[i].str() << std::endl;
      }
      	std::cout << "-----------------------\n";
    }
  } 
	 
	string s = "Hello World!";
    cout << regex_replace(s, regex("[eo]"), "0") << endl;
    // H0ll0 W0rld!
	 
	return 0;
}
