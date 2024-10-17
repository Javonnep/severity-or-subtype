% FreeSurfer Setup
setenv('FREESURFER_HOME', '/usr/local/freesurfer/7.4.1');
fshome = getenv('FREESURFER_HOME');
fsmatlab = sprintf('%s/matlab',fshome);
if exist(fsmatlab) == 7
    addpath(genpath(fsmatlab));
end

% Your existing setup
% FSL Setup
setenv( 'FSLDIR', '/home/javonne/fsl' );
setenv('FSLOUTPUTTYPE', 'NIFTI_GZ');
fsldir = getenv('FSLDIR');
fsldirmpath = sprintf('%s/etc/matlab',fsldir);
path(path, fsldirmpath);
clear fsldir fsldirmpath;

% spm and cat
addpath('/home/javonne/thesis_downloads/cat12_latest/cat12');
addpath('/home/javonne/thesis_downloads/spm12');
