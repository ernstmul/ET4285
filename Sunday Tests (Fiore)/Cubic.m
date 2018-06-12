close all;
clc;

Cubic1 = csvread('results-1528666150.07.csv',1,0,[1,0,300,2]);
Cubic2 = csvread('results-1528666375.11.csv',1,0,[1,0,300,2]);

% Array=csvread('filename.csv');
col11 = Cubic1(:, 1);
col21 = Cubic1(:, 2);
 
col12 = Cubic2(:, 1);
col22 = Cubic2(:, 2);
% plot(col1, col2)

figure
plot(col11,col21)
%p(1).LineWidth = 2;
xlabel('Time')
ylabel('cwnd')
title('Cubic - node06')

figure 
plot(col12,col22)
xlabel('Time')
ylabel('cwnd')
title('Cubic - node07')