close all;
clc;

Mix1 = csvread('results-1528664718.4.csv',1,0,[1,0,300,2]);
Mix2 = csvread('results-1528665015.38.csv',1,0,[1,0,300,2]);

% Array=csvread('filename.csv');
col11 = Mix1(:, 1);
col21 = Mix1(:, 2);
 
col12 = Mix2(:, 1);
col22 = Mix2(:, 2);
% plot(col1, col2)

figure
plot(col11,col21)
%p(1).LineWidth = 2;
xlabel('Time')
ylabel('cwnd')
title('BBR and Cubic - node06')

figure 
plot(col12,col22)
xlabel('Time')
ylabel('cwnd')
title('BBR and Cubic - node07')