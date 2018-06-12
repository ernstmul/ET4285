close all;
clc;

BBR1 = csvread('results-1528664233.24.csv',1,0,[1,0,300,2]);
BBR2 = csvread('results-1528664447.16.csv',1,0,[1,0,300,2]);

% Array=csvread('filename.csv');
col11 = BBR1(:, 1);
col21 = BBR1(:, 2);
 
col12 = BBR2(:, 1);
col22 = BBR2(:, 2);
% plot(col1, col2)

figure
plot(col11,col21)
%p(1).LineWidth = 2;
xlabel('Time')
ylabel('cwnd')
title('BBR - node06')

figure 
plot(col12,col22)
xlabel('Time')
ylabel('cwnd')
title('BBR - node07')