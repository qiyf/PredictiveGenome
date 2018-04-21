%%% main.m
%%% visulize the simulated contact map vs. Hi-C map 
%%% Last modified: 04/17/2018

%% information about the input parameters:
% celltype            % options refer to README 
% chrId               % chromosome id, options refer to README
% resolution          % resolution to visualize contact map
                      % Hi-C map should have consistent resolution
% startnum            % starting postion of the genomic segment
% endnum              % ending postion of the genomic segment
% nbead               % number of beads included to visualize
                      % the size of the contact matrix
% simmap_path         % path to simulated contact map
% hic_path            % path to raw Hi-C map, 
                      % Rao, Suhas S.P. et al. Cell 159, 1665-1680 (2014).
% hic_norm_path       % path to normalization constant of Hi-C map

%% clear all
clc;clf;clear;close all

%% initialize color map (red, green, blue)
load MyColormaps cmap64;
cmap256 = zeros(1024,3);
cmap256(:,1) = interp1(linspace(0,1,64),cmap64(:,1), linspace(0,1,1024));
cmap256(:,2) = interp1(linspace(0,1,64),cmap64(:,2), linspace(0,1,1024));
cmap256(:,3) = interp1(linspace(0,1,64),cmap64(:,3), linspace(0,1,1024));
set(gcf, 'Colormap', cmap256)
    
%% plot the contact map
[cmap,lbl,lbl_tick,celltype,chrId] = initcmap(param);
imagesc(cmap)
colormap(cmap256)
caxis([-7.5,0.1])

%% image settings
set(gcf,'Position',[0 0 580 550])
xticks(lbl);
xticklabels(lbl_tick);
yticks(lbl);
yticklabels(lbl_tick);
title([celltype,', chromosome ' num2str(chrId)])
xlabel ('Genomic sequence (kb)','FontWeight','bold');
ylabel ('Genomic sequence (kb)','FontWeight','bold');
set(gca,'FontSize',26)