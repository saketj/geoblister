This code contains the sample visualizing tool for land cover change detection.
Requirements:
	1) Windows XP,Vista,7 
	2) MATLAB 7 or higher
	3) Python 2.7 (To be installed before hand) 
	[Edit the environment variable path so that python is recognised as a command at the command prompt]
	
	
How to run:
		1) Run MATLAB and load data_score_ix.mat. (this is a sample result file for California fires)
		2) Run the following '.m' matlab file 
			
			generate_html(data,lat,lon,score,ix,K);
	         	
				data: the timeseries data of all the points
    			   lat: the vector of latitude points
				   lon: the vector of longitude points
				   score: the score given by the algorithm
				   ix: the index of the ranked points
				K is the number of the points to be plotted.
		3) Output.html is generated which can be viewed in any browser.
		
Customizations: 
		1) The generate_html is the single function that needs to be executed.
		   data: the timeseries data of all the points
		   lat: the vector of latitude points
		   lon: the vector of longitude points
		   score: the score given by the algorithm
		   ix: the index of the ranked points
		2) The above variable in data_score_ix.mat is a sample. 
		   These variables can be fed as an output of any algorithm.
		   The sample is the output of the yearly delta.
		3) The score is a measure of the change in the EVI.
		   The higher the score, the higher is the change in the timeseries which indicates the fire.
		   High score points are the fire points.