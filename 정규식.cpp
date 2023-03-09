#include<bits/stdc++.h>
using namespace std;
/*
std::regex_match 를 이용해서 정규 표현식으로 전체 문자열 패턴 매칭하기.

std::regex_search 를 이용해서 정규 표현식으로 문자열 검색하기

std::regex_replace 를 이용해서 정규 표현식으로 문자열 치환하기
*/


/*
[]은 1글자, [a-z0-9] a와 z 사이의 한 문자 혹은 0과 9 사이 한 문자 
*는 0회 이상, +는 1회 이상, ?은 0회 혹은 1회 그 대상은 앞에 쓴다.
\는 뒤에 있는 문자를 문자 그대로 쓰게 한다.
^8는 문자열 앞에 8이 있냐 8$ 문자열 뒤에 8이 있냐 
[]속에 ^은 not의 의미다. [^1-2] 1-2를 제외한 숫자 
  [0-9]+-52[0-5]-8585의 한 예: 072-521-8585  
*/

/*
{}의 앞에 있는 문자의 개수를 지정한다.
.{5}이면 어느 문자든 5개 있다. 
[1f]{1,4} 1 또는 f가 1개 이상 4개 이하
{3,} 3이상   {,5} 5 이하
r.*? 수량자 뒤에 ?가 오면 수량자가 나타내는 가장 작은 값으로 한정시킴 r 하나가 됨

\w == [A-z0-9_]
\W != [A-z0-9_]
\d == [0-9]    \D == [^0-9]
\ba...cat\b   axxxcat
\A.. 가장 앞에 문자 3개  ...\Z 가장 뒤에 문자 3개  -> 전체 줄에서 1번씩 적용
^ &은 각 줄마다 적용됨 
[a|e] a 또는 e 한 글자

\w+(?=X) X는 검색할 때 기여해도 선택되지 않는다. AAX--aax라면  AA만 선택됨 
*/


/*
리눅스의 와일드카드(글로빙)과 혼동할 수 있기 때문에 다시 서술한다.
이것은 리눅스 커멘트 라인에서 사용한다.  mv cp ls rm 
그러나 grep은 정규식을 쓴다. 


* 모든 문자이며 개수는 무관
? 모든 문자이면 1개의 문자 

[] 괄호 내부 형태에 해당하는  1개의 문자 

[!]  부정형

[:alnum:] 알파벳과 숫자
[:alpha:], [:digit:] 알파벳, 숫자 
[:lower:], [:upper:] 소문자, 대문자 




*/



int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	regex ppap("a.*b"); // a와 b 사이에 어느 글자든지 상관 없다(.) *는 0회, 다수를 나타냄. 
	if(regex_match("ereraerebrab", ppap)) cout << "matching"<<endl; //정규식과 맞는지 판별
	
	cout << regex_search("ereraerebrab", ppap)<<endl;	
	cout << regex_search("eeeeeeeeee", ppap)<<endl; // 문자열 속에 있는지 없는지 판별
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
  	std::smatch match;  // 매칭된 결과를 string 으로 보관
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
