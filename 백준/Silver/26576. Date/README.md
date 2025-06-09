# [Silver V] Date - 26576 

[문제 링크](https://www.acmicpc.net/problem/26576) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

구현, 파싱, 문자열

### 제출 일자

2025년 6월 9일 13:47:39

### 문제 설명

<p>You are starting to get annoyed with how your phone shows you the date, so you want to put it into a different format. Currently, your phone gives you the date in the format Month Day, Year (ex. July 25, 2018). Your goal is to shorten the format exactly like this, MM/DD/YY, where M is month, D is day, and Y is year (ex. 07/25/18). Write a program that will calculate this format change.</p>

### 입력 

 <p>The first line will contain a single integer n that indicates the number of lines that follow. The next n lines will be in the format Month Day, Year. The full year integer will be between 1 and 300,000,000.</p>

### 출력 

 <p>Your output should be the same date as the input, but in the new format MM/DD/YY. If the month, day or year is only one digit, pad with a 0. If the date is not valid (the month is spelled incorrectly, the day is less than 1 or greater than 31), print Invalid. You do not need to check that the day fits within the month's days, just that it is not greater than 31. The year format will be the last two digits (or 1 digit padded with a 0) of the input year.</p>

