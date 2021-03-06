%********************************************************************************
%* This matlab script reads the airfoil data file, 'airfoil.data', generated by
%* the Karman-Trefftz airfoil generation code 'vkt_airfoil_v1.f90', and plot the
%* airfoil geometry and Cp distribution.
%*
%* Just type vkt_airfoil_v1_display at the Matlab prompt.
%*
%* Katate Masatsuka, Januray 2010. http://www.cfdbooks.com
%********************************************************************************
close('all')
clear
% 1. Load the airfoil data
data =load('airfoil.data');
x  = data(:,1);
y  = data(:,2);
cp = data(:,3);
% 2. Plot -Cp and the airfoil geometry
figure(1)
hold on
grid off
xlabel(   'x','FontName' ,'Times','FontSize',14)
ylabel( '-Cp','FontName' ,'Times','FontSize',14)
%% -Cp distribution
plot(x,-cp,'ko-','LineWidth',1,'MarkerSize',8)
%% Range
xmin = min(x);
xmax = max(x);
ymin = min( min(y), min(-cp));
ymax = max( max(y), max(-cp));
%% Adjustment of y-coordinates of the airfoil.
ratio = (ymax-ymin)/(xmax-xmin);
    y = y.*ratio;
plot(x,y,'k-','LineWidth',2)
%% Fix the range.
axis([xmin, xmax, min(ymin,min(y)), max(ymax,max(y))])
%% Reference line y = 0
xc = [xmin xmax];
yc = [0 0];
plot(xc,yc, 'r-')