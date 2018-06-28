close all;
clc;

% results matrix
% you can call it as you prefer, in my case I used it for BBR

% modify the results file you want to check 
% I usually run the test twice, one per server. So in the BBR1 there's one
% server's values and in BBR2 the other one. 
% Remember: it doesn't work with "-" in the CSV, so before you have to
% replace each "-" in the CSV with 0.

% It's also possible to specify the range of values since the CSV file
% contains up to 900 values. 
% For example, 
% BBR1 = csvread('results-1528664233.24.csv',1,0,[1,0,200,2]) reads the values
% starting from row 1 (we have to avoid the title) up to row 200, and reads
% only the two first values. 
BBR1 = csvread('results-1528664233.24.csv',1,0);
BBR2 = csvread('results-1528664447.16.csv',1,0);



% extracts only the two values we're interested in, such as time and cwnd
 col11 = BBR1(:, 1);
 col21 = BBR1(:, 2);
 
 col12 = BBR2(:, 1);
 col22 = BBR2(:, 2);

% plot the values
figure
plot(col11,col21)
xlabel('Time')
ylabel('cwnd')

figure 
plot(col12,col22)
xlabel('Time')
ylabel('cwnd')