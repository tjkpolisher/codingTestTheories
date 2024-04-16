# [Silver I] 중력 큐 - 28078 

[문제 링크](https://www.acmicpc.net/problem/28078) 

### 성능 요약

메모리: 35704 KB, 시간: 376 ms

### 분류

많은 조건 분기, 자료 구조, 덱, 구현

### 제출 일자

2024년 4월 16일 17:37:40

### 문제 설명

<p>처음에 왼쪽이 큐의 뒤, 오른쪽이 큐의 앞인 가로 방향의 빈 큐가 존재한다. 이 큐에서 공이나 가림막을 하나씩 큐의 뒤에 삽입하거나, 큐의 가장 앞에 있는 공이나 가림막을 꺼낼 수 있으며, 큐를 시계방향이나 반시계방향으로 90도 회전시킬 수 있다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/0d0fe9ca-872a-460a-8f91-828b33259e44/-/preview/"></p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/b540ea39-4533-4561-a53c-95af1a53f3c3/-/preview/"></p>

<p>큐 안의 가림막은 중력의 영향을 받지 않지만, 큐 안의 공은 중력의 영향을 받는다. 따라서 큐를 세로 방향으로 회전시켰을 때, 큐의 가장 아래에 있는 가림막보다 아래에 있는 공들은 모두 떨어져 큐에서 꺼내지게 된다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/402cac13-51af-4115-b810-360b6d88ac2a/-/preview/"></p>

<p>또한, 큐가 세로 방향이면 공을 새로 넣더라도 넣은 공 아래에 가림막이 존재하지 않는 경우 곧바로 큐에서 꺼내지게 된다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/4bb585d8-958e-491b-8935-e0934be80e2f/-/preview/"></p>

<p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D444 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$Q$</span></mjx-container>개의 쿼리가 주어질 때, 처음 빈 상태의 큐에 주어진 쿼리들을 순서대로 수행하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 번째 줄에 쿼리의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D444 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$Q$</span></mjx-container>가 주어진다.</p>

<p>두 번째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D444 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$Q$</span></mjx-container>개의 줄에 걸쳐 첫 번째 쿼리부터 순서대로 각 쿼리의 정보가 순서대로 주어진다.</p>

<ul>
	<li><code>push b</code>: 큐의 뒤에 공 하나를 삽입한다.</li>
	<li><code>push w</code>: 큐의 뒤에 가림막 하나를 삽입한다.</li>
	<li><code>pop</code>: 큐에서 가장 앞쪽에 있는 공이나 가림막을 하나 꺼낸다. 큐가 빈 상태면 아무 일도 일어나지 않는다.</li>
	<li><code>rotate l</code>: 큐를 반시계 방향으로 90도 회전시킨다.</li>
	<li><code>rotate r</code>: 큐를 시계 방향으로 90도 회전시킨다.</li>
	<li><code>count b</code>: 현재 큐에 들어있는 공의 개수를 출력한다.</li>
	<li><code>count w</code>: 현재 큐에 들어있는 가림막의 개수를 출력한다.</li>
</ul>

### 출력 

 <p><code>count b </code>쿼리와 <code>count w</code> 쿼리의 정답을 한 줄에 하나씩 순서대로 출력한다.</p>

