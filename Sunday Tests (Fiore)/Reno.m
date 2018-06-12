close all;
clc;

Reno1 = csvread('results-1528666667.41.csv',1,0,[1,0,300,2]);
Reno2 = csvread('results-1528666814.92.csv',1,0,[1,0,300,2]);

% Array=csvread('filename.csv');
col11 = Reno1(:, 1);
col21 = Reno1(:, 2);
 
col12 = Reno2(:, 1);
col22 = Reno2(:, 2);
% plot(col1, col2)

figure
plot(col11,col21)
%p(1).LineWidth = 2;
xlabel('Time')
ylabel('cwnd')
title('Reno - node06')

figure 
plot(col12,col22)
xlabel('Time')
ylabel('cwnd')
title('Reno - node07')