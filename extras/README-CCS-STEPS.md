# HOW TO RUN THE CCS (For 1 subject)

1. Activate the venv

   ```bash
   conda activate abide
   ```

2. navigate to the root, in my case `irp-jp2923`

3. Set up the BIDS and CCS directories

   ```BASH
   export BIDS_DIR=/home/javonne/irp-jp2923/data/abide_ii/ABIDEII-BNI_1
   export SITE=ABIDEII-BNI_1
   export CCS_DIR=/home/javonne/irp-jp2923/data/abide_ii/ABIDEII-BNI_1/CCS
   export CCS_APP=/home/javonne/thesis_downloads/CCS
   export SUBJECTS_DIR=/home/javonne/irp-jp2923/data/abide_ii/FreeSurfer
   export FREESURFER_HOME=/usr/local/freesurfer/7.2.0
   export ABIDE_DIR=/home/javonne/irp-jp2923/data/abide_ii
   source $FREESURFER_HOME/SetUpFreeSurfer.sh
   subject=001_1
   export MODALITY=s
   ```
   
4. Check Directories have been setup properly

   ```bash
   echo $BIDS_DIR
   echo $CCS_DIR
   echo $CCS_APP
   echo $SUBJECTS_DIR
   echo $FREESURFER_HOME
   echo $subject
   echo $SITE
   echo $ABIDE_DIR
   echo $MODALITY
   ```

   

5. Enforce BIDS formatting on the data

   ```bash
   python src/handle_subjects.py $ABIDE_DIR
   
   python src/handle_bids_format.py $ABIDE_DIR
   
   ```

6. Make folders to store CCS data

   ```bash
   mkdir /home/javonne/irp-jp2923/data/abide_ii/ABIDEII-BNI_1/CCS
   mkdir /home/javonne/irp-jp2923/data/abide_ii/ABIDEII-ETH_1/CCS
   mkdir /home/javonne/irp-jp2923/data/abide_ii/ABIDEII-KUL_3/CCS
   mkdir /home/javonne/irp-jp2923/data/abide_ii/ABIDEII-KKI_1/CCS
   mkdir /home/javonne/irp-jp2923/data/abide_ii/ABIDEII-KKI_2/CCS
   mkdir /home/javonne/irp-jp2923/data/abide_ii/ABIDEII-KKI_3/CCS
   mkdir /home/javonne/irp-jp2923/data/abide_ii/ABIDEII-KKI_4/CCS
   mkdir /home/javonne/irp-jp2923/data/abide_ii/ABIDEII-TCD_1/CCS
   
   ```

7. Convert the BIDS data from one collection to the CCS format. This outputs a folder for each subject @ CCS_DIR

   ```bash
   python $CCS_APP/samplesScripts/ccs_pre_bids2ccs.py --BIDS_DIR $BIDS_DIR --CCS_DIR $CCS_DIR
   ```

8. Preprocess with python!

   ```bash
   python src/preprocess_modality_plel.py $SITE $ABIDE_DIR $MODALITY
   ```

