# __README.md__
&emsp;This markdown helps to understand the codes and the folder(file) structure.<br>
## 1.Folder structure

&emsp;Team CSU123:<br>
&emsp;&emsp;test_x.zip, test_y.zip: test data for evaluation<br><br>
&emsp;\paddlepaddle:<br>
&emsp;&emsp;common.py, metrics.py, model.py, predict.py, train.py, test_data.py, wind_turbine_data.py <br>
&emsp;&emsp;are almost same as officially released. <br>
&emsp;&emsp;data_cleaning.py: KNN to deal with null and abnormal data,  <br> 

&emsp;\paddlepaddle\sample:(partial hyperparameter grid search)<br>
&emsp;&emsp;Similar structure to \paddlepaddle. eva luation.py and train.py were modified. <br>

## 2.Description of modified/extended files 
&emsp;1.\paddlepaddle\sample\prepare.py<br>
&emsp;&emsp;A parameterized __prep_env_search()__ is provided based on the original __prep_env()__.It enables variable hyperparameters(batch size,learning rate, number of layers, and input length).<br>
&emsp;2.\paddlepaddle\sample\train.py<br>
&emsp;&emsp;A multi-stage cycle is designed to realize grid search. That is, train models with different hyperparameter combinations. The trained models were saved at \paddlepaddle\sample with seperate folders.<br>
&emsp;3.\paddlepaddle\sample\evaluation.py<br>
&emsp;&emsp;MAX_RUN_NUM was changed as 1 to avoid error.<br>
&emsp;4.\paddlepaddle\data_cleaning.py<br>
&emsp;&emsp;A method is defined to realize kNN interpolation by kNNImputer.<br>
&emsp;5.\paddlepaddle\make_zip.py<br>
&emsp;&emsp;Compress all files into a zip file according to the submission format requirements.<br>

## 3.Work flow
&emsp;1.Run \paddlepaddle\preprocess.py and get file 'wtdata_245days_knned.CSV'.<br>
&emsp;2.Run \paddlepaddle\sample\train.py to train models on sampled turbines(can be defined in \sample\prepare.py).This yields a group of foldersin \sample\checkpoints where models exist. <br>
&emsp;3.Run \paddlepaddle\make_zip.py. This transform the model folders into .zip files so that satisfy the evaluation procedure.<br>
&emsp;4.Run \paddlepaddle\sample\evaluation.py to evaluate different models.(For some unresolved reason about temporary system path, the eval method can only launch once in a single run, otherwise 'path not found error' will occur. In practice, we record every score manually.)  <br>
&emsp;5.Run \paddlepaddle\train.py to train 134 models using the best set of hyperparameters in step 4(by set prepare.py).<br>