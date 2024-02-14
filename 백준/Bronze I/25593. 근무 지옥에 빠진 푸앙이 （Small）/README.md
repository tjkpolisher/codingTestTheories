# [Bronze I] 근무 지옥에 빠진 푸앙이 (Small) - 25593 

[문제 링크](https://www.acmicpc.net/problem/25593) 

### 성능 요약

메모리: 31120 KB, 시간: 52 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 문자열

### 제출 일자

2024년 2월 14일 22:09:40

### 문제 설명

<p>군대에 간 푸앙이는 4교대 근무를 서게 된다. 근무 시간대는 08:00~12:00, 12:00~18:00, 18:00~22:00, 22:00~08:00 으로 각각 4, 6, 4, 10시간의 근무로 구성되어 있다.</p>

<p>푸앙이와 동기들은 근무 시간이 최대한 공평하게 배분되기를 원한다. 그래서 근무표 전체에서 각 인원의 근무 시간이 12시간 이하로 차이 나게 해서 최대 50주 치 근무표를 짜려고 한다.</p>

<p>푸앙이는 원래 똑똑해서 이 정도는 한눈에 계산이 가능했지만 어째서인지 푸앙이는 계산이 불가능해졌다. 푸앙이를 위해서 대신 근무표가 공평한지 계산해주자.</p>

### 입력 

 <p>첫 번째 줄에 주의 개수인 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 입력된다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>50</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \leq N \leq 50)$</span> </mjx-container></p>

<p>둘째 줄부터 근무표가 주어진다. 각 주는 4개의 줄로 표현되며, 그중 첫째 줄은 각 날의 08:00~12:00에 근무하는 사람의 이름 또는 '-', 둘째 줄은 12:00~18:00, 셋째 줄은 18:00~22:00, 넷째 줄은 22:00~08:00을 나타낸다. '-'는 근무자가 없음을 의미한다. 근무자의 이름은 모두 알파벳 소문자로 이루어져 있고 20글자를 넘지 않는다.</p>

<p>각 날에는 4개의 시간대에 모두 근무자가 있거나 모두 근무자가 없다. 예를 들어 12:00~18:00에만 근무자가 있는 날은 없다.</p>

<p>근무표에 적히지 않은 근무자는 없으며, 근무자 수는 최대 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container>명이다.</p>

### 출력 

 <p>근무표가 공평하면 “<code>Yes</code>”를 아니면 “<code>No</code>”를 출력한다. 단, 아무도 근무하지 않을 경우 공평한 것으로 간주한다.</p>

