# [Silver III] Rolling Encryption - 10465 

[문제 링크](https://www.acmicpc.net/problem/10465) 

### 성능 요약

메모리: 33192 KB, 시간: 288 ms

### 분류

구현, 문자열

### 제출 일자

2025년 5월 4일 23:22:08

### 문제 설명

<p><img alt="" src="https://www.acmicpc.net/upload/images2/snowball.jpg" style="float:right; height:139px; width:300px">You have a sequence of lowercase characters that you want to encrypt.</p>

<p>The first <em>k</em> characters will be encoded as plain-text. All characters after the first <em>k</em> characters will be shifted by the most frequently occuring character that appeared in the previous <em>k</em> characters, with ties broken by the character which occurs first in the alphabet. By "shifted by", we mean that if <code>c</code> was the most frequently occuring character, the character would be shifted ahead by 3 positions (since <code>c</code> is the third letter of the alphabet), modulo 26 (e.g., <code>b</code> becomes <code>e</code>, and <code>z</code> becomes <code>c</code>).</p>

### 입력 

 <p>On the first line of input contains <em>k</em> (1 ≤ <em>k</em> ≤ 10 000). The next line contains <em>c</em> characters (1 ≤ <em>c</em> ≤ 100 000).</p>

### 출력 

 <p>One line, containing the encrypted version of the <em>c</em> characters from the input.</p>

