1. Login to zscaler

2. Login via ssh

   ```bash
   ssh jp2923@login.hpc.imperial.ac.uk
   ```

3. cd into the irp folder

   ```bash
   cd irp-jp2923
   ```

4. Create the matlab userpath

   ```bash
   matlab
   userpath('/rds/general/user/jp2923/home/thesis_downloads/matlab/')
   ```

5. submit the job script. To apply ccs preprocessing to raw ABIDE data submit a job that runs `src/preprocess_modality_plel.py`.


