
function myparam = initparam(myparam)
    
    Mb = 1E6;
    
    myparam.celltype=input('Enter the cell type (default Gm12878):\n','s');
    if isempty(myparam.celltype)
        myparam.celltype = 'Gm12878';
    end
    
    myparam.chrId=input('Enter the chromosome id (default chromosome 1):\n');
    if isempty(myparam.chrId)
        myparam.chrId = 1;
    end
    
    myparam.resolution=input('Enter the resolution of contact map (default 50kb):\n');
    if isempty(myparam.resolution)
        myparam.resolution = 50000;
    end
    
%     currentpath = pwd
    chr_region=load('../../src/chr_region.txt');
    myparam.startnum = chr_region(myparam.chrId,2);
    myparam.endnum = chr_region(myparam.chrId,3);
    gpSta = myparam.startnum+2;
    gpEnd = myparam.endnum-3;
    startid = gpSta*Mb;
    endid = gpEnd*Mb;
    myparam.nbead = (endid-startid)/myparam.resolution;
    

    myparam.simmap_path = ['./cmap/contact_map_CG_comb_' myparam.celltype ...
        '_chr' num2str(myparam.chrId) '.txt'];
    
    myparam.hic_path = input('Enter the path where the Hi-C map is located:\n');
    if isempty(myparam.hic_path)
        myparam.hic_path = ['~/Desktop/nobackup/project_3d_genome/hic_map/hic_processing.50kb/' ...
            myparam.celltype '/hicmat/chr', num2str(myparam.chrId, '%d'), '_50kb_', ...
            num2str(gpSta*Mb/myparam.resolution+1), '_', ...
            num2str(gpEnd*Mb/myparam.resolution),'.mat'];
    end

    myparam.hic_norm_path = input('Enter the path where the normalization constant is located:\n');
    if isempty(myparam.hic_norm_path)
        myparam.hic_norm_path = ['~/Desktop/nobackup/project_3d_genome/hic_map/hic_processing.50kb/' ...
            myparam.celltype '/normalization_contant/normalization_contant','_chr', ...
            num2str(myparam.chrId, '%d'), '_50kb.txt'];
    end
    
end