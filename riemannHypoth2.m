clear all, close all, clc

%riemann hypothesis is that the zeros of the riemann zeta function lie on real line x = 1/2? 
%let's explore this? 

x = 0.7;
hold on
for y = 14:0.1:50
    out1 = 1; 
    out2 = 1; 
    for n = 2:2000
        out1 = out1 + 1/(n.^(x+j*y));
        out2 = out2 + 1/(n.^(0.5+j*y));
    end
    plot(real(out1), imag(out1), '*k');
%     pause(0.5);
    plot(real(out2), imag(out2), '*r');
    grid
    title(y)
    pause(0.01);
end
