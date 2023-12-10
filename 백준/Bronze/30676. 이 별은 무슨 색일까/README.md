# [Bronze V] 이 별은 무슨 색일까 - 30676 

[문제 링크](https://www.acmicpc.net/problem/30676) 

### 성능 요약

메모리: 31120 KB, 시간: 44 ms

### 분류

구현

### 제출 일자

2023년 12월 10일 22:45:24

### 문제 설명

<p>스타는 안에 별이 담긴 기계장치를 보았다. 기계장치 내부를 볼 수 없어 별을 구경할 순 없었지만, 기계장치에는 별빛의 파장을 알려주는 계기판이 있었다. 계기판에 표시된 파장의 값을 토대로 스타는 별의 색을 알아낼 수 있었다. 스타가 알아낸 별의 색은 무엇이었을까?</p>

<p>색상별 파장의 범위는 다음과 같다.</p>

<ul>
	<li>빨간색: 620nm 이상 780nm 이하</li>
	<li>주황색: 590nm 이상 620nm 미만</li>
	<li>노란색: 570nm 이상 590nm 미만</li>
	<li>초록색: 495nm 이상 570nm 미만</li>
	<li>파란색: 450nm 이상 495nm 미만</li>
	<li>남색: 425nm 이상 450nm 미만</li>
	<li>보라색: 380nm 이상 425nm 미만</li>
</ul>

### 입력 

 <p>계기판에 표시된 별빛의 파장 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D706 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\lambda$</span></mjx-container> 가 주어진다. 파장은 항상 정수로 주어지며 단위는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mtext class="mjx-n"><mjx-c class="mjx-c6E"></mjx-c><mjx-c class="mjx-c6D"></mjx-c></mjx-mtext></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>nm</mtext></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\textrm{nm}$</span></mjx-container>이다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c38"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D706 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c37"></mjx-c><mjx-c class="mjx-c38"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>380</mn><mo>≤</mo><mi>λ</mi><mo>≤</mo><mn>780</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(380 \leq \lambda \leq 780)$</span> </mjx-container></p>

### 출력 

 <p>별의 색을 출력한다. 빨간색이면 "<span style="color: rgb(231, 76, 60); --darkreader-inline-color: #e95849;" data-darkreader-inline-color=""><code>Red</code></span>", 주황색이면 "<span style="color: rgb(243, 156, 18); --darkreader-inline-color: #f4a529;" data-darkreader-inline-color=""><code>Orange</code></span>"<code>,</code> 노란색이면 "<span style="color: rgb(241, 196, 15); --darkreader-inline-color: #f2ca27;" data-darkreader-inline-color=""><code>Yellow</code></span>", 초록색이면 "<span style="color: rgb(39, 174, 96); --darkreader-inline-color: #5cda91;" data-darkreader-inline-color=""><code>Green</code></span>", 파란색이면 "<span style="color: rgb(52, 152, 219); --darkreader-inline-color: #46a1de;" data-darkreader-inline-color=""><code>Blue</code></span>", 남색이면 "<span style="color: rgb(44, 62, 80); --darkreader-inline-color: #aec2d3;" data-darkreader-inline-color=""><code>Indigo</code></span>", 보라색이면 "<span style="color: rgb(155, 89, 182); --darkreader-inline-color: #a467bc;" data-darkreader-inline-color=""><code>Violet</code></span>"을 출력한다.</p>

